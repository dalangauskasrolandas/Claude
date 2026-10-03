# Assumptions — WS3 Competitor map

All inputs trace to `research/_work/sources_WS3.csv` (WS3-xxx), the lead analyst's `sources_WS0.csv` (WS0-xxx) or `sources_WS2.csv` (WS2-xxx). Accessed 2026-10-03.

### A-WS3-01 — Implied service value and hourly rate inside a Latvian grant-catalogue Pipedrive package
- Value: about €1,990 of services per package, about €83 per hour (low confidence)
- Formula: licence cost per user-month L = (P10 − P5) / (5 extra users × 12 months) = (3,990 − 2,990) / 60 = €16.67. Service value S = P5 − (5 users × 12 months × L) = 2,990 − 1,000 = €1,990. Included hours H = 12 h implementation + 12 × 1 h monthly support = 24 h. Implied rate = S / H = 1,990 / 24 ≈ €82.9/h.
- Inputs: [V:WS3-017] P5 = €2,990 excl. VAT (Essential, 5 users, 12 months, 12 h implementation + 1 h/month support); [V:WS3-018] P10 = €3,990 excl. VAT (Essential, 10 users, 12 months, same service hours).
- Basis/rationale: the 5→10-user price step is treated as pure licence cost, and the service hours are taken to be the same in both packages. Any margin on licences is counted as "service", so the true hourly rate could be lower. The catalogue listing date is UNKNOWN. The plan names (Essential/Advanced/Professional) may predate a Pipedrive plan rename, so the price may be pre-2025.
- Confidence: low
- Used in: 03_competitors.md § 6 Price bands (LV, CRM setup); § 12 Synthesis inputs

### A-WS3-02 — Ripe Leads first-year cost and average monthly cost
- Value: €35,100 in the first year, an average of €2,925 per month (excl. VAT)
- Formula: 3,750 + 11 × 2,850 = 35,100; 35,100 / 12 = 2,925
- Inputs: [V:WS3-008] €3,750 for month 1, then €2,850 per month
- Basis/rationale: simple arithmetic. It matches the vendor's own "roughly €35,100" first-year figure (same source).
- Confidence: high
- Used in: 03_competitors.md § 1 Key findings; § 6 Price bands (lead gen)

### A-WS3-03 — Lower bound on providers in the Latvian EDIH catalogue's business-process sections
- Value: at least 45 distinct provider names
- Formula: count of distinct provider names in the provider filters of three dih.lv "Biznesa procesi" catalogue URLs returned by WebSearch (filters: administrative; sales + resource management; operations + sales + resource management). Parsed list: `research/_work/data/WS3_dih_providers.csv`.
- Inputs: [V:WS3-042] (LEAD; filter URLs), extract file above
- Basis/rationale: providers show up in a filter only if they have listings in those categories. Only three filter states and pages 2–3 were seen, so the real total is probably higher. Not all 45 sell CRM, automation or sales tools: the list includes web, e-commerce, document-management, telecom and accounting/ERP vendors (e.g. Visma Enterprise, Tet).
- Confidence: medium that at least 45 such providers exist in these catalogue sections; low that all of them compete with the operator
- Used in: 03_competitors.md § 1 Key findings; § 4 (LV); § 7 Gaps (LV); § 12 Synthesis inputs

### A-WS3-04 — Most a digital consultant can be paid from the Estonian EIS business-software (RTE) grant, and the implied project size
- Value: up to €2,500 of aid per company can pay a digital consultant; total eligible project up to about €10,000
- Formula: consultant share = max aid €5,000 × 50% (consultant fees up to 50% of aid) = €2,500. Project size = max aid / (1 − 50% self-financing) = 5,000 / 0.5 = €10,000.
- Inputs: [V:WS2-007] (aid €2,000–5,000; 50% self-financing; consultant fees up to 50% of aid); [V:WS2-010] (a digital consultant must be involved)
- Basis/rationale: my reading of WS2's summary of the EIS terms. WS2 owns the grant facts, and the exact eligible-cost rules may differ.
- Confidence: medium-low
- Used in: 03_competitors.md § 6 Price bands (EE); § 7 Gaps G-8

### A-WS3-05 — Rubric for competition-intensity scores (1–5, where 5 = least competition)
- Value: scoring rubric used in § 9
- Formula/rubric:
  - 1 = a dominant, established player in this country × component, plus at least 5 local providers with published fixed offers.
  - 2 = at least 3 identified providers serve this country × component (verified via a vendor directory or the provider's own pages), including at least one that claims all-Baltic EN + RU + local-language coverage.
  - 3 = 1–2 identified providers, OR the cell was not adequately searched (neutral default, flagged "provisional").
  - 4 = providers exist but none in the operator's languages or delivery model.
  - 5 = no providers found after a thorough search in EN + the local language + RU.
- Inputs: the provider identifications in § 2–4 (source IDs cited per cell in § 9)
- Basis/rationale: a transparent, count-based rubric. Counts are lower bounds from about thirty searches, so scores lean towards "more competition is unseen" (they can only fall as more searching is done).
- Confidence: medium for cells scored 2; low for cells scored 3 (provisional)
- Used in: 03_competitors.md § 12 Synthesis inputs

### A-WS3-06 — Fontakt CRM price per included user per month
- Value: €89.80 (Regular) and €134.90 (Full) per included user per month
- Formula: 449 / 5 users = 89.8; 1,349 / 10 users = 134.9
- Inputs: [V:WS3-005] Regular €449/month including 5 users; Full €1,349/month including 10 users (extra users €49 each)
- Basis/rationale: per-user anchor for a bundled "CRM software + local service" offer in Estonia. Setup hours are billed on top at €110/h.
- Confidence: high (arithmetic)
- Used in: 03_competitors.md § 6 Price bands (EE, CRM support/retainer)
