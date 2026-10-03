# Verification log — "Baltic Revenue Engine" (combined verifier and red team)

**Prepared:** 2026-10-03 by an independent verifier who did not do the original research. **Scope applied:** companies with up to fifty staff (`research/_work/SCOPE_CHANGE.md`). **Companion file:** `red_team.md`. **Recomputation script:** `research/_work/data/VER_recompute.py` (stdlib only, re-runnable).

**Legend.** `[V:WS…-nnn]` and `[V:VL-nnn]` = VERIFIED source row in `sources.csv`. `LEAD VL-nnn` = seen, not confirmable. `[E:A-WS9-nn]` = verifier estimate (`_work/assumptions_VER.md`); `[E:A-WS8-nn]` = red-team estimate (`_work/assumptions_RT.md`). Corrected text in the workstream files carries `(corrected — see VL-nn)`; added caveats carry `(verifier note — see VL-nn)`.

---

## 1. Method and limits

- **What "confirmed" means here.** Evidence is search-extract only. WebSearch returns a synthesised answer plus result URLs; WebFetch and curl are blocked. A claim is "confirmed" when the answer ties the wording or figure to the publisher's own domain or URL and matches the original claim. It is not a full read of the page.
- **Budget.** At most thirty searches in total; all thirty were used: twenty-five for verification and five for the red team (ledger in section 8). One call failed with an API error because a requested domain is not accessible to the crawler; it is counted. Nothing else was fetched and no MCP connector was used.
- **Selection of the thirty claims.** Criteria: (1) the claim decides a scoring cell, a go/no-go statement or a legal limit; (2) it feeds a number in a funnel or a model; (3) it carries legal exposure for the operator; (4) it is a prior lead named in the brief; (5) coverage of all six workstreams and of EE, LV and LT; (6) single-point dependency (one vendor page, one media kit or one database carries many claims). The ten topics the instructions require are all included.
- **Result classes.** *Confirmed*: re-checked by search and the original statement stands. *Corrected*: the original statement was changed, narrowed or put into a range, and the workstream text says so. *Could not verify*: searched, but no usable evidence came back; the claim keeps its original status and says so. *Documentary check only*: not re-searched; the cited `sources.csv` row was checked for support of claim, year and label, and any arithmetic was recomputed.
- **Ids.** Claims are VL-001 to VL-030. Where a claim was re-checked by search, the source row with the same number sits in `_work/sources_VER.csv`; further rows start at VL-031. Red-team sources are RT-001 onward in `_work/sources_RT.csv`.
- **Limits.**
  - Synthesised answers can mis-attribute. The Latvian size query returned garbled shares, and the Ripe Leads answers did not pin a page.
  - A search index can hold an outdated consolidated law. The e-seimas result for Art. 81 was the pre-amendment text, so failing to find the amended wording is not evidence against it.
  - No Russian-language search was run; the cap went to higher-value checks.
  - Hunter counts are vendor-database records that no search can re-verify; they were checked by arithmetic only.

---

## 2. Results at a glance

| Result | Count | Claims |
|---|---|---|
| Confirmed | `14` | VL-001, VL-003, VL-004, VL-005, VL-006, VL-007, VL-009, VL-010, VL-011, VL-012, VL-013, VL-015, VL-016, VL-018 |
| Corrected | `7` | VL-008, VL-014, VL-017, VL-021, VL-022, VL-027, VL-029 |
| Could not verify | `3` | VL-002, VL-019, VL-020 |
| Documentary check only | `6` | VL-023, VL-024, VL-025, VL-026, VL-028, VL-030 |
| Total | `30` | |

Twenty-two of the thirty were re-checked by search (VL-001 to VL-022); three of those came back empty or inconclusive.

