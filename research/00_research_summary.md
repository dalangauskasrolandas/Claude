# 00 — Research summary: "Baltic Revenue Engine" (CRM setup, AI/workflow automation, outbound lead generation; EE / LV / LT)

**Research conclusions, not a plan.** Written last, after verification (2026-10-03). Labels: `[V:id]` = VERIFIED (row in `sources.csv`); `[E:id]` = ESTIMATE (entry in `assumptions.md`); `UNKNOWN` = not established. Scores are analyst JUDGMENT built on labelled evidence (method [E:A-WS0-01]).

**Scope changes made by the user during the run** (`_work/SCOPE_CHANGE.md`): (1) only companies with **up to `50` staff** (size classes `0–9` and `10–49`); (2) gap-fill pass stopped early, results kept; (3) verification and red team combined into one agent with at most `30` searches.

**Method limits that matter for trust.** Direct page fetching was blocked in this environment, so all web evidence comes from search-engine extracts (quotes marked `~` are near-quotes). A shared cap of 200 searches stopped the six workstream agents part-way, so many items are UNKNOWN ("not researched", not "not found"). **No Russian-language searches were run** (brief rule 5 only partly met). Of 30 key claims, 22 were re-checked by search: 14 confirmed, 7 corrected, 3 could not be verified, 6 checked against the cited source only (`verification_log.md`).

---

## 1. Executive summary

1. The evidence does **not** support the concept as specified (all-Baltic, trilingual, three services): no country × component × group combination scores above 3.0 of 5 on the scorecard [E:A-WS0-01].
2. The claimed edge is already sold: Fontakt, Ripe Leads and eXpanby each claim EN + RU + all three local languages across EE/LV/LT [V:WS3-002][V:WS3-009][V:WS3-013]; the operator's EN/RU/LT is a subset.
3. The ≤50-staff market is small: firms with 10–49 staff number EE 6,284 (2025) [V:WS1-095], LV 6,457 (2024 est.) [V:WS1-025], LT 11.3–12.8 thousand (2022) [E:A-WS9-03]; database-reachable 11–50-staff target firms with a named e-mail: EE 703–1,019, LV 542–747, LT 957–1,300 [E:A-WS9-02].
4. Demand evidence is strongest for AI/automation: AI use among firms with 10+ staff rose to 34% in EE (2026) [V:WS2-050] and from 8.8% to 21.3% in LT (2024→2025) [V:WS2-057]; LV lagged at 8.83% (2024) [V:WS2-062]. Estonia's AI grant (€20,000 per firm, 20% own money) was used up the day it opened, 24.08.2026 [V:WS2-001][V:WS2-003].
5. Most measured demand is **subsidised and now closed**: Latvia's 2,908 applications, roughly half for sales digitalisation incl. CRM [V:WS2-069][V:WS2-070], came under programmes now closed [V:VL-008]; Lithuania has no open digitalisation call [V:WS2-036][V:WS2-043]. Own-money willingness to pay among ≤50-staff firms is UNKNOWN.
6. Grants cannot pay the operator at first: Estonia's grant-paid "digital advisor" needs at least 3 similar projects in the previous 4 years [V:WS2-009].
7. Published price anchors: outbound retainer €3,750 first month then €2,850/month [V:WS3-008]; automation €300–3,000+ in LT [V:WS3-024] and from €100 in EE [V:RT-005]; Latvia's CRM bundles at €2,990–7,440 are historical, licence-inclusive list prices [V:VL-014]. All are supply-side; no transaction prices were found.
8. Economics: an Estonian FIE keeps 58.65% of profit [E:A-WS5-01][V:VL-018]; net €/h at mid prices is CRM €34.9, automation €25.4, lead gen €37.9 [E:A-WS5-14][E:A-WS5-20][E:A-WS5-26]; with 40 selling hours per won CRM client it falls to €20.9 [E:A-WS8-01].
9. Capacity: at 15 h/week the ceiling is about 14.7 CRM projects a year or 2 concurrent lead-gen clients [E:A-WS5-38]; lead gen needs about 30% of its hours inside business hours [E:A-WS5-33].
10. Channels: all 19 verified events (Oct 2026–Mar 2027) fall on weekdays [E:A-WS6-01]; the evidenced async routes are public member directories (e.g. Kaubanduskoda ~3,402 members [V:WS6-001]); no Baltic cold-outreach reply benchmark was found (UNKNOWN).
11. Legal: B2B e-mail to generic company addresses is allowed on an opt-out basis in all three states (EE [V:WS4-001], LV [V:WS4-016], LT since 22 Apr 2026 [V:VL-001]); named-employee addresses are unresolved; sole traders count as natural persons and need prior consent (LV [V:WS4-011], LT [V:WS4-028]).
12. Language: Lithuania is the only market with full language fit (operator native; only 31.1% know English [V:WS1-105]); in EE/LV Russian reaches many people (EE mother tongue 29% [V:WS1-099]; LV home language 34.6% [V:WS1-101]), but Estonian/Latvian is effectively required for lead generation and most events.
13. Best-evidenced combinations: automation for Lithuanian SMEs; automation for Estonian SMEs (accounting firms slightly ahead); CRM setup in Latvia. Weakest: lead generation in EE and LV; bundles for foreign firms (G2) in EE and LV (§ 4).
14. The red team found four high-severity failure reasons: no first-client channel that fits evenings and the budget; selling effort vs. capacity; unmeasured unsubsidised demand; the edge is already sold (`red_team.md`).
15. The cheapest decisive evidence still missing: owner interviews on own-money purchases, three incumbent quote requests, a 100-contact language-split pilot, and written questions to the three regulators (test designs [E:A-WS8-07]; kill criteria K1–K7 in `red_team.md`; § 5).

---

## 2. The trilingual all-Baltic advantage — verdict per country

