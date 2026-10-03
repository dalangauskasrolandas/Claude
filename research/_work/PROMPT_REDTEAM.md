# Red-team agent instructions (brief §6.2)

You are the **red team** for the "Baltic Revenue Engine" research. You did not do the original research. Your job: build the strongest evidence-based case that this concept fails **for this specific operator** (Tallinn-based, Lithuanian citizen, EN/RU/LT but no Estonian or Latvian, full-time maritime BD job, 10–20 h/week evenings/weekends, €200–500 budget, Estonian FIE, no non-maritime network, hard exclusions in the brief).

## Read first
- `research/_work/BRIEF.md`, `research/_work/CONVENTIONS.md`.
- `research/01_market_size.md` … `research/06_channels_reachability.md`, `research/competitors.csv`, `research/sources.csv`, `research/assumptions.md`, `research/_work/data/*`. (A verifier may be correcting these files in parallel; re-check via search any number your argument depends on.)

## Network reality
Only WebSearch works (load via ToolSearch "select:WebSearch,WebFetch"; WebFetch/curl are blocked for almost all sites). Use `allowed_domains` for primary sources. Search for **disconfirming** evidence the workstreams may have missed (e.g. failure rates of solo agencies, price compression from AI tools, saturation of "AI automation agency" offers, buyer distrust of cold outreach, vendor-native AI replacing setup work, language expectations of Baltic SME owners). Do not use MCP connectors.

## Deliverable: `research/red_team.md`
- The **7 strongest reasons the concept fails for this operator**, ranked by severity. Together they must cover: customer, competition, legal, capacity/time, language, price, channel (one primary category per reason; a reason may touch several).
- For each reason: the claim (one sentence); the mechanism (why it bites this operator specifically); evidence (source IDs from `sources.csv`, plus new sources you found — record them in `research/_work/sources_RT.csv` with ids `RT-001…`, workstream `RT`, same CSV format as CONVENTIONS); severity **high / medium / low** with justification; which countries/components/groups it hits hardest; what would falsify it (the cheapest specific test or interview question).
- Then: "Where the workstreams are too optimistic" (specific statements, file § and why), and "Kill criteria" — observable results from cheap tests that should make the operator drop a component, country or segment. No offers, pricing pages, names or marketing plans.
- Label every number per CONVENTIONS ([V:id] / [E:id] / UNKNOWN). New estimates go in `research/_work/assumptions_RT.md` with ids `A-WS8-01…` (use WS8 so the lint recognises them).

Final reply (≤250 words): the 7 reasons with severities (one line each) and the 2 most important things the workstreams got wrong or over-stated.
