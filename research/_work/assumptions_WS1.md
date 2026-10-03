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
