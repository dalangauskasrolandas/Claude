# 01 — Market size & structure (WS1)

**Scope:** how many Baltic B2B buyers exist and how they are structured (size, sector, exports, associations, language), per country (EE / LV / LT), plus G1 funnels and a G2 sizing method.

> **Status: PARTIAL.** The session-wide WebSearch budget (shared by all six workstream agents) ran out early in this workstream's run, and direct page fetching (WebFetch/curl) is blocked in this environment. Everything marked **UNKNOWN** below was **not researched**, which is different from "searched and not found". Each UNKNOWN names the exact table, filter or query that resolves it. Most can be resolved in a short session by a person with a normal browser (see §7 and Appendix A). The "plausibly reachable" step uses the lead analyst's Hunter.io database-coverage counts (`research/_work/data/db_coverage.csv`, 2026-10-03), which arrived during this run.
>
> **Gap-fill pass (2026-10-03):** stopped by the user after 41 of 60 searches. It added Estonia's 2025 size and sector counts, census/survey language data for all three states, the scope of the Latvian and Estonian language laws, Latvian Russia/Belarus exporter counts, export partners, and foreign-chamber and accounting-body counts. **Scope change (user, 2026-10-03): only companies with up to 50 staff are in scope.** The funnel and synthesis inputs now use the 0–9 and 10–49 classes (Hunter buckets 1-10 and 11-50); the 50–249 class (Hunter 51-200) is shown for reference only and marked out of scope. ESTIMATE ids A-WS1-16 to A-WS1-24 and sources WS1-095 to WS1-151 come from this pass.

**Legend**
- `[V:WS1-nnn]` = VERIFIED, row in `research/_work/sources_WS1.csv`. `[V:WS6-nnn]`, `[V:WS3-nnn]`, `[V:WS0-nnn]`, `[V:VL-nnn]` = VERIFIED by another workstream, by the lead analyst (WS0) or by the verifier (VL). These rows are cited by ID rather than copied (all merge into `sources.csv`).
- `[E:A-WS1-nn]` = ESTIMATE; formula and inputs in `research/_work/assumptions_WS1.md` (short formula also shown inline). `[E:A-WS9-nn]` = ESTIMATE added by the verifier (`research/_work/assumptions_VER.md`). `(corrected — see VL-nn)` marks text changed by the verification pass and `(verifier note — see VL-nn)` marks an added caveat; both point to `verification_log.md`.
- `LEAD` = seen in a search extract but not tied to a confirmable URL, so not used as evidence.
- `UNKNOWN (resolve: …)` = not established.
- Size-class labels (`0–9`, `10–49`, `50–249`, `250+`) and the brief's ICP definition (`5–100` staff) are category definitions, not statistics.

**Method note:** Evidence gathered via web-search extracts on 2026-10-03; direct page fetching was blocked in this environment. Searches used `allowed_domains` to force primary sources (stat.ee, andmed.stat.ee, stat.gov.lv, data.stat.gov.lv, osp.stat.gov.lt, ec.europa.eu, single-market-economy.ec.europa.eu, eimin.lrv.lt), in EN, ET, LV and LT. No RU-language searches could be run before the budget ran out. Derived numbers were computed in code. Database-coverage rows (Hunter.io Discover, run by the lead analyst; vendor database = secondary; method `api-query`) are cited row by row via their permalinks (WS1-046 to WS1-094).

---

## 0. Scope: companies with up to fifty staff — G1 funnel recomputed by the verifier

*Verifier recomputation, 2026-10-03; method, checks and what changed are in `verification_log.md`. Inputs: statistical size classes `0–9` and `10–49`, Hunter buckets `1-10` and `11-50`, maritime-tagged logistics rows removed. Raw counts: `research/_work/data/db_coverage.csv`; script: `research/_work/data/VER_recompute.py`. Database rows are a reachability proxy, not market size. The original WS1 funnel stays in the funnel section below for comparison.*

| Step | EE | LV | LT |
|---|---|---|---|
| 1. All enterprises | 159,827 (2025) [V:WS1-095] | 107,091 (2024 est., SBS scope) [E:A-WS1-02] | 328.6 thousand (2022, pre-2023) [V:WS1-033] |
| 2. Up to fifty staff (`0–9` + `10–49`) | 158,489 [E:A-WS1-16] | 105,523 [E:A-WS1-18] | ≈325.6 thousand [E:A-WS1-19] |
| 2a. of which `10–49` (core) | 6,284 [V:WS1-095] [V:VL-015] | 6,457 (JRC estimate for 2024) [V:WS1-025] [V:VL-016] | 11.3–12.8 thousand; treat 12,815 as a ceiling (corrected — see VL-017) [E:A-WS9-03] |
| 3. Target sectors within `10–49` | 1,191–3,481 (section level; upper bounds) [E:A-WS1-17] | UNKNOWN (resolve: Eurostat `sbs_sc_ovw`, U1) | UNKNOWN (resolve: Eurostat `sbs_sc_ovw`, U1) |
| 4. Database records in target sectors, `1-10` + `11-50`, maritime-tagged logistics removed | 4,345–5,539 [E:A-WS1-20] | 2,729–3,336 [E:A-WS1-20] | 5,123–6,213 [E:A-WS1-20] |
| 5. ... with at least one indexed e-mail | 3,606–4,598 [E:A-WS1-20] | 2,265–2,769 [E:A-WS1-20] | 4,252–5,157 [E:A-WS1-20] |
| 6. ... with a named (personal) e-mail (corrected — see VL-027) | 2,254–3,381 [E:A-WS9-02] | 1,416–2,036 [E:A-WS9-02] | 2,657–3,793 [E:A-WS9-02] |
| 7. Likelier buyers: `11-50` bucket with a named e-mail (**funnel endpoint**) | **703–1,019** [E:A-WS9-02] | **542–747** [E:A-WS9-02] | **957–1,300** [E:A-WS9-02] |
| 8. After language-workability and Russia/Belarus screens | UNKNOWN (resolve: U3, U5) | UNKNOWN; share of firms trading goods with RU/BY at most 0.6% [E:A-WS1-21] | UNKNOWN (resolve: U3, U5) |

**How to read the endpoint.** Step 7 is the largest pool that is both in the likelier size band and reachable by a named e-mail in the vendor database: about 0.7–1.0 thousand firms in EE, 0.5–0.7 thousand in LV and 1.0–1.3 thousand in LT [E:A-WS9-02]. It is an upper bound for outbound lists built from this database, because the language filter, the sanctions screen, maritime-adjacent firms outside the logistics industry and duplicate domains are not applied (share UNKNOWN). The statistical core in step 2a is larger, but its target-sector share is known only for EE (at most 55.4% [E:A-WS1-17]).

**What changed against the original funnel.**
- Named-e-mail pools are lower. The pooled 61.0% personal-e-mail rate [E:A-WS1-13] was computed mostly from segments in the out-of-scope 51-200 bucket; restricted to in-scope segments it is 51.9% [E:A-WS9-01] (corrected — see VL-027).
- The Lithuanian `10–49` count is a ceiling, not a point estimate (corrected — see VL-017).
- All other arithmetic reproduces: totals, bucket sums, the maritime adjustment and the sector sums match the WS1 values within rounding of ±2 [E:A-WS1-20].

**G2 (foreign sellers into the Baltics), up to fifty staff: UNKNOWN** (resolve: the three routes in the G2 section). The only quantity is a ceiling of about 900 chamber memberships, all sizes, not de-duplicated [E:A-WS1-24]. The sum 470 + 130 + 100 + 100 + 100 was recomputed and holds. The up-to-fifty cut cannot be applied, so the G2 count can only be at most that ceiling.

---

## 1. Key findings

