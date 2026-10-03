# 05 — Pricing, unit economics & tooling (WS5)

## 1. Scope, legend, method

**Scope:** what Baltic buyers pay for CRM setup, automation and lead generation, what the solo tool stack costs, and what a one-person Estonian FIE actually nets per hour after 2026 Estonian taxes. Covers three unit-economics models, price sensitivity and capacity.

**Legend:**
- A label such as `[V:WS5-001]` = VERIFIED, see `_work/sources_WS5.csv`. `[V:WS2-…]` and `[V:WS3-…]` are VERIFIED sources from the WS2 and WS3 fragments, cross-referenced here.
- `[E:A-WS5-xx]` = ESTIMATE, see `_work/assumptions_WS5.md` for formula, inputs and confidence.
- UNKNOWN (resolve: …) = not found. The `SP-xx` codes point to `_work/data/WS5_search_plan.csv`, which gives the exact query, domain and language for each.
- "LEAD WSn-xxx" = seen but not usable as VERIFIED.

**Method:** evidence was gathered via web-search extracts on 2026-10-03. Direct page fetching was blocked in this environment, except claude.com and GitHub, which were fetched directly. All model calculations are in `_work/data/WS5_models.py`, which is re-runnable and writes `_work/data/WS5_models.csv`.

> **Coverage warning — read first.** All six workstreams share one WebSearch budget for the session. It ran out after two dozen WS5 queries. Those queries went on the Estonian tax and VAT rules first, because every model depends on them.
>
> **Not researched in this run (UNKNOWN):**
> - official 2026 vendor pricing pages
> - partner and affiliate programme terms
> - all LV/LT/RU-language price searches
> - FI/SE/PL/DE comparables
> - wage statistics, Intrum late-payment data, and e-mail deliverability rules
>
> Each has a ready query in the search plan (thirty-eight items).
>
> **What still holds:**
> - Market price anchors come from WS2 and WS3 sources, which those workstreams verified.
> - The three models are complete and recomputable.
> - Every unverified cost input is an explicit allowance with a range, and the sensitivity tables show how far each one moves the result.

---

## 2. Key findings

1. **Tax: the operator keeps 58.65% of FIE profit.** Social tax is 33% of P/1.33, i.e. 24.81% of profit (P). Income tax is 22% of the remainder, i.e. 16.54% of P [V:WS5-002][V:WS5-006][V:WS5-007][E:A-WS5-01].
   - No social-tax minimum or advances apply, provided his employer pays at least €877.14 a quarter in social tax for him. Any full-time salary at or above the €886 monthly rate does that [V:WS5-003][V:WS5-001].
   - No basic exemption is left for FIE profit, because the 2026 flat €700/month is used by the salary [V:WS5-006][E:A-WS5-02].
   - The brief's tax assumption matches official 2026 rules only if "social tax deductible" means the statutory 1.33 divisor. A literal reading (S = 0.33 × P) understates net income by 6.4 percentage points: 52.26% instead of 58.65% [E:A-WS5-01].
2. **Net €/h after tax, per unit, base hours:**
   - CRM setup: €16.8 / €34.9 / €69.8 at €1,200 / €2,500 / €5,000 per project [E:A-WS5-13][E:A-WS5-14].
   - Automation project: €9.4 / €25.4 / €63.8 at €450 / €1,200 / €3,000 per project [E:A-WS5-19][E:A-WS5-20].
   - Lead-gen retainer: €19.5 / €37.9 / €62.1 at €1,000 / €1,800 / €2,850 per month [E:A-WS5-25][E:A-WS5-26].
3. **Price floors.** To net €25/h at base hours, the operator needs at least €1,790 per CRM setup, €1,182 per automation project, or €1,237/month per lead-gen client [E:A-WS5-36]. The bottom of the only published Baltic automation band (€450, LT [V:WS3-024]) nets under €10/h [E:A-WS5-19]. It is viable only with heavy template reuse.
4. **Published price anchors exist mainly in LV and LT; EE is thin.** All of these are supply-side list prices, not transaction prices.
   - LV: EDIH-catalogue CRM bundles cost €2,990–7,440 including licences and 12 h of implementation [V:WS3-017][V:WS3-018]. A generic CRM implementation package costs €5,000 [V:WS3-019].
   - LT: automation costs €300–3,000+ [V:WS3-024]. An outbound retainer costs €2,850/month after a €3,750 first month [V:WS3-008].
   - EE: agency setup work is €110–150/h [V:WS3-005]. EIS-procured digital mentoring works out at about €147–149/h [E:A-WS2-05].
5. **Grants anchor prices but lock out a newcomer at first.**
   - LV: LIAA pays 100% aid to micro/small firms when the project total is ≤ €5,000 [V:WS2-020]. The programme's late-2026 status is uncertain [V:WS2-019].
   - EE: the EIS software-adoption grant caps consultant fees at 50% of an aid of €2,000–5,000 [V:WS2-007]. It also requires the "digital advisor" to have at least three similar projects in the prior four years [V:WS2-009]. So the operator's first projects cannot be grant-funded with him as the advisor.
6. **Capacity ceiling at 15 h/week** (supply side only, not a demand forecast) [E:A-WS5-38]:
   - about 14.7 CRM setups a year, or 22.5 automation projects, or 2.0 concurrent lead-gen clients (needing about 3.6 new clients a year at 15% monthly churn) [E:A-WS5-38];
   - all-in net at the mid price: €21.2k, €15.3k or €23.1k a year respectively [E:A-WS5-38].

   Lead generation needs about 4.5 hours a week inside business hours (same-day reply handling, client calls), which collides with the day job [E:A-WS5-33].
7. **Tools barely move the result, except in lead generation.**
   - AI API run-cost for a typical client automation is $2.10–8.40/month for 300 inquiries [V:WS5-020][E:A-WS5-24]. Claude Pro costs $17–20/month [V:WS5-020].
   - Self-hosted n8n carries no licence fee [V:WS5-021]. n8n's licence FAQ explicitly allows running client workflows on the consultant's own instance and charging for it [V:WS5-022].
   - The lead-gen tool and data allowance (€80–300 per client-month) shifts net €/h by about €5 across its range [E:A-WS5-30]. Verified 2026 vendor prices are UNKNOWN (resolve: SP-01…SP-12).
8. **VAT.**
   - VAT registration is needed only if Estonian place-of-supply turnover exceeds €40,000 [V:WS5-012].
   - Services to LV/LT businesses are taxed in the client's state [V:WS5-014].
   - Estonian VAT has been 24% since 1 July 2025 [V:WS5-011]. An unregistered FIE therefore bears 24% non-deductible VAT on tools [E:A-WS5-07].
   - The EU provision on VAT IDs for suppliers of reverse-charged services is Art. 214(1)(e), not (d) [V:WS5-016].