**Most important corrections**
1. **Latvia's grant-linked anchors are historical.** Both LIAA programmes are closed (acceptance stopped 17.06.2025; follow-on closed 07.11.2025) [V:WS2-069] [V:WS2-071] [V:VL-008]. Statements in 05 and 06 that called the status "uncertain" or the EDIC catalogue a "live routing channel" were stale. The Latvian willingness-to-pay score for component A is lowered from 4 to 3.
2. **Named-e-mail pools are smaller.** The pooled 61.0% personal-e-mail rate came mostly from out-of-scope 51-200 segments; restricted to in-scope segments it is 51.9% [E:A-WS9-01]. The 11-50 pools with a named e-mail become EE 703–1,019; LV 542–747; LT 957–1,300 [E:A-WS9-02] (VL-027).
3. **Lithuania's 10–49 class is a ceiling.** Working range 11.3–12.8 thousand instead of a point value of 12,815 [E:A-WS9-03] (VL-017).
4. **Association counts conflict.** ELEA 65–68 members and an average member size of 91 employees (LEAD VL-021); LINEKA 42 in an undated report [V:WS6-008] versus 60 in a report dated 17 Apr 2021 [V:VL-022] (VL-021, VL-022).
5. **Price anchors in 05.** The EIS €2,500 consultant cap is not available to a newcomer, the Latvian bundles include licences, and the model's low automation price (€450) is above the cheapest published offers (LT €300; EE from €100 [V:RT-005]) (VL-029).
6. **Estonian automation is not "unsearched".** Four Estonian agencies advertise AI or workflow automation (RT-005 to RT-008).
7. **Pipedrive's partner tiers need certified staff** [V:RT-003]; a one-person operator may not meet even the entry tier.

**Could not verify (all three remain UNKNOWN).** The Lithuanian named-employee scope (four searches; secondary sources only), the Estonian VAT-number duty for cross-border invoicing, and the Upwatcher median.

---

## 3. The thirty claims

