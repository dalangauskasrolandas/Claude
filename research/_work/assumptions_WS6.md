# Assumptions — WS6 (Reachability & first-client channels)

All inputs trace to `research/_work/sources_WS6.csv` (WS6-…) or to other workstream fragments where cross-referenced (WS2-…, WS3-…). Prepared 2026-10-03.

### A-WS6-01 — Weekday/daytime share of verified in-window events
- Value: 19 of 19 verified events in the Oct 2026 – Mar 2027 window (100%) fall on Tuesday–Friday; 0 fall on a weekend. Every event with published hours runs in business hours.
- Formula: count of VERIFIED-date events in `06_channels_reachability.md` §3.2 grouped by weekday. Weekdays were computed from the calendar dates with Python `datetime` (e.g. 17.11.2026 = Tue; 08.10.2026 = Thu; 27.01.2027 = Wed; 18.03.2027 = Thu).
- Inputs: EE (13 events): [V:WS6-010] [V:WS6-011] [V:WS6-012] [V:WS6-013] [V:WS6-014] [V:WS6-015] [V:WS6-018]; LV (2): [V:WS6-021] [V:WS6-023]; LT (4): [V:WS6-024] [V:WS6-025] [V:WS6-027]. Published hours: RUP.ee 08:55–17:05 [V:WS6-010]; RIGA COMM 10:00–17:00 and 10:00–16:00 [V:WS6-021]; LiMA DAY'26 09:00–19:00 [V:WS6-025].
- Basis/rationale: dates come from organiser pages or the organiser's media kit. Where hours are not published, a daytime conference format is assumed, because these are one- or two-day business conferences at hotels or conference venues.
- Confidence: high for dates; medium for hours where they are not published.
- Used in: 06 §1 Key findings; §3.2; §3.6.

### A-WS6-02 — Working days of leave needed to attend a minimal in-person event shortlist
- Value: 8 working days, plus 0–3 travel days for the Latvian and Lithuanian events, i.e. 8–11 days of leave from the day job.
- Formula: Σ event days attended = RUP.ee (1) + Pereettevõtjate aastakonverents (1) + Logistika aastakonverents (1) + sTARTUp Day (1 of 3) + RIGA COMM (1 of 2) + Transport Innovation Forum (1 of 2) + GROW BEYOND (2) = 8; plus a travel allowance of 0–3 days (assumption).
- Inputs: [V:WS6-010] [V:WS6-013] [V:WS6-014] [V:WS6-018] [V:WS6-021] [V:WS6-024] [V:WS6-027]; all on weekdays [E:A-WS6-01].
- Basis/rationale: the shortlist is the smallest set that touches each country plus the accounting, logistics and SME-owner audiences. The travel allowance is an assumption; Tallinn–Riga and Tallinn–Vilnius travel times were not verified.
- Confidence: medium (event days); low (travel).
- Used in: 06 §3.6; §8 Synthesis inputs.

### A-WS6-03 — Event ticket cost vs the operator's €200–500 budget
- Value: the lowest published ticket at each of the three events with verified prices costs €109–359. Together they total €707, which exceeds the whole €200–500 budget. One TechChill General pass (€359) on its own exceeds the €200 lower bound.
- Formula: 239 (RUP.ee discounted; eligibility for the discount unknown) + 109 (sTARTUp Day Startup ticket) + 359 (TechChill General) = 707. Share of the €500 upper budget: 109/500 = 22%; 239/500 = 48%; 349/500 = 70%; 359/500 = 72%.
- Inputs: [V:WS6-010] (€349 regular / €239 discounted); [V:WS6-019] (€109–169); [V:WS6-023] (€359 General). Budget from BRIEF §2.
- Basis/rationale: published organiser prices. Travel and accommodation are excluded. Ticket prices for the Bonnier B2B conferences, the PwC conference, RIGA COMM, the Transport Innovation Forum, GROW BEYOND and LiMA DAY were not obtained (UNKNOWN).
- Confidence: high (arithmetic); medium (whether the operator qualifies for discounted or startup tiers).
- Used in: 06 §1 Key findings; §3.2; §3.6.

### A-WS6-04 — Outreach volume needed to recruit 15–20 owner interviews per country (sensitivity)
- Value: 75–400 contacts per country (225–1,200 across the three countries), depending on the acceptance rate. Using a single sector association's member list alone would need a 23–48% acceptance rate.
- Formula: contacts = target interviews ÷ acceptance rate r. Target = 15–20 per country (BRIEF §5 WS6). r is assumed at 20% / 10% / 5%, giving 15/0.20 = 75 … 20/0.05 = 400. Single-list required r = target ÷ members: ELEA 15/65 = 23% to 20/65 = 31%; LINEKA 15/42 = 36% to 20/42 = 48%. Time at an assumed 5–10 minutes per personalised contact: 75 × 5 = 375 min (6.3 h) up to 400 × 10 = 4,000 min (66.7 h) per country. In calendar weeks at the operator's 10–20 h/week: 6.3 / 20 = 0.3 weeks up to 66.7 / 10 = 6.7 weeks per country, if all side-hours went to recruitment.
- Inputs: ELEA 65 members incl. 13 associates [V:WS6-007]; LINEKA 42 members [V:WS6-008]. The acceptance rate and minutes per contact are assumptions; no public benchmark for B2B owner-interview acceptance in the Baltics was retrieved (UNKNOWN).
- Basis/rationale: arithmetic sensitivity only, to size the capacity need against 10–20 h/week.
- Confidence: low (r unknown); high for the single-list ceiling arithmetic.
- Used in: 06 §3.7; §7 UNKNOWNs.

### A-WS6-05 — Async/evening-fit scoring rubric (1–5; 5 = fully async-compatible)
- Value: rubric definitions:
  - 5 = entirely async; no live client contact needed.
  - 4 = mostly async; live contact is occasional and can be scheduled early morning, evening or by recorded video.
  - 3 = mixed; recurring live sessions with client staff, likely in business hours (discovery workshops, user training).
  - 2 = mostly live daytime work.
  - 1 = needs on-site daytime presence.
- Formula: analyst judgement against the rubric.
- Inputs: LV EDIH catalogue CRM packages bundle live implementation and training hours (12 h implementation + 3 h training) [V:WS3-018], and 12 h implementation support plus 1 h/month maintenance [V:WS3-017]. All verified events are weekday daytime [E:A-WS6-01].
- Basis/rationale: no time-use study of SME service delivery was retrieved; the scores are explicit judgements for the synthesis and should be revisited after discovery interviews.
- Confidence: low–medium.
- Used in: 06 §3.6; §8 Synthesis inputs.
