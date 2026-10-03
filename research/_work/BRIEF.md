# RESEARCH BRIEF — "Baltic Revenue Engine" (CRM + AI automation + B2B lead generation across EE / LV / LT)

## 0. How to run this
You are Claude Code acting as lead research analyst. Execute this brief end-to-end without stopping to ask me questions. If a step is impossible (blocked site, paywall, missing tool), record it as UNKNOWN with the reason and continue.

- Use WebSearch and WebFetch extensively.
- Run workstreams WS1–WS6 in parallel using subagents (Task/Agent tool). Give each subagent this full brief plus its workstream.
- Write all outputs as files in `./research/`.
- Quality over speed.

This is **research, not a business plan**. Do not design offers, brand names, websites or marketing. Produce the evidence base I will use later to decide.

---

## 1. Objective
Determine, with evidence, whether and where a one-person, part-time operator can sell three services to B2B companies across all three Baltic states (Estonia, Latvia, Lithuania):
- CRM setup
- AI/workflow automation
- outbound lead generation

The research must answer:
1. **Who buys:** which segments, in which country.
2. **How many:** how many such buyers exist, and how many are reachable.
3. **What they pay now, and to whom.**
4. **What blocks them:** budget, trust, language, legal.
5. **The edge:** does a Baltic-wide, trilingual (EN/RU/LT) operator have a real, evidenced advantage, or not?

## 2. The operator (constraints that define relevance)
- **Location and languages:** based in Tallinn, Estonia; Lithuanian citizen. Speaks English, Russian and Lithuanian. **No Estonian, no Latvian.**
- **Day job:** full-time BD/sales manager at a maritime inspection company.
- **Time:** 10–20 h/week on the side, mostly evenings and weekends. Very little availability during business hours. Score async-deliverable work higher, and flag anything that needs daytime calls or on-site presence.
- **Money and legal form:** budget €200–500. Will invoice as an Estonian FIE (sole trader) at first.
- **Skills:** B2B sales and prospecting, daily CRM use, building automations with Claude / Claude Code, learning n8n/Make-type tools.
- **No network yet** of non-maritime decision-makers.
- **Hard exclusions — do not research these as targets:**
  - ship managers/shipowners or anything touching vessel inspections/surveys (employer conflict)
  - brokering between vessels and service providers
  - any client trading with Russia/Belarus (sanctions)
- **Prior idea to include as a segment:** Lithuanian (and other Baltic) accounting firms, both as clients and as referral partners. Interviewing owners was the planned discovery method.

## 3. Concept to test (a hypothesis, not a conclusion)
**Components** (sold separately or bundled):
- **A. CRM setup / cleanup / migration** (Pipedrive, HubSpot, Zoho or similar) for B2B companies with 5–100 staff.
- **B. AI/workflow automation around the revenue and ops pipeline.** For example: inbound inquiry/RFQ → CRM → drafted reply or quote → follow-up; document extraction; pipeline reporting.
- **C. Outbound lead generation:** ICP definition, list building and enrichment, multilingual email/LinkedIn sequences across EE/LV/LT, booked meetings.

**Customer groups:**
- **G1 — Baltic B2B SMEs** wanting more pipeline and less manual work. Sectors to test:
  - logistics & freight forwarding
  - wholesale/trading
  - manufacturing exporters
  - B2B professional services, including accounting firms
- **G2 — Foreign B2B companies** (Nordic, Polish, German, Ukrainian, other EU) wanting to sell into all three Baltic markets, who need Baltic-wide leads and a local operator.

**Claimed advantage (TEST it, do not assume it):** one operator covering all three Baltic states in English, Russian and Lithuanian.

## 4. Rules of evidence (non-negotiable)
1. **No invention.** Never invent companies, prices, statistics, people or URLs. If you can't find something, write UNKNOWN.
2. **Label every key claim.** Use:
   - **VERIFIED** — URL + date accessed + supporting quote of 25 words or fewer, recorded in `sources.csv`
   - **ESTIMATE** — formula and assumptions shown
   - **UNKNOWN** — state what would resolve it
3. **Prefer primary sources:** national statistics offices, Eurostat, official registers, regulators/DPAs, legislation portals, official vendor pricing/partner pages. Treat blogs, listicles and vendor claims (e.g. "8,200+ companies") as secondary leads, and say so.
4. **Recency.** Prefer 2024–2026 data. State the year of every statistic. Flag anything older than 2023.
5. **Search in local languages too:** Estonian, Latvian, Lithuanian and Russian, not just English. Note which language found what.
6. **Conflicting sources:** show both, say which you trust and why.
7. **Traceable math.** Every number in a calculation must trace to a VERIFIED or ESTIMATE line in `assumptions.md`.
8. **No personal data on named individuals.** Company-level and aggregate data only.
9. **Cover each country separately.** Every section must address EE, LV and LT; never silently skip one.