| VL id | Claim | File § | Original value and source id | Result | Corrected value | New source | Note |
|---|---|---|---|---|---|---|---|
| VL-001 | Lithuania amended ERĮ Art. 81 on 22 Apr 2026; direct marketing to legal entities no longer needs prior consent | 04 §1(1), §3.1, §8 | Law XV-815 in force 22 Apr 2026 [V:WS4-029] [V:WS4-031]; opt-out exception for legal entities [V:WS4-036] | Confirmed | None | [V:VL-001] | Date, purpose and FAQ confirmed on VDAI's page. Opt-out mechanics rest on secondary sources; the amended statutory text was not retrievable. |
| VL-002 | The exception covers named employees' work e-mail and work phone numbers | 04 §1(1), §3.1, §3.2, §8 | Secondary only [V:WS4-034] [V:WS4-035] | Could not verify | None; stays secondary-only and provisional | LEAD VL-002 | Four searches (vdai.lrv.lt twice, e-seimas.lrs.lt/e-tar.lt, e-seimas/lrs.lt) did not return the FAQ or the amended wording; a fifth attempt failed with an API error. The suggested legal score of 4 for LT component C depends on this point. |
| VL-003 | Estonia, ESS § 103¹: opt-out for legal persons, consent for natural persons | 04 §3.1 EE, §3.8 | [V:WS4-001] [V:WS4-003] [V:WS4-004] | Confirmed | None | [V:VL-003] | Natural-person clause seen only in an older text (LEAD VL-037). AKI precept-warnings exist for 2020 and, by file path, June 2024 (LEAD VL-032). |
| VL-004 | Latvia, ISPL Art. 9: DVI allows e-mail to a legal entity's address with a valid stop address; no position on named employees | 04 §3.1 LV, §3.8 | [V:WS4-011] [V:WS4-016] [V:WS4-019] | Confirmed | None | [V:VL-004] | Named-employee position still not found (UNKNOWN). A DVI decision document on a company surfaced (LEAD VL-033, not read). |
| VL-005 | EE AI-adoption grant: €20,000 unit price, 20% self-financing, €2.0M, revenue floor €200,000, closed same day | 02 §1(1), §5.1 | [V:WS2-001] [V:WS2-002] [V:WS2-003] | Confirmed | None | [V:VL-005] | Closure 24.08.2026 16:00. Eligible activity per EIS: developing an AI product or integrating AI into a product, service or process; whether outside providers are payable stays UNKNOWN. |
| VL-006 | EE RTE software grant: €2,000–5,000, digital consultant mandatory, at least three similar projects in four years, fees up to 50% of aid | 02 §1(3)-(4), §5.1; 03 G-8; 05 Finding 5 | [V:WS2-007] [V:WS2-009] [V:WS2-010] [V:WS2-011] | Confirmed | None | [V:VL-006] [V:VL-036] | The inference that a new FIE cannot be the paid advisor at launch stays an inference; whether in-house experience counts is UNKNOWN. |
| VL-007 | EE AI use 22% (2025) and 34% (2026); about one-fifth of firms with fewer than 50 employees | 02 §1(6), §2 | [V:WS2-049] [V:WS2-050] | Confirmed | None | [V:VL-007] [V:VL-034] | Survey covers firms with 10+ persons employed [V:WS2-053]. |
| VL-008 | Latvia: RRF programme drew 2,908 applications, 1,438 (about 49%) for sales-process digitalisation; follow-on programme closed | 02 §1(7), §5.2; 05 Finding 5, §5.1, §12; 06 Finding 7, §3.4 | [V:WS2-069] [V:WS2-070] [V:WS2-071]; status "uncertain" in 05, "live" in 06 | Corrected | Follow-on closure 07.11.2025 re-confirmed; the first programme appears as closed ("noslēgta") in the result titles, with the date 17.06.2025 from [V:WS2-069]. The 49% mixes figures from two LIAA pages: read it as roughly one half. LV × A willingness-to-pay score 4 → 3. | [V:VL-008] | No 2026 call surfaced in the search (negative evidence only). EDIC's own test-before-invest service may still run (UNKNOWN [V:WS3-046]). |
| VL-009 | Lithuania: AI call 02-126-K suspended; digital vouchers closed; no open digitalisation call | 02 §1(8), §5.3 | [V:WS2-036] [V:WS2-037] [V:WS2-043] | Confirmed | None | [V:VL-009] | "No open call at all" cannot be proven by search. |
| VL-010 | Fontakt covers ET, LV, LT, RU, EN (plus FI, SV, DE) with almost 100 staff | 03 §1(1), §3, §5 | [V:WS3-001] [V:WS3-002] | Confirmed | None | [V:VL-010] | Languages and the database claim re-confirmed; the staff count was not re-checked. On the Baltic outsourcing page agents are native or fluent in ET, LV, LT, FI, SV and Russian appears only as a calling language; German is not listed there. |
| VL-011 | Ripe Leads price: €3,750 first month, then €2,850 a month, 28 days' notice, tools and data included | 03 §1(2), §3, §6; 05 §5.1 | [V:WS3-008] | Confirmed (domain level) | None | LEAD VL-011 | The answer reproduced every figure and the €35,100 first-year total, but did not pin a page; WS3-008 stays the VERIFIED row. |
| VL-012 | Ripe Leads runs campaigns in LT, LV, ET, PL, CS, SK, DE, EN, RU | 03 §1(1), §3, §5 | [V:WS3-009] | Confirmed, with caveat | None | LEAD VL-012 | Another page says outreach in 7 languages; the Russian claim rests on the nine-language page. |
| VL-013 | eXpanby (Riga) supports EN, ET, LV, LT, RU, UK | 03 §1(1), §2.2, §5 | [V:WS3-013] | Confirmed | Adds: Pipedrive Platinum Partner (top tier); also DE and PL | [V:VL-013] [V:VL-035] | Industries include logistics and transport, manufacturing. |
| VL-014 | Latvian EDIH catalogue: Pipedrive bundles €2,990–7,440; generic CRM implementation €5,000 | 03 §1(3), §6; 05 §5.1, §6.5 | [V:WS3-017] [V:WS3-018] [V:WS3-019] | Corrected | Prices re-confirmed (€2,990; €3,990; €4,990 for 12 months), but they are undated list prices of a closed-grant regime and include licences (service share about €1,990 [E:A-WS3-01]) | [V:VL-014] | Do not read them as current willingness to pay. |
| VL-015 | Estonia 2025: 159,827 enterprises; 10–49 = 6,284; 50–249 = 1,151; under 10 = 152,205 | 01 §3.1, §3.6 | [V:WS1-095] | Confirmed | None | [V:VL-015] | By employees, all sections. |
| VL-016 | Latvia 2024: 10–49 = 6,457 (JRC estimate) | 01 §3.1 | [V:WS1-025] | Confirmed (as an estimate) | None | [V:VL-016] | The SME total 106,886 equals micro + small + medium. A national CSB value is still not extracted. |
| VL-017 | Lithuania 10–49 ≈ 12,815 (2022) | 01 §1(4), §3.1, §3.6, §8 | [E:A-WS1-04] from [V:WS1-033] [V:WS1-034] | Corrected | Ceiling; working range 11.3–12.8 thousand [E:A-WS9-03] | [V:VL-017] | The 3.9% share belongs to non-financial enterprises but was applied to the all-enterprise total; no 2024 or 2025 VDA edition found. |
| VL-018 | FIE keeps 58.65% of profit; the literal brief reading gives 52.26% | 05 §2(1), §3 | [V:WS5-002] [V:WS5-007] [E:A-WS5-01] | Confirmed | None | [V:VL-018] | EMTA divides business income by 1.33, income tax 22%, no advances if an employer pays at least €877.14 per quarter. The literal reading is not how EMTA computes. |
| VL-019 | VAT: Art. 214(1)(e) is the supplier rule; whether an unregistered Estonian FIE needs a VAT number to invoice EU business customers | 05 §2(8), §8.1 | [V:WS5-016]; duty UNKNOWN | Could not verify | None | LEAD VL-019 | The (e) wording stays a documentary check on the EUR-Lex quote in WS5-016. The rate of 24% and the €40,000 threshold are documentary [V:WS5-011] [V:WS5-012]. |
| VL-020 | Prior lead: Upwork AI-automation median about $29.50/h, May 2026 (Upwatcher) | 05 §2(10), §5.2 | Brief lead; UNKNOWN in WS5 | Could not verify | None | LEAD VL-020 | A search restricted to upwatcher.com returned no results. |
| VL-021 | ELEA has about 65 members | 01 §1(7), §3.4, §4.5; 06 §1(5), §3.1, §3.7, §8.1 | 65 incl. 13 associates [V:WS6-007] | Corrected | 65–68; average member size 91 employees (LEAD), so many members exceed the scope | LEAD VL-021 | Another ELEA page gives 68 incl. 17 associates. Acceptance needed for 15–20 interviews: 22–31% [E:A-WS9-04]. |
| VL-022 | LINEKA has 42 members | 01 §1(7), §3.4; 06 §1(5), §3.1, §3.7, §8.1 | [V:WS6-008] | Corrected | 42 (undated report) versus 60 (report dated 17 Apr 2021, pre-2023); "over 40" on the About page | [V:VL-022] [V:VL-031] | Current count unresolved. Acceptance needed: 25–48% [E:A-WS9-04]. |
| VL-023 | EE roadmap grant closed from 24.07.2026; max €10,000; revenue floor €200,000 | 02 §1(2), §5.1 | [V:WS2-004] | Documentary check only | None | none | The EIS page appeared in two result lists but its text was not returned. The row's quote is on point and dated. |
| VL-024 | AKI 2015 guidance: generic addresses are legal-entity addresses; named addresses judged by position and product | 04 §3.1 EE | [V:WS4-005] | Documentary check only | None | none | The PDF is still online (it appeared in results). It predates the GDPR. |
| VL-025 | CRM use among small firms: LT 27.6% (2023); EU 24.69% (2025) | 02 §2 | [V:WS2-059] [V:WS2-064] | Documentary check only | None | none | Years differ. The figures show headroom, not willingness to pay. |
| VL-026 | aigentas.lt prices from €300; €450–1,200; €1,500–3,000+ | 03 §4, §6 | [V:WS3-024] | Documentary check only | None | none | Consistent with the Estonian entry prices found later (RT-005). |
| VL-027 | Database-reachable pools (up to fifty staff); e-mail rates any 83.0%, personal 61.0% | 01 §3.6, §8 | [E:A-WS1-20] [E:A-WS1-13] | Corrected (documentary check plus recomputation) | Arithmetic reproduces within ±2. Personal-e-mail pools lowered: EE 2,254–3,381; LV 1,416–2,036; LT 2,657–3,793; 11-50 bucket EE 703–1,019, LV 542–747, LT 957–1,300 [E:A-WS9-02] | none | Fifteen of the 22 pooled segments sit in the out-of-scope 51-200 bucket [E:A-WS9-01]. |
| VL-028 | G2 network route: about 900 chamber memberships | 01 §3.7, §4.2 | [E:A-WS1-24] | Documentary check only | None | none | Sum 470 + 130 + 100 + 100 + 100 recomputed. All sizes, not de-duplicated; the up-to-fifty cut cannot be applied. |
| VL-029 | Unit-economics inputs, net €/h tables, price floors and capacity | 05 §3, §6, §7, §12 | [E:A-WS5-13] to [E:A-WS5-38] | Corrected (recomputation identical; anchor wording changed) | Outputs unchanged. Changed: the €2,500 EIS cap is not a newcomer anchor; Latvian bundles are licence-inclusive and historical; €450 is not the market floor | none | An independent re-implementation matches to zero difference. Cold-start sensitivity added in [E:A-WS8-01]. |
| VL-030 | Event timing: all 19 verified events on weekdays; ticket total €707 | 06 §1(1)-(3), §3.2, §3.6 | [E:A-WS6-01] [E:A-WS6-03] | Documentary check only | Weekday claim holds. Label fixes: 11 of 13 EE events listed in Estonian plus one bilingual title (was 12); TechChill 18–19 Mar is Thu–Fri; ticket total €707 lowest-listed, €837 regular [E:A-WS9-05] | none | Eleven EE events rest on one organiser media kit [V:WS6-012]. |