| Country | Where EN / RU / LT is enough | Where Estonian or Latvian is effectively required | Verdict |
|---|---|---|---|
| **EE** | Russian: mother tongue of 29% of the population [V:WS1-099]; 39% speak it as a foreign language and 48% speak English [V:WS1-100]. EN/RU is workable for Russian-speaking or internationally run firms; the share of firms run in Russian is UNKNOWN. | Outbound copy to Estonian-speaking owners (competitors write native Estonian [V:WS3-002][V:WS3-009]); 11 of 13 verified Estonian events are listed in Estonian, plus one bilingual (corrected count, `verification_log.md` VL-030) [V:WS6-012][V:WS6-013][V:WS6-014]; client content in Estonian (CRM fields, quotes, templates). HubSpot has no Estonian interface [V:WS0-003]. | **No real advantage.** RU/EN covers a sub-segment only, and incumbents also offer Russian. |
| **LV** | Russian is understood by 91.3% of 25–64-year-olds and English by 64.0% (2022) [V:WS1-104]; 34.6% of adults use Russian at home [V:WS1-101]. The language law does not regulate private B2B e-mail or proposals [V:WS1-132]. | Outbound at scale and grant-catalogue documentation; competitors offer Latvian [V:WS3-013][V:WS3-009]. Social acceptability of Russian-language selling is UNKNOWN (not researched). | **No real advantage** beyond a Russian-speaking sub-segment; Latvian is effectively required for lead generation. |
| **LT** | Lithuanian: operator native; 99.4% of Lithuanians have it as mother tongue [V:WS1-106]; owner and marketing events are listed in Lithuanian [V:WS6-025][V:WS6-027]. English reaches only 31.1% and Russian 60.6% (2021) [V:WS1-105]. | Not applicable. | **Real but not unique.** Native Lithuanian beats English-only providers, but local incumbents (Ripe Leads, Vilnius) are equally native [V:WS3-007]. |
| **G2 (foreign firms)** | English suffices with the client; Lithuanian adds value for Lithuanian targets. | Estonian/Latvian targets need native copy; incumbents already sell Baltic market entry to foreign firms [V:WS3-053][V:WS3-049]. | **No real advantage**, except for Lithuania-only campaigns. |

Supporting point: frontier AI models score well on Estonian and Latvian benchmarks [V:WS0-005][V:WS0-006], but no evidence covers business-writing quality, and the operator cannot proof-read Estonian or Latvian output (UNKNOWN; resolve: native-speaker review of AI drafts, K6).

---

## 3. Evidence scorecard

**How to read it.** Six columns, each scored 1–5 where **5 = most favourable to the operator**: Demand evidence; Willingness-to-pay (WTP) evidence; Competition (5 = least competition); Legal (5 = lowest risk); Async/evening fit (5 = fully async); Language advantage real? Rows: component (A = CRM setup, B = AI/workflow automation, C = outbound lead generation, and the bundles A+B and A+B+C) × group (G1 by sector; G2 = foreign firms selling into the Baltics) × country. "Mean" is the unweighted mean. Every score cites a **basis code** defined in table 3.1; generator `research/_work/tools/scorecard.py`, data `research/_work/data/scorecard.csv` [E:A-WS0-01].

**Two cautions.** (1) A score of 1 marked "gap" means not researched or no evidence, not a negative finding. (2) The evidence does not discriminate between G1 sectors: logistics, wholesale, manufacturing and professional-services rows are identical except where sector evidence exists (only Estonian accounting firms × B, via e-invoicing). Scope: firms with ≤50 staff; for component C the legal score applies to company targets — sole traders need consent [V:WS4-011][V:WS4-028].

Changes applied from verification: LV × A demand 4 → 3 and WTP 4 → 3 (programmes closed; list prices historical) [V:VL-008][V:VL-014]; EE × B competition 3 → 2 (four Estonian automation agencies found) [V:RT-005][V:RT-006]; LT × C legal 4 → 3 (named-employee scope unverified, LEAD VL-002); C async set to 3, not 4 [E:A-WS0-02].

### 3.1 Score basis (codes used in the scorecard)

| Code | Score | Evidence / rule |
|---|---|---|
| D-EE-A | 2 [E:A-WS0-01] | [V:WS2-007][V:WS2-010] |
| D-EE-B | 4 [E:A-WS0-01] | [V:WS2-001][V:WS2-003][V:WS2-049][V:WS2-050] |
| D-EE-C | 1 [E:A-WS0-01] | gap; [V:WS2-016] |
| D-LV-A | 3 [E:A-WS0-01] | [V:WS2-069][V:WS2-070][E:A-WS2-08][V:WS2-020][V:VL-008] (subsidised up to 100%, programmes closed) |
| D-LV-B | 2 [E:A-WS0-01] | [V:WS2-060][V:WS2-062][V:WS2-054] |
| D-LV-C | 1 [E:A-WS0-01] | gap |
| D-LT-A | 2 [E:A-WS0-01] | [V:WS2-059][V:WS2-042][V:WS2-043] |
| D-LT-B | 3 [E:A-WS0-01] | [V:WS2-057][V:WS2-054][V:WS2-067] |
| D-LT-C | 1 [E:A-WS0-01] | gap |
| W-EE-A | 3 [E:A-WS0-01] | [V:WS3-005][E:A-WS2-05][V:WS2-007][V:WS2-009] |
| W-EE-B | 2 [E:A-WS0-01] | [V:WS3-005] |
| W-EE-C | 2 [E:A-WS0-01] | [V:WS3-004][V:WS3-003] |
| W-LV-A | 3 [E:A-WS0-01] | [V:WS3-017][V:WS3-019][V:VL-008][V:VL-014] (historical, licence-inclusive list prices) |
| W-LV-B | 2 [E:A-WS0-01] | [V:WS2-022][V:WS3-046] |
| W-LV-C | 2 [E:A-WS0-01] | [V:WS3-009] |
| W-LT-A | 2 [E:A-WS0-01] | [V:WS3-025] |
| W-LT-B | 3 [E:A-WS0-01] | [V:WS3-024][E:A-WS5-19] |
| W-LT-C | 3 [E:A-WS0-01] | [V:WS3-008] |
| C-EE-A | 2 [E:A-WS0-01] | [V:WS3-026][V:WS3-012][V:WS3-016][V:WS3-021][V:WS3-005][V:WS3-013] |
| C-EE-B | 2 [E:A-WS0-01] | [V:WS3-021][V:WS3-005][V:RT-005][V:RT-006][V:RT-007][V:RT-008] |
| C-EE-C | 2 [E:A-WS0-01] | [V:WS3-001][V:WS3-009] |
| C-LV-A | 2 [E:A-WS0-01] | [V:WS3-013][V:WS3-017][V:WS3-022][E:A-WS3-03] |
| C-LV-B(p) | 3 [E:A-WS0-01] | [V:WS3-013][E:A-WS3-03] |
| C-LV-C | 2 [E:A-WS0-01] | [V:WS3-002][V:WS3-009] |
| C-LT-A | 2 [E:A-WS0-01] | [V:WS3-014][V:WS3-023][V:WS3-025][V:WS3-013] |
| C-LT-B | 2 [E:A-WS0-01] | [V:WS3-024][V:WS3-034][V:WS3-035] |
| C-LT-C | 2 [E:A-WS0-01] | [V:WS3-007][V:WS3-008][V:WS3-002] |
| L-A | 4 [E:A-WS0-01] | [E:A-WS4-01] |
| L-B | 3 [E:A-WS0-01] | [E:A-WS4-01] |
| L-EE-C | 3 [E:A-WS0-01] | [V:WS4-001][V:WS4-004][V:WS4-005] |
| L-LV-C | 3 [E:A-WS0-01] | [V:WS4-016][V:WS4-019][V:WS4-011] |
| L-LT-C | 3 [E:A-WS0-01] | [V:WS4-031][V:VL-001]; named-employee scope LEAD VL-002 (4 if regulator confirms) |
| A-A | 3 [E:A-WS0-01] | [E:A-WS6-05][E:A-WS5-33] (25% of hours need business hours) |
| A-B | 4 [E:A-WS0-01] | [E:A-WS6-05][E:A-WS5-33] (10%) |
| A-C | 3 [E:A-WS0-01] | [E:A-WS5-33] (30%: same-day replies, booking, client calls); WS6 rated 4 — lower value kept [E:A-WS0-02] |
| G-EE | 2 [E:A-WS0-01] | [V:WS1-099][V:WS1-100][V:WS6-012][V:WS3-002][V:WS3-013] |
| G-LV | 2 [E:A-WS0-01] | [V:WS1-101][V:WS1-104][V:WS3-009][V:WS3-013] |
| G-LT | 3 [E:A-WS0-01] | [V:WS1-105][V:WS1-106][V:WS6-025][V:WS6-027][V:WS3-007] |
| Gm-C | −1 [E:A-WS0-01] | -1 for C in EE/LV: outbound copy in ET/LV the operator cannot write or proof-read; competitors are native [V:WS3-002][V:WS3-009]; LLM quality evidence is benchmark-only [V:WS0-005][V:WS0-006] |
| Dm-acct-EE | +1 [E:A-WS0-01] | B for accounting firms in EE: buyers may demand e-invoices since 1 Jul 2025 [V:WS2-073]; LV mandate only from 1 Jan 2028 [V:WS2-075], so no LV modifier |
| D-G2-C | 2 [E:A-WS0-01] | agencies already sell Baltic market-entry outbound to foreign firms [V:WS3-053][V:WS3-049] |
| D-G2-AB | 1 [E:A-WS0-01] | gap: no evidence of foreign firms buying Baltic CRM/automation set-up |
| W-G2-C | 3 [E:A-WS0-01] | [V:WS3-053][V:WS3-008] |
| W-G2-AB | 1 [E:A-WS0-01] | gap |
| C-G2 | 2 [E:A-WS0-01] | [V:WS3-053][V:WS3-049][V:WS3-031] |
| Cb-AB | min(A,B) [E:A-WS0-01] | CRM partners already sell automation [V:WS3-013]; low-end automation vendors integrate CRMs [V:WS3-024] |
| Cb-ABC(p) | 3 [E:A-WS0-01] | no single A+B+C provider found in a limited search (provisional) [V:WS3-005][V:WS3-013][V:WS3-024] |
| min(…) | min [E:A-WS0-01] | bundles: weakest component for demand, WTP, legal, async, language (no evidence of joint demand or joint WTP) [E:A-WS0-01] |

