# Assumptions register (every ESTIMATE input with its basis)

Merged from workstream fragments in `_work/`. IDs `A-WSn-xx` are referenced in the workstream files as `[E:A-WSn-xx]`. Each entry gives value, formula, inputs (VERIFIED source IDs from `sources.csv` or other assumptions), rationale, confidence, and where it is used.


---

## WS1 (24 entries)

## Assumptions — WS1 (Market size & structure)

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

### A-WS1-04 — Lithuania: small enterprises (10–49) in 2022 (pre-2023)
- Value: ≈ 12,815 (range 12,651–12,980)
- Formula: 0.039 × 328,600 = 12,815; range from share rounding: 0.0385 × 328,600 = 12,651 to 0.0395 × 328,600 = 12,980
- Inputs: [V:WS1-033] 328.6 thousand enterprises in operation (2022); [V:WS1-034] small = 3.9% of non-financial enterprises (2022)
- Basis/rationale: Applies the published share to the published total. Assumes the 3.9% share is computed on the same population as the 328.6k total (both from *Business in Lithuania 2023*). Cross-check with 2021: 0.042 × 298,800 = 12,550 ([V:WS1-035], pre-2023) — the small-firm count is stable, growth in the total is driven by very small units.
- Confidence: medium
- Used in: 01_market_size.md §3.1, §3.6, §8

### A-WS1-05 — Lithuania: medium enterprises (50–249) in 2022 (pre-2023)
- Value: ≈ 2,629 (range 2,465–2,793)
- Formula: 0.008 × 328,600 = 2,629; range 0.0075 × 328,600 = 2,465 to 0.0085 × 328,600 = 2,793
- Inputs: [V:WS1-033], [V:WS1-034]
- Basis/rationale: As A-WS1-04. The one-decimal share makes the rounding band wide (±6%). 2021 cross-check: 0.008 × 298,800 = 2,390 ([V:WS1-035]).
- Confidence: medium-low
- Used in: 01_market_size.md §3.1, §3.6, §8

### A-WS1-06 — Lithuania: enterprises with 10–249 persons employed (2022, pre-2023)
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

---

## Gap-fill pass (2026-10-03) — scope change to ≤50 staff

Scope note: on 2026-10-03 the user narrowed the target to companies with **up to 50 staff**. From here on the in-scope size classes are 0–9 and 10–49 (statistics) and 1-10 and 11-50 (Hunter buckets). The 50–249 class (and Hunter 51-200) is out of scope and kept only for reference; A-WS1-06, A-WS1-07, A-WS1-10 to A-WS1-14 describe the earlier 10–249 / 11–200 proxy and are superseded for the funnel by A-WS1-16 to A-WS1-21. A-WS1-08's formula still applies, with N2_c = enterprises with ≤50 staff.

### A-WS1-16 — Estonia: ≤50-staff universe (2025)
- Value: 0–49 employees = 158,489 (0–9: 152,205; 10–49: 6,284); 10–49 = 3.93% of all 159,827 enterprises; reference only (out of scope): 10–249 = 7,435
- Formula: 152,205 + 6,284 = 158,489; 6,284 / 159,827 = 3.93%; 6,284 + 1,151 = 7,435; check 152,205 + 6,284 + 1,151 + 187 = 159,827 (exact)
- Inputs: [V:WS1-095]
- Basis/rationale: Statistics Estonia economic-units page, 2025 reference year, by employees. The 0–9 class includes one-person firms and cannot be split at 5 employees from published data, so 10–49 is the conservative core. The 2024 values ([V:WS1-001], [V:WS1-003]) are superseded, not contradicted.
- Confidence: high (counts)
- Used in: 01_market_size.md §1, §3.1, §3.6, §8

### A-WS1-17 — Estonia: target-sector envelope, 10–49 employees (2025)
- Value: 1,191–3,481 enterprises (lower = manufacturing only; upper = sections C + G + H + M + N = 55.4% of the 10–49 class)
- Formula: upper = 1,191 (C) + 1,036 (G) + 472 (H) + 407 (M) + 375 (N) = 3,481; 3,481 / 6,284 = 55.4%; lower = C = 1,191
- Inputs: [V:WS1-096] (C, G, H), [V:WS1-097] (M, N), [E:A-WS1-16]
- Basis/rationale: Only section C maps fully to a §2 target sector. Section totals for G, H, M and N include out-of-scope divisions (G45 motor trade and G47 retail; H50 water transport and H52.22, which are hard exclusions; M71.2 testing and M75 veterinary; N79 travel agencies), so they are upper bounds. Division-level counts (G46 etc.) remain UNKNOWN (resolve: ER025 at 2–4 digits). Micro class (0–9): sections M = 23,994 and N = 8,003 are known [V:WS1-097]; C, G and H micro counts are UNKNOWN, so no 0–9 envelope is computed.
- Confidence: high (section counts); low (as a target-sector count)
- Used in: 01_market_size.md §1, §3.2, §3.6, §8

### A-WS1-18 — Latvia: ≤50-staff universe (2024 estimate)
- Value: 105,523 enterprises (0–9: 99,066; 10–49: 6,457)
- Formula: 99,066 + 6,457 = 105,523
- Inputs: [V:WS1-025]
- Basis/rationale: EC SME Fact Sheet 2025 (JRC model estimate for 2024, SBS business-economy scope, persons employed). No CSB value could be extracted.
- Confidence: medium
- Used in: 01_market_size.md §3.1, §3.6, §8

### A-WS1-19 — Lithuania: ≤50-staff universe (2022, pre-2023)
- Value: 0–9 ≈ 312,827 (312,663–312,992); 0–49 ≈ 325,643 (325,314–325,971); 10–49 ≈ 12,815 (A-WS1-04)
- Formula: 0.952 × 328,600 = 312,827 (range 0.9515–0.9525 × 328,600); (0.952 + 0.039) × 328,600 = 325,643 (range 0.990–0.992 × 328,600)
- Inputs: [V:WS1-033] (total 2022), [V:WS1-034] (size shares 2022), [E:A-WS1-04]
- Basis/rationale: Same share × total method as A-WS1-04, with the same population caveat (shares of non-financial enterprises applied to all enterprises in operation; the total includes natural persons engaged in business). Cross-check for the 10–49 class: small firms were 12.2% of SMEs in 2022 [V:WS1-098]; with ≈100,000 legal-entity SMEs at the start of 2023 [V:WS1-037] that is ≈12,200, consistent with 12,815. The EC 2024 estimate (11,348 small) is still a LEAD (WS1-039; re-seen in a 2026-10-03 extract, URL not pinned).
- Confidence: medium (10–49); low (0–9, population definition)
- Used in: 01_market_size.md §3.1, §3.6, §8

