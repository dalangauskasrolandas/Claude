### A-WS0-01 — Evidence-scorecard method (lead analyst synthesis)
- Value: six scores per row (Demand, WTP, Competition, Legal, Async, Language), each 1–5 where 5 = most favourable to the operator; "Mean" = unweighted mean of the six.
- Formula: single components = country × component base value from the workstream synthesis inputs (WS2 §12 demand; WS5 §12 WTP; WS3 §12 competition; WS4 §8.1 legal; WS6 §8.2 reconciled with WS5 §7 for async; WS1 §3.5/§8 + WS3 §5 + WS6 §8.3 for language) + evidence-backed group modifiers only (listed in the summary's basis table). Bundles: weakest link (minimum) for demand, WTP, legal, async and language, because no evidence of joint demand or joint WTP was found; competition for A+B = minimum of A and B (CRM partners already sell automation [V:WS3-013]); A+B+C = 3, provisional (no single A+B+C provider found in a limited search [V:WS3-005][V:WS3-013][V:WS3-024]).
- Inputs: the workstream scores cited in each basis code; generator `research/_work/tools/scorecard.py`; output `research/_work/data/scorecard.csv`.
- Basis/rationale: transparent, reproducible aggregation; a score of 1 marked "gap" means not researched / no evidence, not a negative finding. Sector rows differ only where sector-specific evidence exists (most G1 sector rows are therefore identical — the evidence does not discriminate between G1 sectors).
- Confidence: low–medium (scores inherit search-extract evidence and several provisional workstream scores).
- Used in: 00_research_summary.md § Evidence scorecard and § Ranking.

### A-WS0-02 — Async score for lead generation (C) set to 3, not WS6's 4
- Value: 3
- Formula: WS5 daytime share for C = 30% of hours (same-day reply handling, meeting booking, client calls) vs 25% for A (scored 3) and 10% for B (scored 4).
- Inputs: [E:A-WS5-33]; WS6 rubric [E:A-WS6-05].
- Basis/rationale: the two workstreams conflict; the quantified daytime share is the more specific evidence, so C is scored like A.
- Confidence: low (both inputs are estimates).
- Used in: 00_research_summary.md § Evidence scorecard.