### Prior findings to re-verify (starting leads only — do not cite without re-checking)
- Upwork "AI automation" postings had a median rate of about $29.50/h in May 2026 (source: Upwatcher).
- Estonia:
  - The EIS AI-adoption grant (2026) closed the day it opened.
  - The EIS digitalisation-roadmap grant has been closed since 24.07.2026.
- Statistics Estonia: about 22% of enterprises used at least one AI technology (2025 survey).
- ELEA (Estonian logistics & forwarding association) has about 65 members.
- Fontakt and Ripe Leads exist as Baltic lead-gen / B2B data players.

---

## 5. Workstreams (run in parallel; each writes its own file)

### WS1 — Market size & structure → `01_market_size.md`
**Enterprise counts.** Active enterprises per country by size class (0–9, 10–49, 50–249):
- total
- by target sector: NACE G46 wholesale, H49–53 transport/logistics, C manufacturing, M69 accounting, other M/N B2B services

Sources: Statistics Estonia, Latvia CSB (csp.gov.lv), Lithuania State Data Agency (osp.stat.gov.lt), Eurostat SBS. Give exact table/dataset IDs.

**Exporters.** Number of exporting SMEs per country, and their main destination markets.

**Associations and chambers** per country and sector (freight forwarders/logistics, chambers of commerce, exporters, accountants). For each: name, URL, member count, and whether the member list is public.

**Language of business:**
- Russian-speaking share per country (latest census).
- Any evidence on which language SMEs use for sales and internal operations, by country and segment.
- Legal constraints on language in private B2B communication, especially in Latvia and Estonia.

**Deliverables:**
- A funnel per country for G1: total → target sectors → right size → plausibly reachable. Show assumptions at each step.
- A size estimate for G2 with the method shown.

### WS2 — Digital maturity & demand signals → `02_demand_signals.md`
**Enterprise technology use.** Eurostat and national data, per country and size class, latest year, with exact dataset codes:
- CRM use
- AI use
- ERP use

**Job postings as demand signals.** Snapshot counts and salary ranges where shown, from:
- Sites: cv.ee, cvkeskus.ee, cv.lv, cvmarket.lv, cvbankas.lt, cvonline.lt, LinkedIn.
- Roles: CRM administrator, sales ops/RevOps, lead generation/SDR/business development rep, automation (n8n/Make/Zapier), Pipedrive/HubSpot specialist.

**Freelance platforms** (Upwork, Fiverr, Malt, Freelancer, local equivalents). Volume and budgets of projects that mention:
- Estonia/Latvia/Lithuania or Baltic languages
- together with CRM, lead generation or automation work

**Search trends.** Google Trends per country, 5-year direction, for relevant terms in English, local languages and Russian. Mark UNKNOWN if it's unreachable.

**Grants and vouchers (critical).** Public grants that fund SME digitalisation, CRM or AI adoption in 2026–2027. Cover:
- Estonia: EIS
- Latvia: LIAA
- Lithuania: Innovation Agency (Inovacijų agentūra)
- each country's European Digital Innovation Hub(s)
- any EU/Interreg programmes

For each grant record:
- status (open / closed / planned) and next call date
- amount and co-funding rate
- eligibility, including the minimum revenue threshold
- whether external consultants/service providers can be paid from it

**Public procurement.** Small tenders for CRM implementation, sales automation or lead generation in the last 24 months, from riigihanked.riik.ee (EE), EIS (LV) and CVP IS (LT). Report count and typical value.

### WS3 — Competitor map → `03_competitors.md` + `competitors.csv`
**Groups to map:**
1. **CRM partners** listed for each country in official partner directories (Pipedrive, HubSpot, Zoho, SMB-focused Salesforce partners). Record: count, languages, published packages and prices.
2. **Lead generation / appointment setting / outsourced SDR agencies** active in the Baltics. Record: countries covered, languages, pricing model, published prices, minimum contract.
3. **AI/automation agencies and visible freelancers** targeting Baltic SMEs. Record: offers and published prices.

**Questions to answer:**
- (a) Does any player already cover all three Baltic states in English + Russian + the local language?
- (b) What are the price bands per service, per country?
- (c) What gaps exist (segment, language, price point, delivery model)? Give evidence for each.

**`competitors.csv` columns:** name, URL, HQ country, countries served, services, languages, pricing model, published price, date checked, source.

### WS4 — Legal & compliance for outbound lead gen and automation → `04_legal_compliance.md`
**Outreach rules, for EE, LV and LT separately:**
- Unsolicited B2B commercial email, to generic company addresses and to named-employee addresses.
- B2B cold calling.
- LinkedIn outreach.
- GDPR legitimate interest.

