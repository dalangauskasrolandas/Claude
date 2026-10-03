# 03 — Competitor map (WS3): CRM partners, lead-generation agencies and automation providers in EE / LV / LT

**Scope:** who already sells CRM setup (A), AI/workflow automation (B) and outbound lead generation (C) to B2B companies in Estonia, Latvia and Lithuania, covering their languages, coverage, pricing models and published prices. It also tests whether the "all-Baltic, EN + RU + LT" positioning is already taken, and where gaps are evidenced.

**Legend:**
- `[V:WS3-012]` = VERIFIED: a row in `_work/sources_WS3.csv`. `WS0-`/`WS2-` ids are rows in the lead analyst's and WS2's fragments.
- `[E:A-WS3-01]` = ESTIMATE: an entry in `_work/assumptions_WS3.md`.
- `[LEAD:WS3-010]` = seen in a search result but not verified. Never used alone to support a conclusion.
- `UNKNOWN (resolve: …)` = not found.
- Provider counts are **identified via search (lower bound)**. They are never market totals.

**Method note:** Evidence gathered via web-search extracts on 2026-10-03; direct page fetching was blocked in this environment (a WebFetch test on dih.lv returned EGRESS_BLOCKED).

**Coverage limitation (read first):** all six workstreams share one WebSearch budget, and it ran out after thirty-one WS3 queries. The following could not be searched and are UNKNOWN:
- Zoho, Salesforce, Bitrix24 and Kommo partners (UNKNOWN)
- Make/n8n/Zapier expert directories
- Baltic B2B data providers other than Fontakt
- Estonian and Latvian automation agencies
- freelancer supply
- vendor onboarding services
- **every planned Russian-language query**

So a competitor missing from this file is **not** evidence of a gap unless stated. Prices exclude VAT unless stated. Languages and coverage are the competitors' own claims; their actual delivery capacity is UNKNOWN.

> **Verifier note (2026-10-03).** Re-checked by search: Fontakt, Ripe Leads and eXpanby coverage and the Ripe Leads prices (VL-010 to VL-013) and the Latvian catalogue prices (VL-014); all confirmed. Added: eXpanby is a Pipedrive Platinum Partner (VL-013); the Pipedrive tier rules (RT-003); four Estonian automation agencies (RT-005 to RT-008). Corrections: Estonian automation is no longer unsearched, and the Latvian catalogue prices are historical list prices (VL-014). Documentary check only: aigentas.lt prices (VL-026). See `verification_log.md`.

---