9. **The entrepreneur account (ettevõtluskonto) would raise net €/h by about 34–36%, but only where it is usable.** It taxes 20% of receipts up to €40,000 a year in 2026 [V:WS5-018].
   - It is unusable for Estonian company clients, who would owe an extra 22/78 income tax on top [V:WS5-018].
   - For LV/LT clients, eligibility is UNKNOWN (resolve: SP-35).
   - Example: CRM at the mid price nets €47.6/h instead of €34.9/h [E:A-WS5-06].
10. **Largest gaps:**
    - verified 2026 tool prices and partner commissions;
    - hourly freelance rates and pay-per-meeting prices in all three countries and in FI/SE/PL/DE;
    - the Upwork/Upwatcher lead, which is not re-verified;
    - wages for the buyer's alternative cost, and late-payment data.

    All are UNKNOWN (resolve: SP-01…SP-34).

---

## 3. Tax framework — Estonian FIE, 2026 (the model's foundation)

### 3.1 Formula used in every model
For P = revenue excl. VAT − deductible business expenses:

- **Social tax** S = 0.33 × P / 1.33 = 24.81% of P [V:WS5-002]. The FIE maximum for 2026 is €36,867.60, which only binds at P ≥ €148,588 [V:WS5-002][E:A-WS5-05].
- **Income tax** IT = 0.22 × (P − S) = 16.54% of P [V:WS5-006][V:WS5-007].
- **Net** = P − S − IT = P × 0.78 / 1.33 = **0.5865 × P** [E:A-WS5-01].

Social tax itself is not a business expense [V:WS5-004]. Instead it reduces its own base (the 1.33 divisor) and the income-tax base [V:WS5-002][V:WS5-007]. The statute wording is a LEAD (WS5-005), because the act version could not be pinned down.

### 3.2 Brief vs official 2026 rules

| Item in the brief | Official 2026 position | Effect on the model |
|---|---|---|
| "22% income tax" | 22% from 1 Jan 2026 [V:WS5-006]. A 2025 plan to raise it to 24% (LEAD WS5-009) was cancelled (LEAD WS5-008). | none [E:A-WS5-01] |
| "33% social tax on profit; social tax deductible" | 33% on business income after expenses, computed by dividing by 1.33 [V:WS5-002]. Income tax applies to income adjusted for social tax [V:WS5-007]. | Net = 58.65% of P. A literal S = 0.33 × P would give 52.26% [E:A-WS5-01]. |
| "no quarterly social-tax advances (employed elsewhere)" | Correct, provided the employer pays at least €877.14/quarter in social tax for him, counted cumulatively over the year [V:WS5-003]. | No minimum. A non-employed FIE would owe at least €3,508.56 a year [E:A-WS5-03]. |
| Basic exemption (not in the brief) | 2026: flat €700/month (€8,400/year) regardless of income; the "tax hump" is abolished [V:WS5-006]. | Fully used by the salary, so the marginal rate on FIE profit is 22% [E:A-WS5-02]. |
| II pillar (not in the brief) | If enrolled, the FIE pays 2% (or 4%/6%) of social-tax-adjusted business income, assessed by EMTA and due 1 October. The 2026 maximum at 2% is €2,234.40 [V:WS5-010]. | Net cash falls to 57.47% of P. The contribution is the operator's own pension saving [E:A-WS5-04]. |
| Social-tax cap (not in the brief) | €36,867.60 FIE maximum for 2026 [V:WS5-002]. | Not binding [E:A-WS5-05]. |
| Income-tax advances (not in the brief) | Quarterly advances are based on the previous year's taxable business income adjusted for social tax [V:WS5-007]. | No advances in year one, quarterly advances from year two. Cash-flow effect only [V:WS5-007]. |

### 3.3 Tax on a thousand euros of FIE profit (model output)

| Regime | Social tax | II pillar | Income tax | Net | Net share | Label |
|---|---|---|---|---|---|---|
| Official FIE formula (used in all models) | €248.12 | €0.00 | €165.41 | €586.47 | 58.65% | [E:A-WS5-01] |
| Official + II pillar 2% | €248.12 | €15.04 | €162.11 | €574.74 | 57.47% | [E:A-WS5-04] |
| Literal reading of the brief (S = 0.33 × P) | €330.00 | €0.00 | €147.40 | €522.60 | 52.26% | [E:A-WS5-01] |
| Entrepreneur account, zero costs (foreign clients only; eligibility UNKNOWN) | €0.00 | €0.00 | €200.00 | €800.00 | 80.00% | [E:A-WS5-06] |

---

## 4. Solo-scale tool stack (official 2026 prices) and budget fit

### 4.1 Tool costs

| Category | Item | 2026 price | Status / label |
|---|---|---|---|
| AI, operator's own use | Claude Pro | $20/month billed monthly; $17/month on annual billing ($200 up front) | VERIFIED, fetched [V:WS5-020] |
| AI, heavy Claude Code use | Claude Max | from $100/month | VERIFIED [V:WS5-020] |
| AI API, inside client automations | Sonnet 5.5 $2 in / $10 out; Haiku 4.5 $1 / $5; Opus 5.5 $4 / $20 per million tokens; batch processing saves 50% | Cross-checked with Anthropic's bundled API reference | VERIFIED [V:WS5-020] |
| Automation platform | n8n self-hosted (Sustainable Use License) | royalty-free licence; Community edition free | VERIFIED [V:WS5-021][V:WS5-022]. Hosting VPS price UNKNOWN (resolve: SP-19) |
| Automation platform | n8n Cloud; Make | not retrieved | UNKNOWN (resolve: SP-04) |
| CRM partner / sandbox access | Pipedrive, HubSpot developer test accounts, Zoho | not retrieved | UNKNOWN (resolve: SP-01…SP-03) |
| Email sending and warm-up | Instantly, Smartlead, Lemlist | not retrieved | UNKNOWN (resolve: SP-05…SP-07) |
| Mailboxes | Google Workspace, Microsoft 365 | not retrieved | UNKNOWN (resolve: SP-08, SP-09) |
| Domains | .ee / .lv / .lt / .com | not retrieved | UNKNOWN (resolve: SP-14) |
| Enrichment | Apollo, Hunter, Lusha, Dealfront | not retrieved | UNKNOWN (resolve: SP-10, SP-11) |
| Baltic company data | Lursoft, Rekvizitai, Inforegister, Teatmik | not retrieved. For reference, Fontakt sells Estonian B2B contact lists by department at €140–1,590 + VAT [V:WS3-003] | UNKNOWN (resolve: SP-13) |
| LinkedIn tools | Sales Navigator, Waalaxy, Expandi, Dripify | not retrieved | UNKNOWN (resolve: SP-12) |

