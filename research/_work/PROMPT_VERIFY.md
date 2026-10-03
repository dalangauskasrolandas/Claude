# Verification agent instructions (brief §6.1)

You are the **independent verifier** for the "Baltic Revenue Engine" research. You did not do the original research; be sceptical and precise.

## Read first
- `research/_work/BRIEF.md` (governing brief), `research/_work/CONVENTIONS.md` (labels, CSV formats, network constraints), `research/_work/ASSIGNMENTS.md`.
- All workstream outputs: `research/01_market_size.md` … `research/06_channels_reachability.md`, `research/competitors.csv`, `research/sources.csv` (merged), `research/assumptions.md` (merged), `research/_work/data/*` (incl. `WS5_models.*`, `db_coverage.csv`).

## Network reality
Only WebSearch works (WebFetch/curl are blocked for almost all sites). "Re-opening a source" therefore means re-querying it with WebSearch using `allowed_domains` set to the cited URL's domain and **different wording** from the original claim, checking the figure, wording and reference year; where possible find a second independent source. Load tools with ToolSearch "select:WebSearch,WebFetch". Do not use MCP connectors.

## Tasks
1. **Select the 30 most decision-relevant claims** across all six workstreams (state your selection criteria). Must include: enterprise counts feeding the funnels; CRM/AI/ERP adoption figures; grant statuses and consultant eligibility; B2B email/cold-call rules per country; enforcement cases; competitor coverage claims (trilingual all-Baltic answer) and key price bands; partner/affiliate commission terms; Estonian FIE tax and VAT rules; key unit-economics inputs; channel sizes and outreach benchmarks; language/census figures. Cover EE, LV and LT and all six workstreams.
2. For each: re-verify → **confirmed / corrected / could not verify**, with what changed.
3. **Recalculate every model**: WS1 G1 funnels and G2 estimate; WS5 unit economics, tax formula and sensitivity table (re-run `_work/data/WS5_models.*` or rebuild in Python); any other arithmetic (sums, shares, growth rates) in WS2/WS3/WS6. Record every discrepancy.
4. **Lint**: run `python3 research/_work/tools/merge_sources.py` and `python3 research/_work/tools/lint_labels.py`; fix unlabelled numbers (add the correct label or mark UNKNOWN), broken source/assumption IDs, CSV problems, quotes >25 words, missing country coverage.
5. **Apply all corrections** directly in the workstream files (and `competitors.csv`), marking changed text with `(corrected — see VL-xx)`. New sources go in `research/_work/sources_VER.csv` with ids `VL-001…` (workstream `VER`); new estimates in `research/_work/assumptions_VER.md` (ids `A-WS9-01…`, i.e. use WS9 as your number so the lint recognises them). Re-run the two scripts after editing.
6. Write `research/verification_log.md`: method and limits; the 30-claim table (VL id | claim | file § | original value + source id | result | corrected value | new source id | note); model recalculations (inputs, recomputed outputs, differences); lint results before/after; systemic issues (e.g., weak primary coverage in a country, over-reliance on vendor claims); remaining risks.

Rules: no invention; if you cannot verify, say "could not verify" — do not delete the original claim, but downgrade its label in the text (e.g. VERIFIED → LEAD/UNKNOWN) and say why. No personal data on named individuals.

Final reply (≤300 words): counts confirmed/corrected/could-not-verify; the most important corrections; model recalculation outcome; lint before/after; files changed.
