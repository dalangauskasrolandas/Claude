# Shared conventions for all research agents (set by the lead analyst)

Today is **2026-10-03**. Use it as `date_accessed` unless you access later.

## Paths and ownership
- Repo root: `/home/user/Claude`. Outputs: `/home/user/Claude/research/`.
- Write ONLY your own files:
  - your workstream file(s) in `research/` (e.g. `research/01_market_size.md`)
  - `research/_work/sources_WSn.csv` (your source fragment)
  - `research/_work/assumptions_WSn.md` (your ESTIMATE inputs)
  - optional small structured extracts: `research/_work/data/WSn_*.csv|json` (each ≤200 KB)
- Never edit another workstream's files, `sources.csv`, `assumptions.md` or `00_research_summary.md`. The lead analyst merges fragments.

## Network reality (tested 2026-10-03)
- **WebSearch works. WebFetch and curl are blocked** by the environment egress policy for almost every site (stat.ee, andmed.stat.ee, ec.europa.eu, csp.gov.lv, data.stat.gov.lv, osp.stat.gov.lt, riigiteataja.ee, pipedrive.com, hubspot.com, cv.ee, cv.lv, cvbankas.lt, linkedin.com, upwork.com, trends.google.com, wikipedia.org all return EGRESS_BLOCKED). Do not keep retrying WebFetch on them; one quick test of an unusual domain is fine. github.com / raw.githubusercontent.com are reachable.
- Evidence therefore comes from **WebSearch**. The search tool reads pages server-side and returns a synthesized answer plus result URLs. Use it as a page reader:
  - Use `allowed_domains` to force primary sources, e.g. `["stat.ee"]`, `["stat.gov.lv","csp.gov.lv"]`, `["osp.stat.gov.lt","stat.gov.lt"]`, `["ec.europa.eu"]`, `["eis.ee"]`, `["liaa.gov.lv"]`, `["inovacijuagentura.lt"]`, `["riigiteataja.ee"]`, `["likumi.lv"]`, `["e-tar.lt"]`, `["aki.ee"]`, `["dvi.gov.lv"]`, `["vdai.lrv.lt"]`, `["pipedrive.com"]`, `["hubspot.com"]`, `["zoho.com"]`, `["make.com"]`, `["n8n.io"]`.
  - Put the exact figure/wording you need into the query (e.g. "number of enterprises 10-49 persons employed Estonia 2024").
  - A claim is **VERIFIED** only if the search answer ties the figure/wording to a specific result URL from an identifiable publisher and the URL/title fits the claim. Record `method` = `search-extract`. If the answer gives a figure without a clear source URL, it is NOT verified: re-query with `allowed_domains`, or record it as UNKNOWN / LEAD.
  - Quotes: copy the wording as returned (≤25 words). If the tool clearly paraphrased, prefix the quote with `~` (near-quote).
  - Triangulate decision-critical numbers with a second query (different wording or language) where possible.
- **Do NOT use MCP connectors** (Apollo, Hunter, Gmail, Drive, Zoho CRM, etc.). The lead analyst collects Hunter/Apollo database-coverage counts centrally into `research/_work/data/db_coverage.csv`.

## Labels in workstream text
Every quantitative figure (counts, %, €, rates, hours, sizes) carries a label on the same line or table row:
- `[V:WS1-012]` = VERIFIED; the id points to your sources CSV.
- `[E:A-WS1-03]` = ESTIMATE; the id points to your assumptions file (formula + inputs there; also show short formulas inline).
- `UNKNOWN (resolve: …)` = not found; say what would resolve it.
- Exempt: years used as dates, calendar dates, NACE/CPV/ISCO codes, dataset/table IDs, legal section numbers, list numbering, source/assumption IDs.
- State the reference year of every statistic, e.g. "1,234 enterprises (2024) [V:WS1-004]". Flag anything older than 2023 with "(pre-2023)".

IDs: sources `WS1-001`, `WS1-002`…; assumptions `A-WS1-01`… (use your own WS number).