## 1. Key findings
1. **The claimed edge is already taken.** At least three firms already claim to cover all three Baltic states in English, Russian and the local languages:
   - Fontakt (Tallinn; founded 2007; about 100 staff [V:WS3-001]) represents clients in ET/LV/LT/RU/EN, plus FI/SV/DE [V:WS3-002]. (verifier note — see VL-010: on Fontakt's Baltic outsourcing page Russian is listed as a calling language, not among the native or fluent agent languages [V:VL-010].)
   - Ripe Leads (Vilnius) runs campaigns in LT/LV/ET/RU/EN, plus PL/CS/SK/DE [V:WS3-009]. (verifier note — see VL-012: another Ripe Leads page says "outreach in 7 languages" (LEAD VL-012), so the Russian-language claim rests on one page.)
   - Pipedrive partner eXpanby (Riga) lists EN/ET/LV/LT/RU/UK [V:WS3-013].

   All three also offer Estonian and Latvian, which the operator does not.
2. **The published outbound price anchor is about €2,850–3,750/month.** Ripe Leads charges €3,750 for month 1, then €2,850/month, with tools and data included and 28 days' notice to cancel [V:WS3-008]. That is about €35,100 in year 1 [E:A-WS3-02]. Fontakt prices calling per "meaningful conversation" and does not publish the rate [V:WS3-004].
3. **In Latvia, SME CRM work is partly sold as fixed-price packages in the EDIH grant catalogue (dih.lv).**
   - Pipedrive licences + 12 h implementation + 1 h/month support: €2,990–4,990 for 12 months, €7,440 for 24 months [V:WS3-017, WS3-018].
   - A generic CRM implementation package: €5,000 [V:WS3-019].
   - Packaged CRMs: €5,880–9,900 [V:WS3-045, WS3-043].
   - At least 45 providers appear in the catalogue's business-process filters [E:A-WS3-03].
   - Companies need an EDIC maturity test and roadmap before they can apply to LIAA [V:WS3-020].
4. **Lithuania's low end for automation is published, and cheap.** aigentas.lt starts at €300 (one process, up to two integrations), then €450–1,200, then €1,500–3,000+ [V:WS3-024]. LabasClaw and Retos also sell AI implementation in Lithuania [V:WS3-034, WS3-035]. Custom CRM builds cost €9,500–25,000 [V:WS3-025].
5. **Estonia is Pipedrive's home turf.** Pipedrive's Tallinn engineering and product hub has 300+ staff [V:WS3-026]. Local partners include Dominate Sales (Pipedrive partner since 2017, "Elite" [V:WS3-015]; "Regional Partner of the Year for the North" in a secondary source [V:WS3-029]) and TechPeer [V:WS3-016]. None of the Estonian or Lithuanian CRM partners found publishes implementation prices [V:WS3-012, WS3-014, WS3-016, WS3-021, WS3-023].
6. **Fontakt is also a one-stop "data + calling + CRM" competitor in Estonia.** It sells its own CRM for €449–1,349/month plus setup at €110/h [V:WS3-005], and Estonian contact lists for €140–1,590 per list [V:WS3-003].
7. **G2 (foreign firms entering the Baltics) is contested.**
   - Fontakt sells Baltic market entry ("Export to Lithuania – your local sales team") [V:WS3-053].
   - Ripe Leads targets firms selling into the Baltics, DACH and Poland [V:WS3-049].
   - A Finnish HubSpot Diamond partner appears on HubSpot's Estonia listing [V:WS3-031].
8. **HubSpot partners lean towards larger clients.**
   - HubSpot's partner programme is aimed at agencies serving mid-market and enterprise clients [V:WS3-032].
   - The Latvian partner found is enterprise-focused, with about 90 staff [V:WS3-022].
   - The Lithuanian Gold partner works on Pro/Enterprise hubs [V:WS3-023].
   - So small-SME HubSpot work may be less well served (weak evidence: few partners checked).
9. **Grant-funded demand favours established providers.**
   - Estonia's EIS software grant requires a digital consultant [V:WS2-010].
   - Estonian roadmap-grant consultants must show at least 3 similar projects in the previous 4 years [V:WS2-011].
   - Latvian packages are sold through the EDIH catalogue [V:WS3-017].
   - For a new solo operator this is a barrier, not a gap.
10. **Biggest blind spots** (all UNKNOWN because the search budget ran out):
    - the Russian-language CRM ecosystem (Bitrix24/Kommo partners): UNKNOWN
    - Estonian and Latvian automation agencies and freelancers
    - Baltic data-provider prices
    - Zoho and Salesforce partners

    How to resolve each is in § 11.

---

## 2. CRM partners (official directories + local implementers)

### 2.1 Counts identified via search (lower bound; no directory totals were visible)
| Directory / type | EE | LV | LT |
|---|---|---|---|
| Pipedrive Service Partner Directory, HQ in country | Dominate Sales [V:WS3-012] | eXpanby [V:WS3-013] | Sonaro [V:WS3-014] |
| Other Pipedrive implementers / resellers seen | TechPeer [V:WS3-016]; Change Partners, Müügikoolitused, Võti Tulevikku [LEAD:WS3-054, WS3-055, WS3-056] | Squalio (packages in the grant catalogue) [V:WS3-017] | salescrm.lt [LEAD:WS3-039] |
| HubSpot Solutions Partners, HQ in country | Pivot Marketing OÜ [V:WS3-021] | IDEAPORT RIGA [V:WS3-022]; NOTRE [LEAD:WS3-033] | Deeps Solutions (Gold), Kontext Group [V:WS3-023] |
| Foreign HubSpot partners shown for the country | Sales Communications Finland (Diamond), Buldok Marketing (CEE) [V:WS3-031] | UNKNOWN (resolve: HubSpot marketplace, Latvia filter) | UNKNOWN (resolve: HubSpot marketplace, Lithuania filter) |
| Zoho partners | UNKNOWN (resolve: Zoho partner finder, country filter; search was refused by the budget) | UNKNOWN (same) | UNKNOWN (same) |
| SMB-focused Salesforce partners | UNKNOWN (resolve: AppExchange consultants, country filter) | UNKNOWN (same) | UNKNOWN (same) |
| Own-CRM vendors that also implement | Fontakt CRM [V:WS3-005] | grant-catalogue CRMs (Easy CRM, Meemo CRM+, others) [V:WS3-043, WS3-044] | Hanna CRM [LEAD:WS3-038]; WebXpert custom builds [V:WS3-025] |

Partners also sell across borders, so each country's real supply is larger than the HQ-based rows suggest:
- eXpanby (Riga) works in Estonian and Lithuanian [V:WS3-013].
- Dominate Sales (Tallinn) works in Latvian [V:WS3-012].
- Sonaro (Kaunas) works in Latvian [V:WS3-014].

### 2.2 Partner profiles: languages, packages, prices
| Partner | HQ | CRM | Languages | Published packages / prices | Source |
|---|---|---|---|---|---|
| Dominate Sales OÜ | EE (Tallinn) | Pipedrive | EN, ET, LV | Results-based implementation with a 60-day commitment; free first consultation; price not published | [V:WS3-012, WS3-015, WS3-029] |
| TechPeer | UNKNOWN | Pipedrive | ET page | Installation, customisation, optimisation; price not published in extract | [V:WS3-016] |
| eXpanby SIA | LV (Riga) | Pipedrive | EN, ET, LV, LT, RU, UK | Implementation, migration, API work, sales automation, training; industries include logistics & transport and manufacturing; price not published; Pipedrive Platinum Partner, the top tier [V:VL-035] (verifier note — see VL-013) | [V:WS3-013] [V:VL-013] |
| Squalio | UNKNOWN (sells in LV) | Pipedrive | LV (catalogue) | €2,990 / €3,990 / €4,490 / €4,990 for 12 months; €7,440 for 24 months; licences + 12 h implementation + 1 h/month support | [V:WS3-017, WS3-018] |
| IDEAPORT RIGA | LV (Riga) | HubSpot | UNKNOWN | About 90 staff; enterprise CRM; clients in the Nordics, Baltics, UK, NL, DE and CH; price not published | [V:WS3-022] |
| Pivot Marketing OÜ | EE | HubSpot | UNKNOWN | Marketing and sales automation; price not published | [V:WS3-021] |
| Sonaro | LT (Kaunas) | Pipedrive | EN, LV, LT | Pipedrive CRM services (B2B, customer support, SaaS); price not published | [V:WS3-014, WS3-041] |
| Deeps Solutions | LT | HubSpot (Gold) | UNKNOWN | Implementation, onboarding, automation, integrations, RevOps (Pro/Enterprise hubs); price not published | [V:WS3-023] |
| Fontakt (own CRM) | EE (Tallinn) | Fontakt CRM | ET, LV, LT, RU, EN and others | €449/month (5 users) or €1,349/month (10 users); setup €110/h; advanced development €150/h | [V:WS3-005] |

**By country**
- **Estonia:** Pipedrive's product hub is here [V:WS3-026], and partners have been active since 2017 [V:WS3-015]. No Estonian partner found publishes an implementation price. The only published Estonian CRM-service rate is Fontakt's €110/h, for its own CRM [V:WS3-005].
- **Latvia:** the most price-transparent market, because of the EDIH catalogue (§ 6).
  - Pipedrive has a Latvian entity [V:WS3-027].
  - eXpanby, HQ in Riga, is the most language-complete partner found anywhere in the Baltics [V:WS3-013].
- **Lithuania:** Pipedrive and HubSpot partners are both present [V:WS3-014, WS3-023], alongside a custom-CRM build market [V:WS3-025] and a local CRM product [LEAD:WS3-038].

---

## 3. Lead generation, appointment setting, outsourced SDR
| Player | HQ | Countries | Languages | Model | Published price | Minimum contract | Source |
|---|---|---|---|---|---|---|---|
| Fontakt OÜ | EE (Tallinn) | EE, LV, LT, FI, SE | ET, LV, LT, RU, EN, FI, SV, DE | Phone-led telemarketing, presales qualification, appointment setting; data lists; market entry for foreign firms | Per meaningful conversation, rate not published; Estonian data lists €140–1,590 | UNKNOWN | [V:WS3-001, WS3-002, WS3-003, WS3-004, WS3-053] |
| Ripe Leads | LT (Vilnius) | EE, LV, LT, PL, DACH, wider EU | LT, LV, ET, RU, EN, PL, CS, SK, DE | Done-for-you cold email + LinkedIn; claims first-party data for LT/LV/EE/PL/FI | €3,750 for month 1, then €2,850/month; tools and data included | None ("no lock-in"); 28 days' notice | [V:WS3-007, WS3-008, WS3-009, WS3-048] |
| Telemarket | LV | LV | UNKNOWN | Outbound telesales (est. 1998 per list) | UNKNOWN | UNKNOWN | [LEAD:WS3-010] |
| BPO Services | UNKNOWN | LV, LT | multilingual (unspecified) | Call-centre outsourcing | UNKNOWN | UNKNOWN | [LEAD:WS3-010, WS3-011] |
| Sonido | LV | LV | UNKNOWN | Contact centre, including appointment booking | UNKNOWN | UNKNOWN | [LEAD:WS3-010] |
| Telemarketing UAB | LT | LT | UNKNOWN | B2B/B2C outbound, appointment setting (est. 2004 per list) | UNKNOWN | UNKNOWN | [LEAD:WS3-011] |
| Credo Partners | LT | LT | UNKNOWN | Telemarketing, lead generation | UNKNOWN | UNKNOWN | [LEAD:WS3-011] |
| Six Eleven Global Services; SalesRoads | international | include LT / Baltic-targeting clients | UNKNOWN | Call centre / B2B prospecting | UNKNOWN | UNKNOWN | [LEAD:WS3-010, WS3-011] |

The LEAD rows come from Fontakt's own "Top 5" blog lists, which are competitor-authored and secondary. Whether these firms exist as described, whether they do B2B work, and what they charge is UNKNOWN (resolve: one query per firm).

**By country**
- **Estonia:** Fontakt is the incumbent, with HQ and about 100 staff in Tallinn [V:WS3-001]. Ripe Leads also offers Estonian [V:WS3-009]. No other Estonian outbound agency with published prices was found: UNKNOWN (resolve: ET queries "müügivihjete genereerimine hind", "B2B kohtumiste broneerimine teenus").
- **Latvia:** Fontakt and Ripe Leads both work in Latvian [V:WS3-002, WS3-009]. Fontakt's list also names Latvian telemarketing and contact-centre firms (Telemarket, BPO Services, Sonido) [LEAD:WS3-010]. Their prices are UNKNOWN (resolve: LV queries "līdu ģenerēšana cena", "telemārketings B2B cena").
- **Lithuania:** Ripe Leads is Lithuanian-native and publishes its prices [V:WS3-007, WS3-008]. Fontakt also works in Lithuanian [V:WS3-002]. Fontakt's list names Telemarketing UAB and Credo Partners [LEAD:WS3-011].
- **Pay-per-meeting (all three countries):** no published Baltic pay-per-meeting price found. UNKNOWN (resolve: quote requests; WS5 market prices).

---

## 4. AI/automation agencies and visible freelancers
| Provider | HQ | Offer | Published price | Source |
|---|---|---|---|---|
| aigentas.lt | LT | Process automation; integrations (HubSpot, Pipedrive, Make, n8n, Zapier, Paysera); AI agents and chatbots; maintenance; first results promised in 1–2 weeks | From €300; €450–1,200; €1,500–3,000+ | [V:WS3-024] |
| LabasClaw | LT | Implementation and maintenance of AI "employees"; Pipedrive integration | UNKNOWN | [V:WS3-034] |
| Retos | LT | AI training, implementation and solutions | UNKNOWN | [V:WS3-035] |
| WebXpert | LT | Custom CRM plus integrations (Rivilė, Sąskaita.lt, Paysera) | €9,500–15,000 basic; €15,000–25,000 mid-level | [V:WS3-025] |
| AInora; codeai.lt | LT | Publish CRM/automation content; their service offers are not established | UNKNOWN | [LEAD:WS3-036, WS3-037] |
| eXpanby | LV | Pipedrive sales automation; API/integration services | not published | [V:WS3-013] |
| Pivot Marketing OÜ | EE | Marketing and sales automation (HubSpot) | not published | [V:WS3-021] |
| Fontakt | EE | CRM development work | €110/h; advanced €150/h | [V:WS3-005] |

**By country**
- **Estonia:** (corrected — see RT-005) at least four Estonian agencies advertise AI or workflow automation: Growlinee, advertised from EUR 100 [V:RT-005]; WebSystems [V:RT-006]; ADLAB [V:RT-007]; Agentify [V:RT-008]. A search answer also gave about EUR 300 for a simple workflow and about EUR 800 for multi-system workflows (LEAD RT-009). Prices of the other three, and whether any covers LV or LT, are UNKNOWN (resolve: open the four service pages; the Make partner directory filtered to Estonia).
- **Latvia:** the EDIH catalogue's business-process sections list at least 45 providers [E:A-WS3-03]. Which of them sell workflow automation, and at what price, is UNKNOWN (resolve: read the dih.lv "Biznesa procesi" item pages; LV query "procesu automatizācija cena").
- **Lithuania:** the most visible low-end market. At least 3 AI-implementation sellers were verified [V:WS3-024, WS3-034, WS3-035], with entry prices from €300 [V:WS3-024].
- **Freelancers (aggregate only):** UNKNOWN (resolve: Upwork/Fiverr talent search filtered by country for "Pipedrive", "HubSpot", "n8n", "Make", "lead generation"; record counts only, no names; overlaps with WS2). Estonian Pipedrive searches also turned up individual consultants' personal sites; per the personal-data rule they are not named or counted.

---

## 5. (a) Does any player already cover all three Baltic states in EN + RU + the local language?
**For lead generation (C) and Pipedrive CRM work (A): yes, on the players' own claims. For automation (B): none identified, but B was barely searched in Estonia and Latvia, so B is UNKNOWN rather than "no".**

| Player | Component | EE | LV | LT | EN | RU | Local languages | Evidence |
|---|---|---|---|---|---|---|---|---|
| Fontakt | C (also A: own CRM; data) | yes (HQ) | yes | yes | yes | yes | ET, LV, LT | [V:WS3-001, WS3-002] |
| Ripe Leads | C | yes | yes | yes (HQ) | yes | yes | LT, LV, ET | [V:WS3-007, WS3-009] |
| eXpanby | A (Pipedrive) | Estonian offered | yes (HQ) | Lithuanian offered | yes | yes | ET, LV, LT (also UK) | [V:WS3-013] |

**What this means for the operator's claimed edge (EN + RU + LT, no Estonian or Latvian):**
- In C and A, the operator's language set is a strict subset of what these competitors claim, and they already sell across all three Baltic states [V:WS3-002, WS3-009, WS3-013]. "All-Baltic + trilingual" is therefore **not a differentiator on its own**.
- Not evidenced either way: whether the competitors deliver RU and LT at native quality at SME scale. Ripe Leads says its copy is native-quality and never machine-translated (vendor claim, same page as [V:WS3-009]).
- Remaining angles are hypotheses only, not findings:
  - One provider selling A + B + C together in RU/LT was not found. Fontakt covers C plus its own CRM [V:WS3-005]; eXpanby covers A plus Pipedrive automation [V:WS3-013]; aigentas.lt covers B [V:WS3-024].
  - Price point or delivery model (§ 7).

---

## 6. (b) Price bands per service per country (published prices only; excl. VAT)
| Service | EE | LV | LT | Cross-Baltic |
|---|---|---|---|---|
| CRM setup / implementation | Fontakt own-CRM setup €110/h [V:WS3-005]. Pipedrive/HubSpot partner prices not published [V:WS3-012, WS3-016, WS3-021]. Grant-funded projects: up to about €10,000 in total, with up to €2,500 of the aid usable for a consultant [E:A-WS3-04] | Pipedrive licences + 12 h implementation + 1 h/month support: €2,990–4,990 (12 months), €7,440 (24 months) [V:WS3-017, WS3-018]. Implied service value about €1,990, i.e. about €83/h [E:A-WS3-01]. Generic CRM implementation €5,000 [V:WS3-019]. Packaged CRM: €5,880 one-off, or €9,900 with implementation [V:WS3-045, WS3-043] | Custom CRM €9,500–15,000 (basic), €15,000–25,000 (mid-level) [V:WS3-025]. Partner prices for ready-made CRM not published [V:WS3-014, WS3-023]. Typical implementation 4–8 weeks (vendor claim) [V:WS3-057] | — |
| CRM support / retainer | Fontakt CRM €449–1,349/month including software, i.e. €89.80–134.90 per user-month [V:WS3-005] [E:A-WS3-06] | 1 h/month support bundled in catalogue packages [V:WS3-017]. Meemo CRM+ €2,376 for 2 years including updates and support [V:WS3-044] | UNKNOWN (resolve: quote requests to Sonaro / Deeps) | — |
| Automation project | Fontakt development work €110–150/h [V:WS3-005]. Estonian agencies advertise from EUR 100 [V:RT-005]; EUR 300 simple and EUR 800 multi-system are a LEAD RT-009 (corrected — see RT-005) | UNKNOWN (resolve: dih.lv business-process items) | €300 entry; €450–1,200; €1,500–3,000+ [V:WS3-024] | — |
| Lead-gen retainer | Fontakt: per meaningful conversation, rate not published [V:WS3-004] | As Estonia (Fontakt). Local telemarketing prices UNKNOWN | Ripe Leads €3,750 for month 1, then €2,850/month [V:WS3-008] | Ripe Leads covers all three countries: about €35,100 in year 1, averaging €2,925/month [E:A-WS3-02] |
| Pay-per-meeting | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN (resolve: quote requests; WS5) |
| Contact data | Fontakt Estonian lists €140–1,590 per department list [V:WS3-003] | UNKNOWN (Lursoft / Firmas.lv not searched) | UNKNOWN (Rekvizitai not searched) | Fontakt claims 668,000+ companies (vendor claim) [V:WS3-006] |

**Recency flag:** the dih.lv items show no visible publication date in the extracts. The Pipedrive packages use the plan names Essential / Advanced / Professional, so they may predate a plan rename and reflect pre-2025 prices. UNKNOWN (resolve: check the item pages for dates). (corrected — see VL-014: the 2026-10-03 re-check returned the same prices, still undated; both LIAA programmes behind the catalogue are closed [V:WS2-069][V:WS2-071], so these are historical list prices of a closed-grant regime, and the Pipedrive bundles include licences.)

---

## 7. (c) Gaps — with evidence and strength
| # | Gap or non-gap | Type | Evidence | Strength |
|---|---|---|---|---|
| G-1 | **Price transparency for SME CRM setup in Estonia and Lithuania:** the partners found publish no implementation prices. Fixed-price packages exist mainly in Latvia's grant catalogue | price point / delivery model | [V:WS3-012, WS3-014, WS3-016, WS3-021, WS3-023]; Latvian packages [V:WS3-017, WS3-019] | moderate (based on absence in extracts; few partners checked) |
| G-2 | **No published Baltic outbound tier below about €2,850/month:** only Ripe Leads publishes a price; Fontakt does not | price point | [V:WS3-008, WS3-004] | weak–moderate (absence-based; freelancer supply and demand at a lower price are UNKNOWN) |
| G-3 | **Small-SME HubSpot implementation:** the HubSpot partners found lean to mid-market/enterprise | segment | [V:WS3-032, WS3-022, WS3-023] | weak (Pipedrive partners do serve SMEs [V:WS3-012, WS3-013, WS3-014]) |
| G-4 | **Accounting firms as CRM/automation clients:** no competitor targeting them was found, but this was not searched | segment | — | UNKNOWN (resolve: queries "CRM buhalterinei įmonei", "CRM grāmatvedības birojam", "CRM raamatupidamisbüroole"; owner interviews) |
| G-5 | **Logistics / freight forwarding: NOT a gap.** eXpanby lists logistics & transport and manufacturing | segment | [V:WS3-013] | moderate |
| G-6 | **Language (operator's EN/RU/LT): NOT a gap.** Competitors claim EN + RU + ET/LV/LT. Gaps in vendor interfaces affect all implementers equally: HubSpot has no Estonian UI [V:WS0-003]; Zoho supports ET/LV/LT only partially [V:WS0-004]; Pipedrive's Lithuanian UI was not seen [LEAD:WS0-002]. A niche in Lithuanian-language Pipedrive enablement is only a hypothesis | language | [V:WS3-002, WS3-009, WS3-013] | moderate (language claims are self-declared) |
| G-7 | **Async / evening delivery:** Fontakt's core is phone calling, which needs business hours. Ripe Leads' email model is async and already Baltic-native. Dominate Sales sells consultation-led implementation. No competitor explicitly markets async delivery | delivery model | [V:WS3-002, WS3-004, WS3-007, WS3-015, WS3-029] | weak (inferred from service descriptions) |
| G-8 | **Grant-funded demand channel (a barrier, not a gap).** Latvia: CRM packages sold through the EDIH catalogue, which is tied to LIAA support [V:WS3-017, WS3-020]; EDIC test-before-invest up to €20,000 [V:WS3-046]; LIAA's process-digitalisation page is marked closed [LEAD:WS3-047]. Estonia: the EIS software grant requires a digital consultant [V:WS2-010], whose fees can be paid from at most €2,500 of aid [E:A-WS3-04]; roadmap-grant consultants need at least 3 similar projects in the previous 4 years [V:WS2-011] | delivery model / entry barrier | as cited | strong as a barrier for a new solo entrant |
| G-9 | **Low-end automation in Lithuania: NOT a gap.** Prices start at €300, and at least 3 providers were verified | price point | [V:WS3-024, WS3-034, WS3-035] | moderate |
| G-10 | **G2, foreign firms selling into the Baltics: NOT a gap.** Fontakt sells market entry; Ripe Leads targets the Baltics; a Finnish HubSpot Diamond partner is shown for Estonia | segment | [V:WS3-053, WS3-049, WS3-031]; Fontakt also has a page on the Scandinavian Chamber of Commerce in Estonia site [LEAD:WS3-052] | moderate |
| G-11 | **A + B + C bundle from one provider in RU/LT:** not found. Fontakt = C + own CRM; eXpanby = A + Pipedrive automation; aigentas.lt = B | delivery model | [V:WS3-005, WS3-013, WS3-024] | weak (limited search; Estonian and Latvian automation not searched) |

**By country**
- **Estonia:**
  - Evidenced openings: G-1, no published partner prices [V:WS3-012, WS3-016]; and G-11, no A + B + C provider found [V:WS3-005, WS3-013, WS3-024].
  - Not gaps: lead gen, where the Fontakt incumbent is phone-led [V:WS3-001], and Russian-language coverage [V:WS3-002].
  - Barrier: G-8, the EIS consultant rules [V:WS2-010, WS2-011].
- **Latvia:**
  - CRM is the most crowded and price-transparent cell. Openings are least evidenced here [V:WS3-017, WS3-018, WS3-019] [E:A-WS3-03].
  - Automation is UNKNOWN.
- **Lithuania:**
  - Automation is priced low and contested [V:WS3-024].
  - Ripe Leads covers cold email from Vilnius [V:WS3-007].
  - Openings are only G-1, CRM price transparency [V:WS3-014, WS3-023]; and possibly G-3, small-SME HubSpot [V:WS3-023, WS3-032].

---

## 8. Added beyond the brief

### 8.1 Substitutes: vendors' own onboarding and built-in AI
- **Pipedrive:**
  - Tallinn product hub with 300+ staff [V:WS3-026]; a Latvian entity [V:WS3-027].
  - Partner programme in which partners deliver the consulting, onboarding and implementation [LEAD:WS3-028].
  - Latvian UI added in 2022 [V:WS0-001].
  - Vendor-run paid onboarding (scope, price): UNKNOWN (resolve: pipedrive.com "onboarding services"). Built-in AI features and their pricing: UNKNOWN.
- **HubSpot:**
  - Partner programme aimed at mid-market and enterprise [V:WS3-032].
  - Latvian and Lithuanian UI, but no Estonian [V:WS0-003].
  - Onboarding fees: UNKNOWN (resolve: hubspot.com "onboarding fee Professional").
- **Zoho:** full Russian UI; only partial Estonian, Latvian and Lithuanian [V:WS0-004]. Implementation services: UNKNOWN.
- **Local CRM products that substitute for an implementation project:**
  - Fontakt CRM (EE) [V:WS3-005]
  - Meemo CRM+, Easy CRM and other catalogue CRMs (LV) [V:WS3-044, WS3-043]
  - Hanna CRM (LT) [LEAD:WS3-038]
  - custom builds (LT) [V:WS3-025]

### 8.2 Bitrix24 and Kommo (amoCRM) partners in EE / LV / LT — UNKNOWN
UNKNOWN (not searched; budget exhausted). This is the direct test of whether a Russian-language CRM market exists. Resolve with:
- UNKNOWN — RU queries: "Битрикс24 партнер Рига", "Битрикс24 внедрение Таллин", "amoCRM внедрение Латвия", "Kommo partner Lithuania"
- UNKNOWN — or the Bitrix24 partner directory filtered by country (quick manual check)

WS2 also covers the use of Russian-origin CRMs.

### 8.3 Baltic B2B data providers (competitors and enablers)
- Fontakt sells Estonian lists for €140–1,590 [V:WS3-003] and claims 668,000+ companies across 20+ countries [V:WS3-006].
- Ripe Leads claims first-party data for LT, LV, EE, PL and FI [V:WS3-048].
- Lursoft, Firmas.lv, Rekvizitai.lt, Inforegister.ee, Teatmik.ee, Creditinfo, Dealfront/Leadfeeder and Scorify: UNKNOWN (not searched). Resolve with one `allowed_domains` query per vendor, using "hinnakiri" / "cenrādis" / "kainos" / "pricing".

### 8.4 Accounting-software vendors and accounting firms (substitutes in the accounting-firm segment)
- **Latvia:** accounting/ERP vendors sit in the same grant catalogue as CRM sellers: a "Horizon" listing [LEAD:WS3-058], and Visma Enterprise among the provider filters [LEAD:WS3-042].
- **Lithuania:** automation sellers already integrate local accounting and payment tools. WebXpert integrates Rivilė, Sąskaita.lt and Paysera [V:WS3-025]; aigentas.lt integrates Paysera [V:WS3-024].
- **Estonia:** the EIS software grant requires applicants to use or implement e-invoicing [V:WS2-007]. That makes accounting/e-invoicing integration a grant-linked trigger for automation (cross-reference WS2).
- **Accounting firms already selling CRM/automation services:** UNKNOWN (resolve: local-language queries; interview question "Do you resell or implement any software for clients?").
- **Accounting-software vendors' own automation features** (Merit Aktiva, SmartAccounts, Directo, Rivilė, B1, Horizon, Jumis): UNKNOWN.

---

## 9. Conflicts between sources
- **Fontakt's language list:** the about-us extract lists seven languages (no German); the presales page lists eight, including German [V:WS3-002]. Both include EN, RU, ET, LV and LT, so the conclusion is unaffected. I trust the presales page as more specific.
- **Fontakt's age:** founded in 2007 [V:WS3-001] versus "20+ years of experience" [V:WS3-050]. I trust the founding year because it is specific; the "20+" is marketing rounding or the founders' prior experience.
- **Pipedrive partner tiers:** "Authorized, Gold, Platinum" (from a search answer) [LEAD:WS3-028] versus Dominate Sales described as an "Elite" partner [V:WS3-015]. Unresolved (the tiers may have been renamed); not decision-critical. (verifier note — see RT-003: Authorized, Gold and Platinum are confirmed on Pipedrive's programme page [V:RT-003] and eXpanby is Platinum [V:VL-035]; "Elite" does not appear on that page.)
- **Pipedrive in Lithuanian:** a Lithuanian-language search answer claimed Pipedrive offers Lithuanian-language support but gave no source URL, so it was not recorded. The lead analyst did not find Lithuanian in Pipedrive's UI language list [LEAD:WS0-002]. I trust neither until the Pipedrive support article is checked.
- **dih.lv "CRM sistēma":** there are two listings (items 206 and 339). The €5,000 price is confirmed for item 339 only [V:WS3-019]; item 206's price is UNKNOWN.

---

## 10. Search-language log
| Language | Example queries | What it found / didn't |
|---|---|---|
| EN (about two-thirds of queries) | "Fontakt B2B contacts database Baltic lead generation"; "Pipedrive Service Partner Directory Latvia Riga"; "HubSpot Solutions Partner Estonia Tallinn agency"; "Ripe Leads pricing …" | Found: Fontakt and Ripe Leads (prices, languages, HQ); the Pipedrive partners Dominate Sales, eXpanby, Sonaro; the HubSpot partners Pivot Marketing, IDEAPORT RIGA, Deeps Solutions, Kontext Group, plus foreign partners shown for Estonia. Not found: any directory totals |
| ET | "Fontakt hinnakiri telemarketing hind kontakt müügikõne"; "Pipedrive juurutamine partner Eesti hind koolitus" | Found: Fontakt price pages (CRM, app); Estonian Pipedrive providers (Dominate Sales, TechPeer, plus three LEAD sites). Not found: any Estonian implementation price |
| LV | "Pipedrive ieviešana Latvijā partneris cena apmācība"; "dih.lv katalogs CRM ieviešana risinājums cena" | Found: the dih.lv EDIH catalogue with priced CRM packages (the most useful local-language find); Pipedrive Latvia SIA; the LIAA/EDIC prerequisite |
| LT | "Pipedrive partneris Lietuvoje diegimas sertifikuotas partneris"; "HubSpot partneris Lietuvoje diegimas kaina agentūra"; "aigentas.lt kainos …" | Found: Lithuanian AI-automation micro-agencies with published prices; WebXpert's custom-CRM prices; Sonaro, LabasClaw, Retos, Hanna CRM. Lithuanian queries surfaced more small automation sellers than English ones did |
| RU | none run (budget exhausted before the RU block) | UNKNOWN: Russian-language competitors (Bitrix24/amoCRM partners; RU-language agencies in Riga, Tallinn and Narva). See § 11 |

Planned but refused by the budget: Zoho partner queries (two attempts), then everything in § 11.

---

## 11. UNKNOWNs, ranked by decision relevance (cheapest resolution)
1. UNKNOWN — **Russian-language CRM/automation ecosystem in Estonia and Latvia** (Bitrix24/Kommo partners, Russian-speaking agencies). This is the direct test of the RU edge. Resolve: the RU queries in the Bitrix24/Kommo subsection of section 8, or the Bitrix24 partner directory by country (quick manual check).
2. **Native-language delivery capacity and real SME-size prices of Fontakt, Ripe Leads and eXpanby.** Resolve: async mystery-shop requests for a quote on a one-country, one-language pilot, also asking how many native RU and LT speakers each team has.
3. UNKNOWN — **Estonian and Latvian automation agencies and freelancers** (offers, prices, counts). Resolve: the ET/LV queries in section 4; the Make partner directory and n8n experts list filtered by country (quick manual check); Upwork talent search by country (WS2).
4. **Zoho and SMB Salesforce partners per country.** Resolve: Zoho partner finder; AppExchange consultants with a country filter.
5. UNKNOWN — **Baltic B2B data-provider prices** (see the data-providers subsection of section 8).
6. UNKNOWN — **Vendor onboarding services and built-in AI pricing** for Pipedrive, HubSpot and Zoho (see the substitutes subsection of section 8).
7. **Pay-per-meeting prices in the Baltics.** Resolve: quote requests; WS5.
8. **The telemarketing firms in Fontakt's lists** (Telemarket, BPO Services, Sonido, Telemarketing UAB, Credo Partners): do they exist as described, do they do B2B, and what do they charge? Resolve: one query each.
9. **Prices of Estonian and Lithuanian CRM partners** (Dominate Sales, TechPeer, Sonaro, Deeps Solutions). Resolve: a quote request or a check of their pricing pages.
10. UNKNOWN — **Accounting firms selling CRM/automation, and accounting-software automation features** (see the accounting subsection of section 8).
11. **Listing dates of the dih.lv packages** (how recent the prices are).

---

## 12. Synthesis inputs
Competition intensity score: 1–5, where 5 = least competition (rubric in [E:A-WS3-05]). Scores of 3 are provisional, meaning not adequately searched.

| Country | Component | Competition score | Rationale (source ids) | Published price band | Trilingual all-Baltic player present? |
|---|---|---|---|---|---|
| EE | A — CRM setup | 2 [E:A-WS3-05] | Pipedrive hub in Tallinn [V:WS3-026]; Estonian Pipedrive providers [V:WS3-012, WS3-016]; HubSpot partners including foreign ones [V:WS3-021, WS3-031]; Fontakt CRM [V:WS3-005]; eXpanby works in Estonian [V:WS3-013] | €110/h (Fontakt) [V:WS3-005]; partner prices not published | Yes: eXpanby (claimed) [V:WS3-013]; Fontakt [V:WS3-002] |
| EE | B — automation | 3 [E:A-WS3-05] (corrected — see RT-005: no longer "not searched"; four agencies found, none verified as all-Baltic EN + RU + local, so the rubric for 2 is not met) | Pivot Marketing [V:WS3-021], Fontakt's development work [V:WS3-005] and four agencies [V:RT-005] [V:RT-006] [V:RT-007] [V:RT-008] | €110–150/h (Fontakt development) [V:WS3-005]; packages UNKNOWN | UNKNOWN |
| EE | C — lead gen | 2 [E:A-WS3-05] | Fontakt HQ, about 100 staff [V:WS3-001]; Ripe Leads works in Estonian [V:WS3-009] | €2,850–3,750/month (Ripe Leads) [V:WS3-008]; Fontakt per conversation, not published [V:WS3-004]; lists €140–1,590 [V:WS3-003] | Yes: Fontakt, Ripe Leads [V:WS3-002, WS3-009] |
| LV | A — CRM setup | 2 [E:A-WS3-05] | eXpanby HQ (six languages) [V:WS3-013]; Squalio packages [V:WS3-017]; IDEAPORT RIGA [V:WS3-022]; at least 45 catalogue providers [E:A-WS3-03]; Pipedrive Latvian entity [V:WS3-027] | €2,990–7,440 including licences [V:WS3-017, WS3-018]; €5,000–9,900 [V:WS3-019, WS3-043]; about €83/h implied [E:A-WS3-01] | Yes: eXpanby [V:WS3-013] |
| LV | B — automation | 3, provisional [E:A-WS3-05] | eXpanby offers sales automation and API work [V:WS3-013]; the catalogue suggests many providers [E:A-WS3-03]; agencies not searched | UNKNOWN | UNKNOWN |
| LV | C — lead gen | 2 [E:A-WS3-05] | Fontakt and Ripe Leads cover Latvia [V:WS3-002, WS3-009]; local telemarketing firms [LEAD:WS3-010] | as Estonia [V:WS3-008] | Yes [V:WS3-002, WS3-009] |
| LT | A — CRM setup | 2 [E:A-WS3-05] | Sonaro [V:WS3-014]; Deeps Solutions, Kontext Group [V:WS3-023]; WebXpert [V:WS3-025]; eXpanby works in Lithuanian [V:WS3-013] | Custom €9,500–25,000 [V:WS3-025]; partner prices not published | Yes: eXpanby (claimed) [V:WS3-013] |
| LT | B — automation | 2 [E:A-WS3-05] | aigentas.lt, LabasClaw, Retos [V:WS3-024, WS3-034, WS3-035] | €300; €450–1,200; €1,500–3,000+ [V:WS3-024] | None identified (UNKNOWN) |
| LT | C — lead gen | 2, closest to 1 for cold email [E:A-WS3-05] | Ripe Leads HQ in Vilnius, Lithuanian-native, public flat pricing [V:WS3-007, WS3-008]; Fontakt works in Lithuanian [V:WS3-002] | €2,850–3,750/month [V:WS3-008] | Yes: Ripe Leads, Fontakt [V:WS3-009, WS3-002] |
| All | G2 — foreign sellers into the Baltics | 2 [E:A-WS3-05] | Fontakt market entry [V:WS3-053]; Ripe Leads [V:WS3-049]; Finnish HubSpot Diamond partner [V:WS3-031] | as above | Yes [V:WS3-002, WS3-009] |

**Bundles:** no single provider was found selling A + B + C (G-11). For A + B, eXpanby's Pipedrive automation [V:WS3-013] and aigentas.lt's CRM integrations [V:WS3-024] are the closest substitutes.
