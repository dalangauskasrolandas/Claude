# Workstream assignments (lead analyst, 2026-10-03)

Each agent: read `BRIEF.md` (governing document) and `CONVENTIONS.md` first, then execute your section below **in full**: the brief's §5 text for your workstream **plus** the "Added beyond the brief" items (gaps the brief missed that matter for the decision). The concept is a hypothesis to test, not to sell — report disconfirming evidence as carefully as confirming evidence.

---

## WS1 — Market size & structure → `research/01_market_size.md`
Execute brief §5 WS1 fully:
- Active enterprises per country by size class (0–9, 10–49, 50–249): total and by target sector — NACE G46 wholesale; H49–53 transport/logistics; C manufacturing; M69 (and M69.20 accounting specifically if available); other M/N B2B services (state exactly which NACE divisions you include, e.g. M70–M74, N77–N82, and why). Sources: Statistics Estonia, CSB Latvia, Lithuania State Data Agency, Eurostat SBS (e.g. sbs_sc_ovw) — give exact table/dataset IDs. Pages can't be fetched, so also search statistical yearbooks, news releases, "Statistics Explained", and national "enterprises by size" releases.
- Exporters: number of exporting SMEs per country and main destination markets (Eurostat TEC trade-by-enterprise-characteristics; national releases).
- Associations & chambers per country and sector (freight forwarders/logistics, chambers of commerce, exporters, accountants): name, URL, member count, member list public?
- Language of business: Russian-speaking share per country (2021 censuses); evidence on which language SMEs use for sales/internal ops by country and segment; legal constraints on language in private B2B communication (esp. Latvia and Estonia; also Lithuania).
- Deliverables: G1 funnel per country (total → target sectors → right size → plausibly reachable) with assumptions at each step; G2 size estimate with method shown (e.g. Eurostat TEC partner-country data on Nordic/PL/DE enterprises exporting to EE/LV/LT; foreign-controlled enterprises; foreign chambers' membership).
- "Plausibly reachable": the lead analyst is collecting Hunter/Apollo database-coverage counts (country × size × sector) into `research/_work/data/db_coverage.csv`. If the file exists when you finalize, use it as a secondary reachability proxy (cite as Hunter/Apollo database query, secondary); otherwise build the step as an ESTIMATE with explicit basis and leave a note.
- Re-verify prior lead: ELEA (Estonian logistics & freight forwarding association) has ~65 members.

Added beyond the brief:
1. Foreign-language proficiency per country (Eurostat Adult Education Survey 2022 language datasets; Special Eurobarometer on languages 2024): % of adults knowing English and Russian (and level if available) — evidence for the "trilingual edge" test.
2. Foreign chambers / business associations in each Baltic state (Nordic chambers, German-Baltic AHK, Polish, Finnish, Ukrainian) with member counts — for G2 sizing.
3. Any evidence on the size of Russian-speaking-owned or Ukrainian-owned SME populations per country (e.g. register statistics on companies founded by Ukrainian citizens since 2022; regional enterprise counts for Ida-Virumaa / Riga / Vilnius). Note sanctions exclusion.
4. Accounting firms (NACE M69.20) per country with size split, plus professional bodies (number of certified accountants if available).

Synthesis inputs table (per country): enterprises 10–249 total; per target sector counts (10–49, 50–249); funnel endpoint; G2 estimate; Russian-speaking share; English/Russian proficiency; language-law constraint summary; association member lists public (y/n).

---

## WS2 — Digital maturity & demand signals → `research/02_demand_signals.md`
Execute brief §5 WS2 fully:
- Eurostat + national data on CRM, AI and ERP use per country and size class, latest year, exact dataset codes (verify codes; e.g. isoc_eb_ai, integration-of-internal-processes tables). National releases: Statistics Estonia ICT survey, CSB Latvia ICT usage in enterprises, Lithuania "IRT naudojimas įmonėse".
- Job postings as demand signals (cv.ee, cvkeskus.ee, cv.lv, cvmarket.lv, cvbankas.lt, cvonline.lt, LinkedIn) for CRM administrator, sales ops/RevOps, lead gen/SDR/BDR, automation (n8n/Make/Zapier), Pipedrive/HubSpot specialist: snapshot counts + salary ranges. Sites can't be fetched — use WebSearch with `allowed_domains` per site; report what you can see as "indexed postings found via search (lower bound), snapshot 2026-10-03" and label clearly; otherwise UNKNOWN with exact manual-check instructions.
- Freelance platforms (Upwork, Fiverr, Malt, Freelancer, local equivalents, e.g. classifieds ss.lv / skelbiu.lt / okidoki.ee service ads): volume and budgets of projects mentioning EE/LV/LT or Baltic languages together with CRM, lead gen or automation.
- Google Trends per country (5-year direction) — trends.google.com is blocked; search for any published trend evidence; otherwise UNKNOWN with resolution.
- **Grants & vouchers (critical)** for 2026–2027: Estonia EIS; Latvia LIAA; Lithuania Inovacijų agentūra; each country's EDIH(s); EU/Interreg. For each: status (open/closed/planned) + next call date; amount + co-funding rate; eligibility incl. minimum revenue threshold; can external consultants/service providers be paid from it.
- Public procurement: small tenders for CRM implementation, sales automation or lead generation in the last 24 months (riigihanked.riik.ee; Latvia EIS/IUB; Lithuania CVP IS; also TED). Count + typical value; if not obtainable, UNKNOWN with exact CPV codes/search parameters to resolve.
- Re-verify prior leads: EIS AI-adoption grant (2026) closed the day it opened; EIS digitalisation-roadmap grant closed since 24.07.2026; Statistics Estonia ~22% of enterprises used ≥1 AI technology (2025 survey). Note: a stat.ee release titled "65% of people and 34% of enterprises use AI" exists — establish its year and reconcile with the 22% figure.

Added beyond the brief:
1. E-invoicing / e-reporting mandates per country as automation-demand drivers (Estonia B2B e-invoice rules from 2025; Latvia B2B e-invoicing mandate and any postponement; Lithuania i.SAF / e-invoicing plans; EU ViDA timeline) — especially relevant to accounting firms.
2. Local accounting/ERP software ecosystems per country (e.g. EE Merit Aktiva, Directo, SmartAccounts; LV Horizon, Jumis/Tildes Jumis; LT Rivilė, B1, Centas, Finvalda, Agnum) — market-share evidence, API/integration marketplaces — as integration-demand signals for component B.
3. Russian-origin CRM use (Bitrix24, amoCRM/Kommo) among Baltic SMEs and any migration signals or official advice against Russian-origin software.
4. SME digitalisation barriers per country (EIB Investment Survey 2025 country overviews; Digital Decade 2025 country reports — SMEs with at least basic digital intensity; national chamber/employer surveys).

Synthesis inputs table: per country × component (A CRM, B automation, C lead gen): demand-evidence summary + suggested score 1–5 with rationale and source IDs; grants that could fund A/B (yes/no/when, consultant-eligible?); procurement relevance.

---

## WS3 — Competitor map → `research/03_competitors.md` + `research/competitors.csv`
Execute brief §5 WS3 fully:
- CRM partners per country from official partner directories (Pipedrive, HubSpot, Zoho, SMB-focused Salesforce partners): count, languages, published packages and prices. Directories can't be fetched — use WebSearch with `allowed_domains` and local-language searches ("Pipedrive partneris", "HubSpot partner Eesti", "Zoho partneris Latvijā", etc.). Report counts as "identified via search (lower bound)" unless a directory total is visible in a search extract.
- Lead-gen / appointment-setting / outsourced-SDR agencies active in the Baltics (local, plus Nordic/Polish/other agencies covering the Baltics): countries covered, languages, pricing model, published prices, minimum contract.
- AI/automation agencies and visible freelancers targeting Baltic SMEs (Make partner directory, n8n experts, Zapier experts with Baltic locations; local agencies): offers and published prices. Individuals: aggregate only (no names/profile URLs).
- Answer: (a) does any player already cover all three Baltic states in English + Russian + the local language? (b) price bands per service per country; (c) gaps (segment, language, price point, delivery model) with evidence for each.
- `competitors.csv` columns exactly: `name,url,hq_country,countries_served,services,languages,pricing_model,published_price,date_checked,source` then extra columns `source_id,category` (category = crm_partner | leadgen_agency | automation_agency | data_provider | vendor_service | other). All fields double-quoted.
- Re-verify prior lead: Fontakt and Ripe Leads exist as Baltic lead-gen / B2B data players — what they are, HQ, services, prices.

Added beyond the brief:
1. Substitutes: CRM vendors' own onboarding/implementation services and built-in AI (Pipedrive, HubSpot, Zoho) — scope and price.
2. Bitrix24 and Kommo (amoCRM) partners in EE/LV/LT (signal of a Russian-speaking CRM market).
3. Baltic B2B data providers (Lursoft, Firmas.lv, Rekvizitai.lt, Inforegister.ee, Teatmik.ee, Creditinfo, Dealfront/Leadfeeder, Scorify, Fontakt if relevant) as competitors/enablers, with published prices.
4. Accounting-software vendors' automation features and accounting firms that already sell CRM/automation services (substitutes for the accounting-firm segment).

Synthesis inputs table: per country × component: competition intensity score 1–5 (5 = least competition) with rationale and source IDs; price bands; trilingual all-Baltic coverage (yes/no + evidence).

---

## WS4 — Legal & compliance → `research/04_legal_compliance.md`
Execute brief §5 WS4 fully, for EE, LV, LT separately:
- Unsolicited B2B commercial email (generic company addresses vs named-employee addresses); B2B cold calling; LinkedIn outreach; GDPR legitimate interest (Art. 6(1)(f), Recital 47, Art. 14 information duty, Art. 21 objection; CJEU C-621/22 KNLTB 2024; EDPB legitimate-interest guidelines 1/2024).
- Cite exact sections of national law: EE Electronic Communications Act (ESS) § 103¹ and Information Society Services Act; LV Law on Information Society Services (commercial communications section) and Electronic Communications Law; LT Law on Electronic Communications (direct-marketing article, current numbering). Verify every section number.
- DPA guidance: Estonia AKI, Latvia DVI, Lithuania VDAI (also check which body enforces unsolicited commercial communications — e.g. Latvia PTAC; Lithuania RRT/VDAI). Enforcement cases and fines 2020–2026.
- Data sources per country: business registers (EE e-Business Register; LV Register of Enterprises/Lursoft; LT Registrų centras/JAR), Lursoft/Rekvizitai-type databases, Apollo/Hunter-type enrichment tools (include EU comparables: CNIL KASPR decision 2024; Polish UODO Bisnode 2019 Art. 14 precedent — flag pre-2020), scraped data.
- Solo-provider obligations: Art. 28 DPA, Art. 32 security, sub-processors, Art. 30 records, Art. 33 breach notification, Art. 82 liability for client data in automations; EU AI Act — provider vs deployer for this service, Art. 4 AI literacy, Art. 50 transparency (AI-drafted replies, chatbots), high-risk triggers (e.g. recruitment/HR, credit) — with the application timeline as of Oct 2026 and the status of the "Digital Omnibus" amendments.
- Deliverable: plain-language table per country — allowed / risky / forbidden — with citations.

Added beyond the brief:
1. Side business while employed in Estonia: Employment Contracts Act (Töölepingu seadus) — non-compete agreements (§§ 23–24), confidentiality, loyalty; whether employer consent is needed — what the operator should check in their own contract (no personal data).
2. Sanctions compliance for a service provider: EU Reg. 833/2014 Art. 5n (ban on business/management consulting, IT consultancy, advertising, market research, PR, etc. to Russian entities) and Belarus Reg. 765/2006 equivalents; national sanctions acts (EE International Sanctions Act; LV sanctions law; LT sanctions implementation law); practical screening sources.
3. International transfers via US-based AI/automation tools (EU–US Data Privacy Framework status in 2026; SCCs) and the sub-processor chain (Make, n8n, Anthropic, OpenAI, email tools) — what the client DPA must cover.
4. LinkedIn User Agreement restrictions on automation/scraping and enforcement practice.
5. Contract liability caps and professional-indemnity insurance availability for a solo provider in Estonia (brief).
6. Language requirements for commercial communications (B2B vs consumer) per country — cross-check with WS1.

Synthesis inputs table: per country × component (A, B, C): legal-risk score 1–5 (5 = lowest risk) with citations; the allowed/risky/forbidden table.

---

## WS5 — Pricing, unit economics & tooling → `research/05_pricing_unit_economics.md`
Execute brief §5 WS5 fully:
- Market prices in each Baltic country and comparable EU markets (FI, SE, PL, DE): CRM setup packages; CRM support retainers; automation projects; lead-gen retainers; pay-per-meeting; hourly freelance rates by country.
- Solo-scale tool stack costs from official 2026 pricing pages: CRM partner/sandbox access (Pipedrive, HubSpot developer/test accounts, Zoho); n8n (cloud vs self-host) / Make; email sending (Instantly, Smartlead, Lemlist), warm-up, domains, mailboxes (Google Workspace, Microsoft 365); enrichment (Apollo, Hunter, Lusha, Dealfront; Baltic: Lursoft, Rekvizitai, Inforegister); LinkedIn tools (Sales Navigator, Waalaxy/Expandi/Dripify); AI API costs if material. Check fit with the €200–500 budget.
- Partner/affiliate programmes that would pay the operator (Pipedrive, HubSpot Solutions Partner + Affiliate, Zoho, Make, n8n, others such as Instantly, Lemlist, Apollo): official terms only — requirements, commission %, duration.
- Unit-economics models: CRM setup; automation project; lead-gen retainer — delivery hours, sales/admin hours, tool costs, churn assumption, net €/hour after Estonian FIE taxes; sensitivity table at three price levels.
- Tax assumptions from the brief: 22% income tax and 33% social tax on profit; social tax deductible; no quarterly social-tax advances (employed elsewhere). Verify on emta.ee; state the exact formula used (e.g. S = 0.33 × P / 1.33; income tax = 0.22 × (P − S)); flag any discrepancy with official 2026 rules (social-tax cap, II-pillar contribution, basic exemption already used at the employer, minimum-obligation rules when employed).
- Re-verify prior lead: Upwork "AI automation" postings median ≈ $29.50/h in May 2026 (Upwatcher).

Added beyond the brief:
1. VAT for an Estonian FIE selling B2B services to EE, LV, LT (and other EU) clients: registration threshold; whether a VAT number is required for intra-EU B2B services under reverse charge (VAT Directive Art. 214(1)(d) and Estonian VAT Act implementation); Estonian VAT rate in 2026; EU SME scheme from 2025; implications for pricing/admin.
2. Whether the Estonian "ettevõtluskonto" (entrepreneur account) can be used for B2B income — vs FIE.
3. FIE setup and running costs (registration fee, business bank account, accounting software, insurance) against the €200–500 budget.
4. Capacity model: billable capacity at 10 / 15 / 20 h/week after sales/admin overhead; max concurrent clients per model; tasks that require daytime.
5. Email deliverability requirements (Google & Yahoo bulk-sender rules 2024; Microsoft Outlook 2025) and their tooling/cost implications.
6. Buyer's alternative cost: monthly employer cost of an in-house SDR/sales rep and a CRM admin per country (official wage statistics by occupation + employer taxes) as a price anchor.
7. Late-payment behaviour per country (e.g. Intrum European Payment Report 2025) — brief.

Synthesis inputs table: per country × component: willingness-to-pay evidence + suggested score 1–5 with source IDs; net €/h per model at the three price levels; capacity limits.

---

## WS6 — Reachability & first-client channels → `research/06_channels_reachability.md`
Execute brief §5 WS6 fully:
- Channels for G1 and G2, per country: associations and chambers; events between Oct 2026 and Mar 2027; LinkedIn / Facebook / Telegram communities in RU / LT / EN (note ET/LV ones for reference); referral partners (accountants, CRM vendors, web agencies, EDIH hubs). Sizes where verifiable.
- Benchmarks: B2B cold-outreach reply and meeting rates for the Baltics/Nordics (label each source's quality; vendor benchmark reports are secondary).
- Fit with the operator's hours: classify every channel async/evening-compatible vs needs daytime presence.
- Customer discovery: the best publicly evidenced way to recruit 15–20 owner interviews per country cheaply.

Added beyond the brief:
1. Sales-cycle length benchmarks for SME B2B services (CRM / automation / lead gen) — label quality.
2. Foreign chambers & business associations in each Baltic state as G2 channels (Nordic chambers, AHK German-Baltic, Polish, Ukrainian) and their events in the window.
3. Russian-speaking and Ukrainian business communities per country (Telegram/Facebook/associations) with verifiable sizes — note sanctions-screening implications.
4. Evidence on accountants as SMEs' advisers on digital tools / referral sources (IFAC/ACCA/national association surveys), and whether CRM vendors' partner programmes route leads to partners.
5. EDIH "test-before-invest" / voucher services that route SMEs to external providers; can an outside provider register as a service provider with each EDIH?

Synthesis inputs table: per country × group (G1 sectors, G2): best 3 channels (size, async fit, cost); async/evening-fit score 1–5 per component (5 = fully async-compatible) with rationale; evidence on whether RU/LT/EN opens channels (community sizes).