**AI API cost is immaterial.** One automation handling 300 inquiries a month (3,000 input + 800 output tokens each) costs $2.10 on Haiku 4.5, $4.20 on Sonnet 5.5 and $8.40 on Opus 5.5 per month [V:WS5-020][E:A-WS5-24]. These are pass-through running costs of a few euros a month, small next to project prices of €450–3,000 [E:A-WS5-24].

**The n8n licence suits a consultant.** The licence FAQ permits "building, running, and maintaining workflows on your own n8n instance on behalf of clients … including charging consulting or development fees" [V:WS5-022]. It forbids hosting n8n as a service in which clients build their own workflows [V:WS5-022]. This allows a recurring managed-automation fee. Hosting client data on the operator's instance makes him a GDPR processor (see WS4).

### 4.2 Fit with the start budget (BRIEF §2)

| Item | Cost | Label |
|---|---|---|
| Claude Pro, annual, incl. 24% VAT | about €213/yr (or about €21/month if billed monthly) | [V:WS5-020][E:A-WS5-11][E:A-WS5-07] |
| n8n licence | €0 | [V:WS5-022] |
| Social-tax minimum | €0 for this operator, vs at least €3,508.56/yr for a non-employed FIE | [V:WS5-003][E:A-WS5-03] |
| Other fixed items (domain, business e-mail, accounting, bank, insurance) | allowance €150–700/yr | [E:A-WS5-11]; item prices UNKNOWN (resolve: SP-14…SP-18) |
| Lead-gen launch tools for the first client (domains, mailboxes, sending and warm-up platform, data) | allowance €80–300 per client-month, incurred during warm-up before results | [E:A-WS5-30]; UNKNOWN vendor prices (resolve: SP-05…SP-13) |

**Reading** [E:A-WS5-11]:
- CRM setup and automation can start inside €200–500, because the CRM and automation platform are paid by the client or have free tiers [E:A-WS5-11].
- Lead generation is the tightest. One client's first month of tools and data can take most of the budget before any fee is collected [E:A-WS5-30].

### 4.3 Partner and affiliate programmes that would pay the operator

| Programme | Requirements | Commission % | Duration | Status |
|---|---|---|---|---|
| Pipedrive (partner and affiliate) | tiers named in a WS3 extract (Authorized / Gold / Platinum); LEAD WS3-028 | not retrieved | not retrieved | UNKNOWN (resolve: SP-20) |
| HubSpot Solutions Partner, HubSpot Affiliate | Solutions Partner Program "designed for service firms helping mid-market and enterprise customers" [V:WS3-032] | not retrieved | not retrieved | UNKNOWN (resolve: SP-21) |
| Zoho (partner / affiliate) | not retrieved | not retrieved | not retrieved | UNKNOWN (resolve: SP-22) |
| Make, n8n | not retrieved | not retrieved | not retrieved | UNKNOWN (resolve: SP-23) |
| Instantly, Lemlist, Apollo, Smartlead, Hunter | not retrieved | not retrieved | not retrieved | UNKNOWN (resolve: SP-24) |

No commission rate is assumed in any model. Referral income is upside only, and the model excludes it (UNKNOWN until SP-20…SP-24 are resolved).

---

## 5. Market prices by country

### 5.1 Service prices

| Service | EE | LV | LT | Comparable EU (FI, SE, PL, DE) |
|---|---|---|---|---|
| CRM setup packages | No package price found. Agency setup work €110/h, advanced development €150/h [V:WS3-005]. | Pipedrive licence + implementation bundles €2,990–7,440 excl. VAT (12 h implementation; some add 3 h training) [V:WS3-017][V:WS3-018]. Generic CRM implementation €5,000 [V:WS3-019]. "Easy CRM" €9,900 incl. implementation [V:WS3-043]. | Custom CRM builds €9,500–15,000 over 2–3 months [V:WS3-025], a different scope from configuration. Pipedrive/HubSpot packages UNKNOWN (resolve: SP-34). | UNKNOWN (resolve: SP-34) |
| CRM support retainers | UNKNOWN (resolve: SP-34) | 1 h/month maintenance bundled into the €2,990 twelve-month package [V:WS3-017] | UNKNOWN (resolve: SP-34) | UNKNOWN (resolve: SP-34) |
| Automation projects | UNKNOWN (resolve: SP-34) | No price list found. LV EDIC "test before invest" funds up to €20,000 excl. VAT per business at 100% de minimis [V:WS3-046]. | €300 for one process with up to 2 integrations; €450–1,200 process automation; €1,500–3,000+ full implementation [V:WS3-024] | UNKNOWN (resolve: SP-34) |
| Lead-gen retainers | Fontakt prices per "meaningful conversation"; amounts unpublished [V:WS3-004]. UNKNOWN | No LV price found. Ripe Leads serves LV [V:WS3-009]. UNKNOWN (resolve: SP-33) | Ripe Leads (Vilnius): €3,750 first month, then €2,850/month, tools and data included, 28 days' notice [V:WS3-008] | UNKNOWN (resolve: SP-33) |
| Pay-per-meeting | UNKNOWN (resolve: SP-33) | UNKNOWN (resolve: SP-33) | UNKNOWN (resolve: SP-33) | UNKNOWN (resolve: SP-33) |
| Publicly funded price anchors | EIS digital mentoring: €4,460 for 30 h, about €147–149/h [V:WS2-015][E:A-WS2-05]. EIS software-adoption aid €2,000–5,000, consultant share ≤ 50% [V:WS2-007]. | LIAA: 100% aid for micro/small firms if total project ≤ €5,000 [V:WS2-020]; grants up to €10,000 for new digital solutions [V:WS2-022]. | see WS2 (UNKNOWN here) | n/a |

**Reading.** Most Latvian catalogue bundles sit at or below €5,000 (€2,990–5,000 [V:WS3-017][V:WS3-019]; a few run to €7,440–9,900 [V:WS3-018][V:WS3-043]). €5,000 is the LIAA 100%-aid ceiling for micro/small projects [V:WS2-020]. That is a policy-made price point, and it lasts only as long as the programme runs [V:WS2-019].

### 5.2 Hourly rates

