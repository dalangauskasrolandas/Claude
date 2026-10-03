# Assumptions — red team (WS8 = combined verifier/red team, 2026-10-03)

Scenario arithmetic only. Placeholders are marked as such; none is a finding. Recomputation: `research/_work/data/VER_recompute.py`.

### A-WS8-01 — Net €/h when the cold-start sales effort is 40 h or 60 h per won CRM project
- Value: at 40 sales hours: EUR 10.1 / 20.9 / 41.9 (price EUR 1,200 / 2,500 / 5,000). At 60 sales hours: EUR 7.8 / 16.3 / 32.6. WS5 base (12 h) gives EUR 16.8 / 34.9 / 69.8; WS5 high (25 h) gives EUR 12.8 / 26.7 / 53.3.
- Formula: net €/h = price × 0.5865 ÷ (25 delivery + S sales + 2 admin + 3 support), with S = 40 or 60.
- Inputs: [E:A-WS5-14] delivery 25 h; [E:A-WS5-16] [E:A-WS5-17] admin 2 h and support 3 h; [E:A-WS5-15] base sales hours; [E:A-WS5-01] net share 0.5865
- Basis/rationale: WS5's sales-hour range (6–25 h) has no Baltic benchmark behind it (UNKNOWN in WS6). A first client for an operator with no network, no references and evening-only availability is plausibly above the WS5 high case; 40 h and 60 h are sensitivity points, not findings. The contacts-per-win grid [E:A-WS8-03] shows why.
- Confidence: low
- Used in: red_team.md R3, R7, "Where the workstreams are too optimistic"

### A-WS8-02 — Break-even sales hours per won CRM project for net EUR 15 and EUR 25 per hour
- Value: net EUR 15 per hour: EUR 1,200 → 16.9 h; EUR 2,500 → 67.7 h; EUR 5,000 → 165.5 h of sales effort per won project. Net EUR 25 per hour: EUR 2,500 → 28.7 h; EUR 5,000 → 87.3 h; EUR 1,200 → not reachable even with zero sales hours (the price floor is EUR 1,790 [E:A-WS5-36]).
- Formula: allowed total hours = price × 0.5865 ÷ target; sales hours = allowed total − 25 − 2 − 3.
- Inputs: as [E:A-WS8-01]
- Basis/rationale: gives a kill-criterion in hours that can be measured in a pilot. EUR 15 per hour is a scenario target (same as [E:A-WS5-36]), not a market benchmark.
- Confidence: medium (arithmetic)
- Used in: red_team.md R3, Kill criteria

### A-WS8-03 — Contacts needed per won client (scenario grid)
- Value: 133–667 contacts per won client.
- Formula: 1 ÷ (reply rate × meetings per reply × wins per meeting), with reply rate ∈ {3%, 5%}, meetings per reply ∈ {25%, 50%}, wins per meeting ∈ {20%, 30%}.
- Inputs: reply rate 3–5% is a vendor figure for cold e-mail (LEAD RT-001; not a Baltic benchmark). The other two ranges are placeholders with no source (UNKNOWN in WS6).
- Basis/rationale: arithmetic illustration of how many firms must be contacted per win; it becomes evidence only when a pilot replaces the placeholders.
- Confidence: low
- Used in: red_team.md R1, R7

### A-WS8-04 — Pool exhaustion: wins if every named-e-mail firm in the 11–50 bucket were contacted once
- Value: EE 1.1–7.6; LV 0.8–5.6; LT 1.4–9.8 wins.
- Formula: pool ÷ contacts per win, with pool = EE 703–1,019, LV 542–747, LT 957–1,300 [E:A-WS9-02] and contacts per win 133–667 [E:A-WS8-03]; low = low pool ÷ 667, high = high pool ÷ 133.
- Inputs: [E:A-WS9-02], [E:A-WS8-03]
- Basis/rationale: the 11–50 bucket is the likelier buyer segment (1-10 is mostly very small firms). Re-contacting the same firms adds touches, not new firms. Vendor-database counts before language, sanctions and maritime-adjacent screens, so the real pool is smaller.
- Confidence: low
- Used in: red_team.md R1, R7

### A-WS8-05 — Gap between the break-even price and published entry prices for automation
- Value: the price for net EUR 15 per hour (EUR 713) is 2.4 times the Lithuanian entry price of EUR 300; the price for net EUR 25 per hour (EUR 1,182) is 3.9 times. Against the Estonian "from EUR 100" entry price the ratios are 7.1 and 11.8.
- Formula: 713 ÷ 300 = 2.4; 1,182 ÷ 300 = 3.9; 713 ÷ 100 = 7.1; 1,182 ÷ 100 = 11.8.
- Inputs: [E:A-WS5-36] break-even prices; [V:WS3-024] EUR 300 entry (aigentas.lt); [V:RT-005] EUR 100 entry (Growlinee, search-answer wording)
- Basis/rationale: entry prices are for the simplest offer (one process, up to two integrations in the Lithuanian case) and do not show what buyers pay for the scope assumed in the model (15 delivery hours); they show where the low end of the market starts.
- Confidence: medium (arithmetic); low (comparability of scope)
- Used in: red_team.md R2, R6

