# Gap-fill pass — shared rules (lead analyst, 2026-10-03)

The first-pass workstream agents ran out of a shared WebSearch budget (200 calls) part-way through. You are a **fresh gap-fill agent**: close the most decision-relevant UNKNOWNs in the workstream file(s) assigned to you, in priority order, then stop.

## Read first
- `research/_work/BRIEF.md` (governing brief) and `research/_work/CONVENTIONS.md` (labels, CSV formats, network constraints — all still apply).
- Your workstream file(s) in full, especially their UNKNOWNs / appendix sections (they contain ready-made queries), plus your workstream's `research/_work/sources_WSn.csv` and `assumptions_WSn.md` (to continue ID numbering and avoid duplicates).

## Search budget
- Load tools: ToolSearch "select:WebSearch,WebFetch". WebFetch/curl are blocked for almost all sites — don't retry them.
- **Hard cap: 60 WebSearch calls** (count them). If you receive a "web search budget" message, stop searching immediately and finish writing with what you have.
- Make each query count: use `allowed_domains` for primary sources, ask for exact figures and reference years, search ET/LV/LT/RU where the source is local.

## Editing rules
- Edit only the files named in your assignment (+ your workstream's sources/assumptions fragments and `research/_work/data/WSn_*` files). Do not touch other workstreams' files.
- Continue the existing ID sequences: new source ids continue after the highest existing id in `sources_WSn.csv` (do not reuse retired ids); new assumption ids continue after the highest `A-WSn-xx`.
- Replace UNKNOWNs you resolve with labelled findings in place (keep the section structure); add a short line in the file's UNKNOWNs section: "Resolved in gap-fill pass: …". Leave unresolved UNKNOWNs in place with their resolution path.
- If new evidence changes a key finding, synthesis-input score or funnel result, update those sections too and keep the math traceable.
- Use a uniquely named helper script if you need one (e.g. `/tmp/claude-0/.../scratchpad/gf_WSn_helper.py`) — never a generic name in a shared folder.
- Re-run `python3 /home/user/Claude/research/_work/tools/lint_labels.py <your file(s)>` at the end and fix flagged lines.

## Final reply (≤250 words)
What you resolved (with labels), what remains UNKNOWN, number of searches used, new source ids range, and any change to key findings or synthesis-input scores.