Cite exact sections of national law (electronic communications / information society services acts). Cite DPA guidance from Estonia AKI, Latvia DVI and Lithuania VDAI. Find enforcement cases and fines from 2020–2026.

**Data sources.** Is it legal to use each of these for B2B prospecting, per country?
- business registers
- Lursoft / Rekvizitai-type databases
- Apollo/Hunter-type enrichment tools
- scraped data

**Solo-provider obligations:**
- data processing agreements
- liability for client data handled in automations
- whether the EU AI Act creates any obligations for this kind of service

**Deliverable:** a plain-language table per country — allowed / risky / forbidden — with citations.

### WS5 — Pricing, unit economics & tooling → `05_pricing_unit_economics.md`
**Market prices** in each Baltic country and comparable EU markets for:
- CRM setup packages
- CRM support retainers
- automation projects
- lead-gen retainers
- pay-per-meeting
- hourly freelance rates by country

**Solo-scale tool stack costs** from official 2026 pricing pages:
- CRM partner/sandbox access
- n8n / Make
- email sending, warm-up, domains, mailboxes
- enrichment data
- LinkedIn tools

**Partner/affiliate programmes that would pay the operator** (Pipedrive, HubSpot, Zoho, Make, n8n, others). Official terms only: requirements, commission %, duration.

**Unit-economics models.** Build three: CRM setup, automation project, lead-gen retainer. Each includes:
- delivery hours
- sales/admin hours
- tool costs
- client churn assumption
- net €/hour after Estonian FIE taxes

**Tax assumptions for the models:**
- 22% income tax and 33% social tax on profit; social tax is deductible.
- The operator is employed elsewhere, so no quarterly social-tax advances.
- Show a sensitivity table at three price levels.

### WS6 — Reachability & first-client channels → `06_channels_reachability.md`
**Channels.** For G1 and G2, per country, where buyers can actually be reached:
- associations and chambers
- events between Oct 2026 and Mar 2027
- LinkedIn / Facebook / Telegram communities in RU / LT / EN
- referral partners: accountants, CRM vendors, web agencies, EDIH hubs

Give sizes where verifiable.

**Benchmarks.** Cold-outreach reply and meeting rates for B2B in the Baltics/Nordics. Label the quality of each source.

**Fit with the operator's hours.** Classify every channel:
- async / evening-compatible
- needs daytime presence

**Customer discovery.** The best publicly evidenced way to recruit 15–20 owner interviews per country cheaply.

---

## 6. Verification & red team (after WS1–6 finish)
1. **Verification.** Spawn a fresh subagent that did not do the original research. It must:
   - re-open the sources for the 30 most decision-relevant claims
   - recalculate every model
   - write `verification_log.md`, marking each claim confirmed, corrected, or could not verify, with what changed
   - apply all corrections to the workstream files
2. **Red team.** Spawn another fresh subagent. It writes `red_team.md`: the 7 strongest reasons this concept fails for *this operator*. Cover customer, competition, legal, capacity/time, language, price and channel. Give each reason evidence and a severity rating (high / medium / low).

## 7. Synthesis → `00_research_summary.md` (research conclusions, not a plan)
- **Executive summary:** 15 lines, plain English, dense.
- **Evidence scorecard:**
  - Rows: component (A, B, C, and bundles A+B, A+B+C) × customer group (G1 by sector, G2) × country.
  - Columns: demand evidence, willingness-to-pay evidence, competition intensity, legal risk, async/evening fit, language advantage real?
  - Score 1–5, each with a reference to its supporting evidence.
- **The trilingual all-Baltic advantage:** a verdict per country. Where are English, Russian or Lithuanian enough, and where is Estonian or Latvian effectively required?
- **Ranking:** the top 3 evidence-backed combinations and the 3 weakest, with reasons.
- **Open unknowns:** each remaining UNKNOWN, with the cheapest way to resolve it (a specific test, an interview question, or a source).
- Do not write offers, pricing pages, names or marketing plans.

## 8. Output files (`./research/`)
```
00_research_summary.md
01_market_size.md
02_demand_signals.md
03_competitors.md
competitors.csv
04_legal_compliance.md
05_pricing_unit_economics.md
06_channels_reachability.md
verification_log.md
red_team.md
sources.csv      # id, claim, URL, publisher, date published, date accessed, quote ≤25 words, primary/secondary, label
assumptions.md   # every ESTIMATE input with its basis
```

## 9. Done means
- At least 80 distinct sources in `sources.csv`, at least half of them primary.
- EE, LV and LT covered separately in every workstream.
- Zero unlabelled numbers.
- Verification log completed, and corrections applied.
- Summary written last, and consistent with the corrected files.
