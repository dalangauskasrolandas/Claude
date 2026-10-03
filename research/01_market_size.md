# 01 — Market size & structure (WS1)

**Scope:** how many Baltic B2B buyers exist and how they are structured (size, sector, exports, associations, language), per country (EE / LV / LT), plus G1 funnels and a G2 sizing method.

> **Status: PARTIAL.** The session-wide WebSearch budget (shared by all six workstream agents) ran out early in this workstream's run, and direct page fetching (WebFetch/curl) is blocked in this environment. Everything marked **UNKNOWN** below was **not researched**, which is different from "searched and not found". Each UNKNOWN names the exact table, filter or query that resolves it. Most can be resolved in a short session by a person with a normal browser (see §7 and Appendix A). The "plausibly reachable" step uses the lead analyst's Hunter.io database-coverage counts (`research/_work/data/db_coverage.csv`, 2026-10-03), which arrived during this run.

**Legend**
- `[V:WS1-0xx]` = VERIFIED, row in `research/_work/sources_WS1.csv`. `[V:WS6-0xx]`, `[V:WS3-0xx]`, `[V:WS0-0xx]` = VERIFIED by another workstream or by the lead analyst (WS0). These rows are cited by ID rather than copied (all merge into `sources.csv`).
- `[E:A-WS1-0x]` = ESTIMATE; formula and inputs in `research/_work/assumptions_WS1.md` (short formula also shown inline).
- `LEAD` = seen in a search extract but not tied to a confirmable URL, so not used as evidence.
- `UNKNOWN (resolve: …)` = not established.
- Size-class labels (0–9, 10–49, 50–249, 250+) and the brief's ICP definition (5–100 staff) are category definitions, not statistics.

**Method note:** Evidence gathered via web-search extracts on 2026-10-03; direct page fetching was blocked in this environment. Searches used `allowed_domains` to force primary sources (stat.ee, andmed.stat.ee, stat.gov.lv, data.stat.gov.lv, osp.stat.gov.lt, ec.europa.eu, single-market-economy.ec.europa.eu, eimin.lrv.lt), in EN, ET, LV and LT. No RU-language searches could be run before the budget ran out. Derived numbers were computed in code. Database-coverage rows (Hunter.io Discover, run by the lead analyst; vendor database = secondary; method `api-query`) are cited row by row via their permalinks (WS1-046 to WS1-094).

---

## 1. Key findings

1. **The G1 universe is small and hard-capped.** Across the three states there are only ≈30,800 enterprises in the 10–249 size band (range 30,515–31,172; mixed reference years 2022–2024, LT part pre-2023) [E:A-WS1-07]. That band is the closest published proxy for the brief's 5–100-staff ICP. Every later funnel filter (sector, exclusions, reachability, language) can only shrink it.
2. **Estonia: 7,579 enterprises with 10–249 employees in 2024** (6,461 small + 1,118 medium) [V:WS1-003] [E:A-WS1-01], out of 158,378 economically active enterprises [V:WS1-001]. 95.1% have fewer than 10 employees [E:A-WS1-01]. The size classes sum exactly to the total, so this is a reliable count.
3. **Latvia: 7,820 enterprises with 10–249 persons employed (2024 EC/JRC estimate)** (6,457 small + 1,363 medium) [V:WS1-025] [E:A-WS1-02]. The average Latvian "medium" firm employs ≈98.5 persons [E:A-WS1-03], so a material part of the 50–249 class is above the brief's 100-staff ceiling. No CSB national figure could be extracted. The tables are identified (UZS030/UZS031) [V:WS1-030]. Activity is concentrated: the Riga region produced 65.8% of Latvia's GDP in 2023 [V:WS1-032].
4. **Lithuania has about twice the Estonian or Latvian band: ≈12,800 small and ≈2,600 medium enterprises (2022, pre-2023)** [E:A-WS1-04] [E:A-WS1-05]. That gives ≈15,400 in the 10–249 band [E:A-WS1-06], derived from the State Data Agency's total (328.6 thousand enterprises in 2022) [V:WS1-033] and its size shares (3.9% small, 0.8% medium) [V:WS1-034]. An unconfirmed EC 2024 estimate is about 12% lower (LEAD WS1-039; see §5). Lithuania is also the only market where the operator speaks the state language (operator profile, BRIEF §2).
5. **The pool reachable through a standard enrichment tool is a few thousand firms, not tens of thousands.** Hunter lists target-sector firms with 11–200 staff and at least one indexed email as follows [E:A-WS1-14]:

   | Country | Firms with ≥1 indexed email | With a named (personal) email |
   |---|---|---|
   | EE | 1,485–1,810 [E:A-WS1-14] | 1,092–1,331 [E:A-WS1-14] |
   | LV | 1,201–1,383 [E:A-WS1-14] | 883–1,017 [E:A-WS1-14] |
   | LT | 2,117–2,410 [E:A-WS1-14] | 1,556–1,772 [E:A-WS1-14] |
   | Baltic total | 4,803–5,603 [E:A-WS1-14] | 3,531–4,120 [E:A-WS1-14] |

   These counts come before the language and sanctions screens. Hunter covers only ≈42% (LV) and ≈40% (LT) of the statistical 10–249 band, and 62% for EE, where the figure is inflated by internationally run Estonian-registered firms [E:A-WS1-10]. Vendor-database counts are a reachability proxy, not market size.
