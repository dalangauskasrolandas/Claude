"""Text extraction and field detection (type, holder, expiry date) for ExpiryWatch."""
import re
from datetime import date

import pdfplumber

# --------------------------------------------------------------------------- text

def extract_text(file_or_path):
    """Return the text of all pages ('' if none). Raises on unreadable PDFs."""
    parts = []
    with pdfplumber.open(file_or_path) as pdf:
        for page in pdf.pages:
            parts.append(page.extract_text() or "")
    return "\n".join(parts).strip()


# --------------------------------------------------------------------------- dates

_MONTHS = {}


def _add_months(names, abbrevs=()):
    for i, name in enumerate(names, start=1):
        _MONTHS[name] = i
    for abbr, i in abbrevs:
        _MONTHS[abbr] = i


_add_months(
    ["january", "february", "march", "april", "may", "june", "july", "august",
     "september", "october", "november", "december"],
    [("jan", 1), ("feb", 2), ("mar", 3), ("apr", 4), ("jun", 6), ("jul", 7),
     ("aug", 8), ("sep", 9), ("sept", 9), ("oct", 10), ("nov", 11), ("dec", 12)])
_add_months(  # Estonian (nominative)
    ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august",
     "september", "oktoober", "november", "detsember"],
    [("jaan", 1), ("veebr", 2), ("märts", 3), ("okt", 10), ("dets", 12)])
_add_months(  # Russian (genitive, as used in dates) + nominative
    ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа",
     "сентября", "октября", "ноября", "декабря"],
    [("январь", 1), ("февраль", 2), ("март", 3), ("апрель", 4), ("май", 5),
     ("июнь", 6), ("июль", 7), ("август", 8), ("сентябрь", 9), ("октябрь", 10),
     ("ноябрь", 11), ("декабрь", 12)])

_NUM_DMY = re.compile(r"(?<![\d.])(\d{1,2})([./-])(\d{1,2})\2(\d{4})(?!\d)")
_NUM_ISO = re.compile(r"(?<![\d.])(\d{4})([./-])(\d{1,2})\2(\d{1,2})(?!\d)")
_TXT_DMY = re.compile(r"(?<!\d)(\d{1,2})(?:st|nd|rd|th)?\.?\s*([^\W\d_]{3,9})\.?,?\s+(\d{4})(?!\d)")
_TXT_MDY = re.compile(r"(?<![^\W\d_])([^\W\d_]{3,9})\.?\s+(\d{1,2})(?:st|nd|rd|th)?,?\s+(\d{4})(?!\d)")


def _mk(y, m, d):
    try:
        if 1990 <= y <= 2100:
            return date(y, m, d)
    except ValueError:
        pass
    return None


def find_dates(text):
    """Return [(date, start, end)] for every recognised date, in text order."""
    found = []
    for m in _NUM_ISO.finditer(text):
        dt = _mk(int(m[1]), int(m[3]), int(m[4]))
        if dt:
            found.append((dt, m.start(), m.end()))
    for m in _NUM_DMY.finditer(text):
        dt = _mk(int(m[4]), int(m[3]), int(m[1]))  # day first (European)
        if dt:
            found.append((dt, m.start(), m.end()))
    for m in _TXT_DMY.finditer(text):
        mon = _MONTHS.get(m[2].lower())
        dt = _mk(int(m[3]), mon, int(m[1])) if mon else None
        if dt:
            found.append((dt, m.start(), m.end()))
    for m in _TXT_MDY.finditer(text):
        mon = _MONTHS.get(m[1].lower())
        dt = _mk(int(m[3]), mon, int(m[2])) if mon else None
        if dt:
            found.append((dt, m.start(), m.end()))
    found.sort(key=lambda x: (x[1], -(x[2] - x[1])))
    result, last_end = [], -1
    for item in found:  # drop overlapping matches
        if item[1] >= last_end:
            result.append(item)
            last_end = item[2]
    return result


EXPIRY_LABELS = [
    "valid until", "valid to", "valid through", "valid thru", "valid till", "validity",
    "expiry date", "expiration date", "date of expiry", "expires", "expiry", "expiration",
    "expire date", "exp. date", "good until", "policy period", "period of validity",
    "insurance period", "kehtiv kuni", "kehtib kuni", "kehtivusaeg", "kehtivus",
    "kehtiv", "kindlustusperiood", "срок действия", "действителен до", "действительно до",
    "действует до", "годен до", "период действия", "срок страхования",
]
IGNORE_LABELS = [  # a date right after these is NOT the expiry date
    "date of issue", "issue date", "issued", "date of birth", "birth date", "born",
    "policy start", "start date", "valid from", "effective date", "inspection date",
    "date of inspection", "väljaantud", "välja antud", "sünniaeg", "sünnikuupäev",
    "kehtiv alates", "ülevaatuse kuupäev", "koolitus lõpetatud", "дата выдачи", "выдан",
    "выдано", "дата рождения", "действителен с", "дата начала",
]


def _label_re(labels):
    alt = "|".join(re.escape(x) for x in sorted(labels, key=len, reverse=True))
    return re.compile(r"(?<![^\W\d_])(?:%s)(?![^\W\d_])" % alt, re.I)