| Country | Evidence | Label |
|---|---|---|
| EE | Agency rates €110/h for setup and €150/h for advanced development. Publicly funded mentor about €147–149/h. Freelancer rates not found. | [V:WS3-005][E:A-WS2-05]; freelancers UNKNOWN (resolve: SP-32) |
| LV | not found | UNKNOWN (resolve: SP-32) |
| LT | not found | UNKNOWN (resolve: SP-32) |
| FI, SE, PL, DE | not found | UNKNOWN (resolve: SP-32) |
| Global marketplaces | Prior lead "Upwork AI-automation median about $29.50/h, May 2026, Upwatcher": **not re-verified** | UNKNOWN (resolve: SP-31) |

The models imply these billed rates per delivery hour [E:A-WS5-35]:
- CRM: €48 / €100 / €200 [E:A-WS5-35]
- automation: €30 / €80 / €200 [E:A-WS5-35]
- lead gen: €50 / €90 / €142 [E:A-WS5-35]

The mid scenarios sit just below the Estonian agency rate of €110/h [V:WS3-005]. The high scenarios require package or value pricing above agency hourly rates [E:A-WS5-35].

---

## 6. Unit-economics models

### 6.1 Inputs (base values; ranges go into the sensitivity tables)

| Input | CRM setup | Automation project | Lead-gen retainer | Label |
|---|---|---|---|---|
| Price levels, excl. VAT | €1,200 / €2,500 / €5,000 | €450 / €1,200 / €3,000 | €1,000 / €1,800 / €2,850 per month | [E:A-WS5-13][E:A-WS5-19][E:A-WS5-25] |
| Delivery hours | 25 (15–40) | 15 (8–30) | 20 per month (14–30) | [E:A-WS5-14][E:A-WS5-20][E:A-WS5-26] |
| Sales hours per won client | 12 (6–25) | 8 (4–16) | 15 (8–30) | [E:A-WS5-15][E:A-WS5-21][E:A-WS5-28] |
| Admin and unbilled support | 2 + 3 | 1.5 + 3 | 1 per month + 15 onboarding | [E:A-WS5-16][E:A-WS5-17][E:A-WS5-22][E:A-WS5-27][E:A-WS5-31] |
| Direct tool cost, incl. VAT | €0 (€0–100) per project | €10 (€0–50) per project | €150 (€80–300) per client-month | [E:A-WS5-18][E:A-WS5-23][E:A-WS5-30] |
| Churn / lifetime | one-off | one-off | 15% monthly churn (8–25%), lifetime 6.7 months (12.5–4.0) | [E:A-WS5-29] |
| Tax | official FIE formula, net 58.65% of profit | same | same | [E:A-WS5-01] |

Fixed annual overhead (€363 / €606 / €1,980) and fixed admin hours (72 a year) are added only in the capacity results [E:A-WS5-10][E:A-WS5-11].

### 6.2 Results: net €/h at three price levels (base inputs, after tax)

| Model | Price | Hours per unit | Billed rate per delivery h | Pre-tax profit per unit | Net per unit | Gross €/h | **Net €/h** | Label |
|---|---|---|---|---|---|---|---|---|
| CRM setup | €1,200 | 42.0 | €48 | €1,200 | €704 | €28.6 | **€16.8** | [E:A-WS5-13][E:A-WS5-14] |
| CRM setup | €2,500 | 42.0 | €100 | €2,500 | €1,466 | €59.5 | **€34.9** | [E:A-WS5-13][E:A-WS5-14] |
| CRM setup | €5,000 | 42.0 | €200 | €5,000 | €2,932 | €119.0 | **€69.8** | [E:A-WS5-13][E:A-WS5-14] |
| Automation project | €450 | 27.5 | €30 | €440 | €258 | €16.0 | **€9.4** | [E:A-WS5-19][E:A-WS5-20] |
| Automation project | €1,200 | 27.5 | €80 | €1,190 | €698 | €43.3 | **€25.4** | [E:A-WS5-19][E:A-WS5-20] |
| Automation project | €3,000 | 27.5 | €200 | €2,990 | €1,754 | €108.7 | **€63.8** | [E:A-WS5-19][E:A-WS5-20] |
| Lead-gen retainer (per client lifetime, 6.7 months) | €1,000/month | 170.0 | €50 | €5,667 | €3,323 | €33.3 | **€19.5** | [E:A-WS5-25][E:A-WS5-29] |
| Lead-gen retainer | €1,800/month | 170.0 | €90 | €11,000 | €6,451 | €64.7 | **€37.9** | [E:A-WS5-25][E:A-WS5-29] |
| Lead-gen retainer | €2,850/month | 170.0 | €142 | €18,000 | €10,556 | €105.9 | **€62.1** | [E:A-WS5-25][E:A-WS5-29] |

Recompute: net per unit = (price − direct cost) × 0.5865, and net €/h = net per unit / hours per unit. For the retainer, price and tools are multiplied by the lifetime L = 1/churn, and hours = 20 × L + 15 + 15 + 1 × L [E:A-WS5-01][E:A-WS5-29].

### 6.3 Sensitivities (net €/h)

**Delivery hours** (low / base / high) × price (low / mid / high):

| Model | Delivery hours | Low price | Mid price | High price | Label |
|---|---|---|---|---|---|
| CRM setup | 15 | €22.0 | €45.8 | €91.6 | [E:A-WS5-14] |
| CRM setup | 25 | €16.8 | €34.9 | €69.8 | [E:A-WS5-14] |
| CRM setup | 40 | €12.3 | €25.7 | €51.4 | [E:A-WS5-14] |
| Automation project | 8 | €12.6 | €34.0 | €85.5 | [E:A-WS5-20] |
| Automation project | 15 | €9.4 | €25.4 | €63.8 | [E:A-WS5-20] |
| Automation project | 30 | €6.1 | €16.4 | €41.3 | [E:A-WS5-20] |
| Lead-gen retainer | 14 per month | €25.6 | €49.6 | €81.2 | [E:A-WS5-26] |
| Lead-gen retainer | 20 per month | €19.5 | €37.9 | €62.1 | [E:A-WS5-26] |
| Lead-gen retainer | 30 per month | €14.0 | €27.3 | €44.6 | [E:A-WS5-26] |

**Sales hours per won client** (low / base / high) × price:

| Model | Sales h per win | Low price | Mid price | High price | Label |
|---|---|---|---|---|---|
| CRM setup | 6 | €19.5 | €40.7 | €81.5 | [E:A-WS5-15] |
| CRM setup | 12 | €16.8 | €34.9 | €69.8 | [E:A-WS5-15] |
| CRM setup | 25 | €12.8 | €26.7 | €53.3 | [E:A-WS5-15] |
| Automation project | 4 | €11.0 | €29.7 | €74.6 | [E:A-WS5-21] |
| Automation project | 8 | €9.4 | €25.4 | €63.8 | [E:A-WS5-21] |
| Automation project | 16 | €7.3 | €19.7 | €49.4 | [E:A-WS5-21] |
| Lead-gen retainer | 8 | €20.4 | €39.6 | €64.8 | [E:A-WS5-28] |
| Lead-gen retainer | 15 | €19.5 | €37.9 | €62.1 | [E:A-WS5-28] |
| Lead-gen retainer | 30 | €18.0 | €34.9 | €57.1 | [E:A-WS5-28] |

**Lead-gen churn** × price:

| Monthly churn | Lifetime (months) | €1,000/month [E:A-WS5-25] | €1,800/month | €2,850/month | Label |
|---|---|---|---|---|---|
| 8% | 12.5 | €21.3 | €41.4 | €67.7 | [E:A-WS5-29] |
| 15% | 6.7 | €19.5 | €37.9 | €62.1 | [E:A-WS5-29] |
| 25% | 4.0 | €17.5 | €34.0 | €55.6 | [E:A-WS5-29] |

**Lead-gen tools allowance and setup fee** × price:

| Variant | €1,000/month [E:A-WS5-25] | €1,800/month | €2,850/month | Label |
|---|---|---|---|---|
| Tools €80 per client-month | €21.2 | €39.6 | €63.7 | [E:A-WS5-30] |
| Tools €150 per client-month (base) | €19.5 | €37.9 | €62.1 | [E:A-WS5-30] |
| Tools €300 per client-month | €16.1 | €34.5 | €58.6 | [E:A-WS5-30] |
| Base tools + €900 setup fee (published first-month premium) | €22.7 | €41.1 | €65.2 | [E:A-WS5-32][V:WS3-008] |

**What moves the result.** Ranked by how far they shift net €/h across the tested ranges:
1. Price.
2. Delivery hours, a spread of €18–22/h at the mid price between the low and high hour assumptions [E:A-WS5-14][E:A-WS5-20][E:A-WS5-26].
3. Sales hours per win, worth up to about −€8/h at the mid price when a cold start pushes them to the high end [E:A-WS5-15].
4. Churn, worth about €7/h [E:A-WS5-29].
5. Tools, worth about €5/h [E:A-WS5-30].

### 6.4 Tax-regime comparison at the mid price (net €/h)

| Model (mid price) | Official FIE | FIE + II pillar 2% | Literal brief reading | Entrepreneur account (foreign clients; eligibility UNKNOWN) | Label |
|---|---|---|---|---|---|
| CRM setup (€2,500) | €34.9 | €34.2 | €31.1 | €47.6 | [E:A-WS5-01][E:A-WS5-04][E:A-WS5-06] |
| Automation project (€1,200) | €25.4 | €24.9 | €22.6 | €34.5 | [E:A-WS5-01][E:A-WS5-04][E:A-WS5-06] |
| Lead-gen retainer (€1,800/month) | €37.9 | €37.2 | €33.8 | €50.6 | [E:A-WS5-01][E:A-WS5-04][E:A-WS5-06] |

### 6.5 Price needed to reach a target net €/h (base inputs)

| Model | Net €15/h [E:A-WS5-36] | Net €25/h | Net €40/h | Label |
|---|---|---|---|---|
| CRM setup (per project) | €1,074 | €1,790 | €2,865 | [E:A-WS5-36] |
| Automation project (per project) | €713 | €1,182 | €1,886 | [E:A-WS5-36] |
| Lead-gen retainer (per month) | €802 | €1,237 | €1,889 | [E:A-WS5-36] |

Compare these floors with the published anchors [E:A-WS5-36]:
- **CRM:** the €2,500 EIS consultant cap [V:WS2-007] and the LV €2,990–5,000 bundles [V:WS3-017][V:WS3-019] clear the €25/h floor.
- **Automation:** the LT €450–1,200 band [V:WS3-024] clears it only at its top.
- **Lead gen:** the LT €2,850/month price [V:WS3-008] clears the €40/h floor by a wide margin.

---

## 7. Capacity model (the three weekly-hour scenarios)

Capacity is a supply-side ceiling: it assumes a full pipeline and is not a demand forecast. Formula: projects a year = (h/week × 46 − 72) / unit hours. Concurrent retainer clients = monthly available hours / (20 + 1 + churn × (15 + 15)) [E:A-WS5-38][E:A-WS5-08][E:A-WS5-10]. The table uses the mid price and base overhead of €606 a year [E:A-WS5-11].

| Model | h/week | Annual hours | Projects a year (retainer: new clients needed a year) | Concurrent | Revenue/yr excl. VAT | Pre-tax profit/yr | Net/yr | Net €/h all-in | Daytime h/week | Label |
|---|---|---|---|---|---|---|---|---|---|---|
| CRM setup | 10 | 460 | 9.2 | 1.2 | €23,095 | €22,489 | €13,189 | €28.7 | 2.5 | [E:A-WS5-38][E:A-WS5-33] |
| CRM setup | 15 | 690 | 14.7 | 1.9 | €36,786 | €36,180 | €21,218 | €30.8 | 3.8 | [E:A-WS5-38][E:A-WS5-33] |
| CRM setup | 20 | 920 | 20.2 | 2.6 | €50,476 | €49,870 | €29,247 | €31.8 | 5.0 | [E:A-WS5-38][E:A-WS5-33] |
| Automation project | 10 | 460 | 14.1 | 0.9 | €16,931 | €16,184 | €9,491 | €20.6 | 1.0 | [E:A-WS5-38][E:A-WS5-33] |
| Automation project | 15 | 690 | 22.5 | 1.5 | €26,967 | €26,137 | €15,328 | €22.2 | 1.5 | [E:A-WS5-38][E:A-WS5-33] |
| Automation project | 20 | 920 | 30.8 | 2.0 | €37,004 | €36,089 | €21,165 | €23.0 | 2.0 | [E:A-WS5-38][E:A-WS5-33] |
| Lead-gen retainer | 10 | 460 | 2.3 | 1.3 | €27,388 | €24,500 | €14,368 | €31.2 | 3.0 | [E:A-WS5-38][E:A-WS5-33] |
| Lead-gen retainer | 15 | 690 | 3.6 | 2.0 | €43,624 | €39,382 | €23,096 | €33.5 | 4.5 | [E:A-WS5-38][E:A-WS5-33] |
| Lead-gen retainer | 20 | 920 | 5.0 | 2.8 | €59,859 | €54,265 | €31,824 | €34.6 | 6.0 | [E:A-WS5-38][E:A-WS5-33] |