6. **Accounting firms are thin in the database:** Hunter lists only 103 (EE), 67 (LV) and 131 (LT) accounting records with 1–200 staff [E:A-WS1-15]. Outreach to accountants (the brief's planned client and referral segment) would need register or association lists rather than enrichment tools. The statistical M69.20 population is UNKNOWN (§4.4).
7. **Associations:**
   - **Prior lead re-verified:** ELEA lists 65 members, including 13 associate members, on a public list (2026) [V:WS6-007].
   - Logistics associations are small: LINEKA (LT) has 42 members [V:WS6-008], and LAFF (LV) has a public list without a stated count [V:WS6-009].
   - The largest pools are the general chambers: Estonian Chamber of Commerce and Industry ~3,402 listed members [V:WS6-001]; LTRK 6,000 including associations [V:WS6-003] (direct count disputed, LEAD WS6-030); Lithuanian chambers ~2,000 [V:WS6-004].
8. **Multilingual Baltic coverage is not unique in the market.** Fontakt offers representation in ET, RU, DE, EN, FI, SV, LV and LT [V:WS3-002]. Ripe Leads runs campaigns in LT, LV, ET, PL, CZ, SK, DE, EN and RU [V:WS3-009]. A Riga Pipedrive partner lists EN, ET, LV, LT, RU and UK [V:WS3-013]. "EN + RU + LT" alone is therefore not a differentiator unless WS3/WS6 find price, segment or delivery-model gaps.
9. **Tool-language support differs by country:**
   - HubSpot offers Latvian and Lithuanian interfaces but not Estonian [V:WS0-003].
   - Pipedrive added Latvian in 2022 [V:WS0-001].
   - Zoho supports Russian fully, but Estonian, Latvian and Lithuanian only partially [V:WS0-004].

   This is relevant to which language a client's team would run its CRM in.
10. **Still UNKNOWN in this run:** sector × size statistics, exporters, Russian-speaking shares, language proficiency and language-law constraints. The language-workability filter therefore cannot be applied, and the trilingual-edge question cannot be scored from WS1 evidence yet (§7 gives resolutions).

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

**Size.** The brief's ICP is 5–100 staff. Published size classes are 0–9 / 10–49 / 50–249 (EE, LV), and LT also has finer groups. **10–249 is used as the proxy.** It omits firms with 5–9 staff and includes firms with 101–249 staff. The net bias is UNKNOWN (resolve: LT finer personnel groups in VDA tables; EE/LV micro-data are not public, so use the 10–49 band as a conservative core).

---

## 3. Body

### 3.1 Active enterprises by size class — EE / LV / LT

| Size class | EE (2024, national, by employees) | LV (2024, EC SME Fact Sheet 2025 = JRC estimate, SBS scope, persons employed) | LT (2022 (pre-2023), VDA, persons employed) |
|---|---|---|---|
| 0–9 | 150,612 [V:WS1-002] | 99,066 [V:WS1-025] | share 95.2% [V:WS1-034] |
| 10–49 | 6,461 [V:WS1-003] | 6,457 [V:WS1-025] | ≈12,815 (12,651–12,980) [E:A-WS1-04]; share 3.9% [V:WS1-034] |
| 50–249 | 1,118 [V:WS1-003] | 1,363 [V:WS1-025] | ≈2,629 (2,465–2,793) [E:A-WS1-05]; share 0.8% [V:WS1-034] |
| 250+ | 187 [V:WS1-003] | 205 [V:WS1-025] | share 0.1% [V:WS1-034] |
| **Total** | **158,378** [V:WS1-001] | **107,091** [E:A-WS1-02] | **328.6 thousand** [V:WS1-033] |
| **10–249** | **7,579** [E:A-WS1-01] | **7,820** [E:A-WS1-02] | **≈15,444 (15,116–15,773)** [E:A-WS1-06] |
| Source table / dataset | Statistics Estonia ER025 (by employees × EMTAK 2008) [V:WS1-004]; also ER026 | EC SME Performance Review fact sheet [V:WS1-025]; national tables CSB UZS020 [V:WS1-029], UZS030/UZS031 [V:WS1-030] | VDA *Business in Lithuania 2023* [V:WS1-033] [V:WS1-034] |

**Comparability warnings**
- **Population scope differs.**
  - The EE count covers *all economically active enterprises in the statistical profile*, every EMTAK section, by *employees*.
  - The LV count covers the Eurostat SBS business economy (excludes agriculture, finance and most public/social services), by *persons employed* (owners included).
  - The LT total includes very small units such as natural persons engaged in business.

  For the 10–249 band these differences matter less than for the micro class, but they do not vanish.
- **Reference years differ.** EE is 2024 (observed); LV is 2024 (model estimate from 2008–2023 data [V:WS1-027]); LT is 2022 (pre-2023; observed shares × observed total).
- **The LV persons-employed data show the medium class sits near the ICP ceiling.** Small firms average ≈20.4 persons and medium firms ≈98.5 [E:A-WS1-03]; underlying data [V:WS1-026].
- **LT is stable over time.** The 2021 (pre-2023) cross-check gives ≈12,550 small and ≈2,390 medium (shares 4.2% and 0.8% of 298.8 thousand) [V:WS1-035] [E:A-WS1-04] [E:A-WS1-05]. Growth in the LT total comes from very small units, not from the 10–249 band.
- **Eurostat harmonised alternative.** `sbs_sc_ovw` (Enterprise statistics by size class and NACE Rev. 2 activity, from 2021 onwards) holds 2021–2024 data, last updated 15/09/2026 [V:WS1-028]. Its values could not be extracted. It is the single best source to replace all three columns with one methodology (see §7, U1).

Other LT context (not used in calculations):
- About 100,000 legal-entity SMEs were operating at the beginning of 2023 (ministry figure) [V:WS1-037].
- 223,290 legal entities were registered at 1 July 2025, including 100,056 UAB and 60,038 MB (secondary analysis of Registrų centras data) [V:WS1-038].

### 3.2 Enterprises by target sector × size class

| Sector (see §2) | EE 10–49 / 50–249 | LV 10–49 / 50–249 | LT 10–49 / 50–249 |
|---|---|---|---|
| C manufacturing | UNKNOWN (resolve: ER025, 2024, EMTAK section C × employee groups) | UNKNOWN (resolve: CSB UZS030/UZS031, 2024, NACE C × size group) | UNKNOWN (resolve: VDA operating enterprises at start of year by NACE × personnel group) |
| G46 wholesale | UNKNOWN (ER025, G46) | UNKNOWN (UZS030/031, G46) | UNKNOWN (VDA, G46) |
| H49, H51, H52 excl. H52.22, H53 | UNKNOWN (ER025, 3-digit H52 needed to drop H52.22) | UNKNOWN | UNKNOWN |
| M69 / M69.20 | UNKNOWN (ER025 at 4-digit) | UNKNOWN | UNKNOWN |
| Other B2B core (M70, M71.1, M73, M74, N78, N82) | UNKNOWN | UNKNOWN | UNKNOWN |
| Other B2B extended (M72, N77 excl. N77.34, N80, N81) | UNKNOWN | UNKNOWN | UNKNOWN |

**Cheapest resolution (all three countries in one pass).** Eurostat `sbs_sc_ovw` [V:WS1-028]:
- geo = EE, LV, LT
- size classes 10–49 and 50–249
- NACE = C, G46, H49, H51, H52, H53, M69, M70, M71, M72, M73, M74, N77, N78, N80, N81, N82
- indicator = number of enterprises
- latest year (2023 or 2024)

Then use the national tables only for 4-digit splits (M69.20, H52.22, M71.2, N77.34). This is a single short browser session. Note that Eurostat SBS excludes K (finance) and most of A, which is fine for these sectors.

### 3.3 Exporters

| Item | EE | LV | LT |
|---|---|---|---|
| Number of exporting SMEs | UNKNOWN (resolve: Statistics Estonia trade-by-enterprise-size release; a release on medium-sized enterprises contributing most to foreign trade exists, LEAD WS1-041) | UNKNOWN (resolve: Eurostat trade-by-enterprise-characteristics (TEC) tables, LV, size class × exporters count) | UNKNOWN (resolve: Eurostat TEC tables, LT; VDA exports by enterprise size) |
| Main destination markets (share of goods exports) | UNKNOWN (resolve: Statistics Estonia annual foreign-trade release, 2025) | UNKNOWN. Context: total goods exports EUR 18.68 bn in 2024 [V:WS1-031]. Partner ranking is in the same CSB release (resolve: read release WS1-031). | UNKNOWN (resolve: VDA annual exports release, 2025) |
| Exporters trading with Russia/Belarus (exclusion filter) | UNKNOWN (resolve: TEC partner tables with partner = RU, BY; customs data) | UNKNOWN | UNKNOWN |

Why it matters: exporters are the natural buyers of component C (outbound lead generation to foreign markets). The exporter count is also the denominator for any "manufacturing exporters" segment in the scorecard. Eurostat TEC dataset codes should be confirmed in the Eurostat browser, and enterprise-size × partner combinations may be confidential for small countries.

### 3.4 Associations and chambers

| Country | Body | Sector | URL | Members | Member list public? | Source |
|---|---|---|---|---|---|---|
| EE | Estonian Chamber of Commerce and Industry (Eesti Kaubandus-Tööstuskoda) | cross-sector | koda.ee/en/members | ~3,402 listed; "over 3,500" claimed | Yes (members page) | [V:WS6-001] [V:WS6-002] |
| EE | EVEA (Estonian Association of SMEs) | cross-sector SMEs | evea.ee/liikmed | represents >6,000 enterprises (direct + collective) | UNKNOWN | [V:WS6-006]; composition LEAD WS6-031 |
| EE | ELEA (Estonian Logistics and Freight Forwarding Association) | logistics / forwarding | elea.ee/en/members | 65 incl. 13 associate members (2026) | Yes | [V:WS6-007] (**prior lead ~65 confirmed**) |
| EE | Estonian Machinery Industry Association | manufacturing exporters | UNKNOWN | UNKNOWN | UNKNOWN | existence via event [V:WS6-017] |
| EE | Accountants' / auditors' professional bodies | accounting | UNKNOWN | UNKNOWN | UNKNOWN | not researched (see §4.4) |
| LV | Latvian Chamber of Commerce and Industry (LTRK) | cross-sector | chamber.lv | 6,000 members incl. associations and business clubs | UNKNOWN | [V:WS6-003]; conflicting direct-company breakdown LEAD WS6-030 |
| LV | LAFF (Latvian Association of Freight Forwarders and Logistics) | logistics / forwarding | laff.lv/en/biedri | count not stated | Yes | [V:WS6-009] |
| LV | Accountants' bodies; exporters' associations | — | UNKNOWN | UNKNOWN | UNKNOWN | not researched |
| LT | Association of Lithuanian Chambers of Commerce, Industry and Crafts | cross-sector (regional chambers) | chambers.lt | ~2,000 | UNKNOWN | [V:WS6-004] |
| LT | Vilnius Chamber of Commerce, Industry and Crafts | cross-sector | cci.lt (older site) | >550 (date unknown) | UNKNOWN | [V:WS6-005] |
| LT | LINEKA (national forwarders & logistics association) | logistics / forwarding | lineka.lt | 42 (41 companies + 1 education institution) | UNKNOWN | [V:WS6-008] |
| LT | LBAA (Lithuanian Association of Accountants and Auditors) | accounting | UNKNOWN | UNKNOWN | UNKNOWN | LEAD WS6-032 |

**Also to verify (names from analyst knowledge, not checked in this run; no counts or URLs claimed):**
- EE: Estonian Employers' Confederation (Eesti Tööandjate Keskliit); Estonian international road carriers' association (ERAA); Estonian accountants' association (Eesti Raamatupidajate Kogu); Estonian Auditors' Association (Audiitorkogu).
- LV: Employers' Confederation of Latvia (LDDK); international road carriers' association (Latvijas Auto); Latvian Association of Sworn Auditors (LZRA).
- LT: Confederation of Industrialists (LPK); Lithuanian Business Confederation (LVK); road carriers' association (Linava); Lithuanian Chamber of Auditors (Lietuvos auditorių rūmai).

### 3.5 Language of business

**(a) Russian-speaking share per country (2021 censuses)**

| | EE | LV | LT |
|---|---|---|---|
| Russian as mother tongue / main home language, % of population | UNKNOWN (resolve: Statistics Estonia 2021 census tables on mother tongue and languages spoken) | UNKNOWN (resolve: CSB Latvia 2021 census, language mostly spoken at home) | UNKNOWN (resolve: VDA 2021 census, population by mother tongue and languages known) |
| Share of businesses run in Russian | UNKNOWN (no official statistic expected; resolve via interviews/test campaigns, §7 U5) | UNKNOWN | UNKNOWN |

Analyst prior, **not evidence, do not score on it:** Russian-speaking shares are expected to be materially higher in LV and EE than in LT. That is why the census figures are decision-critical for the "Russian opens doors" part of the edge hypothesis. Russian-speaking does not mean sanctions-relevant. The Russia/Belarus-trade exclusion applies to trade links, not to the language of the owner.

**(b) Evidence on which language SMEs use for sales and internal operations.** No survey evidence was gathered (UNKNOWN). The indirect evidence below comes from other workstreams:
- **CRM interface languages** (proxy for the language of internal operations):
  - HubSpot: Latvian and Lithuanian available, Estonian not [V:WS0-003].
  - Pipedrive: added Latvian in 2022 [V:WS0-001].
  - Zoho: Estonian, Latvian and Lithuanian only partially supported [V:WS0-004].

  Interface language is typically a per-user setting (verify per vendor), so the operator can usually work in an English UI. The delivery risk in EE/LV lies in the client's own content: field and stage names, email templates, quotes and documents written in Estonian or Latvian, which the operator cannot read.
- **Competitors already sell multilingual Baltic coverage including Russian:** Fontakt [V:WS3-002], Ripe Leads [V:WS3-009], a Riga Pipedrive partner [V:WS3-013].
- **LLM quality in Baltic languages** is relevant if AI drafts ET/LV copy the operator cannot proof-read. Benchmarks (WS0) show strong but model-dependent performance [V:WS0-005] [V:WS0-006] [V:WS0-007]. They do not measure business-writing quality (UNKNOWN; resolve: native-speaker review of AI drafts in a test campaign).

**(c) Legal constraints on language in private B2B communication.** UNKNOWN in WS1. WS4 holds this item (ASSIGNMENTS WS4 "Added beyond the brief" item 6). The instruments to check, without claims about their content, are:
- EE: Language Act (Keeleseadus)
- LV: State Language Law (Valsts valodas likums), plus consumer-protection and labour-law language provisions
- LT: Law on the State Language (Valstybinės kalbos įstatymas)

The key test per country: do any obligations reach private B2B emails, proposals, contracts or CRM content, or are they limited to public information, consumer information and the public sector?

### 3.6 G1 funnel per country (total → target sectors → right size → plausibly reachable)

The brief's order is total → sectors → size. Here size is applied first because only the size cut is published for all three countries. The order does not change the endpoint.

| Step | EE | LV | LT |
|---|---|---|---|
| 1. All enterprises (scope differs, §3.1) | 158,378 (2024) [V:WS1-001] | 107,091 (2024 est., SBS scope) [E:A-WS1-02] | 328.6 thousand (2022, pre-2023) [V:WS1-033] |
| 2. Right size (proxy 10–249) | 7,579 (2024) [E:A-WS1-01] | 7,820 (2024 est.) [E:A-WS1-02] | ≈15,444 (15,116–15,773; 2022, pre-2023) [E:A-WS1-06] |
| 3. Target sectors (share s, §2) | UNKNOWN (resolve: §3.2 / §7 U1) | UNKNOWN | UNKNOWN |
| 4. Minus hard exclusions (Russia/Belarus trade, share x; H50 and H52.22 already removed by definition) | UNKNOWN (resolve: §7 U3) | UNKNOWN | UNKNOWN |
| 5. Plausibly reachable | See the database route below; the language filter l is still UNKNOWN (§7 U5) | same | same |
| **Evidence-based ceiling on the endpoint** | **≤ 7,579** [E:A-WS1-01] | **≤ 7,820** [E:A-WS1-02] | **≤ ≈15,444** [E:A-WS1-06] |

The statistical-route formula is Reachable_c = N2_c × s_c × (1 − x_c) × d_c × l_c [E:A-WS1-08]. No values were assumed for s or x, because they could not be sourced, and inventing shares would break the traceability rule.

**Database route (secondary reachability proxy, Hunter.io Discover, 2026-10-03).** Counts are company records in a vendor database. **They are a reachability proxy, not market size.** All target-sector rows use the 11–50 + 51–200 headcount buckets.

| Step | EE | LV | LT |
|---|---|---|---|
| D1. All industries, 11–200 staff, in database | 4,675 [V:WS1-046] [V:WS1-047] | 3,268 [V:WS1-061] [V:WS1-062] | 6,116 [V:WS1-076] [V:WS1-077] |
| D1 as a share of the statistical 10–249 band (coverage indicator) | 61.7% (inflated, see caveats) [E:A-WS1-10] | 41.8% [E:A-WS1-10] | 39.6% (38.8–40.5%) [E:A-WS1-10] |
| D2a. Logistics (116) excl. maritime-tagged rows | ≈119 [E:A-WS1-11] | ≈138 [E:A-WS1-11] | ≈292 (upper bound) [E:A-WS1-11] |
| D2b. Wholesale (133) | 146 [V:WS1-050] [V:WS1-051] | 152 [V:WS1-065] [V:WS1-066] | 247 [V:WS1-080] [V:WS1-081] |
| D2c. Manufacturing (25) | 584 [V:WS1-052] [V:WS1-053] | 588 [V:WS1-067] [V:WS1-068] | 1,097 [V:WS1-082] [V:WS1-083] |
| D2d. Professional Services (1810), incl. accounting and consulting; low variant removes IT services (≈1/3) | 783–1,175 [V:WS1-054] [V:WS1-055] [E:A-WS1-12] | 438–657 [V:WS1-069] [V:WS1-070] [E:A-WS1-12] | 707–1,061 [V:WS1-084] [V:WS1-085] [E:A-WS1-12] |
| D2e. Administrative & Support (1912) | 156 [V:WS1-056] [V:WS1-057] | 131 [V:WS1-071] [V:WS1-072] | 206 [V:WS1-086] [V:WS1-087] |
| **D2. Target-sector records (sum)** | **1,788–2,180** [E:A-WS1-12] | **1,447–1,666** [E:A-WS1-12] | **2,549–2,903** [E:A-WS1-12] |
| D3. Email-availability rate (pooled exact segments) | any 83.0%; personal 61.0% [E:A-WS1-13] | same [E:A-WS1-13] | same [E:A-WS1-13] |
| **D4. Database-reachable, ≥1 indexed email** | **1,485–1,810** [E:A-WS1-14] | **1,201–1,383** [E:A-WS1-14] | **2,117–2,410** [E:A-WS1-14] |
| **D4'. Database-reachable, ≥1 personal (named) email** | **1,092–1,331** [E:A-WS1-14] | **883–1,017** [E:A-WS1-14] | **1,556–1,772** [E:A-WS1-14] |
| D5. After language-workability (l) and Russia/Belarus screening (x) | UNKNOWN (§7 U3, U5) | UNKNOWN | UNKNOWN |

**Caveats that travel with the database route** (lead analyst, `db_coverage_README.md`):
1. **Headcount buckets are not statistical size classes.** Hunter's 1-10 / 11-50 / 51-200 are not 0–9 / 10–49 / 50–249. The database route covers roughly 11–200 staff (closer to the brief's 5–100 ICP at the top end than 10–249). It omits 10-person firms and the 201–249 band.
2. **Industry is a LinkedIn-style taxonomy, not NACE.**
   - Accounting and Business Consulting are nested inside Professional Services and are **not** added on top.
   - "Wholesale" contains manufacturers tagged as wholesalers.
   - Admin & Support includes travel and events (≈N79, excluded in §2), and these were not removed.
