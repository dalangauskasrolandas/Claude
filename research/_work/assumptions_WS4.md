# WS4 assumptions (legal-risk scoring)

WS4 makes no numeric market estimates. The only ESTIMATE-type inputs are the judgement-based legal-risk scores used in `04_legal_compliance.md` §8 (Synthesis inputs). Their rubric is recorded here so the scores are traceable and can be re-scored when UNKNOWNs are resolved.

### A-WS4-01 — Legal-risk scoring rubric (1–5, 5 = lowest legal risk for the operator)
- Value: per country × component scores (A CRM setup, B AI/workflow automation, C outbound lead generation) as listed in `04_legal_compliance.md` §8.
- Formula: start from 5 and deduct one point for each of the following that applies (minimum 1):
  1. the core activity needs prior consent from recipients, or the statutory text leaves it unclear whether consent is needed for B2B recipients;
  2. a material sub-case the operator would routinely hit (for example named-employee work addresses, sole traders, LinkedIn messages) has no regulator position or verified statutory answer;
  3. the activity necessarily involves third-party personal data from sources whose lawfulness the operator cannot control (enrichment databases, scraping) or transfers to non-EU sub-processors;
  4. the rule changed recently (2025–2026) or EU-level obligations are in flux (for example the Digital Omnibus on AI), so there is little or no supervisory practice to rely on;
  5. there is evidence of active enforcement in the specific area in that country (not applied in this session because no 2020–2026 case could be verified; this is a known downward-risk gap).
  Add back one point (maximum 5) where a primary source explicitly permits the activity under conditions a solo operator can meet in practice (for example an opt-out link in every message).
- Inputs: [V:WS4-001] [V:WS4-004] [V:WS4-005] (EE); [V:WS4-011] [V:WS4-016] [V:WS4-019] [V:WS4-013] (LV); [V:WS4-028] [V:WS4-031] [V:WS4-034] [V:WS4-036] (LT); EU-level items are UNKNOWN-P in this session (GDPR, AI Act, transfers).
- Basis/rationale: an ordinal judgement, not a probability. It ranks how much legal uncertainty and compliance burden each country × component combination puts on a one-person operator. It is not a forecast of fines.
- Confidence: low–medium. EE and LV outbound scores rest on verified statute and DPA text. The LT outbound score rests partly on secondary sources (employee scope). All A and B scores rest on unverified EU-level knowledge.
- Used in: `04_legal_compliance.md` § Key findings (bullet 10) and §8 Synthesis inputs.
