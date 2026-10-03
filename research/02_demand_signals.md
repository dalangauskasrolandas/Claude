# 02 — Digital maturity & demand signals (WS2)

**Scope:** whether and how much Baltic B2B buyers want CRM setup (A), AI/workflow automation (B) and outbound lead generation (C). Covers technology-use statistics, hiring and freelance demand, search trends, grants and vouchers (critical), and public procurement, for Estonia (EE), Latvia (LV) and Lithuania (LT).

**Legend:** `[V:WS2-xxx]` = VERIFIED (see `_work/sources_WS2.csv`; `[V:WS3-xxx]` points to WS3's fragment) · `[E:A-WS2-xx]` = ESTIMATE (see `_work/assumptions_WS2.md`) · `UNKNOWN (resolve: …)` = not found. "LEAD WS2-xxx" = seen but not usable as VERIFIED.

**Method note:** Evidence gathered via web-search extracts on 2026-10-03; direct page fetching was blocked in this environment.

> **Coverage warning — read first.** All six workstream agents share one WebSearch budget for the session, and it ran out after roughly three dozen WS2 queries. Direct access was also blocked: OECD returned 403 here, and the lead had already found Eurostat, all three statistics offices, the job sites, the procurement portals, Upwork, LinkedIn, Google Trends and DBnomics blocked. As a result:
> - **Estonian grants** were researched in depth from primary sources (EIS pages and Riigi Teataja).
> - **Latvian grants** were researched only partly (LIAA, Ministry of Economics, EU-funds portal).
> - **Lithuanian grants** were not researched.
> - **Not researched at all:** CRM/ERP/AI usage statistics (except one Estonian AI figure), job postings, freelance platforms, search trends, procurement, and most "added beyond the brief" items. They are marked UNKNOWN, with exact resolution protocols in § 11.
>
> This is a **research gap, not negative evidence**. Closing it needs a second WS2 search pass. The lead can ask the user to raise `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION`.

---

## 1. Key findings

1. **EE AI-adoption grant ran out of money the day it opened (prior lead confirmed).**
   - Terms: EUR 20,000 unit price, 20% self-financing, EUR 2.0M budget, prior-year revenue ≥ EUR 200,000 [V:WS2-001].
   - EIS opened it on 24.08.2026 and closed it at 16:00 the same day because requests exceeded the budget [V:WS2-001][V:WS2-003]. Invest in Estonia says it was "fully allocated on the morning" it opened [V:WS2-002].
   - Capacity is about 100 firms (2,000,000 / 20,000) [E:A-WS2-01].
   - This is the strongest component-B demand signal in WS2. But it shows demand for *subsidised* AI projects among firms with at least EUR 200k revenue. It does not show willingness to pay without a subsidy.
2. **EE digitalisation-roadmap grant has been closed since 24.07.2026 09:00 (prior lead confirmed).**
   - Terms: max EUR 10,000, revenue ≥ EUR 200,000 (two-year average) [V:WS2-004].
   - Next call: UNKNOWN (resolve: EIS planned-calls information or an EIS client manager).
3. **Two EE grants that fit components A and B are open now.**
   - **(a) RTE software implementation & integration grant** [V:WS2-007][V:WS2-009][V:WS2-010]:
     - Open on a rolling basis: EUR 2,000–5,000 per company at 50%, from a EUR 1.0M budget.
     - Client conditions: revenue ≥ EUR 50,000, and the client must adopt e-invoicing.
     - A "digital advisor" is **mandatory**, and advisor fees may take up to 50% of the aid.
   - **(b) Roadmap follow-on advisory & development grant** [V:WS2-005]:
     - Max EUR 35,000, with 30–50% self-financing.
     - Revenue ≥ EUR 200,000.
4. **The operator cannot be the grant-paid advisor at launch.**
   - The paid "digital advisor" must have at least 3 similar projects in the preceding 4 years [V:WS2-009]. Roadmap consultants face the same test [V:WS2-011].
   - A new FIE without consulting references therefore probably cannot be paid from these grants at the start. This is an inference from the rule text; whether in-house experience counts is UNKNOWN.
   - Once eligible, the RTE grant could cover up to about EUR 2,500 of advisor fees per client (about a EUR 5,000 invoice) [E:A-WS2-03].
5. **Most other EE digital grants are closed (as of 2026-10-03):**
   - RTE business-process automation, max EUR 150,000 [V:WS2-006].
   - eCMR integration for logistics, max EUR 15,000 at 90% aid [V:WS2-008].
   - Digital transformation, up to 70% support [V:WS2-013].
   - SME development programme, max EUR 300,000 [V:WS2-016].
   - The next-call date is UNKNOWN for every one of them.
6. **EE AI use rose from 14% (2024) to 22% (2025)** of companies using at least one AI technology [V:WS2-018].
   - This is Statistics Estonia data relayed by EIS (a secondary relay); size class and population are not visible.
   - The stat.ee release "34% of enterprises use AI" could not be checked: UNKNOWN (§ 2).
7. **In Latvia, LIAA digitalisation grants route purchases through the EDIC catalogue.**
   - New programme: EUR 27,613,228 for at least 1,750 firms, with grants up to EUR 10,000, from Q3 2025 [V:WS2-021].
   - AI strand: up to EUR 200,000. Aid rates are 50% (small), 40% (medium) and 30% (mid-caps) [V:WS2-022].
   - An EDIC (dih.lv) maturity test is required before applying. The catalogue already lists CRM packages, e.g. a Pipedrive licence with 12 h of implementation for EUR 2,990 excl. VAT [V:WS3-020][V:WS3-017].
   - The earlier EUR 37.5M programme (100% aid for micro/small firms if the project is ≤ EUR 5,000) ran until 31.03.2026 [V:WS2-019][V:WS2-020].
   - UNKNOWN: status as of Oct 2026, minimum revenue, and the rules for getting listed as a provider.
8. **Lithuania: nothing verified** on grants, EDIHs or usage statistics — UNKNOWN. The search budget ran out before any Lithuanian query was executed.
9. **Also UNKNOWN for all three countries:** CRM and ERP adoption, job-posting counts and salaries, freelance volumes, Google Trends and procurement counts. Exact protocols are in § 11.

---

## 2. Enterprise technology use (CRM, AI, ERP)

| Indicator (latest year) | EE | LV | LT | Dataset to use (codes to verify) |
|---|---|---|---|---|
| Enterprises using ≥ 1 AI technology | 22% (2025); 14% (2024) [V:WS2-018] — size class/population not visible (secondary relay of Statistics Estonia) | UNKNOWN | UNKNOWN | Eurostat AI-use table by size class (candidate `isoc_eb_ai`); national ICT-usage-in-enterprises releases |
| AI use by size class (10–49 / 50–249) | UNKNOWN | UNKNOWN | UNKNOWN | as above, size-class breakdown |
| Enterprises using CRM software | UNKNOWN | UNKNOWN | UNKNOWN | Eurostat "integration of internal processes" (ERP/CRM) domain (candidate `isoc_eb_iip`); latest survey year to confirm |
| CRM by size class | UNKNOWN | UNKNOWN | UNKNOWN | as above |
| Enterprises using ERP software | UNKNOWN | UNKNOWN | UNKNOWN | as above |
| ERP by size class | UNKNOWN | UNKNOWN | UNKNOWN | as above |

**Re-verification of the prior lead "about 22% of EE enterprises used AI (2025)":** consistent with [V:WS2-018], but only through EIS's relay of Statistics Estonia. The primary stat.ee table was not opened.

**The "65% of people and 34% of enterprises use AI" stat.ee release:** UNKNOWN. Its year and definitions could not be checked. Hypotheses to test, none verified:
- a different survey year (e.g., 2026);
- a broader AI definition (any AI tool, including generative AI, vs the Eurostat list of AI technologies);
- a different population (all enterprises vs enterprises with 10 or more persons employed).

Resolution: open the stat.ee release and note the reference year, population and AI definition. Then compare with the Eurostat AI-use table for EE in the same year.

---

## 3. Job postings as demand signals

Every site in scope was blocked for direct fetching. The search budget ran out before any indexed-postings query was run. **No snapshot counts or salary ranges were obtained.**

| Site | Country | Roles in scope | Count / salary range |
|---|---|---|---|
| cv.ee | EE | CRM admin, sales ops/RevOps, SDR/BDR/lead gen, automation (n8n/Make/Zapier), Pipedrive/HubSpot | UNKNOWN |
| cvkeskus.ee | EE | same | UNKNOWN |
| cv.lv | LV | same | UNKNOWN |
| cvmarket.lv | LV | same | UNKNOWN |
| cvbankas.lt | LT | same | UNKNOWN |
| cvonline.lt | LT | same | UNKNOWN |
| LinkedIn Jobs | EE/LV/LT | same | UNKNOWN |

The manual-check protocol is in § 11, item U3. Interpretation note for synthesis: in-house hiring for these roles is a **substitute** for outsourced services as well as a demand signal. Record both counts and seniority.

---

## 4. Freelance platforms

Upwork, Fiverr, Malt, Freelancer and the local classifieds (okidoki.ee, ss.lv, skelbiu.lt) were not researched. Project volumes and budgets mentioning EE/LV/LT or the Baltic languages together with CRM, lead generation or automation are **UNKNOWN** (protocol: § 11, item U4).

The prior lead "Upwork AI-automation median about $29.50/h (May 2026, Upwatcher)" belongs to WS5. WS2 did not re-verify it.

---

## 5. Grants and vouchers (critical)

The structured version of this section is in `_work/data/WS2_grants.csv`.

### 5.1 Estonia — EIS (Estonian Business and Innovation Agency)

| # | Programme | Status on 2026-10-03 / next call | Amount & co-funding | Eligibility incl. minimum revenue | External consultants / providers payable? | Fit |
|---|---|---|---|---|---|---|
| EE-1 | Grant for adopting AI (Tehisaru kasutuselevõtmise toetus) | **Closed**: opened and closed 24.08.2026, 16:00, budget exhausted [V:WS2-001][V:WS2-003]. Next call UNKNOWN | EUR 20,000 unit price; 20% self-financing; budget EUR 2.0M [V:WS2-001]; implied project about EUR 25,000 [E:A-WS2-02] | Estonian commercial register; **prior-FY revenue ≥ EUR 200,000**; once per company [V:WS2-001]; project ≤ 9 months with a measurable result [V:WS2-002] | UNKNOWN: unit-price grant, cost lines not itemised in the extract (resolve: measure conditions PDF) | B |
| EE-2 | Digitalisation roadmap grant (Digitaliseerimise teekaardi toetus) | **Closed** since 24.07.2026, 09:00 [V:WS2-004]. Next call UNKNOWN; has reopened in the past (LEAD WS2-032) | max EUR 10,000; budget EUR 2.5M; 30–50% self-financing [V:WS2-004]. 2024 terms: 50% support in Tallinn/Harju/Tartu, 70% elsewhere [V:WS2-012] | **avg revenue ≥ EUR 200,000** over two prior FYs [V:WS2-004] | **Yes**: the roadmap is made with external consultants, each with ≥ 3 similar projects in the previous 4 years; team ≥ 2 years' experience [V:WS2-011] | A/B (diagnosis before purchases) |
| EE-3 | Advisory & development activities following the roadmap | **Open**, rolling [V:WS2-005] | max EUR 35,000; 30–50% self-financing; budget EUR 2.5M [V:WS2-005]; the cap binds at projects of EUR 50,000–70,000 [E:A-WS2-04] | all sizes; **avg revenue ≥ EUR 200,000**; gambling, rental/leasing and temp-agency activities excluded [V:WS2-005]; needs a completed roadmap (implied by the measure) | **Yes**: "advisory services and development activities" on roadmap bottlenecks (digitalisation, automation, cybersecurity) [V:WS2-005]. Consultant qualification rule for this measure: UNKNOWN | A/B |
| EE-4 | RTE software implementation & integration (RTE – tarkvara kasutusele võtmise või liidestamise toetus) | **Open**, rolling since about March 2026 until the EUR 1.0M budget is used [V:WS2-007][V:WS2-010] | EUR 2,000–5,000 per company; 50% self-financing; paid as a fixed amount [V:WS2-007][V:WS2-010]; implied project EUR 4,000–10,000 [E:A-WS2-03] | **avg revenue ≥ EUR 50,000** over two FYs; a staff member completes the free "Ettevõtte digitaliseerimise koolitus" course; client uses or adopts e-invoicing; de minimis [V:WS2-007] | **Yes, and mandatory**: a digital advisor; advisor fees ≤ 50% of aid; advisor needs ≥ 3 similar projects in the preceding 4 years; project ≤ 18 months; advisor fees may start up to 3 months before the application [V:WS2-009]. Software purchase/licence and integration costs also eligible [V:WS2-007] | **A** (CRM adoption), **B** (integration) |
| EE-5 | RTE business-process automation & data exchange | **Closed** [V:WS2-006]. Next call UNKNOWN | max EUR 150,000; 50% self-financing; budget EUR 1.5M [V:WS2-006] | UNKNOWN | UNKNOWN | B |
| EE-6 | eCMR (e-consignment note) integration | **Closed** [V:WS2-008]; eligibility had earlier been widened to all companies (LEAD WS2-031) | max EUR 15,000; 10% self-financing; budget EUR 4.7M [V:WS2-008] | firms for which e-CMR integration makes sense; de minimis ≤ EUR 300,000; no revenue floor in the extract [V:WS2-008] | Development work for e-CMR integration is eligible; provider type not specified [V:WS2-008] | B (logistics/forwarders) |
| EE-7 | Digital transformation (Ettevõtete digipöörde toetus) | **Closed** [V:WS2-013] | up to 70% support (de minimis) [V:WS2-013]; 2024 terms: follow-on support up to EUR 300,000 [V:WS2-012] | **avg turnover ≥ EUR 200,000** [V:WS2-013]; two rounds (manufacturing & mining; other sectors) | **Yes**: digital technologies and robots, with consultancy [V:WS2-013] | B (manufacturing) |
| EE-8 | SME development programme | **Closed** [V:WS2-016] | max EUR 300,000; ≥ 55% self-financing [V:WS2-016] | outside Harju County and Tartu city; **revenue ≥ EUR 200,000**; ≥ 2 full-time staff [V:WS2-016] | **Yes**: purchased services and marketing activities eligible [V:WS2-016] (the only EE measure seen where marketing costs, and so possibly lead generation, are eligible) | A/B/C |
| EE-9 | Digimentorlus (tourism & creative sectors only) | **Open** for 2026–2027 until the budget is used [V:WS2-015] | 30–100 mentor hours; client pays 15–20% (EUR 661.50–882 for 30 h); 30 h = EUR 4,460, i.e. about EUR 147–149/h [V:WS2-015][E:A-WS2-05] | **avg revenue ≥ EUR 50,000** (two FYs) or ≥ EUR 100,000 (prior FY) [V:WS2-015] | No: an EIS-provided mentor (how mentors are selected is UNKNOWN) | outside target sectors |
| EE-10 | Tark tellija (smart-buyer toolkit) | Available; not a grant [V:WS2-017] | free | — | n/a (videos, contract templates for buying IT) | A/B (buyer education) |

Context:
- In 2026 the ministry put EUR 10M into the RTE (real-time economy) digitalisation measures. Grants run from a few thousand euros to EUR 150,000 per project, for business-software adoption, process automation and real-time data-exchange software [V:WS2-014].
- ERR News reported an EUR 85M national AI-uptake plan for the public and private sectors (LEAD WS2-033; split not seen).

### 5.2 Latvia — LIAA / Ministry of Economics

| # | Programme | Status on 2026-10-03 / next call | Amount & co-funding | Eligibility incl. minimum revenue | External consultants / providers payable? | Fit |
|---|---|---|---|---|---|---|
| LV-1 | Support for the digitisation of business processes (EUR 37.5M programme) | Stated end date 31.03.2026, or earlier if funds run out [V:WS2-019], so **closed** by its own terms (inference) | up to EUR 100,000; micro/small firms **100%** if the total project is ≤ EUR 5,000; otherwise 30–60% aid; ≥ 200 recipients by 30.06.2026 [V:WS2-020] | enterprises, associations, foundations, research organisations; an **EDIC digital-maturity test and roadmap first**, then apply via business.gov.lv [V:WS2-019]. Minimum revenue: UNKNOWN | **Yes, via the EDIC catalogue.** It lists CRM packages: Pipedrive licence + 12 h implementation EUR 2,990; Pipedrive bundles up to EUR 7,440; a generic CRM implementation package EUR 5,000 (all excl. VAT) [V:WS3-017][V:WS3-018][V:WS3-019]. Whether these entries belong to LV-1 or LV-2: UNKNOWN | A/B |
| LV-2 | New business-process digitalisation programme | Available from Q3 2025 [V:WS2-021]. Undated articles: EUR 5.4M reserved and funding still available [V:WS2-023]. "Likely accepting until at least the end of this year" (LEAD WS2-027; year unknown). **Current status UNKNOWN** | total EUR 27,613,228; ≥ 1,750 firms; grants ≤ EUR 10,000 [V:WS2-021]. ≤ EUR 10,000 for buying digital solutions and maturity assessment, ≤ EUR 200,000 for AI solutions; aid 50% small / 40% medium / 30% small mid-caps & mid-caps [V:WS2-022] | micro/small/medium firms (incl. farms, cooperatives), small mid-caps, mid-caps, associations uniting ≥ 3 firms [V:WS2-022]. Minimum revenue: UNKNOWN | **Yes for purchased digital solutions** [V:WS2-022]. Consultancy-only projects: UNKNOWN | A/B |
| LV-3 | Innovation vouchers (Inovāciju vaučeru atbalsts) | UNKNOWN (LEAD WS2-030) | UNKNOWN | UNKNOWN | UNKNOWN | ? |
| LV-4 | Norway Grants business & innovation development | UNKNOWN (LEAD WS2-029; title gives "more than EUR 14 million", terms not seen) | UNKNOWN | UNKNOWN | UNKNOWN | ? |

Latvian demand signals (all undated):
- 241 project applications received for process-digitalisation support [V:WS2-025].
- "Most of the funding already reserved" [V:WS2-026].
- EUR 4.28M of reserved funds earmarked for AI projects [V:WS2-024].
- If the EUR 5.4M figure refers to LV-2, only about 19.6% had been reserved at that point [E:A-WS2-07].

### 5.3 Lithuania — Innovation Agency (Inovacijų agentūra) and others

**UNKNOWN for every field.** Not researched because the search budget ran out. Resolution: § 11, item U1. Check these, without assuming any measure exists:
- inovacijuagentura.lt open and planned calls ("kvietimai") on digitalisation, AI adoption and process digitalisation for SMEs;
- the national EU-investment portal (esinvesticijos.lt) for open calls;
- the economy ministry (eimin.lrv.lt) for digitalisation measures;
- INVEGA for digitalisation loans or guarantees.

For each, record status and next call, amount and rate, minimum revenue, and whether consultants or providers are eligible costs.

### 5.4 European Digital Innovation Hubs (EDIHs)

| Country | What is known | Status |
|---|---|---|
| EE | Not researched | UNKNOWN (resolve: EU EDIH network catalogue for Estonia; each hub's service list and its provider-registration rules) |
| LV | The Latvian EDIC is developed by the Latvia IT Cluster at dih.lv. An EDIC digital-maturity test and roadmap are a precondition for LIAA digitalisation support, and dih.lv hosts the solutions catalogue [V:WS3-020][V:WS2-019] | Can a foreign (Estonian FIE) provider list in the catalogue? UNKNOWN (WS6 owns the provider-registration question) |
| LT | Not researched | UNKNOWN |

### 5.5 EU / Interreg / EEA programmes

Interreg (Central Baltic; Estonia–Latvia; Latvia–Lithuania), Digital Europe cascade funding and other EU calls for SME digitalisation were not researched: **UNKNOWN**. The only lead is the Latvian Norway Grants programme (LEAD WS2-029).

### 5.6 What the grant rules imply for this operator

These are inferences from the rule texts. Each rests on the cited sources.

1. **Revenue floors decide who can get grant money in EE.**
   - Five of the EE digital measures set the floor at EUR 200,000 revenue: AI, roadmap, advisory & development, digital transformation and the SME programme [V:WS2-001][V:WS2-004][V:WS2-005][V:WS2-013][V:WS2-016].
   - The only low-floor digital grant seen is the RTE software grant, at EUR 50,000 [V:WS2-007].
   - WS1's enterprise counts should be cut at these floors when grant-backed demand is sized. Revenue-band counts are UNKNOWN in WS2.
2. **An experience floor applies to paid advisors in EE.** A provider needs at least 3 similar projects in 4 years [V:WS2-009][V:WS2-011]. That favours established Pipedrive/HubSpot partners (see WS3) over a newcomer. A plausible route is to do a few unsubsidised projects first; whether that works is untested.
3. **Grant windows can close within hours.** Example: the EE AI grant, first-come-first-served [V:WS2-001][V:WS2-003]. Clients need applications ready at opening, which usually happens in business hours. That is a friction for an operator who works in the evenings.
4. **Latvia buys through a catalogue.** LIAA-funded purchases go through EDIC-catalogue offers, and CRM packages are already listed by established resellers [V:WS3-017][V:WS3-019][V:WS3-020]. Price points there run from EUR 2,990 to 7,440 [V:WS3-017][V:WS3-018]. They anchor what grant-funded LV buyers expect to pay for licence + implementation bundles.
5. **No open grant seen funds outbound lead generation.** The closed EE SME programme's "marketing activities" is the only near-match [V:WS2-016]. Component C has no evidenced subsidy channel in EE or LV; LT is UNKNOWN.

---

## 6. Search trends

Google Trends (trends.google.com) was blocked, and no published trend evidence was found within the search budget. The five-year direction per country is **UNKNOWN** (protocol: § 11, item U5).

---

## 7. Public procurement

Not researched. riigihanked.riik.ee, the Latvian EIS/IUB and Lithuania's CVP IS were all blocked, and no search budget was left for TED. Count and typical value of small tenders for CRM implementation, sales automation or lead generation in the last 24 months: **UNKNOWN** for EE, LV and LT.

Resolution parameters (§ 11, item U6). The CPV codes below are candidates and must be verified against the CPV 2008 list before use:
- **Software:** `48445000-0` (CRM software package), `48451000-4` (ERP software package), `72263000-6` (software implementation), `72265000-0` (software configuration), `72266000-7` (software consultancy).
- **Marketing / consultancy:** `79342000-3` (marketing services), `79342100-4` (direct marketing), `79410000-1` (business and management consultancy).

---

## 8. Added beyond the brief

### 8.1 E-invoicing and e-reporting mandates

- **EE:** the policy push is visible in the grant conditions. The RTE software grant requires the applicant to already use, or adopt, e-invoicing [V:WS2-007][V:WS2-010]. The EUR 10M RTE package funds real-time data-exchange software [V:WS2-014]. For logistics, eCMR integration was subsidised at 90% [V:WS2-008]. The legal B2B e-invoicing rule and its dates are UNKNOWN (resolve: riigiteataja.ee, Accounting Act (Raamatupidamise seadus) e-invoice provisions).
- **LV:** the B2B e-invoicing mandate and any postponement: UNKNOWN (resolve: likumi.lv, Accounting Law (Grāmatvedības likums) transitional provisions on structured e-invoices; VID guidance).
- **LT:** i.SAF and e-invoicing plans: UNKNOWN (resolve: vmi.lt pages on i.SAF and e-invoicing).
- **EU ViDA:** timeline UNKNOWN (resolve: EUR-Lex "VAT in the Digital Age" directive; record the adoption date and when the digital reporting requirements apply).
- **Relevance for accounting firms:** mandates create one-off integration work, which is component B. It cannot be quantified until the dates above are verified.

### 8.2 Local accounting/ERP ecosystems

Market shares were not researched: UNKNOWN for EE (Merit Aktiva, Directo, SmartAccounts), LV (Horizon, Tildes Jumis) and LT (Rivilė, B1, Centas, Finvalda, Agnum). Integration-demand signals:
- EE: the RTE grant explicitly funds "linking of existing software" [V:WS2-007].
- LT: a CRM builder advertises integrations with Rivilė, Saskaita.lt and Paysera [V:WS3-025].

Resolution: each vendor's published client count and API/marketplace pages (§ 11, item U8).

### 8.3 Russian-origin CRM (Bitrix24, amoCRM/Kommo)

Use among Baltic SMEs, migration signals and official advice: UNKNOWN. WS3 owns the partner counts. Resolution: § 11, item U9.

### 8.4 SME digitalisation barriers

EIB Investment Survey 2025 country overviews and the Digital Decade 2025 country reports (share of SMEs with at least basic digital intensity) were not reached: UNKNOWN for EE, LV and LT.

Indirect EE signal (interpretation): EIS pairs money with a mandatory advisor, a compulsory free course and a buyer toolkit [V:WS2-007][V:WS2-009][V:WS2-017]. So the agency treats know-how, not only money, as a barrier. The AI grant's same-day exhaustion [V:WS2-001] suggests that co-funding is a binding constraint for at least the ~55–100 firms it could fund [E:A-WS2-01].

---

## 9. Conflicts between sources

| # | Conflict | Values | Which to trust and why |
|---|---|---|---|
| C1 | EE roadmap grant maximum | EUR 10,000 [V:WS2-004][V:WS2-012] vs EUR 35,000, which one extract attached to the roadmap page | **EUR 10,000.** Two official pages (2024 and 2026) agree. The EUR 35,000 belongs to the follow-on advisory & development measure [V:WS2-005] and was a search-extract mix-up |
| C2 | EE AI grant closure timing | "fully allocated on the morning it opened" [V:WS2-002] vs "closed at 16:00" [V:WS2-001][V:WS2-003] | Consistent: same-day closure, formally at 16:00. Trust the EIS page for the timestamp |
| C3 | EE AI grant budget | EUR 2.0M total [V:WS2-001] vs EUR 1.1M planned for the 2026 round [V:WS2-003] | Both hold. ERR says EUR 2.0M covers 2026–2027 and EIS asked to bring it forward. Capacity is 55 vs 100 firms [E:A-WS2-01] |
| C4 | Digimentorlus price base | EUR 4,460 total vs co-financing figures that imply EUR 4,410 [V:WS2-015][E:A-WS2-05] | Unresolved EUR 50 difference (possibly a fixed fee). Immaterial |
| C5 | LV new-programme grant size | grants capped at EUR 10,000 [V:WS2-021] vs AI strand up to EUR 200,000 [V:WS2-022]; average budget about EUR 15,779 per targeted firm [E:A-WS2-06] | Probably two strands of one programme. Not confirmed |
| C6 | LV funding availability | "most of the funding already reserved" [V:WS2-026] vs "EUR 5.4M reserved, funding still available" [V:WS2-023] | Both undated; probably different programmes (LV-1 vs LV-2) or dates. Current status UNKNOWN |
| C7 | EE AI-use share | 22% in 2025 [V:WS2-018] vs a stat.ee release titled with "34% of enterprises" (per the lead's note) | UNKNOWN. Trust 22% as the Eurostat-style indicator until the 34% release's year and definition are checked |

---

## 10. Search-language log

| Language | Example queries | Found / not found |
|---|---|---|
| ET | "EIS tehisintellekti kasutuselevõtu toetus 2026 taotlusvoor"; "digitaliseerimise teekaardi toetus suletud"; "RTE tarkvara … digitaalse nõustaja nõuded"; "ettevõtete digipöörde toetus 2026"; "Digimentorlus …"; "Tark tellija …" | **Most productive.** EIS measure pages, the Riigi Teataja regulations (RT I, 27.01.2026; RT I, 05.03.2024), the ERR story on the AI grant, and MKM news |
| EN | "RTE Grant for Business Process Automation … EIS"; "Grant for digitalisation roadmap maximum grant"; "LIAA digital transformation support programme 2026" | EIS English measure pages; the Invest in Estonia AI-grant story; LIAA English articles; Latvian Ministry of Economics news. ERR News English search did **not** find the AI-grant story |
| LV | "LIAA atbalsts digitalizācijai 2026 …"; "LIAA mākslīgā intelekta ieviešana komersantiem atbalsts granti 2026" | LIAA service and news pages; esfondi.lv (EU-funds portal) on reserved funds and the AI earmark. Article dates were not visible in the extracts |
| LT | "Inovacijų agentūra kvietimas skaitmeninimas MVĮ 2026 dirbtinio intelekto diegimas" | **Not executed:** search budget exhausted |
| RU | none | **Not executed:** search budget exhausted |

---

## 11. UNKNOWNs and the cheapest resolution for each

| ID | UNKNOWN | Cheapest resolution |
|---|---|---|
| U1 | **LT grants, all fields** (critical) | About 6 searches limited to inovacijuagentura.lt, esinvesticijos.lt and eimin.lrv.lt ("kvietimai skaitmeninimas", "dirbtinio intelekto diegimas MVĮ", "procesų skaitmeninimas 2026"). Alternatively, one email to the Innovation Agency's client service asking for open/planned SME digitalisation calls, the minimum revenue rule and whether consultant fees are eligible |
| U2 | **CRM, ERP and AI use by country and size class**, plus the stat.ee "34%" release | Eurostat Data Browser (blocked here): the AI-use and ERP/CRM tables, filtered to EE/LV/LT, size classes 10–49 / 50–249 / 10+, latest year; record the exact dataset code. Or 3 searches limited to ec.europa.eu with the exact indicator wording. The national releases are fallbacks |
| U3 | **Job-posting snapshot** | Manual check of each site, about 30 minutes per country. Terms by language: **ET** "CRM", "Pipedrive", "HubSpot", "müügijuht B2B", "ärikliendihaldur", "automatiseerimine"; **LV** "CRM", "pārdošanas vadītājs", "biznesa attīstības"; **LT** "CRM", "pardavimų vadybininkas", "verslo plėtros"; **EN** "SDR", "BDR", "Revenue Operations", "Sales Operations", "n8n", "Zapier", "Make". Record active ads, ads with salary ranges, the minimum and maximum salary, and the date. LinkedIn: same terms with a country location filter |
| U4 | **Freelance demand** | Upwork job search with country + skill ("Lithuanian" / "Latvian" / "Estonian" / "Baltic" × "CRM", "lead generation", "automation"); record open projects and budget bands. Fiverr: counts of gigs for the same terms. Local classifieds okidoki.ee, ss.lv and skelbiu.lt: counts of service ads for "CRM" and automation |
| U5 | **Search trends** | trends.google.com, last 5 years, geo EE/LV/LT. Terms: "CRM", "Pipedrive", "HubSpot", "n8n", "ChatGPT"; ET "tehisintellekt", LV "mākslīgais intelekts", LT "dirbtinis intelektas"; RU "CRM система", "автоматизация бизнеса". Record the direction (up / flat / down) and the peak year |
| U6 | **Procurement counts and values** | Portal searches for the last 24 months (from 2024-10-03) using the § 7 CPV candidates and keywords: ET "CRM", "kliendihaldus"; LV "CRM", "klientu attiecību pārvaldība"; LT "CRM", "klientų valdymo sistema". Record count, estimated and awarded value, buyer type and procedure type. Use TED for above-threshold notices |
| U7 | **Next-call dates for the closed EE grants** (AI, roadmap, RTE automation, eCMR, digital transformation); whether external providers can be paid from the AI grant; the consultant rule for the advisory & development grant | The EIS planned-calls information, the measure-conditions PDFs, or one call/email to an EIS client manager |
| U8 | **ERP ecosystem shares** | Vendor sites (published client counts) and their API/marketplace pages; Pipedrive/HubSpot marketplace integration listings for Merit, Directo, Rivilė and B1 |
| U9 | **Russian-origin CRM use and official advice** | Searches in RU/LV/LT ("Bitrix24 Латвия/Литва/Эстония", "amoCRM Kommo Baltija"); advisories from the national cyber-security bodies (RIA in EE, CERT.LV, NKSC in LT) |
| U10 | **SME barriers** | EIB Investment Survey 2025 country overviews (EE/LV/LT) and the Digital Decade 2025 country reports (SMEs with at least basic digital intensity) |
| U11 | **E-invoicing mandates (LV, LT, ViDA; legal basis in EE)** | 3–4 searches limited to riigiteataja.ee, likumi.lv, vmi.lt and eur-lex.europa.eu |
| U12 | **LV programme status, minimum revenue, catalogue-listing rules for a foreign provider; EE/LT EDIH services** | One email to dih.lv / LIAA; the EU EDIH catalogue pages for EE and LT |

---

## 12. Synthesis inputs

Scores run from 1 to 5, where 5 is most favourable to the operator. A score here rates the **strength of the demand evidence WS2 gathered**. A low score caused by a research gap is marked "gap" and is not a negative finding.

| Country × component | Demand-evidence summary | Score | Rationale & sources | Grants that could fund A/B (when; consultant-eligible?) | Procurement relevance |
|---|---|---|---|---|---|
| EE × A (CRM) | A dedicated, open grant for adopting and integrating business software, with a mandatory paid advisor | 3 | Instrument exists and is rolling [V:WS2-007][V:WS2-010]; no usage or posting data (gap) | **Yes, now:** RTE software (EUR 2–5k, 50%; advisor needs ≥ 3 projects in 4 years) [V:WS2-009]; advisory & development (open; needs a roadmap) [V:WS2-005] | UNKNOWN |
| EE × B (automation/AI) | AI grant used up on day one; AI use 14% → 22% (2024 → 2025); automation and eCMR grants closed | 4 | [V:WS2-001][V:WS2-003][V:WS2-018][V:WS2-006][V:WS2-008] | **Partly:** AI grant closed (next call UNKNOWN); advisory & development open [V:WS2-005]; consultants payable with experience thresholds [V:WS2-011] | UNKNOWN |
| EE × C (lead gen) | No WS2 evidence; no open grant funds lead gen | 1 (gap) | Only the closed SME programme listed marketing costs [V:WS2-016] | **No** open instrument found [V:WS2-016] | UNKNOWN |
| LV × A (CRM) | LIAA grants buy digital solutions through the EDIC catalogue; CRM packages already listed; 241 applications (undated) | 3 | [V:WS2-021][V:WS2-022][V:WS2-025][V:WS3-017][V:WS3-020] | **Probably yes:** ≤ EUR 10k strand (status Oct 2026 UNKNOWN); provider must be in the catalogue (foreign-listing rule UNKNOWN) | UNKNOWN |
| LV × B (automation/AI) | AI strand up to EUR 200k; EUR 4.28M of reserved funds earmarked for AI | 3 | [V:WS2-022][V:WS2-024]; no usage statistics (gap) | **Probably yes** (status UNKNOWN; consultancy-only eligibility UNKNOWN) | UNKNOWN |
| LV × C (lead gen) | No evidence | 1 (gap) | UNKNOWN | **None found** — UNKNOWN | UNKNOWN |
| LT × A | Not researched | 1 (gap) | UNKNOWN | UNKNOWN | UNKNOWN |
| LT × B | Not researched | 1 (gap) | UNKNOWN | UNKNOWN | UNKNOWN |
| LT × C | Not researched | 1 (gap) | UNKNOWN | UNKNOWN | UNKNOWN |

**Notes for other workstreams:**
- **WS1:** grant-backed demand in EE is gated by revenue floors of EUR 50k and EUR 200k [V:WS2-007][V:WS2-001]. Revenue-band counts would sharpen the funnel.
- **WS3:** the LV EDIC catalogue is a competitive arena. EE grants favour partners with ≥ 3 similar projects [V:WS2-009].
- **WS5:** the EIS mentor rate of about EUR 147–149/h [E:A-WS2-05] and the LV catalogue CRM bundles at EUR 2,990–7,440 [V:WS3-017][V:WS3-018] are price anchors.
- **WS6:** the EDIC maturity test is a routing point for LV buyers [V:WS3-020].