### A-WS8-06 — Wins per quarter when half of the weekly hours go to selling
- Value: with 13 weeks and 10 / 15 / 20 hours per week: at 12 sales hours per win 5.4 / 8.1 / 10.8; at 25 hours 2.6 / 3.9 / 5.2; at 40 hours 1.6 / 2.4 / 3.2; at 60 hours 1.1 / 1.6 / 2.2.
- Formula: wins = 13 × H × 0.5 ÷ S.
- Inputs: weekly hours from BRIEF §2; S from [E:A-WS5-15] and [E:A-WS8-01]. The 50% selling share is a scenario assumption (first quarter, no pipeline).
- Basis/rationale: shows how slowly the first client arrives when sales effort per win is above the WS5 base case, and that every won project then competes with delivery for the same evening hours.
- Confidence: low
- Used in: red_team.md R3

### A-WS8-07 — Kill-criteria thresholds (test-design parameters, not findings)
- Value: (K1) fewer than 3 of 15–20 owner interviews per country report an own-money purchase in the last 12 months, or fewer than 3 state a budget of at least EUR 1,200; (K2) at least 2 of 3 incumbents quote at or below the break-even prices EUR 1,790 (CRM), EUR 1,182 (automation) or EUR 1,237 per month (lead generation) for comparable scope; (K3) projected sales effort above 28.7 h per won CRM project at EUR 2,500, or no win after 80 selling hours; (K4) positive replies below 1% on at least 100 contacts per language, or interview acceptance below 5% on 20 requests per country; (K5) no written regulator answer within 6 weeks; (K6) the Russian or English version of a message gets less than half the reply rate of the local-language version; (K7) the operator's employment contract or handbook covers sales or consulting side work or requires consent.
- Formula: K1 3 ÷ 20 = 15% and 3 ÷ 15 = 20% incidence; K2 prices from [E:A-WS5-36]; K3 28.7 h from [E:A-WS8-02] and 80 h = twice the 40 h cold-start case [E:A-WS8-01]; K4 1% is one third to one fifth of the vendor's 3–5% reply rate (LEAD RT-001) and 5% is the bottom of the 5–20% acceptance range in [E:A-WS6-04]; K5 and K6 are judgement values.
- Inputs: [E:A-WS5-36], [E:A-WS8-01], [E:A-WS8-02], [E:A-WS6-04], LEAD RT-001
- Basis/rationale: thresholds are set so that a failing test is cheap to run (evenings, no spend) and unambiguous to read. They are decision rules for the operator, not predictions; each can be tightened or loosened without changing the logic.
- Confidence: low (judgement)
- Used in: red_team.md "Kill criteria"

### A-WS8-08 — Micro firms as a share of the up-to-fifty-staff universe
- Value: EE 96.0%; LV 93.9%; LT 96.1% of firms with 0–49 staff are in the `0–9` class; one `10–49` firm for every 24 (EE), 15 (LV) and 24 (LT) micro firms.
- Formula: micro ÷ (micro + small) = 152,205 ÷ 158,489; 99,066 ÷ 105,523; 312,827 ÷ 325,642.
- Inputs: [V:WS1-095] [V:WS1-025] [E:A-WS1-19]
- Basis/rationale: arithmetic on the statistical counts. The `0–9` class is dominated by one-person firms (cannot be cut at five staff in EE or LV data) and ICT surveys do not cover it [V:WS2-053], so adoption and willingness to pay in 94–96% of the in-scope universe are unmeasured.
- Confidence: high for EE (2025); medium for LV (JRC estimate) and LT (2022, pre-2023)
- Used in: red_team.md reason three (customer)

### A-WS8-09 — Net hourly result if the unverified Upwatcher median were right (conditional)
- Value: USD 29.50 per hour ≈ EUR 25.4 gross per hour ≈ EUR 14.9 net per hour after Estonian FIE tax. Conditional on an unverified lead (UNKNOWN); not used as evidence.
- Formula: 29.50 × 0.86 = 25.37; 25.37 × 0.5865 = 14.88.
- Inputs: brief lead (Upwork AI-automation median, May 2026, Upwatcher; not verified, VL-020); working exchange rate 0.86 EUR per USD [E:A-WS5-12]; net share [E:A-WS5-01]
- Basis/rationale: shows what the lead would imply if it held: a global-marketplace reference far below the billed rates of EUR 80–200 per delivery hour implied by the model's mid and high automation prices [E:A-WS5-35]. A median for all postings is not a rate for Baltic client work.
- Confidence: low
- Used in: red_team.md reason six (price), "Where the workstreams are too optimistic"

