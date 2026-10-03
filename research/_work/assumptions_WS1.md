# Assumptions — WS1 (Market size & structure)

Every ESTIMATE used in `research/01_market_size.md` is listed here with its formula and inputs. Inputs reference VERIFIED sources in `research/_work/sources_WS1.csv` ([V:WS1-xxx]) or other entries in this file ([E:A-WS1-xx]). Arithmetic was computed in code (Python) on 2026-10-03.

Note on IDs: source IDs WS1-005 … WS1-024 are retired (rows written into the WS1 file by another workstream's helper script were removed on 2026-10-03; the same claims live in WS3-001…011 and WS6-001…009). WS1 source numbering resumes at WS1-025.

---

### A-WS1-01 — Estonia: enterprises with 10–249 employees (2024)
- Value: 7,579 enterprises (4.79% of the 158,378 economically active enterprises); for reference, enterprises with <10 employees = 95.1% (150,612 / 158,378)
- Formula: N(10–49) + N(50–249) = 6,461 + 1,118 = 7,579; share = 7,579 / 158,378 = 4.79%; micro share = 150,612 / 158,378 = 95.1%
- Inputs: [V:WS1-003] size classes 2024; [V:WS1-001] total 2024; internal check: 150,612 [V:WS1-002] + 6,461 + 1,118 + 187 = 158,378 (exact).
- Basis/rationale: Statistics Estonia statistical-profile counts by *number of employees* (table ER025/ER026; [V:WS1-004]). Covers all economically active enterprises (all EMTAK sections), so it is broader than the Eurostat SBS "business economy" scope used for Latvia (A-WS1-02).
- Confidence: high (for the count); medium (for comparability with LV/LT)
- Used in: 01_market_size.md §3.1, §3.6 (G1 funnel, step 2), §8 synthesis table

### A-WS1-02 — Latvia: enterprises with 10–49 and 50–249 persons employed (2024 estimate)
- Value: 7,820 enterprises (small 6,457 + medium 1,363); 7.30% of 107,091 enterprises in scope
- Formula: 6,457 + 1,363 = 7,820; total in scope = 99,066 + 6,457 + 1,363 + 205 = 107,091; share = 7,820 / 107,091
- Inputs: [V:WS1-025] EC SME Fact Sheet 2025 (Latvia); [V:WS1-027] 2024 values are JRC estimates based on 2008–2023 data.
- Basis/rationale: No CSB Latvia size-class figure could be extracted (tables UZS030/UZS031 identified, [V:WS1-030]; values not readable via search). The EC fact sheet is the best available harmonised figure. Scope = Eurostat SBS business economy (excludes agriculture, finance and most public/social services) and *persons employed* (includes owners), so it is not strictly comparable to the Estonian national count.
- Confidence: medium
- Used in: 01_market_size.md §3.1, §3.6, §8

### A-WS1-03 — Latvia: average persons employed per small and per medium enterprise (2024 estimate)
- Value: small ≈ 20.4 persons; medium ≈ 98.5 persons
- Formula: 131,493 / 6,457 = 20.4; 134,263 / 1,363 = 98.5
- Inputs: [V:WS1-025] (enterprise counts), [V:WS1-026] (persons employed)
- Basis/rationale: Shows that the average 50–249 firm sits close to the top of the brief's 5–100 staff ICP, i.e. a material part of the "medium" class is above 100 staff. The distribution inside the class is UNKNOWN, so no share is derived from this mean.
- Confidence: medium
- Used in: 01_market_size.md §3.1, §3.6 (step 2 caveat)

### A-WS1-04 — Lithuania: small enterprises (10–49) in 2022
- Value: ≈ 12,815 (range 12,651–12,980)
- Formula: 0.039 × 328,600 = 12,815; range from share rounding: 0.0385 × 328,600 = 12,651 to 0.0395 × 328,600 = 12,980
- Inputs: [V:WS1-033] 328.6 thousand enterprises in operation (2022); [V:WS1-034] small = 3.9% of non-financial enterprises (2022)
- Basis/rationale: Applies the published share to the published total. Assumes the 3.9% share is computed on the same population as the 328.6k total (both from *Business in Lithuania 2023*). Cross-check with 2021: 0.042 × 298,800 = 12,550 ([V:WS1-035], pre-2023) — the small-firm count is stable, growth in the total is driven by very small units.
- Confidence: medium
- Used in: 01_market_size.md §3.1, §3.6, §8

### A-WS1-05 — Lithuania: medium enterprises (50–249) in 2022
- Value: ≈ 2,629 (range 2,465–2,793)
- Formula: 0.008 × 328,600 = 2,629; range 0.0075 × 328,600 = 2,465 to 0.0085 × 328,600 = 2,793
- Inputs: [V:WS1-033], [V:WS1-034]
- Basis/rationale: As A-WS1-04. The one-decimal share makes the rounding band wide (±6%). 2021 cross-check: 0.008 × 298,800 = 2,390 ([V:WS1-035]).
- Confidence: medium-low
- Used in: 01_market_size.md §3.1, §3.6, §8

### A-WS1-06 — Lithuania: enterprises with 10–249 persons employed (2022)
- Value: ≈ 15,444 (range 15,116–15,773)
- Formula: (0.039 + 0.008) × 328,600 = 15,444; range (0.046 to 0.048) × 328,600
- Inputs: [E:A-WS1-04], [E:A-WS1-05]
- Basis/rationale: Sum of the two estimates. Conflicts with an unverified LEAD (EC SME Fact Sheet 2025: 11,348 + 2,244 = 13,592 for 2024, [WS1-039] LEAD) and with the 2019 SBA fact sheet (11,147 + 2,118 = 13,265, c.2018, [V:WS1-036], pre-2023). The national (VDA) basis is preferred because it is an observed count, not a model estimate; the gap (~12%) may also reflect different population definitions. See 01_market_size.md §5.
- Confidence: medium-low
- Used in: 01_market_size.md §3.1, §3.6, §5, §8

### A-WS1-07 — Baltic total: enterprises in the 10–249 band (mixed reference years)
- Value: ≈ 30,843 (range 30,515–31,172)
- Formula: EE 7,579 (2024) + LV 7,820 (2024 est.) + LT 15,444 (2022 est.)
- Inputs: [E:A-WS1-01], [E:A-WS1-02], [E:A-WS1-06]
- Basis/rationale: Order-of-magnitude ceiling for the G1 universe before sector, exclusion, language and reachability filters. Mixes years (2022–2024), scopes (national statistical profile vs SBS business economy) and size measures (employees vs persons employed); do not use for more than order of magnitude.
- Confidence: low-medium
- Used in: 01_market_size.md key findings, §3.6, §8

### A-WS1-08 — G1 funnel structure (statistical-route parameters UNKNOWN; database route in A-WS1-10 to A-WS1-14)
- Value: Statistical-route endpoint = UNKNOWN (s, x, l not sourced); evidence-based upper bound per country = N(10–249) from A-WS1-01 / A-WS1-02 / A-WS1-06. Database-route proxy (before language and sanctions screening) = A-WS1-14.
- Formula: Reachable_c = N2_c × s_c × (1 − x_c) × d_c × l_c, where
  - N2_c = enterprises 10–249 in country c (A-WS1-01, -02, -06); proxy for the brief's 5–100 staff ICP
  - s_c = share of N2_c in the target sectors (C; G46; H49, H51, H52 excl. H52.22, H53; M69; M70, M71.1, M73, M74; N77, N78, N80–N82) — UNKNOWN (resolve: Eurostat sbs_sc_ovw by NACE × size; EE ER025; LV UZS030/UZS031; LT VDA operating-enterprise tables)
  - x_c = share excluded under hard exclusions (Russia/Belarus trade; water transport H50 and H52.22 are already removed by sector definition) — UNKNOWN (resolve: Eurostat TEC partner data / customs exporter lists; manual screening)
  - d_c = share with a findable contact. **Now proxied by the database route (A-WS1-10 to A-WS1-14)** using `research/_work/data/db_coverage.csv` (Hunter Discover, supplied by the lead analyst on 2026-10-03). The database route counts target-sector records directly, so it bypasses s_c; it does not bypass x_c or l_c.
  - l_c = share where English, Russian or Lithuanian is a workable sales language — UNKNOWN (resolve: census language data + interview/test-campaign evidence)
- Inputs: as listed; no parameter values are assumed, to avoid inventing shares.
- Basis/rationale: The brief requires traceable math; with the web-search budget exhausted, sector shares and filter rates could not be sourced, so the funnel is specified but not filled beyond step 2.
- Confidence: n/a (method only)
- Used in: 01_market_size.md §3.6

### A-WS1-09 — G2 sizing method (inputs UNKNOWN in this run)
- Value: UNKNOWN
- Formula (three triangulating routes; take the range, not the sum):
  1. Exporter route: Σ_p E(p → c) for p ∈ {FI, SE, NO, DK, PL, DE, UA, other EU} and c ∈ {EE, LV, LT}, where E = number of enterprises in country p exporting goods to c (Eurostat trade-by-enterprise-characteristics partner tables; national customs exporter statistics). De-duplicate firms exporting to more than one Baltic state (unknown overlap → report upper and lower bound: max_c and Σ_c).
  2. Presence route: foreign-controlled enterprises in c by controlling country (Eurostat inward FATS; CSB Latvia UZG030 [V:WS1-042]; VDA "Foreign-owned enterprises in Lithuania" [V:WS1-043]).
  3. Network route: membership of foreign chambers in each Baltic state (Nordic, German-Baltic AHK, Polish, Ukrainian), de-duplicated.
  Then apply the same s (B2B relevance), x (sanctions) and d/l filters as A-WS1-08.
- Inputs: none verified yet beyond the dataset pointers.
- Confidence: n/a (method only)
- Used in: 01_market_size.md §3.7

### A-WS1-10 — Database coverage: Hunter-listed companies with 11–200 employees (all industries) and ratio to the statistical 10–249 band
- Value: EE 4,675 (61.7% of 7,579); LV 3,268 (41.8% of 7,820); LT 6,116 (39.6% of ≈15,444; range 38.8–40.5%)
- Formula: N_db = results(11-50) + results(51-200); ratio = N_db / N(10–249)
- Inputs: EE 3,562 [V:WS1-046] + 1,113 [V:WS1-047]; LV 2,359 [V:WS1-061] + 909 [V:WS1-062]; LT 4,367 [V:WS1-076] + 1,749 [V:WS1-077]; denominators [E:A-WS1-01], [E:A-WS1-02], [E:A-WS1-06]
- Basis/rationale: The ratio is a crude coverage indicator, not a precise one:
  - Hunter buckets 11–200 are not the statistical 10–249 classes. They miss 10-person firms and 201–249 firms.
  - Records are web domains, not legal units.
  - Headcounts are LinkedIn-style ranges.
  - Per the lead analyst's README caveat 4, the EE count is likely inflated by internationally run firms registered in Estonia (e-Residency), so EE coverage of genuinely Estonian SMEs is overstated.
- Confidence: low-medium
- Used in: 01_market_size.md §3.6 (database route), §5, §8

### A-WS1-11 — Logistics records (Hunter industry 116) with 11–200 employees, excluding maritime-tagged rows
- Value: EE ≈119; LV ≈138; LT ≈292 (upper bound)
- Formula: maritime_est = (maritime_rows / sample_n) × results_total where results_total > sample_n; maritime = maritime_rows (exact) where the sample is the full set. Logistics_ex = results(11-50) + results(51-200) − maritime_est(11-50) − maritime(51-200).
- Inputs:
  - EE: 107 − 18/100×107 (=19.3) [V:WS1-048] + 37 − 6 [V:WS1-049] = 118.7
  - LV: 110 − 12/100×110 (=13.2) [V:WS1-063] + 47 − 6 [V:WS1-064] = 137.8
  - LT: 199 − 0/100×199 [V:WS1-078] + 97 − 4 [V:WS1-079] = 292.0
- Basis/rationale: The brief's hard exclusion (shipowners/ship managers) requires removing Maritime Transportation rows. In LT, 99 of the 199 records in the 11–50 bucket were not sampled, so LT is an upper bound. Airlines/Aviation (≈12% of sampled logistics rows per the README) is **retained** pending an operator decision. Maritime-tagged rows can also include ferry and port operators that are not excluded per se; removing all of them is conservative.
- Confidence: medium (EE, LV); low-medium (LT)
- Used in: 01_market_size.md §3.6

### A-WS1-12 — Target-sector records in Hunter (11–200 employees), approximate NACE mapping
- Value: EE 1,788–2,180; LV 1,447–1,666; LT 2,549–2,903
- Formula: Logistics_ex (A-WS1-11) + Wholesale + Manufacturing + Professional Services × {2/3 (low), 1 (high)} + Administrative and Support Services. Each parent = results(11-50) + results(51-200).
- Inputs:
  - **EE:** Wholesale 105 + 41 [V:WS1-050] [V:WS1-051]; Manufacturing 414 + 170 [V:WS1-052] [V:WS1-053]; Prof. Services 945 + 230 [V:WS1-054] [V:WS1-055]; Admin 118 + 38 [V:WS1-056] [V:WS1-057]
  - **LV:** Wholesale 108 + 44 [V:WS1-065] [V:WS1-066]; Manufacturing 381 + 207 [V:WS1-067] [V:WS1-068]; Prof. Services 534 + 123 [V:WS1-069] [V:WS1-070]; Admin 104 + 27 [V:WS1-071] [V:WS1-072]
  - **LT:** Wholesale 170 + 77 [V:WS1-080] [V:WS1-081]; Manufacturing 740 + 357 [V:WS1-082] [V:WS1-083]; Prof. Services 855 + 206 [V:WS1-084] [V:WS1-085]; Admin 166 + 40 [V:WS1-086] [V:WS1-087]
  - Logistics_ex from [E:A-WS1-11]
- Basis/rationale:
  - The five parents are distinct top-level categories in Hunter's LinkedIn-style taxonomy, so they are summed. Accounting and Business Consulting are nested in Professional Services and are **not** added.
  - The low variant removes IT Services/IT Consulting, which is ≈1/3 of the sampled Professional Services rows (lead analyst's README, research/_work/data/db_coverage_README.md; indicative, from samples ranked by email count). IT services (NACE J62) are not a brief target sector and include competitors.
  - Admin & Support includes Travel Arrangements (≈N79, excluded in §2) and Events. These were not removed (share unknown), so this is a slight overstatement.
  - Mapping to NACE is approximate. "Wholesale" contains manufacturers tagged as wholesalers (README).
- Confidence: low-medium
- Used in: 01_market_size.md §3.6, §8

### A-WS1-13 — Share of database records with at least one indexed email (exact segments only)
- Value: any email 83.0% (778 / 937); personal (named) email 61.0% (572 / 937); per-segment personal range 32.6–85.0%
- Formula: Pool the 22 segments where results_total ≤ 100, where the returned sample is the full result set. Count per segment = round(pct × sample_n / 100).
- Inputs: [V:WS1-049] [V:WS1-051] [V:WS1-057] [V:WS1-058] [V:WS1-059] [V:WS1-060] [V:WS1-091] (EE); [V:WS1-064] [V:WS1-066] [V:WS1-072] [V:WS1-073] [V:WS1-074] [V:WS1-075] [V:WS1-092] [V:WS1-093] (LV); [V:WS1-079] [V:WS1-081] [V:WS1-087] [V:WS1-088] [V:WS1-089] [V:WS1-090] [V:WS1-094] (LT)
- Basis/rationale: For segments above 100 records, the shares are upper bounds, because Hunter ranks results by email count and ignores offsets. The exact segments are mostly 51–200 sector slices and accounting. Applying their pooled rate to all segments is an extrapolation. The any-email figure reproduces the lead analyst's README pooled figure (83%).
- Confidence: low-medium
- Used in: 01_market_size.md §3.6, §4.4

### A-WS1-14 — Database-reachable target-sector firms, 11–200 employees (before language filter and sanctions screening)
- Value:
  - With ≥1 indexed email: EE 1,485–1,810; LV 1,201–1,383; LT 2,117–2,410; Baltic sum 4,803–5,603
  - With ≥1 personal (named) email: EE 1,092–1,331; LV 883–1,017; LT 1,556–1,772; Baltic sum 3,531–4,120
- Formula: A-WS1-12 × A-WS1-13 (0.830 any; 0.610 personal)
- Inputs: [E:A-WS1-12], [E:A-WS1-13]
- Basis/rationale: This is the "technically contactable via a standard enrichment tool" pool. It is **not** market size and **not** yet "plausibly reachable" for this operator:
  - The language-workability factor l_c is still UNKNOWN.
  - The Russia/Belarus trade screen (x_c) has not been applied.
  - Database coverage under-represents offline and traditional SMEs.
  - The LT upper bound inherits the maritime caveat from A-WS1-11.
- Confidence: low-medium
- Used in: 01_market_size.md key findings, §3.6, §8

### A-WS1-15 — Accounting firms listed in Hunter (industry 47), 1–200 employees
- Value: EE 103 records (91 = 88.3% with any email; 63 = 61.2% personal); LV 67 (50 = 74.6%; 28 = 41.8%); LT 131 (113 = 86.3%; 62 = 47.3%)
- Formula: Σ results over buckets 1-10, 11-50 and 51-200 (all are full sets, so the email shares are exact); counts = round(pct × n / 100)
- Inputs: EE [V:WS1-058] [V:WS1-059] [V:WS1-060]; LV [V:WS1-073] [V:WS1-074] [V:WS1-075]; LT [V:WS1-088] [V:WS1-089] [V:WS1-090]
- Basis/rationale: Indicates how many accounting firms an enrichment tool can surface. The README notes misclassifications (for example, a security firm and a state audit office tagged Accounting). The statistical M69.20 population is UNKNOWN (U9), so database coverage of accountants cannot yet be expressed as a ratio.
- Confidence: medium (counts), low (as a coverage indicator)
- Used in: 01_market_size.md §4.4, §8