1. **In-scope universe (≤50 staff): the core 10–49 class is small.** Firms with 10–49 staff: EE 6,284 (2025) [V:WS1-095]; LV 6,457 (2024 est.) [V:WS1-025]; LT ≈12,815 (2022, pre-2023) [E:A-WS1-04]. Adding micro firms (0–9) gives EE 158,489 [E:A-WS1-16], LV 105,523 [E:A-WS1-18] and LT ≈325,600 (pre-2023) [E:A-WS1-19], but that class is dominated by one-person firms and cannot be cut at 5 staff in EE/LV data. The 50–249 class (EE 1,151 [V:WS1-095]; LV 1,363 [V:WS1-025]; LT ≈2,629 [E:A-WS1-05]) is now out of scope.
2. **Estonia, 2025, firms with 10–49 employees by section:** manufacturing 1,191 [V:WS1-096]; trade (section G) 1,036 [V:WS1-096]; transport (H) 472 [V:WS1-096]; professional/scientific (M) 407 [V:WS1-097]; admin/support (N) 375 [V:WS1-097]. The target-sector envelope is 1,191–3,481 firms, at most 55% of the class [E:A-WS1-17]. Only manufacturing maps fully to a target sector; the other sections also contain retail, water transport, veterinary and travel agencies.
3. **Latvia:** 6,457 small enterprises (2024 EC/JRC estimate) [V:WS1-025]. No CSB sector × size values could be extracted (tables UZS030/UZS031 [V:WS1-030]), so the LV sector step stays UNKNOWN. The Riga region produced 65.8% of GDP in 2023 [V:WS1-032].
4. **Lithuania has about twice the EE/LV 10–49 class:** ≈12,815 (2022, pre-2023) [E:A-WS1-04]. A VDA cross-check fits (small firms = 12.2% of SMEs in 2022) [V:WS1-098]. No newer national figure was found; the EC 2024 estimate (11,348) is still a LEAD (WS1-039). LT is the only market where the operator speaks the state language (BRIEF §2). (corrected — see VL-017): treat ≈12,815 as a ceiling; working range 11.3–12.8 thousand [E:A-WS9-03]; the re-check on 2026-10-03 found no newer VDA edition [V:VL-017].
5. **Database-reachable pool with ≤50 staff (Hunter 1-10 + 11-50, target sectors, ≥1 indexed email):** EE 3,606–4,598; LV 2,265–2,769; LT 4,252–5,157 [E:A-WS1-20]. In the 11-50 bucket alone (the likelier buyers): EE 1,124–1,386; LV 868–1,016; LT 1,531–1,768 [E:A-WS1-20]. With a named (personal) e-mail the 11-50 pool is EE 703–1,019; LV 542–747; LT 957–1,300 (corrected — see VL-027) [E:A-WS9-02]. These counts come before the language and sanctions screens. They are vendor-database counts (a reachability proxy), not market size.
6. **Accounting firms are thin in the database and only partly counted in statistics.** Hunter lists 97 (EE), 63 (LV) and 126 (LT) accounting records with ≤50 staff [E:A-WS1-20]. Professional bodies: LV ≈2,800 licensed outsourced-accounting providers (mid-2023) [V:WS1-127]; EE 338 sworn auditors and 112 audit firms (2025) [V:WS1-128]; LT >300 certified auditors (2025) [V:WS1-130]. Statistical M69.20 counts remain UNKNOWN (§4.4).
7. **Associations:** ELEA lists 65 members on a public list (prior lead confirmed) [V:WS6-007]; another ELEA page gives 68 members and an average of 91 employees per member (LEAD VL-021), so many members are above the up-to-fifty scope (verifier note — see VL-021); LINEKA (LT) 42 in an undated report [V:WS6-008] versus 60 in a report dated 17 Apr 2021 [V:VL-022] (corrected — see VL-022); Kaubanduskoda ~3,402 listed [V:WS6-001]. Foreign chambers with verified counts add up to ≈900 memberships (not de-duplicated) [E:A-WS1-24]; the largest is the German-Baltic AHK with >470 members and a public member database [V:WS1-110] [V:WS1-111]. Estonia has the EU's second-highest share of foreign-controlled enterprises, 11% (2023) [V:WS1-109].
8. **Multilingual Baltic coverage is not unique, and tool languages differ.** Fontakt [V:WS3-002], Ripe Leads [V:WS3-009] and a Riga Pipedrive partner [V:WS3-013] already sell RU + local-language coverage. HubSpot has Latvian and Lithuanian interfaces but not Estonian [V:WS0-003]; Zoho supports ET/LV/LT only partially [V:WS0-004].
9. **Language reality differs sharply by country.** EE: Russian is the mother tongue of 29% (2021) [V:WS1-099]; English is spoken as a foreign language by 48% and Russian by 39% [V:WS1-100], so ≈68% can speak Russian [E:A-WS1-22]. LV: 34.6% of 18–69-year-olds use Russian at home (2022) [V:WS1-101]; Russian (91.3%) and English (64.0%) are the most common foreign languages spoken or understood [V:WS1-104]. LT: Russian mother tongue ≥≈4.6% [E:A-WS1-23]; 60.6% know Russian and 31.1% English (2021) [V:WS1-105]. The LV and EE language laws regulate private-sector language only where a public interest (consumers, labour, safety) is affected, plus public signs and notices [V:WS1-132] [V:WS1-133]; nothing found targets B2B emails or proposals (LT law not checked).
10. **Exports and the sanctions screen.** Main goods-export partners: EE 2024 Finland 16%, Latvia 11%, Sweden 9% [V:WS1-120]; LV 2024 top five Lithuania, Estonia, Germany, Sweden and Russia (47.5% together) [V:WS1-122]; LT 2022 Germany 9.7%, Poland 9%, Latvia 8.7% (pre-2023) [V:WS1-125]. In Latvia 400 firms exported goods to Russia and 218 to Belarus in Jan–Nov 2023 [V:WS1-123], at most ≈0.6% of Latvian firms with ≤50 staff [E:A-WS1-21]. Exporting-SME counts remain UNKNOWN (§3.3).

---

## 2. Definitions used

**Target sectors (G1).** These are defined so that the brief's hard exclusions are applied at the classification level wherever NACE allows it.

| Group | NACE Rev. 2 codes included | Excluded / flagged | Why |
|---|---|---|---|
| Manufacturing | C (all divisions) | — | Brief §3: manufacturing exporters |
| Wholesale | G46 | — | Brief §3: wholesale/trading |
| Transport & logistics | H49, H51, H52 **excluding H52.22**, H53 | **H50 (water transport) and H52.22 (service activities incidental to water transport)** | H50 contains shipowners/operators, and H52.22 covers ship agency/port services (vessel–service-provider brokering). Both are hard exclusions (BRIEF §2). Freight forwarding (H52.29) stays in scope. |
| Accounting | M69 (M69.20 accounting/bookkeeping/auditing; M69.10 legal shown separately if available) | — | Brief §3 prior idea: accounting firms as clients and referral partners |
| Other B2B services — core | M70 (head offices; management consultancy), M71.1 (architecture/engineering), M73 (advertising, market research), M74 (other professional/technical), N78 (employment activities), N82 (office administration, business support incl. call centres) | **M71.2 (technical testing & analysis)** excluded | M71.2 includes vessel inspection/survey firms (employer conflict). M73 and N82.20 (call centres) are also potential competitors or partners, so flag them. |
| Other B2B services — extended | M72 (R&D), N77 (rental & leasing, **excl. N77.34 water-transport equipment**), N80 (security), N81 (building services) | M75 (veterinary) and N79 (travel agencies) excluded | Extended = more asset-heavy or operational B2B services with weaker CRM/pipeline fit. M75 and N79 are mainly consumer-facing. |

**Classification change.** From the 2025 reference year, national series move to NACE Rev. 2.1. Statistics Estonia publishes EMTAK 2025 series alongside EMTAK 2008 [V:WS1-044], for example table ER0290 [V:WS1-045]. Sector pulls for 2024 should use EMTAK 2008 / NACE Rev. 2 (ER025), and later years need a code mapping.

**Size.** The brief's ICP was 5–100 staff. **Scope change (user, 2026-10-03): only companies with up to 50 staff are in scope.** Published size classes are 0–9 / 10–49 / 50–249, so the in-scope proxy is 0–49, shown as two classes: 0–9 (micro, dominated by one-person firms; it cannot be cut at 5 staff in EE/LV published data, LT finer groups UNKNOWN) and 10–49 (the conservative core). The 50–249 class is out of scope and shown for reference only. In the database route the matching Hunter buckets are 1-10 and 11-50 (a 10-person firm sits in Hunter's 1-10 but in the statistical 10–49 class; UNKNOWN net effect).

---

## 3. Body

### 3.1 Active enterprises by size class — EE / LV / LT

| Size class | EE (2025, national, by employees) | LV (2024, EC SME Fact Sheet 2025 = JRC estimate, SBS scope, persons employed) | LT (2022 (pre-2023), VDA, persons employed) |
|---|---|---|---|
| 0–9 (in scope) | 152,205 [V:WS1-095] | 99,066 [V:WS1-025] | ≈312,827 (312,663–312,992) [E:A-WS1-19]; share 95.2% [V:WS1-034] |
| 10–49 (in scope; core) | 6,284 [V:WS1-095] | 6,457 [V:WS1-025] | ≈12,815 (12,651–12,980) [E:A-WS1-04]; share 3.9% [V:WS1-034] (corrected — see VL-017: ceiling; working range 11.3–12.8 thousand [E:A-WS9-03]) |
| **≤50 staff (0–49), in scope** | **158,489** [E:A-WS1-16] | **105,523** [E:A-WS1-18] | **≈325,643 (325,314–325,971)** [E:A-WS1-19] |
| 50–249 (out of scope since 2026-10-03) | 1,151 [V:WS1-095] | 1,363 [V:WS1-025] | ≈2,629 (2,465–2,793) [E:A-WS1-05]; share 0.8% [V:WS1-034] |
| 250+ | 187 [V:WS1-095] | 205 [V:WS1-025] | share 0.1% [V:WS1-034] |
| **Total** | **159,827** [V:WS1-095] | **107,091** [E:A-WS1-02] | **328.6 thousand** [V:WS1-033] |
| 10–249 (reference only; earlier proxy) | 7,435 [E:A-WS1-16] | 7,820 [E:A-WS1-02] | ≈15,444 (15,116–15,773) [E:A-WS1-06] |
| Source table / dataset | Statistics Estonia economic-units page, 2025 reference year [V:WS1-095]; tables ER025 (by employees × EMTAK 2008) [V:WS1-004] and ER026. Superseded 2024 values: total 158,378 [V:WS1-001]; 10–49 6,461 and 50–249 1,118 [V:WS1-003] | EC SME Performance Review fact sheet [V:WS1-025]; national tables CSB UZS020 [V:WS1-029], UZS030/UZS031 [V:WS1-030] | VDA *Business in Lithuania 2023* [V:WS1-033] [V:WS1-034]; cross-check [V:WS1-098] |