3. **Maritime and aviation inside Logistics.** Maritime Transportation rows must be excluded per the brief (done in D2a). Among the sampled 11–200 logistics rows they were:
   - EE: 18/100 [V:WS1-048] and 6/37 [V:WS1-049]
   - LV: 12/100 [V:WS1-063] and 6/47 [V:WS1-064]
   - LT: 0/100 [V:WS1-078] and 4/97 [V:WS1-079]

   In LT, 99 of the 199 records in the 11–50 bucket were not sampled, so LT is an upper bound. Airlines/Aviation (≈12% of sampled rows, indicative) is **retained** pending an operator decision [E:A-WS1-11].
4. **Email shares.** For segments above 100 records, the `pct_*_email` values are upper bounds, because results are ranked by email count and the offset is ignored. D3 therefore uses only the 22 segments where the sample is the full result set [E:A-WS1-13].
5. **CRM technology filter not supported.** Database counts cannot be split by CRM in use. The lead's indicative website-trace fallback is in the README and is not used here.

Further caveats:
- **Coverage bias.** The database over-represents firms with websites, LinkedIn or English presence, digital and service firms, and capital-city firms. It under-represents offline and traditional SMEs such as small hauliers.
- **EE ratio inflated.** The EE coverage ratio is inflated by internationally run firms registered in Estonia (e-Residency).
- **Not legal units.** Records are web domains, so one firm can appear under several domains.

