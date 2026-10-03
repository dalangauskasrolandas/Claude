# Assumptions — WS5 (Pricing, unit economics & tooling)

Every model input used in `research/05_pricing_unit_economics.md` and `research/_work/data/WS5_models.py`. Format per CONVENTIONS.md. Evidence was gathered via web-search extracts on 2026-10-03. Direct page fetching was blocked except for claude.com and GitHub. The session-wide WebSearch budget ran out after 24 WS5 queries.

**Reading guide.** Tax and VAT inputs (A-WS5-01…07) rest on VERIFIED primary sources. Price levels (A-WS5-13, 19, 25) are anchored to VERIFIED published Baltic prices found by WS2/WS3. Hours, churn and tool-cost allowances are ESTIMATES. No benchmark could be retrieved for these in this run, so each has a range and enters the sensitivity tables. No vendor list price that went unverified is used as a fact anywhere. Unverified cost items are explicit allowances.

---

## A. Tax and VAT (Estonia, 2026)

### A-WS5-01 — FIE tax formula (official mechanism, 2026)
- Value: net = 0.5865 × P (58.65% of profit), where social tax S = 0.2481 × P and income tax IT = 0.1654 × P.
- Formula: P = revenue excl. VAT − deductible business expenses. S = 0.33 × P / 1.33 (capped at €36,867.60 in 2026). IT = 0.22 × (P − S). Net = P − S − IT = P × 0.78 / 1.33.
- Inputs: [V:WS5-001] social tax 33%; [V:WS5-002] FIE social tax is computed by dividing business income after expenses by 1.33; [V:WS5-004] social tax is not a business expense; [V:WS5-007] income tax applies to the social-tax-adjusted business income; [V:WS5-006] 22% income tax in 2026. The statute wording is a LEAD (WS5-005, act version uncertain).
- Basis/rationale: this matches the brief ("22% income tax and 33% social tax on profit; social tax is deductible") when "deductible" means the statutory 1.33 divisor. Social tax is deducted from its own base and from the income-tax base. A literal reading (S = 0.33 × P; IT = 0.22 × (P − S)) gives net = 0.5226 × P. That is 6.4 percentage points too low, and it appears only as a sensitivity row.
- Confidence: high
- Used in: 05 §3, §6, §7; WS5_models.py `tax_fie()`

### A-WS5-02 — No basic exemption available on FIE income
- Value: €0 of basic exemption applied to FIE profit. Every euro of FIE profit is taxed at 22% income tax.
- Formula: n/a
- Inputs: [V:WS5-006] the 2026 basic exemption is €700/month (€8,400/year) regardless of income, and the "tax hump" is abolished.
- Basis/rationale: the operator has a full-time salary (BRIEF §2), which already uses the €700/month exemption, assuming the exemption application sits with the employer. Because the 2026 exemption no longer tapers with income, side income does not claw back any exemption, so the marginal rate is a flat 22%.
- Confidence: high (if the salary is ≥ €700/month and the exemption is claimed at the employer)
- Used in: 05 §3; WS5_models.py

### A-WS5-03 — No social-tax minimum or quarterly advances
- Value: €0 social-tax advances. Social tax is due only on actual profit, assessed from the annual return (form E).
- Formula: the exemption applies if the employer's social tax for the operator is ≥ €877.14 per quarter (= 886 × 3 × 0.33).
- Inputs: [V:WS5-003], [V:WS5-001]
- Basis/rationale: any full-time salary at or above the €886 monthly rate meets the condition. Without employment, the minimum would be at least €3,508.56 a year (= 4 × €877.14, derived from [V:WS5-003]), which by itself would exceed the operator's €200–500 budget.
- Confidence: high
- Used in: 05 §3, §8.3

### A-WS5-04 — II-pillar (funded pension) variant
- Value: F = 0.02 × P / 1.33 = 1.50% of P at the default 2% rate. Net cash = 0.5747 × P if F is deductible from the income-tax base, or 0.5714 × P if it is not.
- Formula: IT = 0.22 × (P − S − F) (deductible case)
- Inputs: [V:WS5-010] EMTA computes the FIE contribution from social-tax-adjusted business income; it is not a business expense on form E but is shown in table 9.1 of form A.
- Basis/rationale: deductibility is inferred from the contribution appearing on form A, and is not explicitly confirmed. The difference is 0.33 percentage points, so it is immaterial. F is the operator's own pension saving, not a cost, so it is shown as a variant only. The 4% or 6% rates are optional.
- Confidence: medium (rule) / low (deductibility)
- Used in: 05 §3, §6.4; WS5_models.py `tax_fie(ii_pillar=True)`