### 3.2 Full scorecard (scope: up to `50` staff; columns scored `1–5`, `5` = most favourable)

#### EE

| Group | Comp. | Demand | WTP | Competition | Legal | Async | Language | Mean | Basis codes |
|---|---|---|---|---|---|---|---|---|---|
| G1-Logistics | A | 2 | 3 | 2 | 4 | 3 | 2 | 2.67 [E:A-WS0-01] | D:D-EE-A; W:W-EE-A; C:C-EE-A; L:L-A; A:A-A; G:G-EE |
| G1-Logistics | B | 4 | 2 | 2 | 3 | 4 | 2 | 2.83 [E:A-WS0-01] | D:D-EE-B; W:W-EE-B; C:C-EE-B; L:L-B; A:A-B; G:G-EE |
| G1-Logistics | C | 1 | 2 | 2 | 3 | 3 | 1 | 2 [E:A-WS0-01] | D:D-EE-C; W:W-EE-C; C:C-EE-C; L:L-EE-C; A:A-C; G:G-EE+Gm-C |
| G1-Logistics | A+B | 2 | 2 | 2 | 3 | 3 | 2 | 2.33 [E:A-WS0-01] | D:min(D-EE-A); W:min(W-EE-B); C:Cb-AB [V:WS3-013][V:WS3-024]; L:min(L-B); A:min(A-A); G:min(G-EE) |
| G1-Logistics | A+B+C | 1 | 2 | 3 | 3 | 3 | 1 | 2.17 [E:A-WS0-01] | D:min(D-EE-C); W:min(W-EE-B); C:Cb-ABC(p) (no A+B+C provider found; weak search) [V:WS3-005][V:WS3-013][V:WS3-024]; L:min(L-B); A:min(A-A); G:min(G-EE+Gm-C) |
| G1-Wholesale | A | 2 | 3 | 2 | 4 | 3 | 2 | 2.67 [E:A-WS0-01] | D:D-EE-A; W:W-EE-A; C:C-EE-A; L:L-A; A:A-A; G:G-EE |
| G1-Wholesale | B | 4 | 2 | 2 | 3 | 4 | 2 | 2.83 [E:A-WS0-01] | D:D-EE-B; W:W-EE-B; C:C-EE-B; L:L-B; A:A-B; G:G-EE |
| G1-Wholesale | C | 1 | 2 | 2 | 3 | 3 | 1 | 2 [E:A-WS0-01] | D:D-EE-C; W:W-EE-C; C:C-EE-C; L:L-EE-C; A:A-C; G:G-EE+Gm-C |
| G1-Wholesale | A+B | 2 | 2 | 2 | 3 | 3 | 2 | 2.33 [E:A-WS0-01] | D:min(D-EE-A); W:min(W-EE-B); C:Cb-AB [V:WS3-013][V:WS3-024]; L:min(L-B); A:min(A-A); G:min(G-EE) |
| G1-Wholesale | A+B+C | 1 | 2 | 3 | 3 | 3 | 1 | 2.17 [E:A-WS0-01] | D:min(D-EE-C); W:min(W-EE-B); C:Cb-ABC(p) (no A+B+C provider found; weak search) [V:WS3-005][V:WS3-013][V:WS3-024]; L:min(L-B); A:min(A-A); G:min(G-EE+Gm-C) |
| G1-Manufacturing | A | 2 | 3 | 2 | 4 | 3 | 2 | 2.67 [E:A-WS0-01] | D:D-EE-A; W:W-EE-A; C:C-EE-A; L:L-A; A:A-A; G:G-EE |
| G1-Manufacturing | B | 4 | 2 | 2 | 3 | 4 | 2 | 2.83 [E:A-WS0-01] | D:D-EE-B; W:W-EE-B; C:C-EE-B; L:L-B; A:A-B; G:G-EE |
| G1-Manufacturing | C | 1 | 2 | 2 | 3 | 3 | 1 | 2 [E:A-WS0-01] | D:D-EE-C; W:W-EE-C; C:C-EE-C; L:L-EE-C; A:A-C; G:G-EE+Gm-C |
| G1-Manufacturing | A+B | 2 | 2 | 2 | 3 | 3 | 2 | 2.33 [E:A-WS0-01] | D:min(D-EE-A); W:min(W-EE-B); C:Cb-AB [V:WS3-013][V:WS3-024]; L:min(L-B); A:min(A-A); G:min(G-EE) |
| G1-Manufacturing | A+B+C | 1 | 2 | 3 | 3 | 3 | 1 | 2.17 [E:A-WS0-01] | D:min(D-EE-C); W:min(W-EE-B); C:Cb-ABC(p) (no A+B+C provider found; weak search) [V:WS3-005][V:WS3-013][V:WS3-024]; L:min(L-B); A:min(A-A); G:min(G-EE+Gm-C) |
| G1-ProfServices | A | 2 | 3 | 2 | 4 | 3 | 2 | 2.67 [E:A-WS0-01] | D:D-EE-A; W:W-EE-A; C:C-EE-A; L:L-A; A:A-A; G:G-EE |
| G1-ProfServices | B | 4 | 2 | 2 | 3 | 4 | 2 | 2.83 [E:A-WS0-01] | D:D-EE-B; W:W-EE-B; C:C-EE-B; L:L-B; A:A-B; G:G-EE |
| G1-ProfServices | C | 1 | 2 | 2 | 3 | 3 | 1 | 2 [E:A-WS0-01] | D:D-EE-C; W:W-EE-C; C:C-EE-C; L:L-EE-C; A:A-C; G:G-EE+Gm-C |
| G1-ProfServices | A+B | 2 | 2 | 2 | 3 | 3 | 2 | 2.33 [E:A-WS0-01] | D:min(D-EE-A); W:min(W-EE-B); C:Cb-AB [V:WS3-013][V:WS3-024]; L:min(L-B); A:min(A-A); G:min(G-EE) |
| G1-ProfServices | A+B+C | 1 | 2 | 3 | 3 | 3 | 1 | 2.17 [E:A-WS0-01] | D:min(D-EE-C); W:min(W-EE-B); C:Cb-ABC(p) (no A+B+C provider found; weak search) [V:WS3-005][V:WS3-013][V:WS3-024]; L:min(L-B); A:min(A-A); G:min(G-EE+Gm-C) |
| G1-Accounting | A | 2 | 3 | 2 | 4 | 3 | 2 | 2.67 [E:A-WS0-01] | D:D-EE-A; W:W-EE-A; C:C-EE-A; L:L-A; A:A-A; G:G-EE |
| G1-Accounting | B | 5 | 2 | 2 | 3 | 4 | 2 | 3 [E:A-WS0-01] | D:D-EE-B+Dm-acct-EE; W:W-EE-B; C:C-EE-B; L:L-B; A:A-B; G:G-EE |
| G1-Accounting | C | 1 | 2 | 2 | 3 | 3 | 1 | 2 [E:A-WS0-01] | D:D-EE-C; W:W-EE-C; C:C-EE-C; L:L-EE-C; A:A-C; G:G-EE+Gm-C |
| G1-Accounting | A+B | 2 | 2 | 2 | 3 | 3 | 2 | 2.33 [E:A-WS0-01] | D:min(D-EE-A); W:min(W-EE-B); C:Cb-AB [V:WS3-013][V:WS3-024]; L:min(L-B); A:min(A-A); G:min(G-EE) |
| G1-Accounting | A+B+C | 1 | 2 | 3 | 3 | 3 | 1 | 2.17 [E:A-WS0-01] | D:min(D-EE-C); W:min(W-EE-B); C:Cb-ABC(p) (no A+B+C provider found; weak search) [V:WS3-005][V:WS3-013][V:WS3-024]; L:min(L-B); A:min(A-A); G:min(G-EE+Gm-C) |
| G2-Foreign | A | 1 | 1 | 2 | 4 | 3 | 2 | 2.17 [E:A-WS0-01] | D:D-G2-AB; W:W-G2-AB; C:C-G2; L:L-A; A:A-A; G:G-EE |
| G2-Foreign | B | 1 | 1 | 2 | 3 | 4 | 2 | 2.17 [E:A-WS0-01] | D:D-G2-AB; W:W-G2-AB; C:C-G2; L:L-B; A:A-B; G:G-EE |
| G2-Foreign | C | 2 | 3 | 2 | 3 | 3 | 1 | 2.33 [E:A-WS0-01] | D:D-G2-C; W:W-G2-C; C:C-G2; L:L-EE-C; A:A-C; G:G-EE+Gm-C |
| G2-Foreign | A+B | 1 | 1 | 2 | 3 | 3 | 2 | 2 [E:A-WS0-01] | D:min(D-G2-AB); W:min(W-G2-AB); C:Cb-AB [V:WS3-013][V:WS3-024]; L:min(L-B); A:min(A-A); G:min(G-EE) |
| G2-Foreign | A+B+C | 1 | 1 | 3 | 3 | 3 | 1 | 2 [E:A-WS0-01] | D:min(D-G2-AB); W:min(W-G2-AB); C:Cb-ABC(p) (no A+B+C provider found; weak search) [V:WS3-005][V:WS3-013][V:WS3-024]; L:min(L-B); A:min(A-A); G:min(G-EE+Gm-C) |