**What the two routes together tell the decision.**
- **Statistical ceiling:** Estonia and Latvia each have fewer than 8,000 firms in the size band before any sector filter [E:A-WS1-01] [E:A-WS1-02]. Lithuania has about twice that [E:A-WS1-06], and it is the market where the operator speaks the state language (BRIEF §2).
- **Practical outbound pool:** for a tool-based outbound approach, the pool in the target sectors is about 1.2k–1.8k firms per country in EE and LV, and about 2.1k–2.4k in LT, with any email [E:A-WS1-14]. It is about 0.9k–1.3k in EE and LV, and about 1.6k–1.8k in LT, with a named contact. All of these are before language and sanctions screening.
- **Implication:** a lead-generation offer to G1 that relies on enrichment-tool lists draws from a pool of low thousands per country. Repeated campaigns would exhaust it, and register-based list building (business registers, association lists) is needed for any deeper coverage. In particular, the database covers roughly 40% of the statistical size band in LV and LT [E:A-WS1-10].

### 3.7 G2 — foreign B2B companies selling into the Baltics: size estimate

**Value:** UNKNOWN [E:A-WS1-09].

**Method (three routes; report the range, not a sum):**
1. **Exporter route:** count enterprises in FI, SE, NO, DK, PL, DE, UA and other EU countries that export goods to EE/LV/LT. Sources: Eurostat TEC partner tables; national customs "exporters by destination" statistics. De-duplicate firms that export to more than one Baltic state by reporting max_c (lower bound) and Σ_c (upper bound).
2. **Presence route:** count foreign-controlled enterprises in each Baltic state by controlling country. Sources: Eurostat inward FATS; CSB Latvia table UZG030 "Number of enterprises in enterprise groups by country" [V:WS1-042]; VDA "Foreign-owned enterprises in Lithuania" [V:WS1-043]. These firms are already present, so they are G2 buyers of local pipeline work rather than market-entry clients.
3. **Network route:** combine the membership of foreign chambers in each Baltic state (§4.2), de-duplicated.

