# Assumptions — verification pass (WS9 = combined verifier, 2026-10-03)

All inputs trace to `research/sources.csv` (WS*, VL-xxx rows), `research/_work/data/db_coverage.csv` or other assumption entries. Recomputation script: `research/_work/data/VER_recompute.py` (stdlib only).

### A-WS9-01 — E-mail availability rates pooled over in-scope (≤50-staff) exact Hunter segments only
- Value: any indexed e-mail 84.5%, personal (named) e-mail 51.9% (n = 374 companies in 7 exact segments). WS1's pooled rate over all 22 exact segments: 83.0% and 61.0% (n = 937).
- Formula: Σ(results_total × share) ÷ Σ results_total, over segments whose full result set was sampled (results_total ≤ 100) and whose headcount bucket is 1-10 or 11-50. The 7 segments are Accounting 1-10 and 11-50 in EE, LV and LT (286 records) plus LV Business Consulting 11-50 (88 records). Query ids in `db_coverage.csv`: EE-ACC-1-10, EE-ACC-11-50, LV-ACC-1-10, LV-ACC-11-50, LV-BCS-11-50, LT-ACC-1-10, LT-ACC-11-50.
- Inputs: `db_coverage.csv` columns `results_total`, `sample_n`, `pct_any_email`, `pct_personal_email`; [E:A-WS1-13] for the pooled-22 comparison.
- Basis/rationale: 15 of the 22 segments WS1 pooled sit in the 51-200 bucket (out of scope since the scope change), so the pooled rate describes larger firms. Restricting to in-scope buckets cuts the personal-e-mail share by 9 percentage points and leaves the any-e-mail share about the same. The 7 in-scope segments are accounting-dominated (micro accounting firms have the lowest personal-e-mail rates), so 51.9% is a lower bracket for the target mix, not a point estimate. For the large target segments only upper bounds exist (top-100 sample by e-mail count).
- Confidence: low
- Used in: 01_market_size.md §3.6 (D3, D4'), §8; verification_log.md

### A-WS9-02 — Corrected ≤50-staff database-reachable pools with a named (personal) e-mail
- Value: target-sector firms with ≥1 personal e-mail, Hunter 1-10 + 11-50: EE 2,254–3,381; LV 1,416–2,036; LT 2,657–3,793. In the 11-50 bucket only: EE 703–1,019; LV 542–747; LT 957–1,300. Any-e-mail pools are unchanged from [E:A-WS1-20] (re-computed values agree within ±2).
- Formula: low = low target count × 51.9% [E:A-WS9-01]; high = high target count × 61.0% [E:A-WS1-13]. Target counts (low–high): EE 4,345–5,539 (11-50: 1,355–1,670); LV 2,729–3,336 (1,046–1,224); LT 5,123–6,213 (1,845–2,130) [E:A-WS1-20].
- Inputs: [E:A-WS1-20], [E:A-WS1-13], [E:A-WS9-01]
- Basis/rationale: brackets the e-mail-rate uncertainty instead of fixing the rate at the pooled-22 value, which mixes in out-of-scope 51-200 segments. Counts are vendor-database records (web domains), not legal entities or market size, and are before the language, sanctions and maritime-adjacent screens.
- Confidence: low
- Used in: 01_market_size.md "Scope ≤50 staff" table, §3.6, §8; verification_log.md

### A-WS9-03 — Lithuania 10–49 class: working range instead of a point estimate
- Value: 11,348 (EC/JRC 2024 estimate; unverified LEAD WS1-039) to 12,815 (VDA shares × total, 2022, pre-2023). Treat 12,815 as a ceiling.
- Formula: upper = 0.039 × 328,600 = 12,815 [E:A-WS1-04]; lower = LEAD value.
- Inputs: [V:WS1-033] total enterprises in operation (2022); [V:WS1-034] size shares of non-financial enterprises (2022); [V:WS1-098] shares of SMEs (2022); [V:WS1-037] about 100,000 legal-entity SMEs; LEAD WS1-039.
- Basis/rationale: the 3.9% share belongs to non-financial enterprises but was applied to the all-enterprise total, and the 12.2% share belongs to a smaller SME population than the 328.6 thousand total. Both effects can only push the true figure down. The search on 2026-10-03 found no newer VDA edition [V:VL-017].
- Confidence: low-medium
- Used in: 01_market_size.md §3.1, §3.6, §8; verification_log.md

### A-WS9-04 — Single-association acceptance rate needed for 15–20 interviews, with corrected member counts
- Value: ELEA (65–68 members) needs 22–31% acceptance; LINEKA (42–60 members) needs 25–48%.
- Formula: 15/68 = 22.1% … 20/65 = 30.8%; 15/60 = 25.0% … 20/42 = 47.6%.
- Inputs: [V:WS6-007] 65 members; LEAD VL-021 68 members; [V:WS6-008] 42 members (undated); [V:VL-022] 60 members (report dated 17 Apr 2021, pre-2023)
- Basis/rationale: replaces the single-count arithmetic of [E:A-WS6-04] where two counts exist. Member lists include firms above 50 staff; ELEA's average member size of 91 employees (LEAD VL-021) suggests many members are out of scope.
- Confidence: medium (arithmetic); low (counts)
- Used in: 06_channels_reachability.md §3.7; verification_log.md

### A-WS9-05 — Ticket total for the three events with published prices
- Value: EUR 707 using the lowest listed tickets; EUR 837 using regular or visitor tickets; budget EUR 200–500.
- Formula: 239 + 109 + 359 = 707; 349 + 129 + 359 = 837.
- Inputs: [V:WS6-010] (EUR 349 regular, EUR 239 discounted); [V:WS6-019] (EUR 109 Startup, EUR 129 Visitor); [V:WS6-023] (EUR 359 General)
- Basis/rationale: EUR 109 is the Startup ticket and EUR 239 a discounted tier; eligibility for either is unknown for this operator.
- Confidence: high (arithmetic)
- Used in: 06_channels_reachability.md §1; verification_log.md