#### LV

| Group | Comp. | Demand | WTP | Competition | Legal | Async | Language | Mean | Basis codes |
|---|---|---|---|---|---|---|---|---|---|
| G1-Logistics | A | 3 | 3 | 2 | 4 | 3 | 2 | 2.83 [E:A-WS0-01] | D:D-LV-A; W:W-LV-A; C:C-LV-A; L:L-A; A:A-A; G:G-LV |
| G1-Logistics | B | 2 | 2 | 3 | 3 | 4 | 2 | 2.67 [E:A-WS0-01] | D:D-LV-B; W:W-LV-B; C:C-LV-B(p); L:L-B; A:A-B; G:G-LV |
| G1-Logistics | C | 1 | 2 | 2 | 3 | 3 | 1 | 2 [E:A-WS0-01] | D:D-LV-C; W:W-LV-C; C:C-LV-C; L:L-LV-C; A:A-C; G:G-LV+Gm-C |
| G1-Logistics | A+B | 2 | 2 | 2 | 3 | 3 | 2 | 2.33 [E:A-WS0-01] | D:min(D-LV-B); W:min(W-LV-B); C:Cb-AB [V:WS3-013][V:WS3-024]; L:min(L-B); A:min(A-A); G:min(G-LV) |
| G1-Logistics | A+B+C | 1 | 2 | 3 | 3 | 3 | 1 | 2.17 [E:A-WS0-01] | D:min(D-LV-C); W:min(W-LV-B); C:Cb-ABC(p) (no A+B+C provider found; weak search) [V:WS3-005][V:WS3-013][V:WS3-024]; L:min(L-B); A:min(A-A); G:min(G-LV+Gm-C) |
| G1-Wholesale | A | 3 | 3 | 2 | 4 | 3 | 2 | 2.83 [E:A-WS0-01] | D:D-LV-A; W:W-LV-A; C:C-LV-A; L:L-A; A:A-A; G:G-LV |
| G1-Wholesale | B | 2 | 2 | 3 | 3 | 4 | 2 | 2.67 [E:A-WS0-01] | D:D-LV-B; W:W-LV-B; C:C-LV-B(p); L:L-B; A:A-B; G:G-LV |
| G1-Wholesale | C | 1 | 2 | 2 | 3 | 3 | 1 | 2 [E:A-WS0-01] | D:D-LV-C; W:W-LV-C; C:C-LV-C; L:L-LV-C; A:A-C; G:G-LV+Gm-C |
| G1-Wholesale | A+B | 2 | 2 | 2 | 3 | 3 | 2 | 2.33 [E:A-WS0-01] | D:min(D-LV-B); W:min(W-LV-B); C:Cb-AB [V:WS3-013][V:WS3-024]; L:min(L-B); A:min(A-A); G:min(G-LV) |
| G1-Wholesale | A+B+C | 1 | 2 | 3 | 3 | 3 | 1 | 2.17 [E:A-WS0-01] | D:min(D-LV-C); W:min(W-LV-B); C:Cb-ABC(p) (no A+B+C provider found; weak search) [V:WS3-005][V:WS3-013][V:WS3-024]; L:min(L-B); A:min(A-A); G:min(G-LV+Gm-C) |
| G1-Manufacturing | A | 3 | 3 | 2 | 4 | 3 | 2 | 2.83 [E:A-WS0-01] | D:D-LV-A; W:W-LV-A; C:C-LV-A; L:L-A; A:A-A; G:G-LV |
| G1-Manufacturing | B | 2 | 2 | 3 | 3 | 4 | 2 | 2.67 [E:A-WS0-01] | D:D-LV-B; W:W-LV-B; C:C-LV-B(p); L:L-B; A:A-B; G:G-LV |
| G1-Manufacturing | C | 1 | 2 | 2 | 3 | 3 | 1 | 2 [E:A-WS0-01] | D:D-LV-C; W:W-LV-C; C:C-LV-C; L:L-LV-C; A:A-C; G:G-LV+Gm-C |
| G1-Manufacturing | A+B | 2 | 2 | 2 | 3 | 3 | 2 | 2.33 [E:A-WS0-01] | D:min(D-LV-B); W:min(W-LV-B); C:Cb-AB [V:WS3-013][V:WS3-024]; L:min(L-B); A:min(A-A); G:min(G-LV) |
| G1-Manufacturing | A+B+C | 1 | 2 | 3 | 3 | 3 | 1 | 2.17 [E:A-WS0-01] | D:min(D-LV-C); W:min(W-LV-B); C:Cb-ABC(p) (no A+B+C provider found; weak search) [V:WS3-005][V:WS3-013][V:WS3-024]; L:min(L-B); A:min(A-A); G:min(G-LV+Gm-C) |
| G1-ProfServices | A | 3 | 3 | 2 | 4 | 3 | 2 | 2.83 [E:A-WS0-01] | D:D-LV-A; W:W-LV-A; C:C-LV-A; L:L-A; A:A-A; G:G-LV |
| G1-ProfServices | B | 2 | 2 | 3 | 3 | 4 | 2 | 2.67 [E:A-WS0-01] | D:D-LV-B; W:W-LV-B; C:C-LV-B(p); L:L-B; A:A-B; G:G-LV |
| G1-ProfServices | C | 1 | 2 | 2 | 3 | 3 | 1 | 2 [E:A-WS0-01] | D:D-LV-C; W:W-LV-C; C:C-LV-C; L:L-LV-C; A:A-C; G:G-LV+Gm-C |
| G1-ProfServices | A+B | 2 | 2 | 2 | 3 | 3 | 2 | 2.33 [E:A-WS0-01] | D:min(D-LV-B); W:min(W-LV-B); C:Cb-AB [V:WS3-013][V:WS3-024]; L:min(L-B); A:min(A-A); G:min(G-LV) |
| G1-ProfServices | A+B+C | 1 | 2 | 3 | 3 | 3 | 1 | 2.17 [E:A-WS0-01] | D:min(D-LV-C); W:min(W-LV-B); C:Cb-ABC(p) (no A+B+C provider found; weak search) [V:WS3-005][V:WS3-013][V:WS3-024]; L:min(L-B); A:min(A-A); G:min(G-LV+Gm-C) |
| G1-Accounting | A | 3 | 3 | 2 | 4 | 3 | 2 | 2.83 [E:A-WS0-01] | D:D-LV-A; W:W-LV-A; C:C-LV-A; L:L-A; A:A-A; G:G-LV |
| G1-Accounting | B | 2 | 2 | 3 | 3 | 4 | 2 | 2.67 [E:A-WS0-01] | D:D-LV-B; W:W-LV-B; C:C-LV-B(p); L:L-B; A:A-B; G:G-LV |
| G1-Accounting | C | 1 | 2 | 2 | 3 | 3 | 1 | 2 [E:A-WS0-01] | D:D-LV-C; W:W-LV-C; C:C-LV-C; L:L-LV-C; A:A-C; G:G-LV+Gm-C |
| G1-Accounting | A+B | 2 | 2 | 2 | 3 | 3 | 2 | 2.33 [E:A-WS0-01] | D:min(D-LV-B); W:min(W-LV-B); C:Cb-AB [V:WS3-013][V:WS3-024]; L:min(L-B); A:min(A-A); G:min(G-LV) |
| G1-Accounting | A+B+C | 1 | 2 | 3 | 3 | 3 | 1 | 2.17 [E:A-WS0-01] | D:min(D-LV-C); W:min(W-LV-B); C:Cb-ABC(p) (no A+B+C provider found; weak search) [V:WS3-005][V:WS3-013][V:WS3-024]; L:min(L-B); A:min(A-A); G:min(G-LV+Gm-C) |
| G2-Foreign | A | 1 | 1 | 2 | 4 | 3 | 2 | 2.17 [E:A-WS0-01] | D:D-G2-AB; W:W-G2-AB; C:C-G2; L:L-A; A:A-A; G:G-LV |
| G2-Foreign | B | 1 | 1 | 2 | 3 | 4 | 2 | 2.17 [E:A-WS0-01] | D:D-G2-AB; W:W-G2-AB; C:C-G2; L:L-B; A:A-B; G:G-LV |
| G2-Foreign | C | 2 | 3 | 2 | 3 | 3 | 1 | 2.33 [E:A-WS0-01] | D:D-G2-C; W:W-G2-C; C:C-G2; L:L-LV-C; A:A-C; G:G-LV+Gm-C |
| G2-Foreign | A+B | 1 | 1 | 2 | 3 | 3 | 2 | 2 [E:A-WS0-01] | D:min(D-G2-AB); W:min(W-G2-AB); C:Cb-AB [V:WS3-013][V:WS3-024]; L:min(L-B); A:min(A-A); G:min(G-LV) |
| G2-Foreign | A+B+C | 1 | 1 | 3 | 3 | 3 | 1 | 2 [E:A-WS0-01] | D:min(D-G2-AB); W:min(W-G2-AB); C:Cb-ABC(p) (no A+B+C provider found; weak search) [V:WS3-005][V:WS3-013][V:WS3-024]; L:min(L-B); A:min(A-A); G:min(G-LV+Gm-C) |