_EXPIRY_RE = _label_re(EXPIRY_LABELS)
_IGNORE_RE = _label_re(IGNORE_LABELS)
_RANGE_SEP = re.compile(r"^\s*(?:-|–|—|to|until|till|kuni|до|по)\s*$", re.I)
MAX_GAP = 25  # max characters between a label and its date


def _label_before(regex, text, start):
    """Gap length to the closest label ending before `start` (None if none close)."""
    best = None
    for m in regex.finditer(text, max(0, start - 60), start):
        gap = text[m.end():start]
        if len(gap) <= MAX_GAP and not re.search(r"\d", gap):
            best = len(gap) if best is None else min(best, len(gap))
    return best


def detect_expiry(text):
    """Return (iso_date_or_None, needs_review, note)."""
    dates = find_dates(text)
    if not dates:
        return None, True, "No date found"

    labelled, loose = [], []  # [(gap, date)], [date]
    for i, (dt, s, e) in enumerate(dates):
        # range "01.01.2026 - 31.12.2026": the end date inherits the start's label
        prev_range = i > 0 and _RANGE_SEP.match(text[dates[i - 1][2]:s])
        next_range = i + 1 < len(dates) and _RANGE_SEP.match(text[e:dates[i + 1][1]])
        if next_range:
            continue  # start of a range, never the expiry
        look_from = dates[i - 1][1] if prev_range else s
        if _label_before(_IGNORE_RE, text, look_from) is not None and not prev_range:
            continue
        gap = _label_before(_EXPIRY_RE, text, look_from)
        if gap is not None:
            labelled.append((gap, dt))
        else:
            loose.append(dt)

    if labelled:
        distinct = {d for _, d in labelled}
        best = min(labelled, key=lambda x: x[0])[1]
        if len(distinct) == 1:
            return best.isoformat(), False, ""
        return best.isoformat(), True, "Several different expiry dates found"
    distinct = sorted(set(loose))
    if len(distinct) == 1:
        return distinct[0].isoformat(), True, "Date has no expiry label"
    if not distinct:
        return None, True, "Only issue/start dates found"
    return None, True, "Several dates, none labelled as expiry"


# --------------------------------------------------------------------------- type

DOC_TYPES = [  # first match wins; title (first 3 lines) is searched before the whole text
    ("CMR insurance", [r"\bcmr\b.*(insur|kindlust|страхов)", r"(insur|kindlust|страхов).*\bcmr\b"]),
    ("Insurance", [r"insurance", r"kindlustus", r"страхов"]),
    ("Vehicle inspection", [r"vehicle inspection", r"technical inspection", r"tehnoülevaatus",
                            r"tehnoyl", r"ülevaatus", r"техосмотр", r"технический осмотр"]),
    ("Driving licence", [r"driving licen[cs]e", r"juhiluba", r"водительск"]),
    ("First-aid certificate", [r"first[- ]aid", r"esmaabi", r"первой помощи"]),
    ("ADR certificate", [r"\badr\b"]),
    ("Licence", [r"licen[cs]e", r"tegevusluba", r"litsents", r"\bluba\b", r"лицензи"]),
    ("Certificate", [r"certificate", r"tunnistus", r"сертификат", r"свидетельство", r"удостоверение"]),
]


def detect_type(text):
    title = "\n".join(text.splitlines()[:3]).lower()
    body = text.lower()
    for haystack in (title, body):
        for name, patterns in DOC_TYPES:
            if any(re.search(p, haystack, re.S) for p in patterns):
                return name
    return "Other"


# --------------------------------------------------------------------------- holder

HOLDER_LABELS = ["holder", "name", "insured", "licensee", "owner", "company", "contractor",
                 "employee", "service provider", "omanik", "nimi", "kindlustusvõtja",
                 "teenuseosutaja", "ettevõte", "лицензиат", "страхователь", "владелец",
                 "держатель", "фио", "организация", "компания"]
VEHICLE_LABELS = ["registreerimismärk", "reg. no", "reg no", "registration number", "plate",
                  "number plate", "vehicle", "sõiduk", "гос. номер", "госномер",
                  "транспортное средство", "автомобиль"]


def _labelled_value(text, labels):
    for label in labels:  # list order = priority
        m = re.search(r"(?im)^[ \t]*(?:[^\W\d_]+[ \t]+)?%s[ \t]*:[ \t]*(.+?)[ \t]*$"
                      % re.escape(label), text)
        if m:
            return m.group(1).strip()
    return ""


def detect_holder(text):
    parts = [v for v in (_labelled_value(text, HOLDER_LABELS),
                         _labelled_value(text, VEHICLE_LABELS)) if v]
    return " / ".join(parts)


# --------------------------------------------------------------------------- entry

def analyse(text):
    """Analyse extracted text -> dict(doc_type, holder, expiry, status, note)."""
    if len(text.strip()) < 5:
        return dict(doc_type="", holder="", expiry=None, status="scanned",
                    note="Scanned, needs manual entry")
    expiry, review, note = detect_expiry(text)
    return dict(doc_type=detect_type(text), holder=detect_holder(text), expiry=expiry,
                status="review" if review else "ok", note=note)