---

## 4. Model recalculations

### 4.1 Tax, unit economics, price floors, capacity

An independent re-implementation (it does not import `WS5_models.py`) was compared with `WS5_models.csv`. Fifteen values were compared across net €/h, tax and capacity, and the maximum absolute difference is zero. Re-running `WS5_models.py` also reproduces the committed CSV byte for byte. Every table in `05 §3, §6, §7` matches.

**Tax.** Net share of FIE profit is 58.65% under the EMTA mechanism (social tax 33% of profit divided by 1.33, income tax 22% of the rest); the literal reading of the brief gives 52.26%, a gap of 6.39 percentage points [E:A-WS5-01] [V:VL-018].

**Net €/h after Estonian FIE tax (base hours, recomputed)**

| Model (low / mid / high price) | Low | Mid | High | Label |
|---|---|---|---|---|
| CRM setup (€1,200 / €2,500 / €5,000) | €16.8 | €34.9 | €69.8 | [E:A-WS5-14] |
| Automation project (€450 / €1,200 / €3,000) | €9.4 | €25.4 | €63.8 | [E:A-WS5-20] |
| Lead-gen retainer (€1,000 / €1,800 / €2,850 per month) | €19.5 | €37.9 | €62.1 | [E:A-WS5-26] [E:A-WS5-29] |