**All-in net €/h across all three price levels** (net a year in brackets):

| Model | Price | 10 h/week [E:A-WS5-09] | 15 h/week | 20 h/week | Label |
|---|---|---|---|---|---|
| CRM setup | €1,200 | €13.4 (€6,146) | €14.5 (€10,000) | €15.1 (€13,854) | [E:A-WS5-38] |
| CRM setup | €2,500 | €28.7 (€13,189) | €30.8 (€21,218) | €31.8 (€29,247) | [E:A-WS5-38] |
| CRM setup | €5,000 | €58.1 (€26,734) | €62.0 (€42,792) | €64.0 (€58,850) | [E:A-WS5-38] |
| Automation project | €450 | €7.1 (€3,285) | €7.9 (€5,444) | €8.3 (€7,602) | [E:A-WS5-38] |
| Automation project | €1,200 | €20.6 (€9,491) | €22.2 (€15,328) | €23.0 (€21,165) | [E:A-WS5-38] |
| Automation project | €3,000 | €53.0 (€24,385) | €56.6 (€39,051) | €58.4 (€53,717) | [E:A-WS5-38] |
| Lead-gen retainer | €1,000/month | €15.7 (€7,230) | €17.0 (€11,726) | €17.6 (€16,222) | [E:A-WS5-38] |
| Lead-gen retainer | €1,800/month | €31.2 (€14,368) | €33.5 (€23,096) | €34.6 (€31,824) | [E:A-WS5-38] |
| Lead-gen retainer | €2,850/month | €51.6 (€23,738) | €55.1 (€38,020) | €56.9 (€52,302) | [E:A-WS5-38] |

**Thresholds the capacity results cross:**
- At 15 h/week or more, lead-gen revenue passes €40,000 a year [E:A-WS5-38]. With Estonian clients, that triggers VAT registration [V:WS5-012]. It also exceeds the entrepreneur-account ceiling [V:WS5-018].
- At 20 h/week, CRM setup revenue does the same [E:A-WS5-38].

**Business-hours tasks** (share of hours) [E:A-WS5-33]:

| Model | Async / evening-compatible | Needs business hours | Share needing business hours |
|---|---|---|---|
| CRM setup | configuration, data cleanup and migration, documentation | requirements workshop, user training, go-live support | 25% [E:A-WS5-33] |
| Automation project | building, testing, documentation | kickoff and handover calls; incident response if the operator hosts | 10% [E:A-WS5-33] |
| Lead-gen retainer | list building, enrichment, copy, sequencing, reporting | same-day reply handling, meeting booking, client calls | 30% [E:A-WS5-33] |

---

## 8. Added beyond the brief

### 8.1 VAT for an Estonian FIE selling cross-border B2B
- **Rate.** Estonian standard VAT is 24% from 1 July 2025; other rates are 13%, 9% and 0% [V:WS5-011].
- **Registration threshold.** Registration is mandatory once Estonian place-of-supply turnover exceeds €40,000 from the start of the year. The way the threshold is counted changed on 1 Jan 2025 [V:WS5-012].
- **Selling to LV/LT businesses.** A B2B service to a taxable person in another Member State is taxed in the recipient's state under the general rule, i.e. reverse charge [V:WS5-014]. An accounting-firm guide says such services do not count toward the €40,000 threshold (secondary, LEAD WS5-017).
- **Art. 214(1)(e).** EU law requires Member States to identify suppliers of services that are reverse-charged in another state under Art. 214(1)(e). The assignment's "(d)" refers to recipients [V:WS5-016]. Whether Estonia makes an unregistered FIE obtain a VAT ID before invoicing LV/LT clients is UNKNOWN (resolve: SP-36, or an EMTA phone consultation).
- **EU SME scheme.** Available from 2025 for total EU turnover ≤ €100,000 in the current and previous year; voluntary [V:WS5-013]. It is of little relevance to reverse-charged B2B services.
- **Input VAT on tools.** An unregistered FIE that buys services from abroad self-assesses Estonian VAT as a "limited taxable person" [V:WS5-015], or pays VAT the supplier charges, with no deduction. The model therefore applies ×1.24 to tool costs [E:A-WS5-07].
- **Voluntary registration.** It would recover tool VAT at the price of monthly returns. At the modelled tool spend of €80–300 per client-month, the VAT at stake is about €15–58 a month [E:A-WS5-07][E:A-WS5-30].

### 8.2 Entrepreneur account (ettevõtluskonto) vs FIE for B2B income
- **2026 terms.** 20% of receipts, or 22/24/26% with a 2/4/6% II pillar. The 20% rate covers all receipts up to €40,000 a year (the 40% band was abolished in 2025). Above €40,000 the person must continue as an FIE or company [V:WS5-018]. A July 2025 act version gave 22% from 2026. That conflicts with EMTA's 2026 page, and EMTA is trusted (LEAD WS5-019).
- **Estonian B2B clients: not usable.** Resident legal persons paying for services into the account owe an extra 22/78 income tax [V:WS5-018], so Estonian company clients would pay about 28% on top.
- **LV/LT clients: potentially attractive, but eligibility UNKNOWN.** The account taxes gross receipts with no expense deduction and no social tax. It would lift net €/h by about 34–36% over the FIE at the mid prices [E:A-WS5-06]. Open questions (resolve: SP-35):
  - whether foreign legal persons may pay into the account;
  - whether it can coexist with an FIE registration;
  - what activity restrictions apply.
- **Caps.** The €40,000 ceiling covers about 1.9 client-years of the mid-price retainer (40,000 / (1,800 × 12)). At 15 h/week, lead-gen revenue of €43,624 would already exceed it [E:A-WS5-38].

### 8.3 FIE setup and running costs vs the start budget

| Item | Cost | Label |
|---|---|---|
| FIE registration fee | not retrieved | UNKNOWN (resolve: SP-15) |
| Business bank account | not retrieved; also unclear whether a personal account may be used | UNKNOWN (resolve: SP-16) |
| Accounting software | not retrieved; includes whether the state's free e-arveldaja suits an FIE | UNKNOWN (resolve: SP-17) |
| Professional liability insurance | not retrieved | UNKNOWN (resolve: SP-18) |
| Social-tax minimum | none for this operator | [V:WS5-003][E:A-WS5-03] |
| Income-tax advances | none in the first year; quarterly from year two | [V:WS5-007] |
| II-pillar payment | assessed annually, due 1 October | [V:WS5-010] |