#### LT

| Group | Comp. | Demand | WTP | Competition | Legal | Async | Language | Mean | Basis codes |
|---|---|---|---|---|---|---|---|---|---|
| G1-Logistics | A | 2 | 2 | 2 | 4 | 3 | 3 | 2.67 [E:A-WS0-01] | D:D-LT-A; W:W-LT-A; C:C-LT-A; L:L-A; A:A-A; G:G-LT |
| G1-Logistics | B | 3 | 3 | 2 | 3 | 4 | 3 | 3 [E:A-WS0-01] | D:D-LT-B; W:W-LT-B; C:C-LT-B; L:L-B; A:A-B; G:G-LT |
| G1-Logistics | C | 1 | 3 | 2 | 3 | 3 | 3 | 2.5 [E:A-WS0-01] | D:D-LT-C; W:W-LT-C; C:C-LT-C; L:L-LT-C; A:A-C; G:G-LT |
| G1-Logistics | A+B | 2 | 2 | 2 | 3 | 3 | 3 | 2.5 [E:A-WS0-01] | D:min(D-LT-A); W:min(W-LT-A); C:Cb-AB [V:WS3-013][V:WS3-024]; L:min(L-B); A:min(A-A); G:min(G-LT) |
| G1-Logistics | A+B+C | 1 | 2 | 3 | 3 | 3 | 3 | 2.5 [E:A-WS0-01] | D:min(D-LT-C); W:min(W-LT-A); C:Cb-ABC(p) (no A+B+C provider found; weak search) [V:WS3-005][V:WS3-013][V:WS3-024]; L:min(L-B); A:min(A-A); G:min(G-LT) |
| G1-Wholesale | A | 2 | 2 | 2 | 4 | 3 | 3 | 2.67 [E:A-WS0-01] | D:D-LT-A; W:W-LT-A; C:C-LT-A; L:L-A; A:A-A; G:G-LT |
| G1-Wholesale | B | 3 | 3 | 2 | 3 | 4 | 3 | 3 [E:A-WS0-01] | D:D-LT-B; W:W-LT-B; C:C-LT-B; L:L-B; A:A-B; G:G-LT |
| G1-Wholesale | C | 1 | 3 | 2 | 3 | 3 | 3 | 2.5 [E:A-WS0-01] | D:D-LT-C; W:W-LT-C; C:C-LT-C; L:L-LT-C; A:A-C; G:G-LT |
| G1-Wholesale | A+B | 2 | 2 | 2 | 3 | 3 | 3 | 2.5 [E:A-WS0-01] | D:min(D-LT-A); W:min(W-LT-A); C:Cb-AB [V:WS3-013][V:WS3-024]; L:min(L-B); A:min(A-A); G:min(G-LT) |
| G1-Wholesale | A+B+C | 1 | 2 | 3 | 3 | 3 | 3 | 2.5 [E:A-WS0-01] | D:min(D-LT-C); W:min(W-LT-A); C:Cb-ABC(p) (no A+B+C provider found; weak search) [V:WS3-005][V:WS3-013][V:WS3-024]; L:min(L-B); A:min(A-A); G:min(G-LT) |
| G1-Manufacturing | A | 2 | 2 | 2 | 4 | 3 | 3 | 2.67 [E:A-WS0-01] | D:D-LT-A; W:W-LT-A; C:C-LT-A; L:L-A; A:A-A; G:G-LT |
| G1-Manufacturing | B | 3 | 3 | 2 | 3 | 4 | 3 | 3 [E:A-WS0-01] | D:D-LT-B; W:W-LT-B; C:C-LT-B; L:L-B; A:A-B; G:G-LT |
| G1-Manufacturing | C | 1 | 3 | 2 | 3 | 3 | 3 | 2.5 [E:A-WS0-01] | D:D-LT-C; W:W-LT-C; C:C-LT-C; L:L-LT-C; A:A-C; G:G-LT |
| G1-Manufacturing | A+B | 2 | 2 | 2 | 3 | 3 | 3 | 2.5 [E:A-WS0-01] | D:min(D-LT-A); W:min(W-LT-A); C:Cb-AB [V:WS3-013][V:WS3-024]; L:min(L-B); A:min(A-A); G:min(G-LT) |
| G1-Manufacturing | A+B+C | 1 | 2 | 3 | 3 | 3 | 3 | 2.5 [E:A-WS0-01] | D:min(D-LT-C); W:min(W-LT-A); C:Cb-ABC(p) (no A+B+C provider found; weak search) [V:WS3-005][V:WS3-013][V:WS3-024]; L:min(L-B); A:min(A-A); G:min(G-LT) |
| G1-ProfServices | A | 2 | 2 | 2 | 4 | 3 | 3 | 2.67 [E:A-WS0-01] | D:D-LT-A; W:W-LT-A; C:C-LT-A; L:L-A; A:A-A; G:G-LT |
| G1-ProfServices | B | 3 | 3 | 2 | 3 | 4 | 3 | 3 [E:A-WS0-01] | D:D-LT-B; W:W-LT-B; C:C-LT-B; L:L-B; A:A-B; G:G-LT |
| G1-ProfServices | C | 1 | 3 | 2 | 3 | 3 | 3 | 2.5 [E:A-WS0-01] | D:D-LT-C; W:W-LT-C; C:C-LT-C; L:L-LT-C; A:A-C; G:G-LT |
| G1-ProfServices | A+B | 2 | 2 | 2 | 3 | 3 | 3 | 2.5 [E:A-WS0-01] | D:min(D-LT-A); W:min(W-LT-A); C:Cb-AB [V:WS3-013][V:WS3-024]; L:min(L-B); A:min(A-A); G:min(G-LT) |
| G1-ProfServices | A+B+C | 1 | 2 | 3 | 3 | 3 | 3 | 2.5 [E:A-WS0-01] | D:min(D-LT-C); W:min(W-LT-A); C:Cb-ABC(p) (no A+B+C provider found; weak search) [V:WS3-005][V:WS3-013][V:WS3-024]; L:min(L-B); A:min(A-A); G:min(G-LT) |
| G1-Accounting | A | 2 | 2 | 2 | 4 | 3 | 3 | 2.67 [E:A-WS0-01] | D:D-LT-A; W:W-LT-A; C:C-LT-A; L:L-A; A:A-A; G:G-LT |
| G1-Accounting | B | 3 | 3 | 2 | 3 | 4 | 3 | 3 [E:A-WS0-01] | D:D-LT-B; W:W-LT-B; C:C-LT-B; L:L-B; A:A-B; G:G-LT |
| G1-Accounting | C | 1 | 3 | 2 | 3 | 3 | 3 | 2.5 [E:A-WS0-01] | D:D-LT-C; W:W-LT-C; C:C-LT-C; L:L-LT-C; A:A-C; G:G-LT |
| G1-Accounting | A+B | 2 | 2 | 2 | 3 | 3 | 3 | 2.5 [E:A-WS0-01] | D:min(D-LT-A); W:min(W-LT-A); C:Cb-AB [V:WS3-013][V:WS3-024]; L:min(L-B); A:min(A-A); G:min(G-LT) |
| G1-Accounting | A+B+C | 1 | 2 | 3 | 3 | 3 | 3 | 2.5 [E:A-WS0-01] | D:min(D-LT-C); W:min(W-LT-A); C:Cb-ABC(p) (no A+B+C provider found; weak search) [V:WS3-005][V:WS3-013][V:WS3-024]; L:min(L-B); A:min(A-A); G:min(G-LT) |
| G2-Foreign | A | 1 | 1 | 2 | 4 | 3 | 3 | 2.33 [E:A-WS0-01] | D:D-G2-AB; W:W-G2-AB; C:C-G2; L:L-A; A:A-A; G:G-LT |
| G2-Foreign | B | 1 | 1 | 2 | 3 | 4 | 3 | 2.33 [E:A-WS0-01] | D:D-G2-AB; W:W-G2-AB; C:C-G2; L:L-B; A:A-B; G:G-LT |
| G2-Foreign | C | 2 | 3 | 2 | 3 | 3 | 3 | 2.67 [E:A-WS0-01] | D:D-G2-C; W:W-G2-C; C:C-G2; L:L-LT-C; A:A-C; G:G-LT |
| G2-Foreign | A+B | 1 | 1 | 2 | 3 | 3 | 3 | 2.17 [E:A-WS0-01] | D:min(D-G2-AB); W:min(W-G2-AB); C:Cb-AB [V:WS3-013][V:WS3-024]; L:min(L-B); A:min(A-A); G:min(G-LT) |
| G2-Foreign | A+B+C | 1 | 1 | 3 | 3 | 3 | 3 | 2.33 [E:A-WS0-01] | D:min(D-G2-AB); W:min(W-G2-AB); C:Cb-ABC(p) (no A+B+C provider found; weak search) [V:WS3-005][V:WS3-013][V:WS3-024]; L:min(L-B); A:min(A-A); G:min(G-LT) |