**Break-evens: price needed for a target net €/h (base hours)**

| Model | Net `€15`/h | Net `€25`/h | Net `€40`/h | Label |
|---|---|---|---|---|
| CRM setup (per project) | €1,074 | €1,790 | €2,865 | [E:A-WS5-36] |
| Automation project (per project) | €713 | €1,182 | €1,886 | [E:A-WS5-36] |
| Lead-gen retainer (per month) | €802 | €1,237 | €1,889 | [E:A-WS5-36] |

**Capacity at the mid price (supply-side ceiling with a full pipeline)**

| Model | `10` h/week | `15` h/week | `20` h/week | Label |
|---|---|---|---|---|
| CRM setup: projects a year / net a year / all-in net €/h | 9.2 / €13,189 / €28.7 | 14.7 / €21,218 / €30.8 | 20.2 / €29,247 / €31.8 | [E:A-WS5-38] |
| Automation: projects a year / net a year / all-in net €/h | 14.1 / €9,491 / €20.6 | 22.5 / €15,328 / €22.2 | 30.8 / €21,165 / €23.0 | [E:A-WS5-38] |
| Lead gen: concurrent clients / net a year / all-in net €/h | 1.3 / €14,368 / €31.2 | 2.0 / €23,096 / €33.5 | 2.8 / €31,824 / €34.6 | [E:A-WS5-38] |

**What the recalculation does not cover.** The arithmetic is right; the inputs are ESTIMATE entries of low confidence.
- Sales hours per won client (6–25) and monthly churn have no Baltic benchmark [E:A-WS5-15] [E:A-WS5-29]. The red-team sensitivity with 40 and 60 sales hours lowers the CRM mid-price result from €34.9 to €20.9 and €16.3 per hour [E:A-WS8-01].
- Capacity results assume a full pipeline from the first hour; no idle or learning time is modelled [E:A-WS5-38].
- Tool prices, partner commissions, FIE set-up costs and the Estonian VAT-number duty are UNKNOWN; they are carried as allowances [E:A-WS5-11] [E:A-WS5-30].
- The automation low price (€450) is above the cheapest published offers [V:WS3-024] [V:RT-005].