Then apply the same B2B-relevance, sanctions and reachability filters as G1 (A-WS1-08).

**Caveat:** route 1 counts goods exporters only. Service exporters (SaaS, consultancies) who are natural buyers of Baltic lead generation are not captured by TEC. Route 3 partly covers them.

---

## 4. Added beyond the brief

### 4.1 Foreign-language proficiency (English, Russian)

UNKNOWN for EE, LV and LT. Resolve via:
- Eurostat Adult Education Survey 2022 language tables (self-reported number of foreign languages known; most-known foreign language; level of best-known language). Filter geo = EE, LV, LT and languages = English, Russian.
- Special Eurobarometer "Europeans and their languages" (2024 edition), country factsheets for EE, LV and LT: the share able to hold a conversation in English and in Russian.

Decision use: if a high share of SME managers in EE/LV are proficient in English, the operator's lack of Estonian/Latvian matters less. A high Russian share in EE/LV would widen the operator's reachable pool there.

### 4.2 Foreign chambers / business associations in each Baltic state (G2 sizing)

UNKNOWN: no member counts were verified. Candidates to verify (names from analyst knowledge; not checked in this run):
- German-Baltic Chamber of Commerce (AHK, covering EE/LV/LT)
- American Chambers of Commerce in each state
- Foreign Investors' Council in Latvia (FICIL)
- Investors' Forum (LT)
- Nordic Chamber of Commerce in Lithuania
- Finnish-Estonian Chamber of Commerce