### A-WS1-20 — Database-reachable target-sector firms with ≤50 staff (Hunter buckets 1-10 + 11-50)
- Value:
  - Target-sector records, 1-10 + 11-50: EE 4,345–5,539; LV 2,729–3,336; LT 5,123–6,213 (11-50 alone: EE 1,355–1,670; LV 1,046–1,224; LT 1,845–2,130)
  - With ≥1 indexed email (× 0.830): EE 3,606–4,598; LV 2,265–2,769; LT 4,252–5,157 (11-50 alone: EE 1,124–1,386; LV 868–1,016; LT 1,531–1,768)
  - With a personal email (× 0.610): EE 2,650–3,379; LV 1,665–2,035; LT 3,125–3,790 (11-50 alone: EE 826–1,019; LV 638–747; LT 1,125–1,299)
  - All-industry records 1-10 + 11-50: EE 11,930; LV 6,609; LT 12,794. Coverage indicator, 11-50 records ÷ statistical 10–49 class: EE 56.7%; LV 36.5%; LT 34.1%
  - Accounting (industry 47) records, 1-10 + 11-50: EE 97; LV 63; LT 126
- Formula: per bucket b ∈ {1-10, 11-50}: Logistics_ex(b) = results(b) − maritime_rows/sample × results(b); target(b) = Logistics_ex + Wholesale + Manufacturing + Admin + Professional Services × {2/3 (low), 1 (high)}; pool = Σ_b target(b) × email rate (A-WS1-13). Coverage = ALL(11-50) / N(10–49).
- Inputs:
  - EE 1-10: ALL 8,368 [V:WS1-134]; LOG 142, maritime 18/100 [V:WS1-135]; WHS 166 [V:WS1-136]; MFG 610 [V:WS1-137]; PRO 2,639 [V:WS1-138]; ADM 338 [V:WS1-139]. EE 11-50: ALL 3,562 [V:WS1-046]; LOG 107, maritime 18/100 [V:WS1-048]; WHS 105 [V:WS1-050]; MFG 414 [V:WS1-052]; PRO 945 [V:WS1-054]; ADM 118 [V:WS1-056]
  - LV 1-10: ALL 4,250 [V:WS1-140]; LOG 116, maritime 14/100 [V:WS1-141]; WHS 113 [V:WS1-142]; MFG 416 [V:WS1-143]; PRO 1,285 [V:WS1-144]; ADM 198 [V:WS1-145]. LV 11-50: ALL 2,359 [V:WS1-061]; LOG 110, maritime 12/100 [V:WS1-063]; WHS 108 [V:WS1-065]; MFG 381 [V:WS1-067]; PRO 534 [V:WS1-069]; ADM 104 [V:WS1-071]
  - LT 1-10: ALL 8,427 [V:WS1-146]; LOG 231, maritime 7/100 [V:WS1-147]; WHS 220 [V:WS1-148]; MFG 822 [V:WS1-149]; PRO 2,414 [V:WS1-150]; ADM 412 [V:WS1-151]. LT 11-50: ALL 4,367 [V:WS1-076]; LOG 199, maritime 0/100 [V:WS1-078]; WHS 170 [V:WS1-080]; MFG 740 [V:WS1-082]; PRO 855 [V:WS1-084]; ADM 166 [V:WS1-086]
  - Accounting: [V:WS1-058] [V:WS1-059] (EE); [V:WS1-073] [V:WS1-074] (LV); [V:WS1-088] [V:WS1-089] (LT)
  - Email rates [E:A-WS1-13]; statistical 10–49: [V:WS1-095], [V:WS1-025], [E:A-WS1-04]
- Basis/rationale: Same method as A-WS1-11 to A-WS1-14, applied to the in-scope buckets. Hunter's 1-10 bucket contains firms with 10 staff (statistical class 10–49) and many one- to four-person firms that are unlikely buyers. The pooled email rates come mostly from 51-200 and accounting segments; the 1-10 accounting segments show lower personal-email rates (32.6–55.1%), so the ≤50 email pools lean high. LT logistics in 11-50 is an upper bound (no maritime rows in the top-100 sample of 199). Vendor database, not a register: reachability proxy, not market size.
- Confidence: low-medium
- Used in: 01_market_size.md §1, §3.6, §4.4, §8

### A-WS1-21 — Latvia: Russia/Belarus exporter bound for the exclusion filter x
- Value: 400–618 enterprises exported goods to Russia and/or Belarus in Jan–Nov 2023 = 0.38–0.59% of Latvia's ≤50-staff enterprises; even if every one of them were a 10–49 firm, ≤9.6% of that class
- Formula: lower = max(400, 218) = 400 (full overlap); upper = 400 + 218 = 618 (no overlap); 400 / 105,523 = 0.38%; 618 / 105,523 = 0.59%; 618 / 6,457 = 9.6%
- Inputs: [V:WS1-123], [E:A-WS1-18], [V:WS1-025]
- Basis/rationale: Exporter counts cover firms of all sizes and goods only, so the shares are upper bounds for the share of in-scope firms trading with RU/BY in goods. Services trade and indirect links (re-export, Russian ownership) are not covered. Trend: 1,013 / 490 firms in 2021 [V:WS1-124]. EE and LT equivalents are UNKNOWN.
- Confidence: medium (counts); low (as x for target sectors)
- Used in: 01_market_size.md §1, §3.3, §3.6, §8

### A-WS1-22 — Estonia: share of population able to speak Russian (2021)
- Value: ≈68%
- Formula: 29% (Russian mother tongue) + 39% (Russian spoken as a foreign language) = 68%
- Inputs: [V:WS1-099], [V:WS1-100]
- Basis/rationale: In the census, foreign languages are languages other than the respondent's mother tongue, so the two groups do not overlap (analyst reading of census definitions; rounding ±1 pp). Population of all ages, not business owners.
- Confidence: medium
- Used in: 01_market_size.md §1, §3.5, §4.1, §8

### A-WS1-23 — Lithuania: Russian mother-tongue share, lower bound (2021)
- Value: ≥ ≈4.6% (≈129,500 people)
- Formula: 141,100 ethnic Russians × 0.918 = 129,530; population = 2,378,000 / 0.846 = 2,810,875; 129,530 / 2,810,875 = 4.61%
- Inputs: [V:WS1-106]
- Basis/rationale: Counts only ethnic Russians who declared Russian as mother tongue. People of other ethnicity (e.g., Poles, Belarusians, Ukrainians) with Russian as mother tongue are not included, so this is a lower bound.
- Confidence: medium (as a lower bound)
- Used in: 01_market_size.md §1, §3.5, §8