The model carries these unverified items as an allowance of €150–700 a year [E:A-WS5-11].

### 8.4 Capacity model and daytime tasks
See §7: units, concurrency and daytime hours at 10 / 15 / 20 h per week [E:A-WS5-38][E:A-WS5-33].

### 8.5 E-mail deliverability rules (Google/Yahoo 2024, Microsoft Outlook 2025)
UNKNOWN in this run (resolve: SP-30). Gmail/Yahoo bulk-sender requirements (SPF/DKIM/DMARC, one-click unsubscribe, spam-rate ceiling) and the 2025 Outlook.com high-volume sender rules were not re-verified. No figures are given.

The tooling consequence is still built into the model as an allowance [E:A-WS5-30]:
- separate sending domains and several warmed mailboxes per client;
- a warm-up period before results, which drives the €80–300 per client-month allowance and the 15 h onboarding [E:A-WS5-27].

### 8.6 The buyer's alternative cost (in-house SDR / CRM admin)
Formula: employer monthly cost = gross wage × (1 + employer contributions) [E:A-WS5-37].
- **EE:** employer social tax is 33% [V:WS5-001]. The employer unemployment-insurance rate and wages by occupation are UNKNOWN (resolve: SP-25, SP-28).
- **LV:** employer contribution rate and wages by occupation are UNKNOWN (resolve: SP-26, SP-28).
- **LT:** employer contribution rate and wages by occupation are UNKNOWN (resolve: SP-27, SP-28).

WS2 obtained no job-posting salary ranges. Until resolved, compare a retainer price only against the published agency price [V:WS3-008].

### 8.7 Late payments
Intrum European Payment Report 2025 data for EE, LV and LT was not retrieved: UNKNOWN (resolve: SP-29). The published Baltic retainer bills monthly in advance with 28 days' notice [V:WS3-008]. That is the only payment-terms evidence found.

---

## 9. Conflicts between sources

| Topic | Source A | Source B | Trusted | Why |
|---|---|---|---|---|
| Income-tax rate 2026 | 24% from 2026 under the 2025 security-tax package (LEAD WS5-009) | 22% from 1 Jan 2026 [V:WS5-006]; increase cancelled (LEAD WS5-008) | 22% | EMTA's 2026 page postdates the plan and comes from the tax authority. |
| Entrepreneur-account rate 2026 | 22% (July 2025 act version, LEAD WS5-019) | 20% in 2026 [V:WS5-018] | 20% | EMTA's 2026 page appeared in two separate searches. Re-check SP-35. |
| Is social tax deductible? | "social tax … cannot be shown as business expenses" [V:WS5-004] | business income ÷ 1.33; income tax on the social-tax-adjusted base [V:WS5-002][V:WS5-007] | both | Not a real conflict. Social tax is not a business expense, but it reduces its own base and the income-tax base. |
| 2026 social-tax monthly rate | €886; quarterly minimum €877.14 [V:WS5-001][V:WS5-003] | EMTA's FIE maxima (€36,867.60 [V:WS5-002]; €2,234.40 [V:WS5-010]) only add up if the rate is €886 for 3 months and €946 for 9 months: 0.33 × 10 × (886 × 3 + 946 × 9) = 36,867.60 [E:A-WS5-03] | open | Possibly a mid-2026 rise. Irrelevant for this operator, whose employer's social tax exceeds either. UNKNOWN (resolve: SP-37) |
| VAT-ID provision for suppliers | ASSIGNMENTS cites Art. 214(1)(d) | Reg. 282/2011 Art. 3: (d) is services received, (e) is services supplied [V:WS5-016] | (e) | Directive and regulation wording. |
| The brief's tax wording | literal S = 0.33 × P gives net 52.26% | official 1.33 mechanism gives net 58.65% [E:A-WS5-01] | official | Statute and EMTA guidance [V:WS5-002]. |

## 10. Search-language log

| Language | Example queries | What it found / didn't |
|---|---|---|
| ET | "FIE sotsiaalmaks 33% ettevõtlustulu avansilised maksed töötaja miinimumkohustus 2026"; "tulumaksumäär 2026 jääb 22 protsendile…"; "piiratud maksukohustuslane registreerimine teenuse osutamine…"; "ettevõtluskonto maksumäär 2026…" | Found EMTA handbooks [V:WS5-002][V:WS5-003][V:WS5-010][V:WS5-014][V:WS5-015] (FIE obligations, advance-payment exemption, II pillar, services, limited taxable person), the EMTA 2026 tax-changes page, Riigi Teataja acts, fin.ee news and accounting-firm blogs. Did not find a clear statement on VAT-ID duty for cross-border services. |
| EN | "self-employed person FIE social tax income tax 2026 …"; "Estonia VAT rate 24% from 1 July 2025"; "VAT Directive Article 214(1)(d) …"; "entrepreneur account 2026 tax rate …" | Found EMTA English pages [V:WS5-001][V:WS5-007][V:WS5-011][V:WS5-012][V:WS5-013][V:WS5-018] (social tax, income tax, VAT rate and threshold, SME scheme, entrepreneur account) and EUR-Lex [V:WS5-016]. Secondary sources were e-resident VAT guides. |
| LV | not run: search budget exhausted | LV price evidence comes from WS3 (dih.lv catalogue, LV-language pages) and WS2 (LIAA). |
| LT | not run: search budget exhausted | LT price evidence comes from WS3 (aigentas.lt, webxpert.lt, Ripe Leads). |
| RU | not run: search budget exhausted | none |

Fetched directly (not searched): claude.com/pricing; GitHub n8n `LICENSE.md` and `license-faq.md`. Vendor domains tested and refused by the proxy: n8n.io, make.com, instantly.ai, smartlead.ai, hunter.io, support.google.com, intrum.com, lhv.ee and emta.ee.

## 11. UNKNOWNs (cheapest resolution first)