**Comparability warnings**
- **Population scope differs.**
  - The EE count covers *all economically active enterprises in the statistical profile*, every EMTAK section, by *employees*.
  - The LV count covers the Eurostat SBS business economy (excludes agriculture, finance and most public/social services), by *persons employed* (owners included).
  - The LT total includes very small units such as natural persons engaged in business.

  For the `10–249` band these differences matter less than for the micro class, but they do not vanish.
- **Reference years differ.** EE is 2025 (observed) [V:WS1-095]; LV is 2024 (model estimate from 2008–2023 data [V:WS1-027]); LT is 2022 (pre-2023; observed shares × observed total). No newer LT national count was found in the gap-fill pass (UNKNOWN; resolve: VDA operating enterprises at the start of 2025 by personnel group).
- **Latvian small firms average ≈20.4 persons employed** (medium firms ≈98.5, now out of scope) [E:A-WS1-03]; underlying data [V:WS1-026].
- **LT is stable over time.** The 2021 (pre-2023) cross-check gives ≈12,550 small and ≈2,390 medium (shares 4.2% and 0.8% of 298.8 thousand) [V:WS1-035] [E:A-WS1-04] [E:A-WS1-05]. Growth in the LT total comes from very small units, not from the 10–249 band.
- **Eurostat harmonised alternative.** `sbs_sc_ovw` (Enterprise statistics by size class and NACE Rev. 2 activity, from 2021 onwards) holds 2021–2024 data, last updated 15/09/2026 [V:WS1-028]. Its values could not be extracted. It is the single best source to replace all three columns with one methodology (see §7, U1).

Other LT context (not used in calculations):
- About 100,000 legal-entity SMEs were operating at the beginning of 2023 (ministry figure) [V:WS1-037].
- 223,290 legal entities were registered at 1 July 2025, including 100,056 UAB and 60,038 MB (secondary analysis of Registrų centras data) [V:WS1-038].

### 3.2 Enterprises by target sector × size class

Only Estonia could be filled (2025, NACE section level). The `50–249` class is out of scope and shown in the last row for reference.

| Sector (see §2) | EE small, `10–49` (2025) | EE micro, `0–9` (2025) | LV `10–49` | LT `10–49` |
|---|---|---|---|---|
| C manufacturing (fully in target) | 1,191 [V:WS1-096] | UNKNOWN (resolve: ER025, section C, <10 employees) | UNKNOWN (resolve: CSB UZS030/UZS031, 2024, NACE C × size group) | UNKNOWN (resolve: VDA operating enterprises by NACE × personnel group) |
| G46 wholesale | ≤1,036 (whole section G, incl. G45 motor trade and G47 retail) [V:WS1-096] | UNKNOWN | UNKNOWN | UNKNOWN |
| H49, H51, H52 excl. H52.22, H53 | ≤472 (whole section H, incl. excluded H50 and H52.22) [V:WS1-096] | UNKNOWN | UNKNOWN | UNKNOWN |
| M69 / M69.20 and other M target divisions | ≤407 (whole section M, incl. excluded M71.2 and M75) [V:WS1-097] | ≤23,994 (whole section M) [V:WS1-097] | UNKNOWN | UNKNOWN |
| N target divisions (N77, N78, N80–N82) | ≤375 (whole section N, incl. excluded N79) [V:WS1-097] | ≤8,003 (whole section N) [V:WS1-097] | UNKNOWN | UNKNOWN |
| **Target envelope** | **1,191–3,481** (C only … all five sections; ≤55.4% of the class) [E:A-WS1-17] | UNKNOWN (C, G and H micro counts missing) | UNKNOWN | UNKNOWN |
| Reference, 50–249 (out of scope) | C 397, G 178, H 74 [V:WS1-096]; M 47, N 85 [V:WS1-097] | — | UNKNOWN | UNKNOWN |

**Cheapest resolution (all three countries in one pass).** Eurostat `sbs_sc_ovw` [V:WS1-028]:
- geo = EE, LV, LT
- size classes `0–9` and `10–49` (in scope)
- NACE = C, G46, H49, H51, H52, H53, M69, M70, M71, M72, M73, M74, N77, N78, N80, N81, N82
- indicator = number of enterprises
- latest year (2023 or 2024)

Then use the national tables only for 4-digit splits (M69.20, H52.22, M71.2, N77.34). This is a single short browser session. Eurostat SBS excludes K (finance) and most of A, which is fine for these sectors. The EE division split (G46 inside G; H without H50/H52.22) needs ER025 at 2–4 digits (UNKNOWN in this pass).

### 3.3 Exporters

| Item | EE | LV | LT |
|---|---|---|---|
| Number of exporting SMEs | UNKNOWN (resolve: Eurostat `ext_tec01`, trade by NACE and enterprise size class [V:WS1-126]). LEAD: micro firms were 78% of exporting units and medium firms produced 38% of exports in 2023 (WS1-121) | UNKNOWN (resolve: `ext_tec01` [V:WS1-126]) | UNKNOWN (resolve: `ext_tec01` [V:WS1-126]; VDA) |
| Main destination markets (share of goods exports) | 2024: Finland 16%, Latvia 11%, Sweden 9% [V:WS1-120] | 2024: Lithuania, Estonia, Germany, Sweden and Russia are the top five, 47.5% together [V:WS1-122]; total EUR 18.68 bn [V:WS1-031] | 2022 (pre-2023), goods of Lithuanian origin: Germany 9.7%, Poland 9%, Latvia 8.7%, USA 7.8%, Netherlands 7.5% [V:WS1-125]; 2024–2025 ranking UNKNOWN (resolve: VDA annual trade release) |
| Exporters trading with Russia/Belarus (exclusion filter) | UNKNOWN (resolve: Statistics Estonia / customs count of exporters by partner = RU, BY) | Jan–Nov 2023: 400 firms exported goods to Russia and 218 to Belarus (821 and 370 a year earlier) [V:WS1-123]; 2021: 1,013 and 490 [V:WS1-124]. Upper bound ≈0.6% of LV firms with ≤50 staff [E:A-WS1-21] | UNKNOWN (resolve: VDA / customs exporters by partner) |

Why it matters: exporters are the natural buyers of component C (outbound lead generation to foreign markets). Russia is still among Latvia's five largest export partners in 2024 [V:WS1-122], so the sanctions screen is not academic there, although the number of firms involved is small and falling [V:WS1-123] [V:WS1-124]. Enterprise-size × partner combinations in TEC may be confidential for small countries.

### 3.4 Associations and chambers