Polish and Ukrainian business associations per country were not researched. Resolve: one search per body for "members"/"liikmed"/"biedri"/"nariai" on its own domain.

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
| Accounting records in Hunter database, 1–200 staff (reachability proxy; industry 47, misclassification noise noted) | 103 (1-10: 78; 11-50: 19; 51-200: 6); ≥1 email 88.3%, personal 61.2% [V:WS1-058] [V:WS1-059] [V:WS1-060] [E:A-WS1-15] | 67 (46 / 17 / 4); ≥1 email 74.6%, personal 41.8% [V:WS1-073] [V:WS1-074] [V:WS1-075] [E:A-WS1-15] | 131 (89 / 37 / 5); ≥1 email 86.3%, personal 47.3% [V:WS1-088] [V:WS1-089] [V:WS1-090] [E:A-WS1-15] |
| Certified/licensed accountants | UNKNOWN (resolve: Estonian Qualifications Authority register of certified accountants) | UNKNOWN (lead to verify: Latvia's State Revenue Service licenses outsourced accounting service providers; the public licence register would give an exact count of outsourced-accounting firms) | UNKNOWN (no licensing known; resolve: LBAA membership, LEAD WS6-032) |
| Structural expectation | Most M69.20 firms are expected to be micro (0–9) in all three countries. If so, accounting firms are better **referral partners** (many small offices, each serving many SME clients) than direct buyers of a CRM project. This is a hypothesis to test with the counts above. The database counts point the same way: most listed accounting records are in the 1-10 bucket [E:A-WS1-15]. | same | same |

**Reading the database counts.** The database lists only about a hundred accounting firms per country [E:A-WS1-15]. Building a list of accountants as referral partners would therefore rely on register extracts (EMTAK/NACE 69.20 filters in national business registers or Lursoft/Rekvizitai-type tools; WS4 covers the legality of these) and on association lists, not on enrichment tools.

### 4.5 Re-verification of prior lead: ELEA member count

**Confirmed.** ELEA lists 65 members, including 13 associate members, on a public members page (2026) [V:WS6-007]. WS6 verified this, and WS1 re-checked the row.

---

## 5. Conflicts between sources

| Topic | Value A | Value B | Which we trust and why |
|---|---|---|---|
| LT enterprises 10–249 | ≈15,444 (2022, pre-2023) from VDA total × VDA shares [E:A-WS1-06] | 13,592 (2024 est.) from EC SME Fact Sheet 2025, LEAD WS1-039, not tied to a URL; 13,265 (c.2018) from 2019 SBA fact sheet [V:WS1-036] (pre-2023) | **VDA-based estimate**, because it is an observed national count, consistent with 2021 (pre-2023: ≈14,940 [V:WS1-035]). The EC figures are model estimates; the 2025 one is unverified. The ~12% gap may reflect different population definitions. Resolve with Eurostat `sbs_sc_ovw` for 2023–2024 (§7 U1). |
| LT "operating economic entities" | 122,458 at 1 Jan 2023 (+7.9%) (LEAD; extract from osp.stat.gov.lt, page not identified) | 151,868 at start of 2025 (+6.2%) (LEAD WS1-040) | Neither used. Growth from A to B implies about +24% in two years, which is inconsistent with +6.2% p.a. The definitions likely differ (legal entities vs all entities). |
| LTRK membership | 6,000 members incl. associations and business clubs [V:WS6-003] | ~3,000 enterprises + ~3,000 via associations, or >2,600 individual members + ~60 associations (LEAD WS6-030) | Use **"≈2,600–3,000 direct company members"** as the working range for list-building, with low confidence. The 6,000 headline includes indirect members. |
| Kaubanduskoda membership | ~3,402 listed on the members page [V:WS6-001] | "over 3,500 direct members" [V:WS6-002] | **~3,400 listed** for list-building (observable); the 3,500 claim may be older or rounded. |
| Size of the 10–249 universe: statistics vs database | Statistics: EE 7,579 [E:A-WS1-01]; LV 7,820 [E:A-WS1-02]; LT ≈15,444 [E:A-WS1-06] | Hunter 11–200 records: EE 4,675; LV 3,268; LT 6,116 [E:A-WS1-10] | Not a true conflict: different units (legal enterprises vs web domains) and bands. **Use statistics for market size and the database for reachability.** The database's relative ordering (EE above LV) partly reflects database composition (Estonian-registered international firms), not the economy. |
| EE vs LV size counts | EE 10–249: 7,579 (all sectors, employees) [E:A-WS1-01] | LV 10–249: 7,820 (SBS scope, persons employed) [E:A-WS1-02] | Not directly comparable (§3.1). The LV figure likely *undercounts* relative to the EE definition, because SBS excludes agriculture/finance/public. Treat both as about 7.6–7.8 thousand with ± uncertainty, pending §7 U1. |

---

## 6. Search-language log

| Language | Example queries | Found | Not found |
|---|---|---|---|
| EN | "Statistics Estonia number of economically active enterprises 2024 by number of persons employed 10-49 50-249" (stat.ee); "CSB Latvia economically active enterprises 2024 … size group" (stat.gov.lv); "SME country fact sheet 2025 Latvia …" (ec.europa.eu); "SMEs in operation Lithuania …" (osp.stat.gov.lt); "Eurostat sbs_sc_ovw …" | EE totals and size classes (WS1-001–004); LV EC fact sheet (WS1-025–027); Eurostat `sbs_sc_ovw` metadata (WS1-028); LT *Business in Lithuania* totals and shares (WS1-033–036); LV trade and Riga GDP releases (WS1-031, WS1-032); EMTAK 2025 pointers (WS1-044, WS1-045) | CSB national size counts; LT 2024/2025 counts; EE and LT 2025 SME fact sheets |
| ET | "majanduslikult aktiivsed ettevõtted 2024 tööga hõivatud isikute arv statistikaamet"; "Eesti ettevõtted 2024 töötajate arvu järgi 10–49 50–249" | The EE 10–49 count of 6,461 [V:WS1-003] was first surfaced by the ET query; trade-by-size release title (WS1-041) | 50–249 count (found later via EN) |
| LV | "ekonomiski aktīvo uzņēmumu skaits 2024 pēc lieluma grupām"; "tirgus sektora ekonomiski aktīvo uzņēmumu skaits 2024" | Table IDs UZS020, UZS030/UZS031, UZS041, UZS011 (WS1-029, WS1-030) | Any LV size-class values (PxWeb tables are not readable via search) |
| LT | "veikiančių ūkio subjektų skaičius 2025 m. pradžioje pagal darbuotojų skaičių"; "Verslas Lietuvoje 2025 …"; "Lietuva skaičiais 2025 …" | Registrų centras legal-entity counts via duomenugalia.lt (WS1-038); conflicting operating-entity LEADs (WS1-040) | VDA 2024/2025 size-class values |
| RU | none run (budget exhausted) | — | Russian-language business-community and language-use evidence is entirely open |
| (API, not search) | Hunter.io Discover natural-language company queries, run by the lead analyst (`db_coverage.csv`) | Database-coverage counts by country × headcount × industry (WS1-046 to WS1-094) | CRM-technology split (filter not supported) |

---

## 7. UNKNOWNs and cheapest resolution

| # | Unknown | Countries | Cheapest resolution |
|---|---|---|---|
| U1 | Target-sector × size counts (C, G46, H49–H53 minus H50/H52.22, M69/M69.20, M70–M74, N77–N82) | EE, LV, LT | Eurostat `sbs_sc_ovw` [V:WS1-028], a single short browser session (filters in §3.2). 4-digit splits from EE ER025 [V:WS1-004], LV UZS030/UZS031 [V:WS1-030], LT VDA indicators database. |
| U2 | National 2024/2025 size counts for LV (replacing the EC model estimate) and LT (replacing the 2022 estimate) | LV, LT | CSB UZS031 (2024) and VDA "operating enterprises at the beginning of 2025 by personnel group". One browser session each. |
| U3 | Exporting SMEs, destination markets, and the share trading with RU/BY (exclusion filter x) | EE, LV, LT | Eurostat TEC tables (size class × exporters; partner tables incl. RU/BY); national annual trade releases (EE, LV [V:WS1-031], LT) |
| U4 | Russian-speaking share (2021 census) | EE, LV, LT | National census tables (mother tongue / home language); one search per country with allowed_domains = national statistics office |
| U5 | Language actually used by SMEs for sales and internal operations, by segment | EE, LV, LT | Interview question: "In which language do you (a) sell to Baltic customers, (b) run your CRM and internal documents, (c) prefer to buy services?" Plus an A/B test: the same cold sequence in EN vs RU vs local language to a few dozen target firms per arm (size the arms with WS6 reply-rate benchmarks). |
| U6 | English and Russian proficiency | EE, LV, LT | Eurostat AES 2022 language tables; Special Eurobarometer "Europeans and their languages" (2024) country factsheets |
| U7 | Legal constraints on language in private B2B communication | EE, LV, LT | WS4 item 6; check whether state-language obligations extend beyond public, consumer and employment contexts |
| U8 | G2 size | EE, LV, LT | §3.7 routes 1–3; start with CSB UZG030 [V:WS1-042] and VDA foreign-owned enterprises [V:WS1-043] |
| U9 | Accounting firms M69.20 by size; certified/licensed accountants | EE, LV, LT | §4.4 tables; LV State Revenue Service licence register for outsourced accountants (lead to verify) |
| U10 | Database reachability: **partly resolved** with Hunter counts (§3.6 database route; [E:A-WS1-14]). Still open: (a) email rates for large segments, where only upper bounds exist; (b) Apollo coverage (not in the supplied file); (c) the share of statistical target-sector firms *absent* from databases, which needs U1 sector counts as the denominator | EE, LV, LT | (a)/(b) A small random sample (a few dozen firms) per country from a register extract (not ranked by email count), checked in Hunter/Apollo. This gives an unbiased hit rate. (c) U1 |
| U11 | Foreign chambers' member counts | EE, LV, LT | One search per body (§4.2) |
| U12 | Russian-/Ukrainian-owned SME counts; regional counts (Ida-Virumaa, Riga, Vilnius) | EE, LV, LT | Register statistics (§4.3); EE county tables; CSB UZS030/031; VDA county tables |
| U13 | LAFF member count; LTRK direct company count; LT chamber direct counts; accountants' and exporters' associations | LV, LT, EE | Count rows on the public lists (LAFF [V:WS6-009]); ask the associations directly |

---

## 8. Synthesis inputs (per country)

All scores are 1–5, where 5 = most favourable to the operator. Scores are suggested only where WS1 evidence supports them; otherwise they are UNKNOWN.

| Item | EE | LV | LT |
|---|---|---|---|
| Enterprises 10–249, total | 7,579 (2024) [E:A-WS1-01] | 7,820 (2024 est.) [E:A-WS1-02] | ≈15,444 (2022, pre-2023) [E:A-WS1-06] |
| Target-sector counts 10–49 / 50–249 | UNKNOWN (U1) | UNKNOWN (U1) | UNKNOWN (U1) |
| G1 funnel endpoint (statistical route) | UNKNOWN; ceiling ≤7,579 [E:A-WS1-01] | UNKNOWN; ceiling ≤7,820 [E:A-WS1-02] | UNKNOWN; ceiling ≤≈15,444 [E:A-WS1-06] |
| G1 database-reachable target-sector firms, 11–200 staff, ≥1 email (before language and sanctions screens) | 1,485–1,810 [E:A-WS1-14] | 1,201–1,383 [E:A-WS1-14] | 2,117–2,410 [E:A-WS1-14] |
| Same, with a named (personal) email | 1,092–1,331 [E:A-WS1-14] | 883–1,017 [E:A-WS1-14] | 1,556–1,772 [E:A-WS1-14] |
| Database coverage of the statistical 10–249 band | 61.7% (inflated) [E:A-WS1-10] | 41.8% [E:A-WS1-10] | 39.6% [E:A-WS1-10] |
| Accounting firms listed in database (1–200 staff) | 103 [E:A-WS1-15] | 67 [E:A-WS1-15] | 131 [E:A-WS1-15] |
| Suggested market-size score (G1 ceiling only) | 2 (ceiling under 8k; basis [E:A-WS1-01]) | 2 (ceiling under 8k; basis [E:A-WS1-02]) | 3 (about twice EE/LV; basis [E:A-WS1-06]) |
| G2 estimate | UNKNOWN (U8) | UNKNOWN (U8) | UNKNOWN (U8) |
| Russian-speaking share | UNKNOWN (U4) | UNKNOWN (U4) | UNKNOWN (U4) |
| English / Russian proficiency | UNKNOWN (U6) | UNKNOWN (U6) | UNKNOWN (U6) |
| Language-law constraint summary | UNKNOWN; WS4 item 6 (U7) | UNKNOWN; WS4 item 6 (U7) | UNKNOWN; WS4 item 6 (U7) |
| Operator speaks state language? | No (BRIEF §2) | No (BRIEF §2) | Yes (BRIEF §2) |
| Association member lists public? | Yes: Kaubanduskoda ~3,402 [V:WS6-001]; ELEA 65 [V:WS6-007] | Partly: LAFF yes [V:WS6-009]; LTRK UNKNOWN | UNKNOWN: LINEKA count only (42) [V:WS6-008]; chambers ~2,000 [V:WS6-004], list status UNKNOWN |
| Multilingual (incl. RU) Baltic coverage already offered by competitors? | Yes [V:WS3-002] [V:WS3-009] | Yes [V:WS3-002] [V:WS3-009] [V:WS3-013] | Yes [V:WS3-002] [V:WS3-009] |

---

## Appendix A — Follow-up query plan (to close UNKNOWNs if the search budget is raised)

These are listed in priority order; together they need a few dozen searches.
1. `allowed_domains=["ec.europa.eu"]`: "sbs_sc_ovw Estonia Latvia Lithuania number of enterprises 10-49 manufacturing wholesale G46 2023". Then repeat per sector.
2. `["stat.gov.lv"]`: "UZS031 2024 10-49 50-249 nodarbināto" and the CSB annual press release on economically active enterprises (LV).
3. `["osp.stat.gov.lt"]`: "veikiančių įmonių skaičius 2025 m. pradžioje darbuotojų skaičiaus grupės 10–19 20–49 50–99 100–249".
4. Census language: `["stat.ee","rahvaloendus.ee"]` "emakeel vene 2021 rahvaloendus"; `["stat.gov.lv"]` "2021 tautas skaitīšana mājās runātā valoda krievu"; `["osp.stat.gov.lt"]` "2021 surašymas gimtoji kalba rusų".
5. `["europa.eu"]`: "Special Eurobarometer Europeans and their languages 2024 Estonia Latvia Lithuania English Russian".
6. `["ec.europa.eu"]`: "Adult Education Survey 2022 foreign language knowledge Estonia Latvia Lithuania Russian English".
7. Eurostat TEC: "trade by enterprise characteristics number of exporting enterprises Estonia size class 2023"; partner tables for RU/BY.
8. Foreign chambers (§4.2) and accountants' bodies (§4.4): one query each on their own domains.
9. RU-language: "русскоязычный бизнес Латвия Эстония язык общения с клиентами исследование" (any survey evidence on business language use).