### 4.2 G1 funnel, up to fifty staff (recomputed from the raw counts)

The table shows the statistical route (size classes `0–9` and `10–49`) and the database route (Hunter buckets `1-10` and `11-50`, maritime-tagged logistics rows removed). The same table sits at the top of `01_market_size.md`.

| Step | EE | LV | LT | Label |
|---|---|---|---|---|
| Statistical `10–49` class | 6,284 (2025) | 6,457 (2024 est.) | ≤12,815 (2022); range 11.3–12.8 thousand | [V:VL-015] [V:VL-016] [E:A-WS9-03] |
| Target sectors within `10–49` | 1,191–3,481 | UNKNOWN | UNKNOWN | [E:A-WS1-17] |
| Database records, target sectors, `1-10` + `11-50` | 4,345–5,539 | 2,729–3,336 | 5,123–6,213 | [E:A-WS1-20] |
| with at least one indexed e-mail (reproduced) | 3,608–4,600 | 2,266–2,770 | 4,254–5,159 | [E:A-WS1-20] reproduced within ±2 |
| with a named e-mail, original | 2,650–3,379 | 1,665–2,035 | 3,125–3,790 | [E:A-WS1-20] |
| with a named e-mail, corrected | 2,254–3,381 | 1,416–2,036 | 2,657–3,793 | [E:A-WS9-02] |
| `11-50` bucket, named e-mail, original (the likelier buyers) | 826–1,019 | 638–747 | 1,125–1,299 | [E:A-WS1-20] |
| **`11-50` bucket, named e-mail, corrected (funnel endpoint)** | **703–1,019** | **542–747** | **957–1,300** | [E:A-WS9-02] |

Recomputation notes:
- Totals, bucket sums, the maritime adjustment (logistics records times the sampled non-maritime share per bucket) and the sector sums all match WS1 within rounding.
- The pooled e-mail rates: all 22 exact segments give any 83.0% and personal 61.0% (937 records); the 7 in-scope exact segments give any 84.5% and personal 51.9% (374 records, accounting-dominated) [E:A-WS9-01]. The corrected range uses the lower in-scope rate for the low end and the pooled rate for the high end.
- Not applied, so the endpoint is an upper bound: language workability, the Russia/Belarus screen (share UNKNOWN), maritime-adjacent firms outside the logistics industry, and duplicate domains.
- Coverage indicator (database `11-50` records over the statistical `10–49` class): EE 56.7%, LV 36.5%, LT 34.1% [E:A-WS1-20]; the Estonian ratio is inflated by internationally run firms.

### 4.3 G2

The only quantity is a ceiling of about 900 chamber memberships, all sizes, not de-duplicated: 470 + 130 + 100 + 100 + 100 [E:A-WS1-24]. The sum was recomputed and holds. The up-to-fifty cut cannot be applied, so the G2 count is UNKNOWN and at most that ceiling.

### 4.4 Other arithmetic checked
- **Events.** Every start and end date of the 19 verified events in 06 §3.2 falls on a Tuesday to Friday; none on a weekend [E:A-WS6-01]. The ticket total is €707 using the lowest listed tickets and €837 using regular or visitor tickets [E:A-WS9-05].
- **Interview recruitment.** Acceptance needed from one association list for 15–20 interviews: ELEA 22–31%, LINEKA 25–48% [E:A-WS9-04]; the original 23–31% and 36–48% used single counts [E:A-WS6-04].
- **Funnel sums.** EE envelope 1,191 + 1,036 + 472 + 407 + 375 = 3,481 [E:A-WS1-17]; Latvian classes sum to 107,091 [E:A-WS1-02]; Ripe Leads first year 3,750 + 11 × 2,850 = 35,100 [E:A-WS3-02].

---

## 5. Lint

| Check | Before | After |
|---|---|---|
| Unlabelled-number lines in `01_market_size.md` | `19` | `0` |
| Unlabelled-number lines in `02`–`06` | `0` | `0` |
| Placeholder ids in `01_market_size.md` | Four V ids (`WS0`, `WS1`, `WS3`, `WS6` with the suffix `0xx`) and one E id (`A-WS1-0x`) | `0` |
| Source rows with a quote over `25` words | One (`WS2-082`, `26` words) | `0` |
| Missing source or assumption ids in any file | `0` | `0` |