| Country | Body | Sector | URL | Members | Member list public? | Source |
|---|---|---|---|---|---|---|
| EE | Estonian Chamber of Commerce and Industry (Eesti Kaubandus-Tööstuskoda) | cross-sector | koda.ee/en/members | ~3,402 listed; "over 3,500" claimed | Yes (members page) | [V:WS6-001] [V:WS6-002] |
| EE | EVEA (Estonian Association of SMEs) | cross-sector SMEs | evea.ee/liikmed | represents >6,000 enterprises (direct + collective) | UNKNOWN | [V:WS6-006]; composition LEAD WS6-031 |
| EE | ELEA (Estonian Logistics and Freight Forwarding Association) | logistics / forwarding | elea.ee/en/members | 65 incl. 13 associate members (2026); 68 incl. 17 associates and an average of 91 employees per member on another ELEA page (LEAD VL-021) (corrected — see VL-021) | Yes | [V:WS6-007] (**prior lead ~65 confirmed**) |
| EE | Estonian Machinery Industry Association | manufacturing exporters | UNKNOWN | UNKNOWN | UNKNOWN | existence via event [V:WS6-017] |
| EE | Audiitorkogu (Estonian Auditors' Association); Eesti Raamatupidajate Kogu (ERK, accountants) | accounting / audit | audiitorkogu.ee; erk.ee | Audiitorkogu 450 members = 338 sworn auditors + 112 audit firms (30.06.2025); ERK count UNKNOWN (certified accountants 4,182 in 2020 is a LEAD, WS1-129) | UNKNOWN | [V:WS1-128] |
| LV | Latvian Chamber of Commerce and Industry (LTRK) | cross-sector | chamber.lv | 6,000 members incl. associations and business clubs | UNKNOWN | [V:WS6-003]; conflicting direct-company breakdown LEAD WS6-030 |
| LV | LAFF (Latvian Association of Freight Forwarders and Logistics) | logistics / forwarding | laff.lv/en/biedri | count not stated | Yes | [V:WS6-009] |
| LV | Licensed outsourced-accounting providers (VID licence, mandatory since 1 July 2023); accountants' and exporters' associations | accounting | vid.gov.lv (licence register) | ≈2,800 licences (mid-2023; 5,886 providers were registered before licensing); association counts UNKNOWN | UNKNOWN (resolve: VID public licence register) | [V:WS1-127] |
| LT | Association of Lithuanian Chambers of Commerce, Industry and Crafts | cross-sector (regional chambers) | chambers.lt | ~2,000 | UNKNOWN | [V:WS6-004] |
| LT | Vilnius Chamber of Commerce, Industry and Crafts | cross-sector | cci.lt (older site) | >550 (date unknown) | UNKNOWN | [V:WS6-005] |
| LT | LINEKA (national forwarders & logistics association) | logistics / forwarding | lineka.lt | 42 (41 companies + 1 education institution; undated report) [V:WS6-008] versus 60 (54 companies + 6 related organisations; report dated 17 Apr 2021, pre-2023) [V:VL-022] (corrected — see VL-022) | UNKNOWN | [V:WS6-008] [V:VL-022] [V:VL-031] |
| LT | LBAA (Lithuanian Association of Accountants and Auditors) | accounting | lbaa.lt | UNKNOWN: >700 vs 472 (2020), conflicting (LEAD WS1-131) | UNKNOWN | LEAD WS6-032, WS1-131 |
| LT | Lithuanian Chamber of Auditors (Lietuvos auditorių rūmai) | audit | lar.lt | >300 certified auditors (2025) | UNKNOWN | [V:WS1-130] |

**Also to verify (names from analyst knowledge, not checked in this run; no counts or URLs claimed):**
- EE: Estonian Employers' Confederation (Eesti Tööandjate Keskliit); Estonian international road carriers' association (ERAA); Estonian accountants' association (Eesti Raamatupidajate Kogu); Estonian Auditors' Association (Audiitorkogu).
- LV: Employers' Confederation of Latvia (LDDK); international road carriers' association (Latvijas Auto); Latvian Association of Sworn Auditors (LZRA).
- LT: Confederation of Industrialists (LPK); Lithuanian Business Confederation (LVK); road carriers' association (Linava); Lithuanian Chamber of Auditors (Lietuvos auditorių rūmai).

### 3.5 Language of business

**(a) Russian-speaking share per country (2021 censuses; Latvia: 2022 survey)**

| | EE | LV | LT |
|---|---|---|---|
| Russian as mother tongue / home language | Mother tongue 29% of the population (2021 census) [V:WS1-099] | Russian used at home by 34.6% of 18–69-year-olds (Adult Education Survey 2022; the 2021 census did not collect language data) [V:WS1-101]; mother tongue 37.7% is a LEAD (WS1-103) | Mother tongue ≥≈4.6% (lower bound); ethnic Russians 5.0%, Poles 6.5% (2021 census) [E:A-WS1-23] [V:WS1-106] |
| State language as mother tongue | Estonian 67% (2021) [V:WS1-099] | Latvian 64.3% of 18–69-year-olds [V:WS1-102]; Latvian used at home 62.0% [V:WS1-101] | Lithuanians are 84.6% of the population and 99.4% of them have Lithuanian as mother tongue (2021) [V:WS1-106] |
| Population able to use Russian | ≈68% (29% mother tongue + 39% foreign language) [E:A-WS1-22] | 91.3% of 25–64-year-olds speak or understand Russian as a foreign language, even a little (2022) [V:WS1-104] | 60.6% have a command of Russian (2021) [V:WS1-105] |
| Share of businesses run in Russian | UNKNOWN (no official statistic expected; resolve via interviews/test campaigns, §7 U5) | UNKNOWN | UNKNOWN |

Reading: Russian reaches about two-thirds of Estonia's population [E:A-WS1-22] and is the home language of about a third of Latvian adults [V:WS1-101], but it is the mother tongue of only about one in twenty people in Lithuania [E:A-WS1-23]. These are population figures, not evidence on the language firms use for sales (U5 stays open). Russian-speaking does not mean sanctions-relevant: the Russia/Belarus exclusion applies to trade links, not to the language of the owner.

**(b) Evidence on which language SMEs use for sales and internal operations.** No survey evidence was gathered (UNKNOWN). The indirect evidence below comes from other workstreams:
- **CRM interface languages** (proxy for the language of internal operations):
  - HubSpot: Latvian and Lithuanian available, Estonian not [V:WS0-003].
  - Pipedrive: added Latvian in 2022 [V:WS0-001].
  - Zoho: Estonian, Latvian and Lithuanian only partially supported [V:WS0-004].

  Interface language is typically a per-user setting (verify per vendor), so the operator can usually work in an English UI. The delivery risk in EE/LV lies in the client's own content: field and stage names, email templates, quotes and documents written in Estonian or Latvian, which the operator cannot read.
- **Competitors already sell multilingual Baltic coverage including Russian:** Fontakt [V:WS3-002], Ripe Leads [V:WS3-009], a Riga Pipedrive partner [V:WS3-013].
- **LLM quality in Baltic languages** is relevant if AI drafts ET/LV copy the operator cannot proof-read. Benchmarks (WS0) show strong but model-dependent performance [V:WS0-005] [V:WS0-006] [V:WS0-007]. They do not measure business-writing quality (UNKNOWN; resolve: native-speaker review of AI drafts in a test campaign).

**(c) Legal constraints on language in private B2B communication.** Resolved for LV and EE in the gap-fill pass (analyst reading of official English translations; not legal advice). LT remains UNKNOWN. WS4 deferred this item to WS1.
- **LV, Official Language Law** [V:WS1-132]:
  - Section 2 regulates language use by private companies and self-employed persons only where their activities affect lawful public interests (public security, health, morality, health care, consumer and employment rights, workplace safety, administrative supervision), and only proportionately.
  - Section 21 requires public information in Latvian from state and municipal bodies, and from private entities when they perform public functions.
- **EE, Language Act** [V:WS1-133]:
  - Language use by private-law legal persons is regulated only if justified for fundamental rights or the public interest (public safety and order, administration, education, health, consumer protection, occupational safety).
  - Public signs, outdoor advertising and a legal person's notices must be in Estonian; a foreign-language translation may be added.
  - Employees of companies must speak Estonian only where this is justified in the public interest.
- **LT, Law on the State Language:** UNKNOWN (resolve: one search on e-tar.lt for the law's scope for private companies and consumer information).

Implication: nothing found in the LV or EE acts targets private B2B emails, proposals or CRM content. The constraints bite on public-facing material (signs, advertising, consumer information) and on staff in public-interest roles. Consumer-facing campaigns, which are not this brief's focus, would need state-language versions.

### 3.6 G1 funnel per country (total → right size → target sectors → plausibly reachable), scope: up to fifty staff

The brief's order is total → sectors → size. Here size is applied first because only the size cut is published for all three countries; the order does not change the endpoint. Since the user's scope change (2026-10-03), the size step is "up to fifty staff" (`0–9` + `10–49`) and the `50–249` class is out of scope.

| Step | EE | LV | LT |
|---|---|---|---|
| 1. All enterprises (scope differs, §3.1) | 159,827 (2025) [V:WS1-095] | 107,091 (2024 est., SBS scope) [E:A-WS1-02] | 328.6 thousand (2022, pre-2023) [V:WS1-033] |
| 2. Right size, ≤50 staff (0–49) | 158,489 (2025) [E:A-WS1-16] | 105,523 (2024 est.) [E:A-WS1-18] | ≈325,643 (2022, pre-2023) [E:A-WS1-19] |
| 2a. of which 10–49 (core) | 6,284 [V:WS1-095] | 6,457 [V:WS1-025] | ≈12,815 [E:A-WS1-04] |
| 3. Target sectors, 10–49 | 1,191–3,481 (section level) [E:A-WS1-17] | UNKNOWN (resolve: §3.2 / §7 U1) | UNKNOWN (resolve: §3.2 / §7 U1) |
| 3a. Target sectors, 0–9 | UNKNOWN (C, G, H micro counts missing; sections M 23,994 and N 8,003 known [V:WS1-097]) | UNKNOWN | UNKNOWN |
| 4. Minus hard exclusions (Russia/Belarus trade, share x; H50 and H52.22 removed by definition) | UNKNOWN (resolve: §7 U3) | x ≤≈0.6% of step 2 (400–618 RU/BY goods exporters of all sizes, Jan–Nov 2023) [E:A-WS1-21] | UNKNOWN (resolve: §7 U3) |
| 5. Plausibly reachable | See the database route below; the language filter l is still UNKNOWN (§7 U5) | same | same |
| **Evidence-based ceiling on the core endpoint (10–49)** | **≤ 3,481** [E:A-WS1-17] | **≤ 6,457** [V:WS1-025] | **≤ ≈12,815** [E:A-WS1-04] |
| Reference: 50–249 (out of scope) | 1,151 [V:WS1-095] | 1,363 [V:WS1-025] | ≈2,629 [E:A-WS1-05] |

The statistical-route formula is Reachable_c = N2_c × s_c × (1 − x_c) × d_c × l_c [E:A-WS1-08], with N2_c now the ≤50-staff count. No values were assumed for s (LV, LT) or l, because they could not be sourced.

**Database route (secondary reachability proxy, Hunter.io Discover, 2026-10-03), up to fifty staff.** Counts are company records in a vendor database: **a reachability proxy, not market size.** All rows use the `1-10` + `11-50` headcount buckets; the `11-50` bucket is also shown alone because most `1-10` records are firms with one to four staff.

| Step | EE | LV | LT |
|---|---|---|---|
| D1. All industries, 1-10 + 11-50 staff, in database | 11,930 (8,368 + 3,562) [V:WS1-134] [V:WS1-046] | 6,609 (4,250 + 2,359) [V:WS1-140] [V:WS1-061] | 12,794 (8,427 + 4,367) [V:WS1-146] [V:WS1-076] |
| D1a. 11-50 records as a share of the statistical 10–49 class (coverage indicator) | 56.7% (inflated, see caveats) [E:A-WS1-20] | 36.5% [E:A-WS1-20] | 34.1% [E:A-WS1-20] |
| D2a. Logistics (116) excl. maritime-tagged rows | ≈204 [E:A-WS1-20] | ≈197 [E:A-WS1-20] | ≈414 (upper bound) [E:A-WS1-20] |
| D2b. Wholesale (133) | 271 [V:WS1-136] [V:WS1-050] | 221 [V:WS1-142] [V:WS1-065] | 390 [V:WS1-148] [V:WS1-080] |
| D2c. Manufacturing (25) | 1,024 [V:WS1-137] [V:WS1-052] | 797 [V:WS1-143] [V:WS1-067] | 1,562 [V:WS1-149] [V:WS1-082] |
| D2d. Professional Services (1810); low variant removes IT services (≈1/3) | 2,389–3,584 [V:WS1-138] [V:WS1-054] [E:A-WS1-20] | 1,213–1,819 [V:WS1-144] [V:WS1-069] [E:A-WS1-20] | 2,179–3,269 [V:WS1-150] [V:WS1-084] [E:A-WS1-20] |
| D2e. Administrative & Support (1912) | 456 [V:WS1-139] [V:WS1-056] | 302 [V:WS1-145] [V:WS1-071] | 578 [V:WS1-151] [V:WS1-086] |
| **D2. Target-sector records, ≤50 (sum)** | **4,345–5,539** [E:A-WS1-20] | **2,729–3,336** [E:A-WS1-20] | **5,123–6,213** [E:A-WS1-20] |
| D2 in the 11-50 bucket only | 1,355–1,670 [E:A-WS1-20] | 1,046–1,224 [E:A-WS1-20] | 1,845–2,130 [E:A-WS1-20] |
| D3. Email-availability rate (pooled exact segments) | any 83.0%; personal 61.0% [E:A-WS1-13]; in-scope segments only: any 84.5%, personal 51.9% [E:A-WS9-01] (verifier note — see VL-027) | same [E:A-WS1-13] | same [E:A-WS1-13] |
| **D4. Database-reachable, ≥1 indexed email, ≤50** | **3,606–4,598** [E:A-WS1-20] | **2,265–2,769** [E:A-WS1-20] | **4,252–5,157** [E:A-WS1-20] |
| D4 in the 11-50 bucket only | 1,124–1,386 [E:A-WS1-20] | 868–1,016 [E:A-WS1-20] | 1,531–1,768 [E:A-WS1-20] |
| **D4'. With ≥1 personal (named) email, ≤50** (corrected — see VL-027) | **2,254–3,381** [E:A-WS9-02] (was 2,650–3,379 [E:A-WS1-20]) | **1,416–2,036** [E:A-WS9-02] (was 1,665–2,035 [E:A-WS1-20]) | **2,657–3,793** [E:A-WS9-02] (was 3,125–3,790 [E:A-WS1-20]) |
| D4' in the 11-50 bucket only (corrected — see VL-027) | 703–1,019 [E:A-WS9-02] (was 826–1,019 [E:A-WS1-20]) | 542–747 [E:A-WS9-02] (was 638–747 [E:A-WS1-20]) | 957–1,300 [E:A-WS9-02] (was 1,125–1,299 [E:A-WS1-20]) |
| D5. After language-workability (l) and Russia/Belarus screening (x) | UNKNOWN (§7 U3, U5) | UNKNOWN; x ≤≈0.6% [E:A-WS1-21] | UNKNOWN |

The earlier `11–200` version of this table (`51-200` bucket now out of scope) is kept in A-WS1-10 to A-WS1-14 for reference.

**Caveats that travel with the database route** (lead analyst, `db_coverage_README.md`):
1. **Headcount buckets are not statistical size classes.** Hunter's 1-10 / 11-50 do not match 0–9 / 10–49 (UNKNOWN net effect): a 10-person firm is in Hunter's 1-10 but in the statistical 10–49 class.
2. **Industry is a LinkedIn-style taxonomy, not NACE.**
   - Accounting and Business Consulting are nested inside Professional Services and are **not** added on top.
   - "Wholesale" contains manufacturers tagged as wholesalers.
   - Admin & Support includes travel and events (≈N79, excluded in §2), and these were not removed.
3. **Maritime and aviation inside Logistics.** Maritime Transportation rows are excluded per the brief (done in D2a), using the sampled shares per bucket (UNKNOWN beyond the samples):
   - EE: 18/100 in 1-10 [V:WS1-135] and 18/100 in 11-50 [V:WS1-048]
   - LV: 14/100 in 1-10 [V:WS1-141] and 12/100 in 11-50 [V:WS1-063]
   - LT: 7/100 in 1-10 [V:WS1-147] and 0/100 in 11-50 [V:WS1-078]

   In LT, 99 of the 199 records in the 11-50 bucket were not sampled, so LT is an upper bound. Airlines/Aviation is **retained** pending an operator decision [E:A-WS1-11].
4. **Email shares.** All 1-10 and 11-50 sector segments exceed 100 records, so their own email shares are upper bounds. D3 therefore uses the pooled rate from the 22 exact segments [E:A-WS1-13], which come mostly from larger firms; micro accounting firms show lower personal-email rates (32.6–55.1%) [V:WS1-058] [V:WS1-073] [V:WS1-088], so the ≤50 pools lean high. Fifteen of the 22 exact segments are in the 51-200 bucket, which is out of scope; restricted to in-scope segments the personal-email share is 51.9% [E:A-WS9-01] (corrected — see VL-027).
5. **CRM technology filter not supported.** Database counts cannot be split by CRM in use.

Further caveats:
- **Coverage bias.** The database over-represents firms with websites, LinkedIn or English presence, digital and service firms, and capital-city firms. It under-represents offline and traditional SMEs such as small hauliers.
- **EE ratio inflated.** The EE coverage ratio is inflated by internationally run firms registered in Estonia (e-Residency).
- **Not legal units.** Records are web domains, so one firm can appear under several domains.

**What the two routes together tell the decision (scope: up to fifty staff).**
- **Statistical core:** the in-scope 10–49 class holds ≈6.3k firms in EE [V:WS1-095], ≈6.5k in LV [V:WS1-025] and ≈12.8k in LT [E:A-WS1-04], across all sectors. In Estonia at most ≈3.5k of them sit in the target sections [E:A-WS1-17].
- **Practical outbound pool:** with any indexed email, ≈2.3k–5.2k target-sector firms per country with ≤50 staff, but only ≈0.9k–1.8k per country in the 11-50 bucket [E:A-WS1-20]. The extra volume from the 1-10 bucket is mostly firms too small to buy a CRM or lead-generation retainer (UNKNOWN share; test in interviews).
- **Implication:** an enrichment-tool list for G1 is exhausted after a few campaigns, especially in LV. Deeper coverage needs register-based list building (business registers, association lists); WS4 covers the legality.

### 3.7 G2 — foreign B2B companies selling into the Baltics: size estimate

**Value:** no buyer count yet (UNKNOWN) [E:A-WS1-09]. Partial results from the gap-fill pass:
- **Network route:** foreign chambers with verified counts add up to ≈900 memberships, not de-duplicated [E:A-WS1-24]: AHK Baltic >470 [V:WS1-110]; Scandinavian Chamber EE ≈130 [V:WS1-112]; Norwegian Chamber LV ≈100 [V:WS1-113]; Norwegian-Lithuanian Chamber >100 [V:WS1-114]; Swedish Chamber LT >100 [V:WS1-115].
- **Presence route:** 11% of Estonian enterprises are foreign-controlled, the EU's second-highest share (2023) [V:WS1-109]; LV and LT shares UNKNOWN.
- **Exporter route:** UNKNOWN; partner-country customs databases (e.g., Finnish Customs' Uljas) could not be read via search.
- **Scope note:** chamber members include large firms and Baltic-registered firms; the ≤50-staff filter cannot be applied to G2 counts (UNKNOWN).

**Method (three routes; report the range, not a sum):**
1. **Exporter route:** count enterprises in FI, SE, NO, DK, PL, DE, UA and other EU countries that export goods to EE/LV/LT. Sources: Eurostat TEC partner tables; national customs "exporters by destination" statistics. De-duplicate firms that export to more than one Baltic state by reporting max_c (lower bound) and Σ_c (upper bound).
2. **Presence route:** count foreign-controlled enterprises in each Baltic state by controlling country. Sources: Eurostat inward FATS; CSB Latvia table UZG030 "Number of enterprises in enterprise groups by country" [V:WS1-042]; VDA "Foreign-owned enterprises in Lithuania" [V:WS1-043]. These firms are already present, so they are G2 buyers of local pipeline work rather than market-entry clients.
3. **Network route:** combine the membership of foreign chambers in each Baltic state (see the foreign-chambers section), de-duplicated.

Then apply the same B2B-relevance, sanctions and reachability filters as G1 (A-WS1-08).

**Caveat:** the exporter route counts goods exporters only. Service exporters (SaaS, consultancies) who are natural buyers of Baltic lead generation are not captured by TEC. The network route partly covers them.

---

## 4. Added beyond the brief

### 4.1 Foreign-language proficiency (English, Russian)

Resolved in the gap-fill pass from national census/survey releases. The measures differ by country (census of all ages vs adult survey), so compare directions, not decimals.

| | EE (2021 census) | LV (Adult Education Survey 2022) | LT (2021 census) |
|---|---|---|---|
| Speaks at least one foreign language | 76% of the population [V:WS1-100] | 95.0% of 25–64-year-olds (Eurostat AES) [V:WS1-107] | 76.5% of the population [V:WS1-105] |
| English | 48% speak it as a foreign language [V:WS1-100] | 64.0% speak or understand it (25–64); 46% of those with English as best foreign language rate it advanced [V:WS1-104] | 31.1% have a command of it [V:WS1-105] |
| Russian (non-native speakers) | 39% speak it as a foreign language [V:WS1-100] | 91.3% speak or understand it; 64% of those with Russian as best foreign language rate it advanced [V:WS1-104] | 60.6% have a command of it [V:WS1-105] |
| Harmonised check (Eurostat AES 2022, ≥1 foreign language, 25–64) | 95.5% [V:WS1-107] | 95.0%; 51.5% proficient in best-known language [V:WS1-107] | 95.3% [V:WS1-107] |

A Eurobarometer extract (2024) also ranks Russian as the most widely spoken foreign language in LT (80%), LV (67%) and EE (56%); it is a LEAD because the page was not pinned (WS1-108); treat as UNKNOWN until verified.

Decision use: English is a workable sales language for roughly half of Estonians [V:WS1-100] and about two-thirds of Latvian adults [V:WS1-104], but only for about a third of Lithuanians [V:WS1-105], where the operator's Lithuanian covers the gap. Russian is widely understood in all three, but it is a home language for large groups only in EE and LV (§3.5). These are population shares; owner/manager shares and business-language preferences remain UNKNOWN (U5).

### 4.2 Foreign chambers / business associations in each Baltic state (G2 sizing)

| Country | Body | Members | Member list public? | Source |
|---|---|---|---|---|
| EE, LV, LT | German-Baltic Chamber of Commerce (AHK Baltische Staaten; offices in Tallinn, Riga, Vilnius) | >470 member companies (a newer page: almost 500) | Yes (member database) | [V:WS1-110] [V:WS1-111] |
| EE | Scandinavian Chamber of Commerce in Estonia (merger of the Swedish, Danish and Norwegian chambers on 1 Jan 2025) | ≈130 companies | UNKNOWN | [V:WS1-112] |
| EE | Finnish-Estonian Chamber of Commerce (FECC) | UNKNOWN | UNKNOWN | not found |
| EE | Ukrainian-Estonian Chamber of Commerce (UECC, founded 2019) | UNKNOWN | UNKNOWN | [V:WS1-118] |
| LV | Norwegian Chamber of Commerce in Latvia (NCCL) | close to 100 | UNKNOWN | [V:WS1-113] |
| LV | Finnish Chamber of Commerce in Latvia (FCCL) | UNKNOWN (36 corporate members at end-2020 is a LEAD, WS1-116) | UNKNOWN | LEAD |
| LV | Polish chamber (plcc.lv); Swedish and Danish chambers | UNKNOWN | UNKNOWN | not verified |
| LT | Norwegian-Lithuanian Chamber of Commerce (NLCC) | >100 companies | UNKNOWN | [V:WS1-114] |
| LT | Swedish Chamber of Commerce in Lithuania (SCCL) | >100 companies and "Fan-Club" members | UNKNOWN | [V:WS1-115] |
| LT | Polish and Lithuanian Chamber of Commerce | UNKNOWN | UNKNOWN | [V:WS1-117] |
| LT | Ukrainian-Lithuanian Chamber of Commerce (>120 participants at the founding meeting) | UNKNOWN | UNKNOWN | [V:WS1-119] |

Sum of verified counts: ≈900 memberships, not de-duplicated [E:A-WS1-24]. Still to verify: American Chambers, FICIL (LV), Investors' Forum (LT), Danish/Finnish chambers in LT. Resolve: one search per body for "members" on its own domain.

### 4.3 Russian-speaking-owned and Ukrainian-owned SME populations

UNKNOWN. Resolve via business-register statistics by owner citizenship:
- LV: Lursoft publishes statistics on companies registered with Ukrainian participants since 2022.
- EE: e-Business Register (RIK) / Inforegister owner-citizenship statistics.
- LT: Registrų centras / JAR founder statistics.

Also needed are regional counts for Ida-Virumaa (EE: Statistics Estonia county tables), Riga (LV: CSB UZS030/UZS031 regional split [V:WS1-030]; Riga region = 65.8% of GDP in 2023 [V:WS1-032]) and Vilnius county (LT: VDA). Sanctions note: owner nationality is not a sanctions criterion. Screening applies to trade with or control from Russia/Belarus and to listed persons (WS4 holds the screening method).

### 4.4 Accounting firms (NACE M69.20) and professional bodies

| | EE | LV | LT |
|---|---|---|---|
| M69.20 enterprises, total / 10–49 / 50–249 | UNKNOWN (resolve: ER025 at 4-digit EMTAK 69201–69203, 2024) | UNKNOWN (resolve: CSB UZS020/UZS030 at NACE 69.20) | UNKNOWN (resolve: VDA operating enterprises, NACE 69.20) |
| Accounting records in Hunter database (reachability proxy; industry 47, misclassification noise noted) | ≤50 staff (1-10 + 11-50): 97 (78 + 19) [E:A-WS1-20]; 1–200 staff: 103 [E:A-WS1-15]; ≥1 email 88.3%, personal 61.2% (1–200) [V:WS1-058] [V:WS1-059] [V:WS1-060] | ≤50: 63 (46 + 17) [E:A-WS1-20]; 1–200: 67 [E:A-WS1-15]; ≥1 email 74.6%, personal 41.8% [V:WS1-073] [V:WS1-074] [V:WS1-075] | ≤50: 126 (89 + 37) [E:A-WS1-20]; 1–200: 131 [E:A-WS1-15]; ≥1 email 86.3%, personal 47.3% [V:WS1-088] [V:WS1-089] [V:WS1-090] |
| Certified/licensed accountants and auditors | Audiitorkogu: 338 sworn auditors and 112 audit firms (30.06.2025) [V:WS1-128]; certified accountants (ERK) 4,182 in 2020 is a LEAD (WS1-129); current count UNKNOWN (resolve: Estonian Qualifications Authority register) | ≈2,800 VID licences for outsourced-accounting providers (mid-2023; down from 5,886 registered providers) [V:WS1-127]: the closest available count of firms and individuals selling bookkeeping | >300 certified auditors (2025) [V:WS1-130]; LBAA membership conflicting (LEAD WS1-131); no licensing of bookkeepers known |
| Structural expectation | Most M69.20 firms are expected to be micro (0–9) in all three countries. If so, accounting firms are better **referral partners** (many small offices, each serving many SME clients) than direct buyers of a CRM project. This is a hypothesis to test with the counts above. The database counts point the same way: most listed accounting records are in the 1-10 bucket [E:A-WS1-15]. With the ≤50-staff scope, almost all accounting firms are in scope by size. | same | same |

**Reading the database counts.** The database lists only about a hundred accounting firms per country [E:A-WS1-15]. Building a list of accountants as referral partners would therefore rely on register extracts (EMTAK/NACE 69.20 filters in national business registers or Lursoft/Rekvizitai-type tools; WS4 covers the legality of these) and on association lists, not on enrichment tools.

### 4.5 Re-verification of prior lead: ELEA member count

**Confirmed.** ELEA lists 65 members, including 13 associate members, on a public members page (2026) [V:WS6-007]. WS6 verified this, and WS1 re-checked the row. Verifier re-check (2026-10-03): the prior lead of about 65 holds, but another page on the ELEA site reports 68 members including 17 associates and 6,170 employees in member companies, an average of 91 per member (LEAD VL-021; page attribution not pinned). If the average is representative, many members are above the up-to-fifty scope (corrected — see VL-021).

---

## 5. Conflicts between sources

| Topic | Value A | Value B | Which we trust and why |
|---|---|---|---|
| LT enterprises 10–249 | ≈15,444 (2022, pre-2023) from VDA total × VDA shares [E:A-WS1-06] | 13,592 (2024 est.) from EC SME Fact Sheet 2025, LEAD WS1-039, not tied to a URL; 13,265 (c.2018) from 2019 SBA fact sheet [V:WS1-036] (pre-2023) | **VDA-based estimate**, because it is an observed national count, consistent with 2021 (pre-2023: ≈14,940 [V:WS1-035]). The EC figures are model estimates; the 2025 one is unverified. The ~12% gap may reflect different population definitions. Resolve with Eurostat `sbs_sc_ovw` for 2023–2024 (§7 U1). |
| LT "operating economic entities" | 122,458 at 1 Jan 2023 (+7.9%) (LEAD; extract from osp.stat.gov.lt, page not identified) | 151,868 at start of 2025 (+6.2%) (LEAD WS1-040) | Neither used. Growth from A to B implies about +24% in two years, which is inconsistent with +6.2% p.a. The definitions likely differ (legal entities vs all entities). Count UNKNOWN until definitions are checked. |
| LTRK membership | 6,000 members incl. associations and business clubs [V:WS6-003] | ~3,000 enterprises + ~3,000 via associations, or >2,600 individual members + ~60 associations (LEAD WS6-030) | Use **"≈2,600–3,000 direct company members"** as the working range for list-building, with low confidence. The 6,000 headline includes indirect members. |
| Kaubanduskoda membership | ~3,402 listed on the members page [V:WS6-001] | "over 3,500 direct members" [V:WS6-002] | **~3,400 listed** for list-building (observable); the 3,500 claim may be older or rounded. |
| Size of the 10–249 universe: statistics vs database | Statistics: EE 7,579 [E:A-WS1-01]; LV 7,820 [E:A-WS1-02]; LT ≈15,444 [E:A-WS1-06] | Hunter 11–200 records: EE 4,675; LV 3,268; LT 6,116 [E:A-WS1-10] | Not a true conflict: different units (legal enterprises vs web domains) and bands. **Use statistics for market size and the database for reachability.** The database's relative ordering (EE above LV) partly reflects database composition (Estonian-registered international firms), not the economy. |
| EE vs LV size counts | EE 10–249: 7,579 (all sectors, employees) [E:A-WS1-01] | LV 10–249: 7,820 (SBS scope, persons employed) [E:A-WS1-02] | Not directly comparable (§3.1). The LV figure likely *undercounts* relative to the EE definition, because SBS excludes agriculture/finance/public. Treat both as about 7.6–7.8 thousand with ± uncertainty, pending §7 U1. |
| EE enterprise counts 2024 vs 2025 | 2024: total 158,378; 10–49 6,461 [V:WS1-001] [V:WS1-003] | 2025: total 159,827; 10–49 6,284 [V:WS1-095] | Not a conflict (different reference years). **Use 2025.** An extract also mentioned 159,747 for 2024; it does not match the verified 2024 total and is not used. |
| LV Russian share | Used at home 34.6% (18–69, AES 2022) [V:WS1-101] | Mother tongue 37.7% (LEAD WS1-103) | Use the home-language figure (pinned to a CSB release). Mother tongue and home language measure different things. |
| LT size classes 2024 | EC SME Fact Sheet 2025: small 11,348 (LEAD WS1-039, re-seen 2026-10-03, URL not pinned) | VDA-based 2022: ≈12,815 [E:A-WS1-04]; cross-check 12.2% of SMEs [V:WS1-098] | Keep the VDA-based figure until `sbs_sc_ovw` or a VDA 2025 table is read. |
| LBAA membership (LT) | >700 members (LEAD WS1-131) | 472 (2020), 464 (2018) (same LEAD) | Neither used; membership UNKNOWN. Ask LBAA directly. |

---

## 6. Search-language log

| Language | Example queries | Found | Not found |
|---|---|---|---|
| EN | "Statistics Estonia number of economically active enterprises 2024 by number of persons employed 10-49 50-249" (stat.ee); "CSB Latvia economically active enterprises 2024 … size group" (stat.gov.lv); "SME country fact sheet 2025 Latvia …" (ec.europa.eu); "SMEs in operation Lithuania …" (osp.stat.gov.lt); "Eurostat sbs_sc_ovw …" | EE totals and size classes [V:WS1-001] [V:WS1-003] (also WS1-002, WS1-004); LV EC fact sheet (WS1-025–027); Eurostat `sbs_sc_ovw` metadata (WS1-028); LT *Business in Lithuania* totals and shares (WS1-033–036); LV trade and Riga GDP releases (WS1-031, WS1-032); EMTAK 2025 pointers (WS1-044, WS1-045) | CSB national size counts; LT 2024/2025 counts; EE and LT 2025 SME fact sheets |
| ET | "majanduslikult aktiivsed ettevõtted 2024 tööga hõivatud isikute arv statistikaamet"; "Eesti ettevõtted 2024 töötajate arvu järgi 10–49 50–249" | The EE 10–49 count of 6,461 [V:WS1-003] was first surfaced by the ET query; trade-by-size release title (WS1-041) | 50–249 count (found later via EN) |
| LV | "ekonomiski aktīvo uzņēmumu skaits 2024 pēc lieluma grupām"; "tirgus sektora ekonomiski aktīvo uzņēmumu skaits 2024" | Table IDs UZS020, UZS030/UZS031, UZS041, UZS011 (WS1-029, WS1-030) | Any LV size-class values (PxWeb tables are not readable via search) |
| LT | "veikiančių ūkio subjektų skaičius 2025 m. pradžioje pagal darbuotojų skaičių"; "Verslas Lietuvoje 2025 …"; "Lietuva skaičiais 2025 …" | Registrų centras legal-entity counts via duomenugalia.lt (WS1-038); conflicting operating-entity LEADs (WS1-040) | VDA 2024/2025 size-class values |
| RU | none run (budget exhausted) | — | Russian-language business-community and language-use evidence is entirely open |
| (API, not search) | Hunter.io Discover natural-language company queries, run by the lead analyst (`db_coverage.csv`) | Database-coverage counts by country × headcount × industry (WS1-046 to WS1-094) | CRM-technology split (filter not supported) |
| EN (gap-fill) | stat.ee "economically active enterprises 2025 … 10-49 50-249"; stat.gov.lv AES language releases; osp.stat.gov.lt census; Eurostat AES, FATS, TEC; chamber member counts; likumi.lv, riigiteataja.ee language acts | EE 2025 size and section counts [V:WS1-095] [V:WS1-096] [V:WS1-097]; census/AES language data (WS1-099–107); foreign-control share (WS1-109); chambers (WS1-110–119); export partners and RU/BY exporters (WS1-120–126); language-law scope (WS1-132–133) | LV/LT sector × size values; exporter counts; Finnish exporter counts to the Baltics |
| ET (gap-fill) | "2025. aastal majanduslikult aktiivseid ettevõtteid … 10–49 50–249"; "Eesti Raamatupidajate Kogu liikmete arv … vandeaudiitorite arv" | EE 2025 size totals [V:WS1-095]; Audiitorkogu counts [V:WS1-128] | ERK member count |
| LV (gap-fill) | "ārpakalpojuma grāmatvedības pakalpojumu sniedzēji … licence skaits" | VID licensing count (WS1-127) | CSB size × sector values |
| LT (gap-fill) | "veikiančių mažų ir vidutinių įmonių skaičius 2025 …"; "2021 m. surašymas gimtoji kalba …"; "Lietuvos auditorių rūmai auditorių skaičius" | 2022 SME structure (WS1-098); census languages (WS1-105); auditors (WS1-130) | VDA 2025 size or sector counts; 2024–2025 export partners |
| DE (gap-fill) | "Deutsch-Baltische Handelskammer … Mitglieder Anzahl" | AHK member count (WS1-110, WS1-111; logged as EN in the CSV because the field allows only EN/ET/LV/LT/RU) | — |
| RU (gap-fill) | none run (pass stopped by the user) | — | Russian-language business-language evidence is still open |

---

## 7. UNKNOWNs and cheapest resolution

**Resolved in gap-fill pass (2026-10-03, 41 searches, stopped by the user):** U4 Russian-speaking shares (EE, LV, LT) [V:WS1-099] [V:WS1-101] [E:A-WS1-23]; U6 English/Russian proficiency (EE, LV, LT) [V:WS1-100] [V:WS1-104] [V:WS1-105]; U7 language-law scope for LV and EE [V:WS1-132] [V:WS1-133]. Partly resolved: U1 (EE at section level only) [E:A-WS1-17]; U2 (EE updated to 2025 [V:WS1-095]; LV and LT not); U3 (export partners for all three, LV Russia/Belarus exporter counts [V:WS1-123]; exporter counts open); U8 and U11 (foreign-chamber counts [E:A-WS1-24]; EE foreign-control share [V:WS1-109]); U9 (professional bodies [V:WS1-127] [V:WS1-128] [V:WS1-130]; M69.20 statistics open). **Scope change:** only firms with ≤50 staff are in scope; resolutions below now need the 0–9 and 10–49 classes only (50–249 out of scope).

| # | Unknown | Countries | Cheapest resolution |
|---|---|---|---|
| U1 | Target-sector × size counts (C, G46, H49–H53 minus H50/H52.22, M69/M69.20, M70–M74, N77–N82) | EE, LV, LT | Eurostat `sbs_sc_ovw` [V:WS1-028], a single short browser session (filters in §3.2). 4-digit splits from EE ER025 [V:WS1-004], LV UZS030/UZS031 [V:WS1-030], LT VDA indicators database. |
| U2 | UNKNOWN: national 2024/2025 size counts (0–9, 10–49) for LV (replacing the EC model estimate) and LT (replacing the 2022 estimate); EE done (2025) | LV, LT | CSB UZS031 (2024) and VDA "operating enterprises at the beginning of 2025 by personnel group". One browser session each. |
| U3 | Exporting SMEs, destination markets, and the share trading with RU/BY (exclusion filter x) | EE, LV, LT | Eurostat TEC tables (size class × exporters; partner tables incl. RU/BY); national annual trade releases (EE, LV [V:WS1-031], LT) |
| U4 | **Resolved** (see line above). Residual UNKNOWN: LV mother-tongue share (LEAD WS1-103) | LV | CSB AES 2022 release on mother tongue |
| U5 | UNKNOWN: language actually used by SMEs for sales and internal operations, by segment | EE, LV, LT | Interview question: "In which language do you (a) sell to Baltic customers, (b) run your CRM and internal documents, (c) prefer to buy services?" Plus an A/B test: the same cold sequence in EN vs RU vs local language to a few dozen target firms per arm (size the arms with WS6 reply-rate benchmarks). |
| U6 | **Resolved** at population level (§4.1). Residual UNKNOWN: proficiency of SME owners/managers specifically | EE, LV, LT | Interview question on working language; Eurobarometer 2024 country factsheets (LEAD WS1-108) |
| U7 | **Resolved for LV and EE** (§3.5c). Still UNKNOWN: LT Law on the State Language | LT | One search on e-tar.lt for the law's scope for private companies |
| U8 | G2 size | EE, LV, LT | §3.7 routes 1–3; start with CSB UZG030 [V:WS1-042] and VDA foreign-owned enterprises [V:WS1-043] |
| U9 | UNKNOWN: accounting firms M69.20 by size (bodies partly resolved, §4.4) | EE, LV, LT | §4.4 tables; LV State Revenue Service licence register for outsourced accountants (lead to verify) |
| U10 | Database reachability: **partly resolved** with Hunter counts (§3.6 database route; [E:A-WS1-14]). Still open: (a) email rates for large segments, where only upper bounds exist; (b) Apollo coverage (not in the supplied file); (c) the share of statistical target-sector firms *absent* from databases, which needs U1 sector counts as the denominator | EE, LV, LT | (a)/(b) A small random sample (a few dozen firms) per country from a register extract (not ranked by email count), checked in Hunter/Apollo. This gives an unbiased hit rate. (c) U1 |
| U11 | UNKNOWN: remaining foreign chambers' member counts (partly resolved, §4.2) | EE, LV, LT | One search per body (§4.2) |
| U12 | UNKNOWN: Russian-/Ukrainian-owned SME counts; regional counts (Ida-Virumaa, Riga, Vilnius) | EE, LV, LT | Register statistics (§4.3); EE county tables; CSB UZS030/031; VDA county tables |
| U13 | LAFF member count; LTRK direct company count; LT chamber direct counts; accountants' and exporters' associations | LV, LT, EE | Count rows on the public lists (LAFF [V:WS6-009]); ask the associations directly |

---

## 8. Synthesis inputs (per country)

All scores are 1–5, where 5 = most favourable to the operator. Scores are suggested only where WS1 evidence supports them; otherwise they are UNKNOWN. **Scope: firms with ≤50 staff (user, 2026-10-03); 50–249 out of scope.**

| Item | EE | LV | LT |
|---|---|---|---|
| Enterprises 10–49 (core of the ≤50 scope) | 6,284 (2025) [V:WS1-095] | 6,457 (2024 est.) [V:WS1-025] | ≈12,815 (2022, pre-2023) [E:A-WS1-04] |
| Enterprises 0–9 (in scope, mostly one-person firms) | 152,205 (2025) [V:WS1-095] | 99,066 (2024 est.) [V:WS1-025] | ≈312,827 (2022, pre-2023) [E:A-WS1-19] |
| Target-sector counts, 10–49 | 1,191–3,481 (section level) [E:A-WS1-17]; C 1,191, G ≤1,036, H ≤472 [V:WS1-096]; M ≤407, N ≤375 [V:WS1-097] | UNKNOWN (U1) | UNKNOWN (U1) |
| Target-sector counts, 50–249 | out of scope (not needed) | out of scope (UNKNOWN, not needed) | out of scope (UNKNOWN, not needed) |
| G1 funnel endpoint (statistical route, core 10–49) | ceiling ≤3,481 [E:A-WS1-17] | UNKNOWN; ceiling ≤6,457 [V:WS1-025] | UNKNOWN; ceiling ≤≈12,815 [E:A-WS1-04] |
| G1 database-reachable target-sector firms, ≤50 staff, ≥1 email (before language and sanctions screens) | 3,606–4,598 [E:A-WS1-20] | 2,265–2,769 [E:A-WS1-20] | 4,252–5,157 [E:A-WS1-20] |
| Same, 11-50 bucket only | 1,124–1,386 [E:A-WS1-20] | 868–1,016 [E:A-WS1-20] | 1,531–1,768 [E:A-WS1-20] |
| Same, with a named (personal) email, ≤50 (corrected — see VL-027) | 2,254–3,381 [E:A-WS9-02] | 1,416–2,036 [E:A-WS9-02] | 2,657–3,793 [E:A-WS9-02] |
| Database coverage of the statistical 10–49 class (11-50 records) | 56.7% (inflated) [E:A-WS1-20] | 36.5% [E:A-WS1-20] | 34.1% [E:A-WS1-20] |
| Accounting firms listed in database (≤50 staff) | 97 [E:A-WS1-20] | 63 [E:A-WS1-20] | 126 [E:A-WS1-20] |
| Accounting professional bodies | 338 sworn auditors, 112 audit firms (2025) [V:WS1-128] | ≈2,800 licensed outsourced-accounting providers (2023) [V:WS1-127] | >300 certified auditors (2025) [V:WS1-130] |
| Suggested market-size score (G1, ≤50 scope) | 2 (core class ≈6.3k, target ≤3.5k; basis [E:A-WS1-17]) | 2 (core class ≈6.5k; basis [V:WS1-025]) | 3 (about twice EE/LV; basis [E:A-WS1-04]) |
| G2 estimate | UNKNOWN; network route ≈900 chamber memberships Baltic-wide (not de-duplicated) [E:A-WS1-24]; 11% of enterprises foreign-controlled (2023) [V:WS1-109] | UNKNOWN; network route as EE [E:A-WS1-24] | UNKNOWN; network route as EE [E:A-WS1-24] |
| Russian-speaking share | Mother tongue 29% [V:WS1-099]; ≈68% can speak Russian [E:A-WS1-22] | Russian at home 34.6% (18–69) [V:WS1-101] | Mother tongue ≥≈4.6% [E:A-WS1-23] |
| English / Russian proficiency | English 48%, Russian 39% as foreign languages (2021) [V:WS1-100] | English 64.0%, Russian 91.3% spoken or understood (2022) [V:WS1-104] | English 31.1%, Russian 60.6% (2021) [V:WS1-105] |
| Language-law constraint summary | Private-sector language regulated only for public-interest cases; public signs, advertising and notices in Estonian; no B2B-email rule found [V:WS1-133] | Same pattern (Section 2 public-interest test; Section 21 public information) [V:WS1-132] | UNKNOWN (U7) |
| Russia/Belarus exporter exposure | UNKNOWN | 400–618 firms (Jan–Nov 2023), ≤≈0.6% of ≤50 firms [E:A-WS1-21] | UNKNOWN |
| Operator speaks state language? | No (BRIEF §2) | No (BRIEF §2) | Yes (BRIEF §2) |
| Association member lists public? | Yes: Kaubanduskoda ~3,402 [V:WS6-001]; ELEA 65–68 [V:WS6-007] (corrected — see VL-021); AHK database [V:WS1-111] | Partly: LAFF yes [V:WS6-009]; AHK database [V:WS1-111]; LTRK UNKNOWN | Partly: AHK database [V:WS1-111]; LINEKA count only (42 undated; 60 in 2021) [V:WS6-008] [V:VL-022] (corrected — see VL-022); chambers ~2,000 [V:WS6-004], list status UNKNOWN |
| Multilingual (incl. RU) Baltic coverage already offered by competitors? | Yes [V:WS3-002] [V:WS3-009] | Yes [V:WS3-002] [V:WS3-009] [V:WS3-013] | Yes [V:WS3-002] [V:WS3-009] |

---

## Appendix A — Follow-up query plan (to close UNKNOWNs if the search budget is raised)

These are listed in priority order; together they need a few dozen searches.
1. `allowed_domains=["ec.europa.eu"]`: `"sbs_sc_ovw Estonia Latvia Lithuania number of enterprises 10-49 manufacturing wholesale G46 2023"`. Then repeat per sector.
2. `["stat.gov.lv"]`: `"UZS031 2024 10-49 50-249 nodarbināto"` and the CSB annual press release on economically active enterprises (LV).
3. `["osp.stat.gov.lt"]`: `"veikiančių įmonių skaičius 2025 m. pradžioje darbuotojų skaičiaus grupės 10–19 20–49 50–99 100–249"`.
4. Census language: `["stat.ee","rahvaloendus.ee"]` "emakeel vene 2021 rahvaloendus"; `["stat.gov.lv"]` "2021 tautas skaitīšana mājās runātā valoda krievu"; `["osp.stat.gov.lt"]` "2021 surašymas gimtoji kalba rusų".
5. `["europa.eu"]`: "Special Eurobarometer Europeans and their languages 2024 Estonia Latvia Lithuania English Russian".
6. `["ec.europa.eu"]`: "Adult Education Survey 2022 foreign language knowledge Estonia Latvia Lithuania Russian English".
7. Eurostat TEC: "trade by enterprise characteristics number of exporting enterprises Estonia size class 2023"; partner tables for RU/BY.
8. Foreign chambers (see the foreign-chambers section) and accountants' bodies (see the accounting section): one query each on their own domains.
9. RU-language: "русскоязычный бизнес Латвия Эстония язык общения с клиентами исследование" (any survey evidence on business language use).
