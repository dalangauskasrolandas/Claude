# ExpiryWatch

Local web app that reads business PDFs (licences, inspections, insurance, certificates) and tracks expiry dates.

## Setup (3 steps)

1. Install Python 3.11+ and run: `pip install -r requirements.txt`
2. Optional test data: `python make_samples.py` (creates 10 fake PDFs in `samples/`)
3. Run `python app.py`, open http://localhost:5000, drop PDFs on the page.

Data is stored in `expirywatch.db` next to `app.py`. Nothing leaves your computer.

## Usage

- **Colours:** red = expired or <7 days, orange = <30, yellow = <60, green = otherwise, grey = needs review / scanned.
- **Edit:** click *Edit*, change any field, *Save*. A saved row with a date counts as verified (OK).
- **CSV:** *Export CSV* (UTF-8 with BOM, `;` separated, opens directly in Excel with European settings).
- **Alerts:** `python app.py --check` prints documents expiring within 60 days (including expired). Schedule it with cron / Task Scheduler.
- **Tests:** `python -m pytest`

## Known limitations

- No OCR: scanned PDFs are marked "Scanned, needs manual entry".
- Numeric dates are read day-first (`05/06/2026` = 5 June). US-style numeric dates will be wrong; 2-digit years are not recognised.
- Months are recognised only in English, Estonian and Russian. Inflected Estonian forms (e.g. "detsembril") are not.
- Document type and holder come from a keyword list and `Label: value` lines. Unusual layouts give blank or wrong values (edit manually).
- Several different dates with expiry labels, or a single unlabelled date, are flagged "needs review" rather than guessed.
- CSV uses `;`. In an Excel set to a comma separator, use Data > From Text/CSV and pick `;`.
- Uploaded PDFs are not stored, only the extracted fields. No login: the server listens on 127.0.0.1 only.
- The same file uploaded twice creates two rows.