How they were fixed: size-class labels and query strings were put in backticks or reworded; legend placeholders were renamed `nnn`/`nn`; table rows that cited bare source ids got proper `[V:…]` tags; the WS2-082 quote was cut to 17 words without changing its meaning. `merge_sources.py` and `lint_labels.py` were re-run at the end; the final output is in section 7.

---

## 6. Systemic issues

1. **Search-extract only.** Every VERIFIED row rests on a synthesised answer, not a page read. Two attribution failures were found during this pass (Latvian size shares; Ripe Leads pricing and language pages).
2. **Stale cross-file statements.** Files `03`, `05` and `06` were written before WS2's gap-fill established that both Latvian programmes had closed. They called the status "uncertain" or the catalogue "live". Fixed (VL-008, VL-014).
3. **Pooled rates built before the scope change.** The e-mail rates pooled segments from the out-of-scope `51-200` bucket (VL-027).
4. **Supply-side price evidence.** All price anchors are list prices on vendor or catalogue pages; none is a transaction price, several are undated, and some include licences (VL-014, VL-029).
5. **Self-declared competitor coverage.** Language coverage of Fontakt, Ripe Leads and eXpanby comes from their own pages; delivery capacity at SME scale is untested. Russian at Fontakt is a calling language only (VL-010), and Ripe Leads gives two different language counts (VL-012).
6. **Single-point dependencies.** One organiser media kit carries eleven Estonian events; one database carries all reachability counts; one undated catalogue carries the Latvian prices.
7. **Hard-exclusion screening is partial.** The maritime tag was removed only inside the logistics industry; maritime-adjacent firms in manufacturing, wholesale, professional services and staffing are not screened, and the Russia/Belarus screen could be applied only as a Latvian upper bound.
8. **Unverified legal layers.** The GDPR articles, the AI Act, sanctions rules, employment law and the LinkedIn terms (secondary only) are still `UNKNOWN-P` in 04; the Lithuanian named-employee scope is secondary-only (VL-002).
9. **No Russian-language searching anywhere.** Not in WS2 to WS6 and not here. The Russian-language competitor and channel picture is unobserved, not absent.
10. **Pre-2023 data.** Lithuanian size data are 2022; the LINEKA report with sixty members is from 2021 (VL-017, VL-022).

---

## 7. Remaining risks

| Risk | Why it matters | Cheapest way to close it |
|---|---|---|
| Lithuanian named-employee scope unconfirmed | It governs the highest-volume tactic in the only country where the operator is native | Read the FAQ linked from the VDAI news item, or ask VDAI in writing |
| Latvian and Estonian named-address positions | LV has no DVI position; EE rests on 2015 guidance | One written question each to DVI and AKI |
| Enforcement and fine amounts unknown in all three countries | Legal risk cannot be calibrated | Read the AKI, DVI and VDAI decision lists and annual reviews (leads exist: VL-032, VL-033, RT-010) |
| Reachability counts are vendor records | Top-hundred-by-e-mail sample bias, shell firms, duplicate domains, no language or sanctions screen | Unbiased random sample of thirty to fifty firms per country from a register extract, checked in the database |
| Sales hours, conversion, churn, tool costs | They decide net €/h; none has a Baltic benchmark | A logged pilot of one hundred contacts per language; open the vendor pricing pages |
| Estonian VAT-number duty | Admin load and tool-VAT recovery | One EMTA consultation |
| Upwatcher lead (UNKNOWN) | If a global rate near the lead's median is right it caps price | Check the source directly |
| Competitor delivery capacity | Language and speed claims are self-declared | Asynchronous quote requests to three incumbents |
| Association sizes (ELEA, LINEKA) and their up-to-fifty share | Interview recruitment arithmetic | Count rows on the public member lists |

**Final tool output (run at the end of this pass):**

```
python3 research/_work/tools/merge_sources.py
python3 research/_work/tools/lint_labels.py
```

