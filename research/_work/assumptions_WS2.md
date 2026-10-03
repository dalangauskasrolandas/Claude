# Assumptions — WS2 (Digital maturity & demand signals)

Format per CONVENTIONS.md. Every ESTIMATE used in `research/02_demand_signals.md` traces to an entry here. Inputs point to `research/_work/sources_WS2.csv` (or, where stated, another workstream's fragment).

### A-WS2-01 — Capacity of the Estonian AI-adoption grant (number of companies funded)
- Value: 100 companies at the full EUR 2.0M budget; 55 companies at the EUR 1.1M initially planned for the 2026 round.
- Formula: 2,000,000 / 20,000 = 100; 1,100,000 / 20,000 = 55.
- Inputs: [V:WS2-001] total budget EUR 2,000,000 and unit price EUR 20,000; [V:WS2-003] EUR 1.1M planned for the year; ERR's own "55 instead of 100" companies.
- Basis/rationale: the grant is a fixed unit price per company, so capacity = budget / unit price. The ERR-reported 55 and 100 match the arithmetic. Because the round closed the day it opened with the budget exhausted, at least 55 applications (lower bound) arrived within about one business day.
- Confidence: high (arithmetic on verified inputs). The lower bound on applications is medium, because it is unclear whether EUR 1.1M or EUR 2.0M was available on 24.08.2026.
- Used in: 02_demand_signals.md § 1 Key findings; § 5.1 Estonia; § 8.4; § 9 (C3)

### A-WS2-02 — Implied minimum project value behind one EUR 20,000 AI grant
- Value: about EUR 25,000 per project.
- Formula: 20,000 / (1 − 0.20) = 25,000.
- Inputs: [V:WS2-001] unit price EUR 20,000; self-financing 20%.
- Basis/rationale: assumes the 20% self-financing is a share of total project cost.
- Confidence: medium. The unit-price mechanism may not require cost documentation at this level.
- Used in: 02_demand_signals.md § 5.1 Estonia (row EE-1)

### A-WS2-03 — EE RTE software grant: implied project size and ceiling on paid digital-advisor fees
- Value: project size about EUR 4,000–10,000. Grant money for the advisor is at most EUR 2,500 per project. If the 50% rate also applies to the advisor's invoice, that invoice is about EUR 5,000 at most.
- Formula: project = grant / 0.50, so 2,000 / 0.50 = 4,000 and 5,000 / 0.50 = 10,000. Advisor share of aid ≤ 0.50 × 5,000 = 2,500. Advisor invoice ≈ 2,500 / 0.50 = 5,000.
- Inputs: [V:WS2-007] EUR 2,000–5,000 grant, 50% self-financing; [V:WS2-009] advisor fees ≤ 50% of project support; [V:WS2-010] grant paid as a fixed amount.
- Basis/rationale: an upper-bound reading. Because the grant is paid as a fixed amount, it is not confirmed how co-financing maps onto individual cost lines.
- Confidence: low–medium.
- Used in: 02_demand_signals.md § 1 Key findings; § 5.1 Estonia (row EE-4)

### A-WS2-04 — EE advisory & development grant: project size at which the EUR 35,000 cap binds
- Value: EUR 50,000 (at 70% support) to EUR 70,000 (at 50% support).
- Formula: 35,000 / 0.70 = 50,000; 35,000 / 0.50 = 70,000.
- Inputs: [V:WS2-005] max grant EUR 35,000; self-financing 30–50% (so support is 50–70%).
- Basis/rationale: above these project sizes the client pays everything beyond the cap.
- Confidence: medium. The support rate depends on aid basis and location: [V:WS2-012] gives 50% for Tallinn/Harju/Tartu and 70% elsewhere for the related roadmap grant (2024).
- Used in: 02_demand_signals.md § 5.1 Estonia (row EE-3)

### A-WS2-05 — Implied hourly rate of EIS-procured digital mentors (price anchor)
- Value: about EUR 147–149 per hour excl. VAT.
- Formula: 4,460 / 30 = 148.7 (total quoted price). The co-financing figures imply a base of 661.50 / 0.15 = 4,410 and 882 / 0.20 = 4,410, so 4,410 / 30 = 147.0.
- Inputs: [V:WS2-015] 30-hour service = EUR 4,460 total; company co-financing EUR 661.50 (15%) or EUR 882 (20%).
- Basis/rationale: the two bases differ by EUR 50, which is unexplained (UNKNOWN; possibly a fixed fee). Both give an hourly rate of about EUR 147–149.
- Confidence: medium.
- Used in: 02_demand_signals.md § 5.1 Estonia (row EE-9); § 9 (C4); § 12 notes for WS5

### A-WS2-06 — Latvia new digitalisation programme: average budget per targeted beneficiary
- Value: about EUR 15,779 per business.
- Formula: 27,613,228 / 1,750 = 15,779.
- Inputs: [V:WS2-021] total EUR 27,613,228; at least 1,750 businesses; grants capped at EUR 10,000.
- Basis/rationale: the average is above the EUR 10,000 cap. So either the budget also funds a larger strand (the AI strand of up to EUR 200,000 in [V:WS2-022]), or 1,750 is a minimum target that will be exceeded. This is a consistency check, not a forecast.
- Confidence: low (interpretive).
- Used in: 02_demand_signals.md § 9 (C5)

### A-WS2-07 — Latvia: share of the new programme already reserved (if the EUR 5.4M refers to it)
- Value: about 19.6% reserved and about 80% unreserved at the (undated) article date.
- Formula: 5.4 / 27.613 = 0.196.
- Inputs: [V:WS2-023] EUR 5.4M reserved, funding still available; [V:WS2-021] EUR 27,613,228 total.
- Basis/rationale: assumes the EUR 5.4M article refers to the EUR 27.6M programme. Neither article's date is visible, and [V:WS2-026] separately says "most of the funding already reserved", possibly for the earlier EUR 37.5M programme.
- Confidence: low.
- Used in: 02_demand_signals.md § 5.2 Latvia (demand signals)