1. **Tool prices (2026):** UNKNOWN. Resolve: SP-01…SP-14, SP-19. Open each official pricing page in a normal browser (about 2 minutes each, 30 minutes total). Then paste the values into `WS5_models.py` (`OVERHEAD`, `tools_month`, `direct_cost`) and re-run.
2. **Partner and affiliate terms:** UNKNOWN. Resolve: SP-20…SP-24, from the official programme pages. Record the commission %, duration and requirements.
3. **Market prices** for CRM packages and retainers in EE/LT, automation in EE/LV, lead-gen retainers in EE/LV, and pay-per-meeting everywhere, plus FI/SE/PL/DE comparables: UNKNOWN. Resolve: SP-33 and SP-34 with LV/LT/RU/ET queries.
4. **Hourly freelance rates** by country, and the Upwatcher "$29.50/h" lead: UNKNOWN. Resolve: SP-31 and SP-32. Cheapest test: an Upwork search for "Pipedrive" / "n8n" filtered to Estonia, Latvia and Lithuania, recording the rates on 20 profiles per country in aggregate only.
5. **Entrepreneur account for LV/LT company clients:** UNKNOWN. Resolve: SP-35, by e-mailing EMTA: "May a non-resident legal person pay for services into an ettevõtluskonto, and may the holder also be registered as an FIE?"
6. **VAT ID for cross-border invoicing (Art. 214(1)(e)):** UNKNOWN. Resolve: SP-36, through an EMTA consultation.
7. **Sales hours per win, win rates, delivery hours and churn:** ESTIMATE only [E:A-WS5-15][E:A-WS5-29]. Resolve with WS6 benchmarks, plus two interview questions to Baltic CRM partners and agencies: "hours per Pipedrive setup for a 10-user SME?" and "average retainer length in months?"
8. **Wages and employer contributions** for the buyer's alternative cost: UNKNOWN. Resolve: SP-25…SP-28 from the national statistics occupation tables.
9. **Late-payment data:** UNKNOWN. Resolve: SP-29 (Intrum EPR 2025 country pages).
10. **Deliverability rules:** UNKNOWN. Resolve: SP-30 (Google, Yahoo and Microsoft sender pages).
11. **FIE setup costs** (registration, bank, accounting, insurance): UNKNOWN. Resolve: SP-15…SP-18.
12. **Monthly social-tax rate during 2026** (€886 vs €946): UNKNOWN. Resolve: SP-37. **Deductibility of the II pillar for the FIE**: UNKNOWN. Resolve: SP-38. Both are immaterial to the results.

## 12. Synthesis inputs

**Willingness-to-pay evidence by country and component** (score from one to five, where five = most favourable to the operator). All evidence is supply-side published prices or grant rules, not transactions.

| Country | A: CRM setup | B: Automation | C: Lead generation |
|---|---|---|---|
| EE | **3**: agency setup €110–150/h [V:WS3-005]; EIS mentor about €147–149/h [E:A-WS2-05]; EIS consultant fees ≤ 50% of €2,000–5,000 aid [V:WS2-007], but a newcomer is ineligible as advisor [V:WS2-009]; no package price | **2**: no EE automation price found; only the general development rate €110–150/h [V:WS3-005] | **2**: priced per conversation, amounts unpublished [V:WS3-004]; contact lists €140–1,590 + VAT [V:WS3-003] |
| LV | **4**: catalogue bundles €2,990–7,440 [V:WS3-017][V:WS3-018]; €5,000 implementation [V:WS3-019]; LIAA 100% aid ≤ €5,000 [V:WS2-020], status uncertain [V:WS2-019] | **2**: funding exists (AI grants up to €200,000 [V:WS2-022]; EDIC testing ≤ €20,000 [V:WS3-046]) but no price list | **2**: no LV retainer price found; the LT agency covers LV [V:WS3-009] |
| LT | **2**: only custom builds €9,500–15,000 [V:WS3-025]; configuration packages UNKNOWN | **3**: published €300–3,000+ [V:WS3-024]; the low band is not viable for a solo operator [E:A-WS5-19] | **3**: €2,850/month after a €3,750 first month, published [V:WS3-008]; one agency only |
| G2 (foreign firms entering the Baltics) | n/a | n/a | Agencies sell Baltic market-entry outbound to foreign firms [V:WS3-053]; the retainer price above applies [V:WS3-008]; score as LT C (**3**) |

**Net €/h after Estonian FIE taxes** (unit level, base hours, low / mid / high price):

| Model | Low price | Mid price | High price | Label |
|---|---|---|---|---|
| CRM setup (€1,200 / €2,500 / €5,000) | €16.8 | €34.9 | €69.8 | [E:A-WS5-13][E:A-WS5-14] |
| Automation project (€450 / €1,200 / €3,000) | €9.4 | €25.4 | €63.8 | [E:A-WS5-19][E:A-WS5-20] |
| Lead-gen retainer (€1,000 / €1,800 / €2,850 per month) | €19.5 | €37.9 | €62.1 | [E:A-WS5-25][E:A-WS5-29] |

**Capacity limits** (mid price; the three weekly-hour scenarios [E:A-WS5-09]):

| Model | Units or concurrent clients | Daytime h/week | Label |
|---|---|---|---|
| CRM setup | 9.2 / 14.7 / 20.2 projects a year (1.2 / 1.9 / 2.6 in parallel) | 2.5 / 3.8 / 5.0 | [E:A-WS5-38][E:A-WS5-33] |
| Automation project | 14.1 / 22.5 / 30.8 projects a year | 1.0 / 1.5 / 2.0 | [E:A-WS5-38][E:A-WS5-33] |
| Lead-gen retainer | 1.3 / 2.0 / 2.8 concurrent clients | 3.0 / 4.5 / 6.0 | [E:A-WS5-38][E:A-WS5-33] |

## 13. Notes for other workstreams and the lead
- **WS3:** the model's price levels are built on WS3's published prices [V:WS3-005][V:WS3-008][V:WS3-017][V:WS3-019][V:WS3-024]. Any new published EE/LT CRM package, EE/LV retainer or pay-per-meeting price should replace A-WS5-13, A-WS5-19 or A-WS5-25, after which `WS5_models.py` should be re-run [E:A-WS5-13].
- **WS6:** sales hours per win and churn are the weakest inputs [E:A-WS5-15][E:A-WS5-29]. WS6 reply, meeting and sales-cycle benchmarks should replace them.
- **WS4:**
  - The n8n licence lets the operator host client workflows [V:WS5-022], which makes him a processor (DPA, sub-processors).
  - Lead generation relies on separate sending domains and mailboxes [E:A-WS5-30].
  - Art. 214(1)(e), not (d), is the supplier VAT-ID rule [V:WS5-016].
- **WS2:** the EIS "digital advisor" rule (at least three similar projects in four years [V:WS2-009]) shuts the operator out of grant-funded EE projects at the start.
- **Lead and summary:** the brief's tax assumption is consistent with official 2026 rules under the 1.33 reading, giving a net share of 58.65% [E:A-WS5-01].
- **Process note for the lead:** `tools/merge_sources.py` ignores CLI flags and always writes `research/sources.csv`. WS5 triggered it once by mistake and deleted the generated file at once. No fragment was changed.