```
merge_sources.py   rows: 422 | VERIFIED: 328 | LEAD: 94 | distinct URLs: 363 | primary URLs: 257 | domains: 134
                   fragments: sources_RT.csv, sources_VER.csv, sources_WS0.csv ... sources_WS6.csv
                   problems (0)
merge_assumptions  merged 9 files, 102 assumption entries
lint_labels.py     known source ids: 422 | assumption ids: 102
                   01_market_size.md ...... unlabelled-number lines: 0 | missing V ids: 0 | missing E ids: 0
                   02_demand_signals.md ... unlabelled-number lines: 0 | missing V ids: 0 | missing E ids: 0
                   03_competitors.md ...... unlabelled-number lines: 0 | missing V ids: 0 | missing E ids: 0
                   04_legal_compliance.md . unlabelled-number lines: 0 | missing V ids: 0 | missing E ids: 0
                   05_pricing_unit_economics.md ... 0 | 0 | 0
                   06_channels_reachability.md .... 0 | 0 | 0
                   red_team.md ............ unlabelled-number lines: 0 | missing V ids: 0 | missing E ids: 0
                   verification_log.md .... unlabelled-number lines: 0 | missing V ids: 0 | missing E ids: 0
```

---

## 8. Search ledger (thirty searches)

| # | Purpose | Domains | Query language | Outcome |
|---|---|---|---|---|
| `1` | LT Art. 81 date and employee scope | vdai.lrv.lt | LT | Date and purpose confirmed; employee scope not returned |
| `2` | LT Art. 81 statutory wording | e-seimas.lrs.lt, e-tar.lt | LT | Pre-amendment consolidated text only |
| `3` | EE ESS § 103¹ | riigiteataja.ee, aki.ee | ET | Confirmed; AKI precept-warning files surfaced |
| `4` | LV ISPL Art. 9 | dvi.gov.lv, likumi.lv | LV | Confirmed; no named-employee position |
| `5` | EE AI-adoption grant | eis.ee | ET | Confirmed |
| `6` | EE RTE grant and advisor rule | eis.ee, riigiteataja.ee | ET | Confirmed |
| `7` | EE AI use | stat.ee | ET | Confirmed |
| `8` | EE enterprise counts | stat.ee | EN | Confirmed |
| `9` | LV size classes | stat.gov.lv, ec.europa.eu | EN | SME total consistent; share figures garbled |
| `10` | LT size classes | osp.stat.gov.lt | LT | Nothing newer than the 2023 edition |
| `11` | LV LIAA status | liaa.gov.lv, liaa.business.gov.lv | LV | Closed; no 2026 call surfaced |
| `12` | LT grants | inovacijuagentura.lt, esinvesticijos.lt, eimin.lrv.lt | LT | AI call suspended; vouchers closed |
| `13` | Fontakt and Ripe Leads | fontakt.com, ripeleads.eu | EN | Fontakt confirmed; Ripe Leads pricing not returned |
| `14` | eXpanby | pipedrive.com, expanby.com | EN | Confirmed; Platinum Partner |
| `15` | Latvian catalogue prices | dih.lv | LV | Confirmed |
| `16` | ELEA and LINEKA counts | elea.ee, lineka.lt | EN | LINEKA `60` versus `42`; ELEA total not returned |
| `17` | Ripe Leads price | ripeleads.eu | EN | Confirmed at domain level; "seven languages" on another page |
| `18` | LT FAQ on employees (retry) | vdai.lrv.lt and others | LT | API error: one requested domain not accessible; counted |
| `19` | LINEKA report year | lineka.lt | EN | Sixty members, report dated 17 Apr 2021 |
| `20` | ELEA members | elea.ee | ET | `68` incl. `17` associates; average `91` employees |
| `21` | VDAI FAQ (retry) | vdai.lrv.lt | LT | FAQ not returned |
| `22` | EMTA tax mechanism | emta.ee | ET | Confirmed |
| `23` | VAT-number duty | emta.ee, eur-lex.europa.eu | EN | Not settled |
| `24` | Upwatcher median | upwatcher.com | EN | No results |
| `25` | Law `XV-815` text | e-seimas.lrs.lt, lrs.lt | LT | Amended wording not returned |
| `26` | Red team: cold-email benchmarks | ripeleads.eu | EN | Vendor figure only (LEAD RT-001) |
| `27` | Red team: LinkedIn automation | none | EN | Secondary summaries of `section 8.2` (RT-004) |
| `28` | Red team: VDAI enforcement | vdai.lrv.lt | LT | Decision lists exist; no amounts (LEAD RT-010) |
| `29` | Red team: Estonian automation agencies | none | ET | Four agencies (RT-005 to RT-008) |
| `30` | Red team: Pipedrive partner programme | pipedrive.com | EN | Tiers and certified-staff rules (RT-003) |