### A-WS1-24 — G2 network route: verified foreign-chamber memberships (lower bound)
- Value: ≈900 memberships, not de-duplicated
- Formula: AHK Baltic 470 + Scandinavian Chamber EE 130 + Norwegian Chamber LV 100 + Norwegian-Lithuanian Chamber 100 + Swedish Chamber LT 100 = 900 ("more than", "about" and "close to" values taken at face value)
- Inputs: [V:WS1-110], [V:WS1-112], [V:WS1-113], [V:WS1-114], [V:WS1-115]
- Basis/rationale: Lower bound for the network route of A-WS1-09. Excluded for lack of a verified count: Finnish chambers (FCCL 36 corporate members in 2020 is a LEAD, WS1-116), Swedish and Danish chambers in LV, Polish and Ukrainian chambers ([V:WS1-117], [V:WS1-118], [V:WS1-119]), AmChams and investor councils. Members include Baltic-registered firms and large corporations; the ≤50-staff filter cannot be applied. Presence route context: 11% of Estonian enterprises are foreign-controlled (2023) [V:WS1-109].
- Confidence: low
- Used in: 01_market_size.md §1, §3.7, §4.2, §8


---

## WS2 (12 entries)

## Assumptions — WS2 (Digital maturity & demand signals)

Format per CONVENTIONS.md. Every ESTIMATE used in `research/02_demand_signals.md` traces to an entry here. Inputs point to `research/_work/sources_WS2.csv` (or, where stated, another workstream's fragment).

### A-WS2-01 — Capacity of the Estonian AI-adoption grant (number of companies funded)
- Value: 100 companies at the full EUR 2.0M budget; 55 companies at the EUR 1.1M initially planned for the 2026 round.
- Formula: 2,000,000 / 20,000 = 100; 1,100,000 / 20,000 = 55.
- Inputs: [V:WS2-001] total budget EUR 2,000,000 and unit price EUR 20,000; [V:WS2-003] EUR 1.1M planned for the year; ERR's own "55 instead of 100" companies.
- Basis/rationale: the grant is a fixed unit price per company, so capacity = budget / unit price. The ERR-reported 55 and 100 match the arithmetic. Because the round closed the day it opened with the budget exhausted, at least 55 applications (lower bound) arrived within about one business day.
- Confidence: high (arithmetic on verified inputs). The lower bound on applications is medium, because it is unclear whether EUR 1.1M or EUR 2.0M was available on 24.08.2026.
- Used in: 02_demand_signals.md § 1 Key findings; § 5.1 Estonia; § 8.4; § 9 (C3)

### A-WS2-02 — Implied minimum project value behind one EUR 20,000 AI grant
- Value: about EUR 25,000 per project.
- Formula: 20,000 / (1 − 0.20) = 25,000.
- Inputs: [V:WS2-001] unit price EUR 20,000; self-financing 20%.
- Basis/rationale: assumes the 20% self-financing is a share of total project cost.
- Confidence: medium. The unit-price mechanism may not require cost documentation at this level.
- Used in: 02_demand_signals.md § 5.1 Estonia (row EE-1)

### A-WS2-03 — EE RTE software grant: implied project size and ceiling on paid digital-advisor fees
- Value: project size about EUR 4,000–10,000. Grant money for the advisor is at most EUR 2,500 per project. If the 50% rate also applies to the advisor's invoice, that invoice is about EUR 5,000 at most.
- Formula: project = grant / 0.50, so 2,000 / 0.50 = 4,000 and 5,000 / 0.50 = 10,000. Advisor share of aid ≤ 0.50 × 5,000 = 2,500. Advisor invoice ≈ 2,500 / 0.50 = 5,000.
- Inputs: [V:WS2-007] EUR 2,000–5,000 grant, 50% self-financing; [V:WS2-009] advisor fees ≤ 50% of project support; [V:WS2-010] grant paid as a fixed amount.
- Basis/rationale: an upper-bound reading. Because the grant is paid as a fixed amount, it is not confirmed how co-financing maps onto individual cost lines.
- Confidence: low–medium.
- Used in: 02_demand_signals.md § 1 Key findings; § 5.1 Estonia (row EE-4)

### A-WS2-04 — EE advisory & development grant: project size at which the EUR 35,000 cap binds
- Value: EUR 50,000 (at 70% support) to EUR 70,000 (at 50% support).
- Formula: 35,000 / 0.70 = 50,000; 35,000 / 0.50 = 70,000.
- Inputs: [V:WS2-005] max grant EUR 35,000; self-financing 30–50% (so support is 50–70%).
- Basis/rationale: above these project sizes the client pays everything beyond the cap.
- Confidence: medium. The support rate depends on aid basis and location: [V:WS2-012] gives 50% for Tallinn/Harju/Tartu and 70% elsewhere for the related roadmap grant (2024).
- Used in: 02_demand_signals.md § 5.1 Estonia (row EE-3)

### A-WS2-05 — Implied hourly rate of EIS-procured digital mentors (price anchor)
- Value: about EUR 147–149 per hour excl. VAT.
- Formula: 4,460 / 30 = 148.7 (total quoted price). The co-financing figures imply a base of 661.50 / 0.15 = 4,410 and 882 / 0.20 = 4,410, so 4,410 / 30 = 147.0.
- Inputs: [V:WS2-015] 30-hour service = EUR 4,460 total; company co-financing EUR 661.50 (15%) or EUR 882 (20%).
- Basis/rationale: the two bases differ by EUR 50, which is unexplained (UNKNOWN; possibly a fixed fee). Both give an hourly rate of about EUR 147–149.
- Confidence: medium.
- Used in: 02_demand_signals.md § 5.1 Estonia (row EE-9); § 9 (C4); § 12 notes for WS5

### A-WS2-06 — Latvia new digitalisation programme: average budget per targeted beneficiary
- Value: about EUR 15,779 per business.
- Formula: 27,613,228 / 1,750 = 15,779.
- Inputs: [V:WS2-021] total EUR 27,613,228; at least 1,750 businesses; grants capped at EUR 10,000.
- Basis/rationale: the average is above the EUR 10,000 cap. So either the budget also funds a larger strand (the AI strand of up to EUR 200,000 in [V:WS2-022]), or 1,750 is a minimum target that will be exceeded. This is a consistency check, not a forecast.
- Confidence: low (interpretive).
- Used in: 02_demand_signals.md § 9 (C5)

### A-WS2-07 — Latvia: share of the new programme already reserved (if the EUR 5.4M refers to it)
- Value: about 19.6% reserved and about 80% unreserved at the (undated) article date.
- Formula: 5.4 / 27.613 = 0.196.
- Inputs: [V:WS2-023] EUR 5.4M reserved, funding still available; [V:WS2-021] EUR 27,613,228 total.
- Basis/rationale: assumes the EUR 5.4M article refers to the EUR 27.6M programme. Neither article's date is visible, and [V:WS2-026] separately says "most of the funding already reserved", possibly for the earlier EUR 37.5M programme.
- Confidence: low.
- Used in: 02_demand_signals.md § 5.2 Latvia (demand signals)

### A-WS2-08 — Latvia RRF digitalisation programme: sales-process share and average request
- Value: about 49.4% of applications were for sales-process digitalisation (incl. websites, CRM, booking, payments); average request about EUR 12,687 per application.
- Formula: 1,438 / 2,908 = 0.494; 36,892,501 / 2,908 = 12,687.
- Inputs: [V:WS2-069] 2,908 applications, EUR 36,892,501 requested; [V:WS2-070] 1,438 sales-process applications.
- Basis/rationale: CRM is only one item in the sales-process group, so the CRM-specific share is UNKNOWN (lower than 49.4%).
- Confidence: medium (the two figures may come from two LIAA pages of slightly different dates).
- Used in: 02_demand_signals.md § 1; § 5.2; § 12

### A-WS2-09 — Lithuania AI-solutions call: capacity and implied project size
- Value: about 53 projects at the EUR 70,000 maximum, up to 250 at the EUR 15,000 minimum; implied project size EUR 30,000–140,000.
- Formula: 3,750,000 / 70,000 = 53.6; 3,750,000 / 15,000 = 250; 15,000 / 0.50 = 30,000; 70,000 / 0.50 = 140,000.
- Inputs: [V:WS2-035] EUR 3.75M total, EUR 15,000–70,000 per project, up to 50%.
- Basis/rationale: assumes aid at the 50% maximum; lower aid rates imply larger projects.
- Confidence: medium.
- Used in: 02_demand_signals.md § 5.3

### A-WS2-10 — Lithuania small grants: number of firms fundable
- Value: about 27 firms ("palydimosios subsidijos 2026") and about 166 firms (digital SME vouchers) at maximum grant.
- Formula: 408,000 / 15,000 = 27.2; 1,000,000 / 6,000 = 166.7.
- Inputs: [V:WS2-042] EUR 408,000 total, ≤ EUR 15,000 each; [V:WS2-043] EUR 1,000,000 total, ≤ EUR 6,000 each.
- Basis/rationale: lower bounds on recipients; smaller grants mean more recipients.
- Confidence: high (arithmetic).
- Used in: 02_demand_signals.md § 5.3

### A-WS2-11 — Estonia: consistency check 22% (2025) vs 34% (2026)
- Value: about 33% expected for 2026 from 22% × 1.5, consistent with the published 34%.
- Formula: 0.22 × 1.5 = 0.33.
- Inputs: [V:WS2-049] 22% in 2025; [V:WS2-050] 34% in 2026, growth 1.5× among enterprises.
- Basis/rationale: shows the two Statistics Estonia figures are successive survey years, not conflicting definitions (rounding explains 33% vs 34%).
- Confidence: high.
- Used in: 02_demand_signals.md § 2; § 9 (C7)

### A-WS2-12 — Lithuania: AI-use growth multiple 2024 → 2025
- Value: about 2.4× (21.3% / 8.8%), +12.5 pp.
- Formula: 21.3 / 8.8 = 2.42; 21.3 − 8.8 = 12.5.
- Inputs: [V:WS2-057] 8.8% (2024), 21.3% (2025); [V:WS2-054] Eurostat +12.5 pp for Lithuania.
- Basis/rationale: the +12.5 pp matches Eurostat's published increase, which triangulates the LRT figures.
- Confidence: medium-high.
- Used in: 02_demand_signals.md § 1; § 2; § 9 (C8)


---

## WS3 (6 entries)

## Assumptions — WS3 Competitor map

All inputs trace to `research/_work/sources_WS3.csv` (WS3-xxx), the lead analyst's `sources_WS0.csv` (WS0-xxx) or `sources_WS2.csv` (WS2-xxx). Accessed 2026-10-03.

### A-WS3-01 — Implied service value and hourly rate inside a Latvian grant-catalogue Pipedrive package
- Value: about €1,990 of services per package, about €83 per hour (low confidence)
- Formula: licence cost per user-month L = (P10 − P5) / (5 extra users × 12 months) = (3,990 − 2,990) / 60 = €16.67. Service value S = P5 − (5 users × 12 months × L) = 2,990 − 1,000 = €1,990. Included hours H = 12 h implementation + 12 × 1 h monthly support = 24 h. Implied rate = S / H = 1,990 / 24 ≈ €82.9/h.
- Inputs: [V:WS3-017] P5 = €2,990 excl. VAT (Essential, 5 users, 12 months, 12 h implementation + 1 h/month support); [V:WS3-018] P10 = €3,990 excl. VAT (Essential, 10 users, 12 months, same service hours).
- Basis/rationale: the 5→10-user price step is treated as pure licence cost, and the service hours are taken to be the same in both packages. Any margin on licences is counted as "service", so the true hourly rate could be lower. The catalogue listing date is UNKNOWN. The plan names (Essential/Advanced/Professional) may predate a Pipedrive plan rename, so the price may be pre-2025.
- Confidence: low
- Used in: 03_competitors.md § 6 Price bands (LV, CRM setup); § 12 Synthesis inputs

### A-WS3-02 — Ripe Leads first-year cost and average monthly cost
- Value: €35,100 in the first year, an average of €2,925 per month (excl. VAT)
- Formula: 3,750 + 11 × 2,850 = 35,100; 35,100 / 12 = 2,925
- Inputs: [V:WS3-008] €3,750 for month 1, then €2,850 per month
- Basis/rationale: simple arithmetic. It matches the vendor's own "roughly €35,100" first-year figure (same source).
- Confidence: high
- Used in: 03_competitors.md § 1 Key findings; § 6 Price bands (lead gen)

### A-WS3-03 — Lower bound on providers in the Latvian EDIH catalogue's business-process sections
- Value: at least 45 distinct provider names
- Formula: count of distinct provider names in the provider filters of three dih.lv "Biznesa procesi" catalogue URLs returned by WebSearch (filters: administrative; sales + resource management; operations + sales + resource management). Parsed list: `research/_work/data/WS3_dih_providers.csv`.
- Inputs: [V:WS3-042] (LEAD; filter URLs), extract file above
- Basis/rationale: providers show up in a filter only if they have listings in those categories. Only three filter states and pages 2–3 were seen, so the real total is probably higher. Not all 45 sell CRM, automation or sales tools: the list includes web, e-commerce, document-management, telecom and accounting/ERP vendors (e.g. Visma Enterprise, Tet).
- Confidence: medium that at least 45 such providers exist in these catalogue sections; low that all of them compete with the operator
- Used in: 03_competitors.md § 1 Key findings; § 4 (LV); § 7 Gaps (LV); § 12 Synthesis inputs

### A-WS3-04 — Most a digital consultant can be paid from the Estonian EIS business-software (RTE) grant, and the implied project size
- Value: up to €2,500 of aid per company can pay a digital consultant; total eligible project up to about €10,000
- Formula: consultant share = max aid €5,000 × 50% (consultant fees up to 50% of aid) = €2,500. Project size = max aid / (1 − 50% self-financing) = 5,000 / 0.5 = €10,000.
- Inputs: [V:WS2-007] (aid €2,000–5,000; 50% self-financing; consultant fees up to 50% of aid); [V:WS2-010] (a digital consultant must be involved)
- Basis/rationale: my reading of WS2's summary of the EIS terms. WS2 owns the grant facts, and the exact eligible-cost rules may differ.
- Confidence: medium-low
- Used in: 03_competitors.md § 6 Price bands (EE); § 7 Gaps G-8

### A-WS3-05 — Rubric for competition-intensity scores (1–5, where 5 = least competition)
- Value: scoring rubric used in § 9
- Formula/rubric:
  - 1 = a dominant, established player in this country × component, plus at least 5 local providers with published fixed offers.
  - 2 = at least 3 identified providers serve this country × component (verified via a vendor directory or the provider's own pages), including at least one that claims all-Baltic EN + RU + local-language coverage.
  - 3 = 1–2 identified providers, OR the cell was not adequately searched (neutral default, flagged "provisional").
  - 4 = providers exist but none in the operator's languages or delivery model.
  - 5 = no providers found after a thorough search in EN + the local language + RU.
- Inputs: the provider identifications in § 2–4 (source IDs cited per cell in § 9)
- Basis/rationale: a transparent, count-based rubric. Counts are lower bounds from about thirty searches, so scores lean towards "more competition is unseen" (they can only fall as more searching is done).
- Confidence: medium for cells scored 2; low for cells scored 3 (provisional)
- Used in: 03_competitors.md § 12 Synthesis inputs

### A-WS3-06 — Fontakt CRM price per included user per month
- Value: €89.80 (Regular) and €134.90 (Full) per included user per month
- Formula: 449 / 5 users = 89.8; 1,349 / 10 users = 134.9
- Inputs: [V:WS3-005] Regular €449/month including 5 users; Full €1,349/month including 10 users (extra users €49 each)
- Basis/rationale: per-user anchor for a bundled "CRM software + local service" offer in Estonia. Setup hours are billed on top at €110/h.
- Confidence: high (arithmetic)
- Used in: 03_competitors.md § 6 Price bands (EE, CRM support/retainer)


---

## WS4 (1 entries)

## WS4 assumptions (legal-risk scoring)

WS4 makes no numeric market estimates. The only ESTIMATE-type inputs are the judgement-based legal-risk scores used in `04_legal_compliance.md` §8 (Synthesis inputs). Their rubric is recorded here so the scores are traceable and can be re-scored when UNKNOWNs are resolved.

### A-WS4-01 — Legal-risk scoring rubric (1–5, 5 = lowest legal risk for the operator)
- Value: per country × component scores (A CRM setup, B AI/workflow automation, C outbound lead generation) as listed in `04_legal_compliance.md` §8.
- Formula: start from 5 and deduct one point for each of the following that applies (minimum 1):
  1. the core activity needs prior consent from recipients, or the statutory text leaves it unclear whether consent is needed for B2B recipients;
  2. a material sub-case the operator would routinely hit (for example named-employee work addresses, sole traders, LinkedIn messages) has no regulator position or verified statutory answer;
  3. the activity necessarily involves third-party personal data from sources whose lawfulness the operator cannot control (enrichment databases, scraping) or transfers to non-EU sub-processors;
  4. the rule changed recently (2025–2026) or EU-level obligations are in flux (for example the Digital Omnibus on AI), so there is little or no supervisory practice to rely on;
  5. there is evidence of active enforcement in the specific area in that country (not applied in this session because no 2020–2026 case could be verified; this is a known downward-risk gap).
  Add back one point (maximum 5) where a primary source explicitly permits the activity under conditions a solo operator can meet in practice (for example an opt-out link in every message).
- Inputs: [V:WS4-001] [V:WS4-004] [V:WS4-005] (EE); [V:WS4-011] [V:WS4-016] [V:WS4-019] [V:WS4-013] (LV); [V:WS4-028] [V:WS4-031] [V:WS4-034] [V:WS4-036] (LT); EU-level items are UNKNOWN-P in this session (GDPR, AI Act, transfers).
- Basis/rationale: an ordinal judgement, not a probability. It ranks how much legal uncertainty and compliance burden each country × component combination puts on a one-person operator. It is not a forecast of fines.
- Confidence: low–medium. EE and LV outbound scores rest on verified statute and DPA text. The LT outbound score rests partly on secondary sources (employee scope). All A and B scores rest on unverified EU-level knowledge.
- Used in: `04_legal_compliance.md` § Key findings (bullet 10) and §8 Synthesis inputs.


---

## WS5 (38 entries)

## Assumptions — WS5 (Pricing, unit economics & tooling)

Every model input used in `research/05_pricing_unit_economics.md` and `research/_work/data/WS5_models.py`. Format per CONVENTIONS.md. Evidence was gathered via web-search extracts on 2026-10-03. Direct page fetching was blocked except for claude.com and GitHub. The session-wide WebSearch budget ran out after 24 WS5 queries.

**Reading guide.** Tax and VAT inputs (A-WS5-01…07) rest on VERIFIED primary sources. Price levels (A-WS5-13, 19, 25) are anchored to VERIFIED published Baltic prices found by WS2/WS3. Hours, churn and tool-cost allowances are ESTIMATES. No benchmark could be retrieved for these in this run, so each has a range and enters the sensitivity tables. No vendor list price that went unverified is used as a fact anywhere. Unverified cost items are explicit allowances.

---

## A. Tax and VAT (Estonia, 2026)

### A-WS5-01 — FIE tax formula (official mechanism, 2026)
- Value: net = 0.5865 × P (58.65% of profit), where social tax S = 0.2481 × P and income tax IT = 0.1654 × P.
- Formula: P = revenue excl. VAT − deductible business expenses. S = 0.33 × P / 1.33 (capped at €36,867.60 in 2026). IT = 0.22 × (P − S). Net = P − S − IT = P × 0.78 / 1.33.
- Inputs: [V:WS5-001] social tax 33%; [V:WS5-002] FIE social tax is computed by dividing business income after expenses by 1.33; [V:WS5-004] social tax is not a business expense; [V:WS5-007] income tax applies to the social-tax-adjusted business income; [V:WS5-006] 22% income tax in 2026. The statute wording is a LEAD (WS5-005, act version uncertain).
- Basis/rationale: this matches the brief ("22% income tax and 33% social tax on profit; social tax is deductible") when "deductible" means the statutory 1.33 divisor. Social tax is deducted from its own base and from the income-tax base. A literal reading (S = 0.33 × P; IT = 0.22 × (P − S)) gives net = 0.5226 × P. That is 6.4 percentage points too low, and it appears only as a sensitivity row.
- Confidence: high
- Used in: 05 §3, §6, §7; WS5_models.py `tax_fie()`

### A-WS5-02 — No basic exemption available on FIE income
- Value: €0 of basic exemption applied to FIE profit. Every euro of FIE profit is taxed at 22% income tax.
- Formula: n/a
- Inputs: [V:WS5-006] the 2026 basic exemption is €700/month (€8,400/year) regardless of income, and the "tax hump" is abolished.
- Basis/rationale: the operator has a full-time salary (BRIEF §2), which already uses the €700/month exemption, assuming the exemption application sits with the employer. Because the 2026 exemption no longer tapers with income, side income does not claw back any exemption, so the marginal rate is a flat 22%.
- Confidence: high (if the salary is ≥ €700/month and the exemption is claimed at the employer)
- Used in: 05 §3; WS5_models.py

### A-WS5-03 — No social-tax minimum or quarterly advances
- Value: €0 social-tax advances. Social tax is due only on actual profit, assessed from the annual return (form E).
- Formula: the exemption applies if the employer's social tax for the operator is ≥ €877.14 per quarter (= 886 × 3 × 0.33).
- Inputs: [V:WS5-003], [V:WS5-001]
- Basis/rationale: any full-time salary at or above the €886 monthly rate meets the condition. Without employment, the minimum would be at least €3,508.56 a year (= 4 × €877.14, derived from [V:WS5-003]), which by itself would exceed the operator's €200–500 budget.
- Confidence: high
- Used in: 05 §3, §8.3

### A-WS5-04 — II-pillar (funded pension) variant
- Value: F = 0.02 × P / 1.33 = 1.50% of P at the default 2% rate. Net cash = 0.5747 × P if F is deductible from the income-tax base, or 0.5714 × P if it is not.
- Formula: IT = 0.22 × (P − S − F) (deductible case)
- Inputs: [V:WS5-010] EMTA computes the FIE contribution from social-tax-adjusted business income; it is not a business expense on form E but is shown in table 9.1 of form A.
- Basis/rationale: deductibility is inferred from the contribution appearing on form A, and is not explicitly confirmed. The difference is 0.33 percentage points, so it is immaterial. F is the operator's own pension saving, not a cost, so it is shown as a variant only. The 4% or 6% rates are optional.
- Confidence: medium (rule) / low (deductibility)
- Used in: 05 §3, §6.4; WS5_models.py `tax_fie(ii_pillar=True)`

### A-WS5-05 — Social-tax cap not binding
- Value: the cap binds only at P ≥ €148,588.
- Formula: 36,867.60 / 0.33 × 1.33 = 148,588
- Inputs: [V:WS5-002]
- Basis/rationale: modelled profits are far below this.
- Confidence: high
- Used in: 05 §3

### A-WS5-06 — Entrepreneur-account variant (foreign clients only; eligibility UNKNOWN)
- Value: tax = 20% of gross receipts (22% with the 2% II pillar). Costs are not deductible. Receipts must stay ≤ €40,000/year. Net = 0.80 × receipts − costs.
- Formula: net = R × (1 − 0.20) − C
- Inputs: [V:WS5-018]. A conflicting LEAD is WS5-019 (a July 2025 act version gave 22% from 2026; EMTA's 2026 page says 20%, and EMTA is trusted).
- Basis/rationale: Estonian resident legal persons paying into the account owe an extra 22/78 (28.2%) on top [V:WS5-018], which makes it unusable for Estonian B2B clients. EMTA's wording targets resident payers. Several points are UNKNOWN: whether foreign (LV/LT) legal persons may pay into the account without restriction, whether it can coexist with FIE registration, and any other activity restrictions.
- Confidence: low (eligibility)
- Used in: 05 §6.4, §8.2; WS5_models.py `tax_entre_account()`

### A-WS5-07 — VAT treatment in the model
- Value: prices are excl. VAT. The operator is not VAT-registered in the base case, and tool and subscription costs carry 24% non-deductible VAT (multiplier 1.24).
- Formula: tool cost incl. VAT = list price × 1.24
- Inputs: [V:WS5-011] 24% standard rate; [V:WS5-012] the €40,000 registration threshold counts only Estonian place-of-supply turnover; [V:WS5-014] B2B services to LV/LT businesses are taxed in the customer's state; [V:WS5-015] limited-taxable-person self-assessment applies to services bought from abroad; [V:WS5-016] Art. 214(1)(e).
- Basis/rationale: B2B clients deduct VAT, so output VAT does not change the price. A non-registered FIE cannot deduct input VAT on tools. Foreign SaaS VAT is either self-assessed under the limited-taxable-person regime or charged by the supplier. Voluntary registration would recover tool VAT but adds monthly returns (hours UNKNOWN).
- Confidence: medium
- Used in: 05 §8.1; WS5_models.py `VAT`

## B. Capacity and overhead

### A-WS5-08 — Working weeks per year
- Value: 46
- Formula: 52 − 6
- Inputs: none (ESTIMATE)
- Basis/rationale: about 6 weeks lost to holidays, day-job peaks and illness for an evenings-and-weekends operator.
- Confidence: medium-low
- Used in: 05 §7; WS5_models.py `WEEKS_PER_YEAR`

### A-WS5-09 — Weekly hours scenarios
- Value: 10 / 15 / 20 h per week
- Formula: n/a
- Inputs: BRIEF §2 (10–20 h/week)
- Basis/rationale: given by the brief.
- Confidence: high
- Used in: 05 §7

### A-WS5-10 — Fixed non-client hours
- Value: 72 h per year
- Formula: bookkeeping and invoicing 12 (1 h/month) + annual tax return 4 + tool upkeep and learning 48 (4 h/month) + miscellaneous 8
- Inputs: ESTIMATE
- Basis/rationale: FIE bookkeeping and form E/A filing [V:WS5-002], plus the upkeep needed to stay current on n8n/Make, CRM and AI tools.
- Confidence: medium-low
- Used in: 05 §7; WS5_models.py `FIXED_ADMIN_H`

### A-WS5-11 — Fixed annual overhead (€, incl. VAT)
- Value: low €363 / base €606 / high €1,980
- Formula: Claude subscription (USD) × 0.86 × 1.24 + other allowance
- Inputs: Claude Pro is $200/yr on annual billing (low) or 12 × $20 = $240/yr monthly (base). Max "from $100/month" = $1,200/yr (high) [V:WS5-020]. The other allowance (domain, business e-mail, accounting software, bank fees, insurance) is €150 / €350 / €700. Prices for these items are UNKNOWN in this run.
- Basis/rationale: Claude is the only verified price. The rest is an explicit allowance to be replaced by verified quotes (search plan items SP-14…SP-19).
- Confidence: low
- Used in: 05 §7, §8.3; WS5_models.py `OVERHEAD`

### A-WS5-12 — FX rate
- Value: €0.86 per USD
- Formula: n/a
- Inputs: ESTIMATE (working rate, not an ECB fixing)
- Basis/rationale: used only to convert Claude prices. A ±10% FX move shifts base overhead by about €26 a year, which is immaterial.
- Confidence: low (immaterial)
- Used in: WS5_models.py `FX`

## C. CRM setup model

### A-WS5-13 — CRM setup price levels (excl. VAT)
- Value: €1,200 / €2,500 / €5,000
- Formula: low ≈ 11 h × €110/h; mid = 50% × €5,000; high = €5,000
- Inputs: low comes from the Fontakt setup-work rate of €110/h [V:WS3-005], roughly the 12 h of implementation bundled in the LV EDIH Pipedrive packages [V:WS3-017]. Mid is the EIS RTE software-adoption grant cap, where consultant fees are ≤ 50% of a ≤ €5,000 aid [V:WS2-007][V:WS2-009]. High is the LV EDIH catalogue's generic CRM implementation package of €5,000 [V:WS3-019], which also equals the LIAA ceiling for 100% aid to micro/small firms on projects ≤ €5,000 [V:WS2-020].
- Basis/rationale: published anchors exist in EE (hourly rate), EE (grant cap) and LV (package). There is no LT configuration-package price. LT only has custom-CRM builds at €9,500–15,000 [V:WS3-025], which is a different scope. A newcomer cannot be the funded EIS "digital advisor" before completing ≥ 3 similar projects in 4 years [V:WS2-009].
- Confidence: medium (anchors verified; actual willingness to pay unknown)
- Used in: 05 §5, §6; WS5_models.py `PROJECTS['CRM setup']`

### A-WS5-14 — CRM delivery hours
- Value: base 25 h (range 15–40)
- Formula: 15 h vendor-partner bundle × about 1.7 newcomer factor
- Inputs: the LV partner bundle gives 12 h implementation + 3 h training [V:WS3-018]. Ready-made CRM implementations take 4–8 weeks and include audit, Excel migration, configuration and training [V:WS3-057].
- Basis/rationale: a solo newcomer without templates is slower than an established partner. Data cleanup scope drives the range.
- Confidence: low-medium
- Used in: 05 §6; WS5_models.py

### A-WS5-15 — CRM sales hours per won project
- Value: base 12 h (range 6–25)
- Formula: about 4 h per qualified opportunity (discovery, proposal, follow-up) × 3 opportunities per win
- Inputs: ESTIMATE. No Baltic sales-effort or win-rate benchmark was available (WS6 benchmarks may replace this).
- Basis/rationale: with no network (BRIEF §2), early deals sit near the high end.
- Confidence: low
- Used in: 05 §6; WS5_models.py

### A-WS5-16 — CRM admin hours per project
- Value: 2 h
- Formula: contract + invoice + bookkeeping entry
- Inputs: ESTIMATE
- Basis/rationale: small fixed admin per deal.
- Confidence: medium
- Used in: WS5_models.py

### A-WS5-17 — CRM unbilled post-go-live support
- Value: 3 h
- Formula: n/a
- Inputs: ESTIMATE
- Basis/rationale: fixes and questions in the first weeks after go-live.
- Confidence: low-medium
- Used in: WS5_models.py

### A-WS5-18 — CRM direct costs per project (incl. VAT)
- Value: €0 (range €0–100)
- Formula: n/a
- Inputs: ESTIMATE. The cost of vendor trial, sandbox and partner accounts is UNKNOWN (search plan SP-01…SP-03).
- Basis/rationale: assumes free trial or partner access. The upper bound allows for a paid data-migration utility.
- Confidence: low
- Used in: WS5_models.py

## D. Automation project model

### A-WS5-19 — Automation price levels (excl. VAT)
- Value: €450 / €1,200 / €3,000
- Formula: published band edges
- Inputs: aigentas.lt (LT) publishes €450–1,200 for process automation and €1,500–3,000+ for full implementation [V:WS3-024].
- Basis/rationale: this is the only published Baltic automation price list found. It is from LT only, and EE/LV equivalents are UNKNOWN.
- Confidence: medium
- Used in: 05 §5, §6

### A-WS5-20 — Automation delivery hours
- Value: base 15 h (range 8–30)
- Formula: n/a
- Inputs: ESTIMATE. The scope reference is "one process, up to 2 integrations" [V:WS3-024].
- Basis/rationale: one revenue workflow (inquiry → CRM → AI-drafted reply → follow-up task), including testing, documentation and handover.
- Confidence: low-medium
- Used in: WS5_models.py

### A-WS5-21 — Automation sales hours per won project
- Value: base 8 h (range 4–16)
- Formula: n/a
- Inputs: ESTIMATE
- Basis/rationale: a smaller ticket and shorter decision than a CRM setup.
- Confidence: low
- Used in: WS5_models.py

### A-WS5-22 — Automation admin and hypercare
- Value: admin 1.5 h; unbilled hypercare 3 h
- Formula: n/a
- Inputs: ESTIMATE
- Basis/rationale: small fixed overhead per deal.
- Confidence: medium-low
- Used in: WS5_models.py

### A-WS5-23 — Automation direct cost per project (incl. VAT)
- Value: €10 (range €0–50)
- Formula: 200 test runs × (4,000 input + 1,000 output tokens) on Sonnet 5.5 = 0.8 MTok × $2 + 0.2 MTok × $10 = $3.60, rounded up to a €10 allowance incl. VAT
- Inputs: [V:WS5-020] API prices
- Basis/rationale: in the base case, hosting costs the operator nothing because the workflow runs on the client's instance or n8n Cloud account. An operator-hosted instance is allowed by the licence FAQ [V:WS5-022], but VPS prices are UNKNOWN.
- Confidence: medium (immaterial)
- Used in: WS5_models.py

### A-WS5-24 — Client LLM run-cost example (pass-through)
- Value: $4.20/month (Sonnet 5.5), $2.10 (Haiku 4.5), $8.40 (Opus 5.5)
- Formula: 300 inquiries/month × (3,000 input × in-price + 800 output × out-price) / 1,000,000
- Inputs: [V:WS5-020]. The token counts per inquiry are an ESTIMATE.
- Basis/rationale: shows that AI API cost is immaterial against project prices of €450–3,000.
- Confidence: medium
- Used in: 05 §4

## E. Lead-generation retainer model

### A-WS5-25 — Lead-gen monthly price levels (excl. VAT)
- Value: €1,000 / €1,800 / €2,850 per month
- Formula: high = published benchmark; mid ≈ 0.63 × high; low ≈ 0.35 × high
- Inputs: Ripe Leads (Vilnius) charges €2,850/month after a €3,750 first month, with tools and data included [V:WS3-008].
- Basis/rationale: this is the only published Baltic retainer found. The two lower levels are scenarios for a solo, unproven operator, not market observations.
- Confidence: low (low and mid levels)
- Used in: 05 §6

### A-WS5-26 — Lead-gen delivery hours per client-month
- Value: base 20 h (range 14–30)
- Formula: list building and enrichment 6 + copy and multilingual sequence iteration 4 + campaign ops and deliverability 3 + reply handling and booking 5 + reporting/client call 2
- Inputs: ESTIMATE
- Basis/rationale: steady-state multilingual (EN/RU/LT) outbound for one client.
- Confidence: low
- Used in: WS5_models.py

### A-WS5-27 — Lead-gen onboarding hours (once per client, unbilled unless there is a setup fee)
- Value: 15 h
- Formula: n/a
- Inputs: ESTIMATE
- Basis/rationale: ICP workshop, sending domains and mailboxes, warm-up supervision, first list and first copy.
- Confidence: low
- Used in: WS5_models.py

### A-WS5-28 — Lead-gen sales hours per won client
- Value: base 15 h (range 8–30)
- Formula: n/a
- Inputs: ESTIMATE
- Basis/rationale: a higher-trust recurring commitment than a one-off project.
- Confidence: low
- Used in: WS5_models.py

### A-WS5-29 — Lead-gen monthly churn
- Value: base 15% (range 8–25%), giving an expected client lifetime of 6.7 (12.5–4.0) months
- Formula: lifetime L = 1 / churn (constant monthly hazard)
- Inputs: the published Baltic retainer is cancellable monthly with 28 days' notice [V:WS3-008]. No churn benchmark was found.
- Basis/rationale: no lock-in implies high churn. This parameter is the largest single driver of retainer economics after price.
- Confidence: low
- Used in: 05 §6.3

### A-WS5-30 — Lead-gen tools and data per client-month (incl. VAT)
- Value: €150 (range €80–300)
- Formula: allowance
- Inputs: ESTIMATE. Vendor prices are UNKNOWN in this run (search plan SP-05…SP-12). The market norm is that tools are included in the fee [V:WS3-008].
- Basis/rationale: covers dedicated sending domains, several mailboxes, a share of a sending/warm-up platform, enrichment credits and an optional LinkedIn tool.
- Confidence: low
- Used in: 05 §6.3

### A-WS5-31 — Lead-gen admin per client-month
- Value: 1 h
- Formula: n/a
- Inputs: ESTIMATE
- Basis/rationale: invoice, bookkeeping and contract admin.
- Confidence: medium-low
- Used in: WS5_models.py

### A-WS5-32 — Lead-gen setup fee
- Value: €0 in the base case; €900 in the alternative case
- Formula: 3,750 − 2,850 = 900
- Inputs: [V:WS3-008]
- Basis/rationale: the alternative mirrors the published first-month premium.
- Confidence: medium
- Used in: 05 §6.3

## F. Cross-model parameters

### A-WS5-33 — Share of hours that must fall in business hours
- Value: CRM 25%, automation 10%, lead-gen 30%
- Formula: task decomposition
- Inputs: ESTIMATE
- Basis/rationale: CRM needs a requirements workshop, user training and go-live support. Automation needs a kickoff and a handover call. Lead generation needs same-day reply handling, meeting booking and client calls.
- Confidence: low
- Used in: 05 §7

### A-WS5-34 — Elapsed calendar weeks per project (for concurrency)
- Value: CRM 6, automation 3
- Formula: n/a
- Inputs: CRM implementations take 4–8 weeks [V:WS3-057]. The automation figure is an ESTIMATE.
- Basis/rationale: converts projects per year into projects running in parallel.
- Confidence: low-medium
- Used in: 05 §7

### A-WS5-35 — Effective billed rate per delivery hour (derived)
- Value: see results table
- Formula: price / delivery hours
- Inputs: [E:A-WS5-13], [E:A-WS5-14], [E:A-WS5-19], [E:A-WS5-20], [E:A-WS5-25], [E:A-WS5-26]
- Basis/rationale: allows comparison with hourly market rates: €110–150/h agency [V:WS3-005] and about €147–149/h for the EIS mentor [E:A-WS2-05].
- Confidence: as inputs
- Used in: 05 §6.1

### A-WS5-36 — Price required for a target net €/h (derived)
- Value: see results table
- Formula: projects: P_req = target × unit hours / 0.5865 + direct cost. Retainer: P_req = target × lifetime hours / (0.5865 × L) + tools per month.
- Inputs: [E:A-WS5-01] and the hours inputs. The targets of €15, €25 and €40 per hour are scenario values, not benchmarks.
- Basis/rationale: turns the model into a price floor for each net-hourly ambition.
- Confidence: as inputs
- Used in: 05 §6.5

### A-WS5-37 — Buyer's alternative cost (formula only; inputs mostly UNKNOWN)
- Value: employer monthly cost = gross wage × (1 + employer contribution rate)
- Formula: see value
- Inputs: EE social tax 33% [V:WS5-001]. The EE employer unemployment-insurance rate, the LV and LT employer contribution rates, and wages by occupation (SDR/sales rep, CRM admin) are all UNKNOWN in this run (search plan SP-24…SP-27).
- Basis/rationale: price anchor requested by the lead analyst.
- Confidence: n/a
- Used in: 05 §8.6

### A-WS5-38 — Capacity model
- Value: see results table
- Formula: projects/year = (H × 46 − 72) / unit hours. Concurrent retainer clients N = ((H × 46 − 72) / 12) / (delivery + admin + churn × (onboarding + sales)).
- Inputs: [E:A-WS5-08], [E:A-WS5-09], [E:A-WS5-10] and the hours inputs above
- Basis/rationale: a supply-side ceiling that assumes a full pipeline. It is not a demand forecast.
- Confidence: as inputs
- Used in: 05 §7


---

## WS6 (5 entries)

## Assumptions — WS6 (Reachability & first-client channels)

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
