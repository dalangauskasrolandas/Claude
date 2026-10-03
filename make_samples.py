"""Generate 10 fake PDFs (EN / ET / RU) into ./samples plus samples/expected.json.

Dates are relative to today so the colour buckets are always exercised:
expired, 10 days, 25 days, 45 days, and far-future.
"""
import json
import os
from datetime import date, timedelta

from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "samples")
TODAY = date.today()

FONT_CANDIDATES = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/dejavu/DejaVuSans.ttf",
    "/Library/Fonts/Arial Unicode.ttf",
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "C:/Windows/Fonts/arial.ttf",
]

ET_MONTHS = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli",
             "august", "september", "oktoober", "november", "detsember"]
RU_MONTHS = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля",
             "августа", "сентября", "октября", "ноября", "декабря"]
EN_MONTHS = ["January", "February", "March", "April", "May", "June", "July",
             "August", "September", "October", "November", "December"]


def register_font():
    for path in FONT_CANDIDATES:
        if os.path.exists(path):
            pdfmetrics.registerFont(TTFont("Body", path))
            return "Body"
    raise SystemExit("No Unicode TTF font found (needed for Cyrillic). "
                     "Edit FONT_CANDIDATES in make_samples.py.")


def dmy_dot(d): return f"{d.day:02d}.{d.month:02d}.{d.year}"
def dmy_slash(d): return f"{d.day:02d}/{d.month:02d}/{d.year}"
def iso(d): return d.isoformat()
def long_et(d): return f"{d.day}. {ET_MONTHS[d.month - 1]} {d.year}"
def long_ru(d): return f"{d.day} {RU_MONTHS[d.month - 1]} {d.year}"
def long_en(d): return f"{d.day} {EN_MONTHS[d.month - 1]} {d.year}"


def d(days): return TODAY + timedelta(days=days)


def samples():
    """(filename, expected expiry or None, lines)."""
    exp = {k: d(v) for k, v in dict(
        lic=1100, insp=10, cmr=25, aid=45, biz=400, adr=-40, ins=120,
        clinic=200).items()}
    return [
        ("01_driving_licence_en.pdf", exp["lic"], [
            "DRIVING LICENCE", "Republic of Estonia",
            "Holder: John Smith", "Date of birth: 12.03.1985",
            "Categories: B, C, CE", f"Date of issue: {iso(d(-700))}",
            f"Valid until: {iso(exp['lic'])}"]),
        ("02_tehnoulevaatus_et.pdf", exp["insp"], [
            "SÕIDUKI TEHNOÜLEVAATUSE TÕEND", "Registreerimismärk: 123 ABC",
            "Sõiduk: Volvo FH16 veoauto", "Omanik: Kaubavedu OÜ",
            f"Ülevaatuse kuupäev: {dmy_dot(d(-355))}",
            f"Kehtiv kuni {dmy_dot(exp['insp'])}"]),
        ("03_cmr_insurance_en.pdf", exp["cmr"], [
            "CMR CARRIER'S LIABILITY INSURANCE POLICY", "Policy No: CMR-2025-88412",
            "Insured: Baltic Haulage Ltd", "Vehicle: MAN TGX, reg. 456 DEF",
            f"Policy start: {dmy_slash(d(-340))}",
            f"Expires: {dmy_slash(exp['cmr'])}"]),
        ("04_esmaabi_tunnistus_et.pdf", exp["aid"], [
            "ESMAABI KOOLITUSE TUNNISTUS", "Tunnistuse omanik: Mari Tamm",
            f"Koolitus lõpetatud: {long_et(d(-320))}",
            f"Tunnistus kehtiv kuni {long_et(exp['aid'])}"]),
        ("05_litsenziya_ru.pdf", exp["biz"], [
            "ЛИЦЕНЗИЯ НА ОСУЩЕСТВЛЕНИЕ ДЕЯТЕЛЬНОСТИ", "Лицензиат: ООО «Чистый Дом»",
            "Вид деятельности: клининговые услуги",
            f"Срок действия: {long_ru(exp['biz'])}"]),
        ("06_adr_certificate_en.pdf", exp["adr"], [
            "ADR DRIVER TRAINING CERTIFICATE", "Name: Peter Jones",
            f"Issued: {dmy_dot(d(-1500))}",
            f"Valid until: {dmy_dot(exp['adr'])}"]),
        ("07_strahovanie_ru.pdf", exp["ins"], [
            "СТРАХОВОЙ ПОЛИС ГРАЖДАНСКОЙ ОТВЕТСТВЕННОСТИ", "Страхователь: ИП Иванов Сергей",
            f"Дата выдачи: {dmy_dot(d(-245))}",
            f"Договор действителен до {long_ru(exp['ins'])}"]),
        ("08_tegevusluba_et.pdf", exp["clinic"], [
            "TERVISHOIUTEENUSE TEGEVUSLUBA", "Teenuseosutaja: Hea Tervis Kliinik OÜ",
            f"Väljaantud: {dmy_dot(d(-1000))}",
            f"Luba kehtiv kuni {dmy_dot(exp['clinic'])}"]),
        # Two unlabeled dates -> must be flagged, not guessed.
        ("09_inspection_record_en.pdf", None, [
            "VEHICLE INSPECTION RECORD", "Vehicle: Ford Transit, reg. 789 GHI",
            f"Dates: {dmy_dot(d(-30))} and {dmy_dot(d(335))}"]),
        # No date at all.
        ("10_safety_certificate_en.pdf", None, [
            "SITE SAFETY INDUCTION CERTIFICATE", "Name: Alex Brown",
            "Contractor: BuildRight Contractors Ltd",
            "Completed the site safety induction course."]),
    ]


def write_pdf(path, lines, font):
    c = canvas.Canvas(path, pagesize=A4)
    y = 780
    c.setFont(font, 16)
    c.drawString(60, y, lines[0])
    c.setFont(font, 12)
    for line in lines[1:]:
        y -= 28
        c.drawString(60, y, line)
    c.save()


def main():
    os.makedirs(OUT, exist_ok=True)
    font = register_font()
    expected = {}
    for name, expiry, lines in samples():
        write_pdf(os.path.join(OUT, name), lines, font)
        expected[name] = expiry.isoformat() if expiry else None
    with open(os.path.join(OUT, "expected.json"), "w", encoding="utf-8") as f:
        json.dump(expected, f, indent=2)
    print(f"Wrote {len(expected)} PDFs to {OUT}")


if __name__ == "__main__":
    main()