## `sources_WSn.csv` format
UTF-8, every field double-quoted, inner quotes doubled. Header exactly:
```
id,claim,url,publisher,date_published,date_accessed,quote,primary_secondary,label,method,search_language,country,workstream
```
- `claim`: precisely what the source supports ("Vendor X claims a database of 8,200+ companies", not "8,200 companies exist").
- `primary_secondary`: `primary` = statistics offices, Eurostat, official registers, regulators/DPAs, legislation portals, courts, official vendor pricing/partner/programme pages (for the vendor's own terms), associations' own pages (for their own member counts). `secondary` = media, blogs, listicles, aggregators, vendor marketing claims about markets.
- `label`: `VERIFIED` (source says it; confirmed via search-extract or fetch) or `LEAD` (seen but not confirmable / not used as VERIFIED in the text).
- `method`: `search-extract` | `fetched` | `api-query` | `derived`
- `search_language`: `EN` | `ET` | `LV` | `LT` | `RU`
- `country`: `EE` | `LV` | `LT` | `Baltic` | `EU` | `other`
- `date_published`: YYYY-MM-DD, YYYY-MM, YYYY or `n.d.`; `date_accessed`: 2026-10-03.
- `workstream`: `WS1`…`WS6`.

## `assumptions_WSn.md` entry format
```
### A-WS1-03 — <short name>
- Value: …
- Formula: …
- Inputs: [V:WS1-004] …, [E:A-WS1-01] …
- Basis/rationale: …
- Confidence: low | medium | high
- Used in: <file § section>
```

## Workstream file structure
1. Title; one-line scope; legend; method note ("Evidence gathered via web-search extracts on 2026-10-03; direct page fetching was blocked in this environment").
2. Key findings (≤10 bullets, each labelled).
3. Body following the brief; EE, LV and LT each covered (subsections or columns). If nothing found for a country, say UNKNOWN for that country — never skip silently.
4. "Added beyond the brief" (items assigned to you by the lead analyst).
5. Conflicts between sources (both values, which you trust and why).
6. Search-language log (language | example queries | what it found / didn't).
7. UNKNOWNs (each with the cheapest resolution: a specific test, interview question or source).
8. Synthesis inputs (compact table defined in your assignment). **All suggested scores are 1–5 where 5 = most favourable to the operator** (e.g. competition 5 = least competition; legal 5 = lowest risk).

## Rules restated from the brief
No invention. Label everything. Primary sources first; 2024–2026 data preferred. Search in ET/LV/LT/RU as well as EN and log which language found what. Cover EE/LV/LT separately. Traceable math. No personal data on named individuals (company and association names are fine; freelancers = aggregate only, no names or profile URLs; no named people anywhere).

Hard exclusions: do not research ship managers/shipowners, vessel inspection/survey, vessel–service-provider brokering, or any client trading with Russia/Belarus. Freight forwarding/logistics is in scope; where identifiable, exclude Russia/Belarus-transit-oriented firms from target counts (or state that you could not).

## Work style
Write files progressively (append sources as you go) so nothing is lost. Quality over speed, but stop when extra queries stop changing conclusions. Target ≥25 sources, ≥55% primary.

**Final reply to the lead analyst (≤300 words):** files written; source count (primary/secondary); the 5 most decision-relevant findings with labels; top 3 UNKNOWNs; anything another workstream should know.

## Local-language starter terms (verify spelling; extend)
- CRM implementation — ET "CRM juurutamine", "kliendihaldus"; LV "CRM ieviešana", "klientu attiecību vadība"; LT "CRM diegimas", "klientų valdymo sistema"; RU "внедрение CRM".
- Lead generation — ET "müügivihjed", "potentsiaalsed kliendid", "müügi outsourcing"; LV "potenciālo klientu piesaiste", "līdu ģenerēšana"; LT "potencialių klientų paieška", "B2B klientų paieška", "pardavimų užsakomosios paslaugos"; RU "лидогенерация", "аутсорсинг продаж B2B".
- Automation / AI — ET "protsesside automatiseerimine", "tehisintellekt ettevõtetes"; LV "procesu automatizācija", "mākslīgais intelekts uzņēmumos"; LT "procesų automatizavimas", "dirbtinis intelektas įmonėse"; RU "автоматизация бизнес-процессов", "ИИ для бизнеса".
- Accounting firms — ET "raamatupidamisteenus", "raamatupidamisbüroo"; LV "grāmatvedības pakalpojumi"; LT "buhalterinės apskaitos paslaugos".
- Grants — ET "EIS toetus digitaliseerimine", "tehisintellekti toetus"; LV "LIAA atbalsts digitalizācijai"; LT "Inovacijų agentūra kvietimas skaitmeninimas".
- Direct-marketing law — ET "otseturustus elektroonilised kontaktandmed"; LV "komercpaziņojumi bez piekrišanas"; LT "tiesioginė rinkodara elektroniniu paštu".
