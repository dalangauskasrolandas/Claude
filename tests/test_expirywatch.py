import csv
import io
import json
import os
import subprocess
import sys
from datetime import date, timedelta

import pytest

import app as appmod
import extractor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAMPLES = os.path.join(ROOT, "samples")


def post_files(client, paths):
    data = {"files": [(open(p, "rb"), os.path.basename(p)) for p in paths]}
    r = client.post("/api/upload", data=data, content_type="multipart/form-data")
    assert r.status_code == 200
    return r.get_json()


def upload_all(client, names=None):
    names = names or sorted(n for n in os.listdir(SAMPLES) if n.endswith(".pdf"))
    return post_files(client, [os.path.join(SAMPLES, n) for n in names])


def docs_by_name(client):
    return {d["filename"]: d for d in client.get("/api/documents").get_json()}


@pytest.fixture
def client():
    return appmod.app.test_client()


# ---- date detection ---------------------------------------------------------

@pytest.mark.parametrize("text,expected", [
    ("Valid until 31.12.2026", "2026-12-31"),
    ("Expires: 31/12/2026", "2026-12-31"),
    ("Valid until: 2026-12-31", "2026-12-31"),
    ("Valid until 31 December 2026", "2026-12-31"),
    ("Kehtiv kuni 31. detsember 2026", "2026-12-31"),
    ("Срок действия: 31 декабря 2026", "2026-12-31"),
    ("Действителен до 31.12.2026", "2026-12-31"),
    ("Expiry date: December 31, 2026", "2026-12-31"),
    ("Policy period: 01.01.2026 - 31.12.2026", "2026-12-31"),
    ("Issued 01.01.2020\nValid until 05.05.2027", "2027-05-05"),
])
def test_date_formats(text, expected):
    assert extractor.detect_expiry(text) == (expected, False, "")


def test_unlabelled_range_is_flagged():
    iso, review, _ = extractor.detect_expiry("Valid 01.01.2026 - 31.12.2026")
    assert review


def test_unlabelled_single_date_is_flagged():
    iso, review, _ = extractor.detect_expiry("Certificate 12.05.2027")
    assert iso == "2027-05-12" and review


def test_invalid_date_ignored():
    assert extractor.detect_expiry("Valid until 31.02.2026")[0] is None


def test_conflicting_labelled_dates_flagged():
    _, review, _ = extractor.detect_expiry("Valid until 01.01.2027\nExpires 01.01.2028")
    assert review


def test_nearest_label_wins_over_other_dates():
    text = "Date of birth: 01.01.1980\nIssued: 02.02.2020\nValid until: 03.03.2030"
    assert extractor.detect_expiry(text) == ("2030-03-03", False, "")


# ---- acceptance: samples ----------------------------------------------------

def test_samples_accuracy(client):
    expected = json.load(open(os.path.join(SAMPLES, "expected.json")))
    upload_all(client)
    docs = docs_by_name(client)
    assert len(docs) == 10
    correct = silently_wrong = 0
    for name, exp in expected.items():
        d = docs[name]
        if d["status"] == "ok":
            if d["expiry"] == exp:
                correct += 1
            else:
                silently_wrong += 1
        else:
            assert d["colour"] == "grey"
    assert silently_wrong == 0
    assert correct >= 8


def test_type_and_holder_detected(client):
    upload_all(client)
    docs = docs_by_name(client)
    assert docs["01_driving_licence_en.pdf"]["doc_type"] == "Driving licence"
    assert docs["01_driving_licence_en.pdf"]["holder"] == "John Smith"
    assert docs["02_tehnoulevaatus_et.pdf"]["doc_type"] == "Vehicle inspection"
    assert docs["03_cmr_insurance_en.pdf"]["doc_type"] == "CMR insurance"
    assert docs["05_litsenziya_ru.pdf"]["doc_type"] == "Licence"


# ---- acceptance: colours ----------------------------------------------------

@pytest.mark.parametrize("days,expected", [
    (-1, "red"), (0, "red"), (6, "red"), (7, "orange"), (29, "orange"),
    (30, "yellow"), (59, "yellow"), (60, "green"), (500, "green")])
def test_colour_boundaries(days, expected):
    today = date(2026, 6, 1)
    exp = (today + timedelta(days=days)).isoformat()
    assert appmod.colour("ok", exp, today) == expected


def test_grey_when_not_ok():
    assert appmod.colour("review", "2030-01-01") == "grey"
    assert appmod.colour("scanned", None) == "grey"
    assert appmod.colour("ok", None) == "grey"


def test_colours_for_samples(client):
    upload_all(client)
    c = {n: d["colour"] for n, d in docs_by_name(client).items()}
    assert c["06_adr_certificate_en.pdf"] == "red"       # expired
    assert c["02_tehnoulevaatus_et.pdf"] == "orange"     # 10 days
    assert c["03_cmr_insurance_en.pdf"] == "orange"      # 25 days
    assert c["04_esmaabi_tunnistus_et.pdf"] == "yellow"  # 45 days
    assert c["01_driving_licence_en.pdf"] == "green"
    assert c["09_inspection_record_en.pdf"] == "grey"


