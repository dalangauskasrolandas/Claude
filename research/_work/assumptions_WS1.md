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

### A-WS1-08 — G1 funnel structure (parameters UNKNOWN in this run)
- Value: Funnel endpoint = UNKNOWN; an evidence-based upper bound per country = N(10–249) from A-WS1-01 / A-WS1-02 / A-WS1-06.
- Formula: Reachable_c = N2_c × s_c × (1 − x_c) × d_c × l_c, where
  - N2_c = enterprises 10–249 in country c (A-WS1-01, -02, -06); proxy for the brief's 5–100 staff ICP
  - s_c = share of N2_c in the target sectors (C; G46; H49, H51, H52 excl. H52.22, H53; M69; M70, M71.1, M73, M74; N77, N78, N80–N82) — UNKNOWN (resolve: Eurostat sbs_sc_ovw by NACE × size; EE ER025; LV UZS030/UZS031; LT VDA operating-enterprise tables)
  - x_c = share excluded under hard exclusions (Russia/Belarus trade; water transport H50 and H52.22 are already removed by sector definition) — UNKNOWN (resolve: Eurostat TEC partner data / customs exporter lists; manual screening)
  - d_c = share with a findable decision-maker contact in Hunter/Apollo — UNKNOWN unless `research/_work/data/db_coverage.csv` is supplied
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