---

## 4. Ranking

Means are close together and every input is low-to-medium confidence, so this ranking is ordinal and fragile [E:A-WS0-01].

**Top three evidence-backed combinations**

| # | Combination | Mean | Why it ranks here | What could sink it |
|---|---|---|---|---|
| 1 | **B (automation) × G1 SMEs × LT** (all sectors) | 3.0 [E:A-WS0-01] | AI adoption 8.8% → 21.3% (2024→2025), one of the EU's largest rises [V:WS2-057][V:WS2-054]; published automation prices exist [V:WS3-024]; native-language fit [V:WS1-105]; delivery is about 90% async [E:A-WS5-33] | Crowded low end: entry offers from €300 [V:WS3-024], below the €1,182 needed for €25/h net [E:A-WS5-36]; no open grant [V:WS2-036] |
| 2 | **B × G1 accounting firms × EE** (other EE G1 sectors at 2.83 [E:A-WS0-01]) | 3.0 [E:A-WS0-01] | Strongest demand signals: AI use 34% (2026) [V:WS2-050]; AI grant (20% own money) exhausted on day one [V:WS2-001][V:WS2-003]; buyers may demand e-invoices since 1 Jul 2025 [V:WS2-073] | No Estonian; four local automation agencies [V:RT-005][V:RT-006][V:RT-007][V:RT-008]; grant-paid advisor role closed to a newcomer [V:WS2-009]; accounting firms thin in databases (97 records) [E:A-WS1-20] |
| 3 | **A (CRM setup) × G1 SMEs × LV** | 2.83 [E:A-WS0-01] | Largest measured CRM-type demand (2,908 applications, about half sales digitalisation) [V:WS2-069][V:WS2-070]; CRM packages had published prices [V:VL-014]; CRM setup is the lowest legal risk [E:A-WS4-01] | Demand was subsidised up to 100% and the programmes are closed [V:WS2-020][V:VL-008]; at least 45 catalogue providers [E:A-WS3-03]; no Latvian; Pipedrive partner tiers need certified staff [V:RT-003] |