### A-WS5-05 — Social-tax cap not binding
- Value: the cap binds only at P ≥ €148,588.
- Formula: 36,867.60 / 0.33 × 1.33 = 148,588
- Inputs: [V:WS5-002]
- Basis/rationale: modelled profits are far below this.
- Confidence: high
- Used in: 05 §3

### A-WS5-06 — Entrepreneur-account variant (foreign clients only; eligibility UNKNOWN)
- Value: tax = 20% of gross receipts (22% with the 2% II pillar). Costs are not deductible. Receipts must stay ≤ €40,000/year. Net = 0.80 × receipts − costs.
- Formula: net = R × (1 − 0.20) − C
- Inputs: [V:WS5-018]. A conflicting LEAD is WS5-019 (a July 2025 act version gave 22% from 2026; EMTA's 2026 page says 20%, and EMTA is trusted).
- Basis/rationale: Estonian resident legal persons paying into the account owe an extra 22/78 (28.2%) on top [V:WS5-018], which makes it unusable for Estonian B2B clients. EMTA's wording targets resident payers. Several points are UNKNOWN: whether foreign (LV/LT) legal persons may pay into the account without restriction, whether it can coexist with FIE registration, and any other activity restrictions.
- Confidence: low (eligibility)
- Used in: 05 §6.4, §8.2; WS5_models.py `tax_entre_account()`

### A-WS5-07 — VAT treatment in the model
- Value: prices are excl. VAT. The operator is not VAT-registered in the base case, and tool and subscription costs carry 24% non-deductible VAT (multiplier 1.24).
- Formula: tool cost incl. VAT = list price × 1.24
- Inputs: [V:WS5-011] 24% standard rate; [V:WS5-012] the €40,000 registration threshold counts only Estonian place-of-supply turnover; [V:WS5-014] B2B services to LV/LT businesses are taxed in the customer's state; [V:WS5-015] limited-taxable-person self-assessment applies to services bought from abroad; [V:WS5-016] Art. 214(1)(e).
- Basis/rationale: B2B clients deduct VAT, so output VAT does not change the price. A non-registered FIE cannot deduct input VAT on tools. Foreign SaaS VAT is either self-assessed under the limited-taxable-person regime or charged by the supplier. Voluntary registration would recover tool VAT but adds monthly returns (hours UNKNOWN).
- Confidence: medium
- Used in: 05 §8.1; WS5_models.py `VAT`

## B. Capacity and overhead

### A-WS5-08 — Working weeks per year
- Value: 46
- Formula: 52 − 6
- Inputs: none (ESTIMATE)
- Basis/rationale: about 6 weeks lost to holidays, day-job peaks and illness for an evenings-and-weekends operator.
- Confidence: medium-low
- Used in: 05 §7; WS5_models.py `WEEKS_PER_YEAR`

### A-WS5-09 — Weekly hours scenarios
- Value: 10 / 15 / 20 h per week
- Formula: n/a
- Inputs: BRIEF §2 (10–20 h/week)
- Basis/rationale: given by the brief.
- Confidence: high
- Used in: 05 §7

### A-WS5-10 — Fixed non-client hours
- Value: 72 h per year
- Formula: bookkeeping and invoicing 12 (1 h/month) + annual tax return 4 + tool upkeep and learning 48 (4 h/month) + miscellaneous 8
- Inputs: ESTIMATE
- Basis/rationale: FIE bookkeeping and form E/A filing [V:WS5-002], plus the upkeep needed to stay current on n8n/Make, CRM and AI tools.
- Confidence: medium-low
- Used in: 05 §7; WS5_models.py `FIXED_ADMIN_H`

### A-WS5-11 — Fixed annual overhead (€, incl. VAT)
- Value: low €363 / base €606 / high €1,980
- Formula: Claude subscription (USD) × 0.86 × 1.24 + other allowance
- Inputs: Claude Pro is $200/yr on annual billing (low) or 12 × $20 = $240/yr monthly (base). Max "from $100/month" = $1,200/yr (high) [V:WS5-020]. The other allowance (domain, business e-mail, accounting software, bank fees, insurance) is €150 / €350 / €700. Prices for these items are UNKNOWN in this run.
- Basis/rationale: Claude is the only verified price. The rest is an explicit allowance to be replaced by verified quotes (search plan items SP-14…SP-19).
- Confidence: low
- Used in: 05 §7, §8.3; WS5_models.py `OVERHEAD`

### A-WS5-12 — FX rate
- Value: €0.86 per USD
- Formula: n/a
- Inputs: ESTIMATE (working rate, not an ECB fixing)
- Basis/rationale: used only to convert Claude prices. A ±10% FX move shifts base overhead by about €26 a year, which is immaterial.
- Confidence: low (immaterial)
- Used in: WS5_models.py `FX`

## C. CRM setup model

### A-WS5-13 — CRM setup price levels (excl. VAT)
- Value: €1,200 / €2,500 / €5,000
- Formula: low ≈ 11 h × €110/h; mid = 50% × €5,000; high = €5,000
- Inputs: low comes from the Fontakt setup-work rate of €110/h [V:WS3-005], roughly the 12 h of implementation bundled in the LV EDIH Pipedrive packages [V:WS3-017]. Mid is the EIS RTE software-adoption grant cap, where consultant fees are ≤ 50% of a ≤ €5,000 aid [V:WS2-007][V:WS2-009]. High is the LV EDIH catalogue's generic CRM implementation package of €5,000 [V:WS3-019], which also equals the LIAA ceiling for 100% aid to micro/small firms on projects ≤ €5,000 [V:WS2-020].
- Basis/rationale: published anchors exist in EE (hourly rate), EE (grant cap) and LV (package). There is no LT configuration-package price. LT only has custom-CRM builds at €9,500–15,000 [V:WS3-025], which is a different scope. A newcomer cannot be the funded EIS "digital advisor" before completing ≥ 3 similar projects in 4 years [V:WS2-009].
- Confidence: medium (anchors verified; actual willingness to pay unknown)
- Used in: 05 §5, §6; WS5_models.py `PROJECTS['CRM setup']`

### A-WS5-14 — CRM delivery hours
- Value: base 25 h (range 15–40)
- Formula: 15 h vendor-partner bundle × about 1.7 newcomer factor
- Inputs: the LV partner bundle gives 12 h implementation + 3 h training [V:WS3-018]. Ready-made CRM implementations take 4–8 weeks and include audit, Excel migration, configuration and training [V:WS3-057].
- Basis/rationale: a solo newcomer without templates is slower than an established partner. Data cleanup scope drives the range.
- Confidence: low-medium
- Used in: 05 §6; WS5_models.py

### A-WS5-15 — CRM sales hours per won project
- Value: base 12 h (range 6–25)
- Formula: about 4 h per qualified opportunity (discovery, proposal, follow-up) × 3 opportunities per win
- Inputs: ESTIMATE. No Baltic sales-effort or win-rate benchmark was available (WS6 benchmarks may replace this).
- Basis/rationale: with no network (BRIEF §2), early deals sit near the high end.
- Confidence: low
- Used in: 05 §6; WS5_models.py

### A-WS5-16 — CRM admin hours per project
- Value: 2 h
- Formula: contract + invoice + bookkeeping entry
- Inputs: ESTIMATE
- Basis/rationale: small fixed admin per deal.
- Confidence: medium
- Used in: WS5_models.py

### A-WS5-17 — CRM unbilled post-go-live support
- Value: 3 h
- Formula: n/a
- Inputs: ESTIMATE
- Basis/rationale: fixes and questions in the first weeks after go-live.
- Confidence: low-medium
- Used in: WS5_models.py

### A-WS5-18 — CRM direct costs per project (incl. VAT)
- Value: €0 (range €0–100)
- Formula: n/a
- Inputs: ESTIMATE. The cost of vendor trial, sandbox and partner accounts is UNKNOWN (search plan SP-01…SP-03).
- Basis/rationale: assumes free trial or partner access. The upper bound allows for a paid data-migration utility.
- Confidence: low
- Used in: WS5_models.py

## D. Automation project model

### A-WS5-19 — Automation price levels (excl. VAT)
- Value: €450 / €1,200 / €3,000
- Formula: published band edges
- Inputs: aigentas.lt (LT) publishes €450–1,200 for process automation and €1,500–3,000+ for full implementation [V:WS3-024].
- Basis/rationale: this is the only published Baltic automation price list found. It is from LT only, and EE/LV equivalents are UNKNOWN.
- Confidence: medium
- Used in: 05 §5, §6

### A-WS5-20 — Automation delivery hours
- Value: base 15 h (range 8–30)
- Formula: n/a
- Inputs: ESTIMATE. The scope reference is "one process, up to 2 integrations" [V:WS3-024].
- Basis/rationale: one revenue workflow (inquiry → CRM → AI-drafted reply → follow-up task), including testing, documentation and handover.
- Confidence: low-medium
- Used in: WS5_models.py

### A-WS5-21 — Automation sales hours per won project
- Value: base 8 h (range 4–16)
- Formula: n/a
- Inputs: ESTIMATE
- Basis/rationale: a smaller ticket and shorter decision than a CRM setup.
- Confidence: low
- Used in: WS5_models.py

### A-WS5-22 — Automation admin and hypercare
- Value: admin 1.5 h; unbilled hypercare 3 h
- Formula: n/a
- Inputs: ESTIMATE
- Basis/rationale: small fixed overhead per deal.
- Confidence: medium-low
- Used in: WS5_models.py

### A-WS5-23 — Automation direct cost per project (incl. VAT)
- Value: €10 (range €0–50)
- Formula: 200 test runs × (4,000 input + 1,000 output tokens) on Sonnet 5.5 = 0.8 MTok × $2 + 0.2 MTok × $10 = $3.60, rounded up to a €10 allowance incl. VAT
- Inputs: [V:WS5-020] API prices
- Basis/rationale: in the base case, hosting costs the operator nothing because the workflow runs on the client's instance or n8n Cloud account. An operator-hosted instance is allowed by the licence FAQ [V:WS5-022], but VPS prices are UNKNOWN.
- Confidence: medium (immaterial)
- Used in: WS5_models.py

### A-WS5-24 — Client LLM run-cost example (pass-through)
- Value: $4.20/month (Sonnet 5.5), $2.10 (Haiku 4.5), $8.40 (Opus 5.5)
- Formula: 300 inquiries/month × (3,000 input × in-price + 800 output × out-price) / 1,000,000
- Inputs: [V:WS5-020]. The token counts per inquiry are an ESTIMATE.
- Basis/rationale: shows that AI API cost is immaterial against project prices of €450–3,000.
- Confidence: medium
- Used in: 05 §4

## E. Lead-generation retainer model

### A-WS5-25 — Lead-gen monthly price levels (excl. VAT)
- Value: €1,000 / €1,800 / €2,850 per month
- Formula: high = published benchmark; mid ≈ 0.63 × high; low ≈ 0.35 × high
- Inputs: Ripe Leads (Vilnius) charges €2,850/month after a €3,750 first month, with tools and data included [V:WS3-008].
- Basis/rationale: this is the only published Baltic retainer found. The two lower levels are scenarios for a solo, unproven operator, not market observations.
- Confidence: low (low and mid levels)
- Used in: 05 §6

### A-WS5-26 — Lead-gen delivery hours per client-month
- Value: base 20 h (range 14–30)
- Formula: list building and enrichment 6 + copy and multilingual sequence iteration 4 + campaign ops and deliverability 3 + reply handling and booking 5 + reporting/client call 2
- Inputs: ESTIMATE
- Basis/rationale: steady-state multilingual (EN/RU/LT) outbound for one client.
- Confidence: low
- Used in: WS5_models.py

### A-WS5-27 — Lead-gen onboarding hours (once per client, unbilled unless there is a setup fee)
- Value: 15 h
- Formula: n/a
- Inputs: ESTIMATE
- Basis/rationale: ICP workshop, sending domains and mailboxes, warm-up supervision, first list and first copy.
- Confidence: low
- Used in: WS5_models.py

### A-WS5-28 — Lead-gen sales hours per won client
- Value: base 15 h (range 8–30)
- Formula: n/a
- Inputs: ESTIMATE
- Basis/rationale: a higher-trust recurring commitment than a one-off project.
- Confidence: low
- Used in: WS5_models.py

### A-WS5-29 — Lead-gen monthly churn
- Value: base 15% (range 8–25%), giving an expected client lifetime of 6.7 (12.5–4.0) months
- Formula: lifetime L = 1 / churn (constant monthly hazard)
- Inputs: the published Baltic retainer is cancellable monthly with 28 days' notice [V:WS3-008]. No churn benchmark was found.
- Basis/rationale: no lock-in implies high churn. This parameter is the largest single driver of retainer economics after price.
- Confidence: low
- Used in: 05 §6.3

### A-WS5-30 — Lead-gen tools and data per client-month (incl. VAT)
- Value: €150 (range €80–300)
- Formula: allowance
- Inputs: ESTIMATE. Vendor prices are UNKNOWN in this run (search plan SP-05…SP-12). The market norm is that tools are included in the fee [V:WS3-008].
- Basis/rationale: covers dedicated sending domains, several mailboxes, a share of a sending/warm-up platform, enrichment credits and an optional LinkedIn tool.
- Confidence: low
- Used in: 05 §6.3

### A-WS5-31 — Lead-gen admin per client-month
- Value: 1 h
- Formula: n/a
- Inputs: ESTIMATE
- Basis/rationale: invoice, bookkeeping and contract admin.
- Confidence: medium-low
- Used in: WS5_models.py

### A-WS5-32 — Lead-gen setup fee
- Value: €0 in the base case; €900 in the alternative case
- Formula: 3,750 − 2,850 = 900
- Inputs: [V:WS3-008]
- Basis/rationale: the alternative mirrors the published first-month premium.
- Confidence: medium
- Used in: 05 §6.3

## F. Cross-model parameters

### A-WS5-33 — Share of hours that must fall in business hours
- Value: CRM 25%, automation 10%, lead-gen 30%
- Formula: task decomposition
- Inputs: ESTIMATE
- Basis/rationale: CRM needs a requirements workshop, user training and go-live support. Automation needs a kickoff and a handover call. Lead generation needs same-day reply handling, meeting booking and client calls.
- Confidence: low
- Used in: 05 §7

### A-WS5-34 — Elapsed calendar weeks per project (for concurrency)
- Value: CRM 6, automation 3
- Formula: n/a
- Inputs: CRM implementations take 4–8 weeks [V:WS3-057]. The automation figure is an ESTIMATE.
- Basis/rationale: converts projects per year into projects running in parallel.
- Confidence: low-medium
- Used in: 05 §7

### A-WS5-35 — Effective billed rate per delivery hour (derived)
- Value: see results table
- Formula: price / delivery hours
- Inputs: [E:A-WS5-13], [E:A-WS5-14], [E:A-WS5-19], [E:A-WS5-20], [E:A-WS5-25], [E:A-WS5-26]
- Basis/rationale: allows comparison with hourly market rates: €110–150/h agency [V:WS3-005] and about €147–149/h for the EIS mentor [E:A-WS2-05].
- Confidence: as inputs
- Used in: 05 §6.1

### A-WS5-36 — Price required for a target net €/h (derived)
- Value: see results table
- Formula: projects: P_req = target × unit hours / 0.5865 + direct cost. Retainer: P_req = target × lifetime hours / (0.5865 × L) + tools per month.
- Inputs: [E:A-WS5-01] and the hours inputs. The targets of €15, €25 and €40 per hour are scenario values, not benchmarks.
- Basis/rationale: turns the model into a price floor for each net-hourly ambition.
- Confidence: as inputs
- Used in: 05 §6.5

### A-WS5-37 — Buyer's alternative cost (formula only; inputs mostly UNKNOWN)
- Value: employer monthly cost = gross wage × (1 + employer contribution rate)
- Formula: see value
- Inputs: EE social tax 33% [V:WS5-001]. The EE employer unemployment-insurance rate, the LV and LT employer contribution rates, and wages by occupation (SDR/sales rep, CRM admin) are all UNKNOWN in this run (search plan SP-24…SP-27).
- Basis/rationale: price anchor requested by the lead analyst.
- Confidence: n/a
- Used in: 05 §8.6

### A-WS5-38 — Capacity model
- Value: see results table
- Formula: projects/year = (H × 46 − 72) / unit hours. Concurrent retainer clients N = ((H × 46 − 72) / 12) / (delivery + admin + churn × (onboarding + sales)).
- Inputs: [E:A-WS5-08], [E:A-WS5-09], [E:A-WS5-10] and the hours inputs above
- Basis/rationale: a supply-side ceiling that assumes a full pipeline. It is not a demand forecast.
- Confidence: as inputs
- Used in: 05 §7