# ---- scanned / bad files ----------------------------------------------------

def test_scanned_pdf(client, tmp_path):
    from reportlab.pdfgen import canvas
    p = tmp_path / "blank.pdf"
    c = canvas.Canvas(str(p))
    c.showPage()
    c.save()
    post_files(client, [p])
    d = client.get("/api/documents").get_json()[0]
    assert d["status"] == "scanned" and "manual entry" in d["note"] and d["colour"] == "grey"


def test_corrupt_and_non_pdf(client, tmp_path):
    bad = tmp_path / "bad.pdf"
    bad.write_bytes(b"not a pdf")
    txt = tmp_path / "x.txt"
    txt.write_text("hi")
    assert post_files(client, [bad])[0]["status"] == "scanned"
    assert post_files(client, [txt])[0]["error"]


# ---- acceptance: manual edit persists across restart ------------------------

def test_edit_persists_after_restart(client):
    upload_all(client, ["10_safety_certificate_en.pdf"])
    doc = client.get("/api/documents").get_json()[0]
    assert doc["status"] == "review"
    r = client.post(f"/api/documents/{doc['id']}", json={
        "filename": "renamed.pdf", "doc_type": "Certificate", "holder": "Alex B.",
        "expiry": "2031-01-15"})
    assert r.status_code == 200
    # "restart": a brand-new Python process reading the same DB file
    out = subprocess.run(
        [sys.executable, "-c", "import json, app; print(json.dumps(app.all_documents()))"],
        cwd=ROOT, capture_output=True, text=True, check=True,
        env={**os.environ, "EXPIRYWATCH_DB": appmod.DB_PATH}).stdout
    d = json.loads(out)[0]
    assert (d["filename"], d["holder"], d["expiry"], d["status"]) == (
        "renamed.pdf", "Alex B.", "2031-01-15", "ok")


def test_edit_validation(client):
    upload_all(client, ["10_safety_certificate_en.pdf"])
    i = client.get("/api/documents").get_json()[0]["id"]
    assert client.post(f"/api/documents/{i}", json={"filename": "a.pdf", "expiry": "31.12.2026"}).status_code == 400
    assert client.post(f"/api/documents/{i}", json={"filename": "", "expiry": ""}).status_code == 400
    assert client.post("/api/documents/9999", json={"filename": "a"}).status_code == 404


# ---- acceptance: CSV --------------------------------------------------------

def test_csv_excel_friendly(client):
    upload_all(client)
    raw = client.get("/export.csv").data
    assert raw.startswith(b"\xef\xbb\xbf")  # BOM -> Excel reads UTF-8
    rows = list(csv.reader(io.StringIO(raw.decode("utf-8-sig")), delimiter=";"))
    assert rows[0][:5] == ["File name", "Type", "Holder", "Expiry date", "Days left"]
    assert len(rows) == 11 and all(len(x) == 7 for x in rows)
    assert any("Чистый Дом" in x[2] for x in rows)  # Cyrillic survives
    assert any("Kaubavedu OÜ" in x[2] for x in rows)


def test_csv_formula_injection_neutralised():
    assert appmod._safe("=HYPERLINK(1)").startswith("'")
    assert appmod._safe("normal") == "normal"


# ---- acceptance: --check ----------------------------------------------------

def test_check_lists_exactly_under_60_days(client):
    upload_all(client)
    out = subprocess.run([sys.executable, os.path.join(ROOT, "app.py"), "--check"],
                         capture_output=True, text=True, check=True,
                         env={**os.environ, "EXPIRYWATCH_DB": appmod.DB_PATH}).stdout
    listed = {n for n in os.listdir(SAMPLES) if n.endswith(".pdf") and n in out}
    assert listed == {"06_adr_certificate_en.pdf", "02_tehnoulevaatus_et.pdf",
                      "03_cmr_insurance_en.pdf", "04_esmaabi_tunnistus_et.pdf"}
    assert "EXPIRED 40 days ago" in out


def test_check_boundary():
    today = date(2026, 6, 1)
    for days, inside in [(59, True), (60, False), (-5, True)]:
        with appmod.db() as conn:
            conn.execute("DELETE FROM documents")
            conn.execute("INSERT INTO documents (filename, expiry, status, uploaded_at)"
                         " VALUES ('x.pdf', ?, 'ok', 'now')",
                         ((today + timedelta(days=days)).isoformat(),))
        assert bool(appmod.expiring_soon(today=today)) == inside


def test_check_empty(capsys):
    appmod.run_check()
    assert "No documents expiring" in capsys.readouterr().out