Next in line: C × LT and A+B × LT (2.5 each [E:A-WS0-01]) — Lithuania's 2026 opt-out rule helps C, but Ripe Leads sells native Lithuanian outbound from Vilnius [V:WS3-007][V:WS3-008].

**Three weakest combinations**

| # | Combination | Mean | Why |
|---|---|---|---|
| 1 | **C (lead gen) × G1 × EE and LV** | 2.0 [E:A-WS0-01] | No demand evidence (gap); copy must be Estonian/Latvian, which the operator cannot write [V:WS3-002][V:WS3-009]; native incumbents; about 30% of hours in business hours [E:A-WS5-33]; named-employee e-mail unresolved [V:WS4-005][V:WS4-019] |
| 2 | **A+B and A+B+C × G2 (foreign firms) × EE and LV** | 2.0 [E:A-WS0-01] | No evidence that foreign firms buy Baltic CRM/automation set-up (gap); incumbents already sell market entry [V:WS3-053][V:WS3-049]; G2 cannot be sized below an all-sizes ceiling of about 900 chamber memberships [E:A-WS1-24] |
| 3 | **A+B+C × G1 × EE and LV** | 2.17 [E:A-WS0-01] | Inherits C's weaknesses (weakest-link rule) plus the capacity limit: at 15 h/week, about 2 lead-gen clients alone fill the hours [E:A-WS5-38] |

---

## 5. Open unknowns — cheapest way to resolve each

Decision-critical first. Full registers with resolution paths: `01` §7, `02` §11, `03` §11, `04` §7, `05` §11, `06` §7, plus `verification_log.md` §7 and the kill criteria in `red_team.md`.

| # | UNKNOWN | Why it matters | Cheapest resolution |
|---|---|---|---|
| U1 | Own-money willingness to pay among in-scope firms (up to `50` staff) | All price and demand scores rest on subsidised or list-price evidence | owner interviews per country (`15–20`, brief §6 design [E:A-WS8-07]); question: "what did you buy with your own money for sales or admin software/services in the last 12 months, and for how much?" (K1) |
| U2 | Selling hours per won client; reply and meeting rates | Sales effort drives net €/h (€34.9 → €20.9 at 40 h) [E:A-WS8-01] | Small pilot per language (`100` contacts [E:A-WS8-07]); time log from first outreach (K3, K4) |
| U3 | Named-employee work e-mail rules (EE, LV; LT scope secondary-only) | Decides whether C can target named people | One written question each to AKI, DVI and VDAI (K5) |
| U4 | Does RU/EN outreach work in EE/LV compared with the local language? | Core of the trilingual claim | Matched message split in one batch, local version proof-read by a native speaker (K6) |
| U5 | Russian-language ecosystem: Bitrix24/Kommo partners, RU business communities | The only untested route to a Russian-language edge; no RU searches were run | A handful of Russian-language searches (`5–10`); partner-directory check (03 §11) |
| U6 | Incumbent prices and delivery quality at SME scale | Tests whether there is a price or speed gap | Asynchronous quote requests to three incumbents per component [E:A-WS8-07], same scope (K2) |
| U7 | Whether an unregistered Estonian FIE needs a VAT number to invoice LV/LT companies | Admin cost and timing of cross-border invoicing | E-mail EMTA, or read the VAT Act provisions implementing Art. 214(1)(e) [V:WS5-016] |
| U8 | Employment contract restrictions on side business | Could stop the concept outright | Read own contract and handbook; written consent if a clause applies (K7) |
| U9 | Next grant calls (EIS, LIAA, Inovacijų agentūra) | Subsidised demand drives the strongest signals | Subscribe to each agency's planned-calls page or newsletter |
| U10 | Partner and affiliate commissions (Pipedrive, HubSpot, Zoho, Make, n8n) and 2026 tool prices | Upside income; budget fit for lead gen | Read the official programme and pricing pages (05 §11 SP-01…SP-24) |
| U11 | Target-sector × size counts for LV and LT; share of `0–9` firms that actually buy | Funnel precision | CSB tables UZS030/UZS031; State Data Agency tables; interview screener for micro firms |
| U12 | Enforcement cases and fines 2020–2026 | Size of the legal tail risk | AKI, DVI and VDAI annual reports |
| U13 | Upwork AI-automation median (Upwatcher prior lead of $29.50/h — UNKNOWN, not re-verified) | Freelance price floor | Open the Upwatcher report directly (not reachable here) |
| U14 | G2 size within the `50`-staff scope | G2 cannot be sized | Eurostat trade-by-enterprise-characteristics partner tables; de-duplicated chamber lists |
| U15 | Entrepreneur account (ettevõtluskonto) for foreign payers | Would raise net €/h by about 34–36% for LV/LT clients [E:A-WS5-06] | E-mail EMTA |
| U16 | Job-posting, procurement and search-trend counts | Secondary demand signals | Manual searches on cv.ee, cv.lv, cvbankas.lt and the three procurement portals (02 §11) |
| U17 | AI Act, sanctions service ban, EU–US transfers, LinkedIn terms (marked UNKNOWN-P in 04) | Compliance load for B and C | Read the primary texts listed in 04 §7 |

---

## 6. Gaps the brief missed, and what was added

| Added item | Status | Where |
|---|---|---|
| Estonian FIE tax mechanics in 2026 (1.33 divisor, basic exemption used by the salary, II pillar) | Done: 58.65% net share, not 52.26% [E:A-WS5-01][V:VL-018] | 05 §3 |
| VAT for cross-border B2B invoicing as an FIE | Partly: the supplier rule is Art. 214(1)(e), not (d) [V:WS5-016]; the Estonian duty is UNKNOWN (U7) | 05 §8.1 |
| Entrepreneur account vs FIE | Partly: unusable for Estonian company clients [V:WS5-018]; foreign payers UNKNOWN (U15) | 05 §8.2 |
| Capacity and daytime-hours model | Done [E:A-WS5-38][E:A-WS5-33] | 05 §7 |
| Database reachability of firms (Hunter, free counts) | Done [E:A-WS9-02] | 01 §3.6; `_work/data/db_coverage.csv` |
| Sole traders inside the ≤50 scope need consent for e-mail | Done (LV, LT verified; EE inferred) [V:WS4-011][V:WS4-028] | 04 §3.8 |
| E-invoicing mandates as automation drivers | Done: EE from 1 Jul 2025 [V:WS2-073]; LV from 1 Jan 2028 [V:WS2-075] | 02 §8.1 |
| CRM interface languages; AI quality in Baltic languages | Done (HubSpot has no Estonian UI [V:WS0-003]; Zoho partial [V:WS0-004]); AI writing quality UNKNOWN | 01 §3.5 |
| Language proficiency from surveys | Done [V:WS1-100][V:WS1-104][V:WS1-105] | 01 §4.1 |
| Employment-law limits on side business; sanctions service ban; AI Act; EU–US transfers; LinkedIn terms | Not verified (UNKNOWN-P; U8, U17) | 04 §4 |
| Russian-origin CRM ecosystem (Bitrix24/Kommo) | Not researched (U5) | 02 §8.3, 03 §8.2 |
| Buyer's alternative cost (in-house SDR / CRM admin) | Not researched | 05 §8.6 |

---

## 7. "Done means" check (brief §9)

| Criterion | Result |
|---|---|
| At least `80` distinct sources, half primary | Met: `363` distinct URLs, `257` of them primary (`422` rows incl. leads; counts computed by `_work/tools/merge_sources.py`) |
| EE, LV, LT covered separately in every workstream | Met in structure; depth is uneven (LV thinnest; many cells UNKNOWN) |
| Zero unlabelled numbers | Met on the heuristic lint (`_work/tools/lint_labels.py`: no flagged lines, no broken ids) |
| Verification log completed, corrections applied | Met in reduced form (user instruction: one agent, `30` searches; `22` of `30` claims re-searched) |
| Summary written last, consistent with corrected files | Met (this file) |

**Files:** `01_market_size.md` · `02_demand_signals.md` · `03_competitors.md` + `competitors.csv` · `04_legal_compliance.md` · `05_pricing_unit_economics.md` · `06_channels_reachability.md` · `verification_log.md` · `red_team.md` · `sources.csv` · `assumptions.md`. Working files (fragments, prompts, data, tools) are in `_work/`.
