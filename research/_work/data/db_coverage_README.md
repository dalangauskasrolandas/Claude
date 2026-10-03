# Hunter.io Discover: database coverage counts for EE / LV / LT

**What this is:** counts of company records in Hunter.io's *Discover* prospecting database, by HQ country × headcount bucket × industry, plus a check on whether website-technology (CRM) filters can be applied. These counts are a **database-coverage / reachability proxy, NOT official market size**. Everything here is company-level aggregates. No person names or email addresses were retrieved or stored, and the sample statistics use only Hunter's per-company `emails_count` totals.

* **Data file:** `db_coverage.csv` has 99 rows (one per query), UTF-8, all fields double-quoted.
* **Date accessed:** 2026-10-03 (snapshot; the vendor database changes continuously).

## Get-Usage before and after (no credits used)

| Hunter quota bucket (period resets 2026-11-01) | Before (start of run) | After (end of run) |
|---|---:|---:|
| credits used / available | 0 / 50 | 0 / 50 |
| searches used / available | 0 / 50 | 0 / 50 |
| verifications used / available | 0 / 100 | 0 / 100 |

The run made 107 `Find-Companies` calls: 99 grid queries, 1 retry after a rate-limit error, and 7 diagnostic calls (1 offset test and 6 technology-filter phrasings). Usage was identical before and after, so **0 credits were consumed**. No other Hunter or Apollo tool was called (no Domain Search, Email Finder, enrichment, leads or sequences).

## Method

1. **Tool.** Hunter MCP `Find-Companies` takes a natural-language query. Hunter infers filters from it and returns `meta.results` (total matches), `meta.filters` (the filters actually applied), `meta.permalink`, and the first page of up to 100 companies.
2. **Query templates.**
   * All industries: `companies headquartered in {Country} with {bucket} employees`
   * One industry: `companies in the {Industry} industry headquartered in {Country} with {bucket} employees`
   * Country total: `companies headquartered in {Country}`
   * Technology: `companies headquartered in {Country} with 11-50 or 51-200 employees that use {Tech}`
3. **Filter verification.** Each row's `meta.filters` was checked programmatically against the intended country, headcount and industry. All 78 non-technology rows matched exactly. For example, LV × 11-50 × Logistics gives 110, which reproduces the brief's test query. `filters_json` holds the filters actually applied, and `permalink` reopens the same query in the Hunter web UI.
4. **Industry names Hunter accepts.** Hunter uses a LinkedIn-style taxonomy, and the ID comes from `industry_included=` in the permalink:
   * Transportation, Logistics, Supply Chain and Storage (116)
   * Wholesale (133)
   * Manufacturing (25)
   * Accounting (47)
   * Professional Services (1810)
   * Business Consulting and Services (11)
   * Administrative and Support Services (1912), which exists as a parent

   **Parent filters include their sub-industries.** Accounting and Business Consulting and Services are both inside Professional Services (1810), so do not add those rows together.
5. **Sample metrics.** These come from the returned first page (≤100 rows).
   * `pct_any_email`, `pct_personal_email` and `pct_generic_email` are the share of sampled companies with `emails_count.total`, `.personal` or `.generic` above 0.
   * `maritime_rows_in_sample` is the number of sampled rows whose industry is "Maritime Transportation".

   **Ranking bias:** Hunter returns the first page sorted by number of indexed emails (descending), and the NL tool ignores any offset ("offset 2300" was tested and still returned page 1). So:
   * Where `results_total` ≤ 100 (22 segments), the sample **is** the full result set and the percentages are exact. Across those segments, any email = 60–100% (median 83%), personal = 33–85% (median 67%), generic = 59–95% (median 77%). Pooled, 778 of 937 companies (83%) have ≥1 indexed email.
   * Where `results_total` > 100 (56 segments), the percentages describe the top-100 most-indexed companies and are **upper bounds** (median 100% any email).
6. **Technology rows.** The CSV marks these `filter not supported`, with blank counts (see the technology section below).

## Pivot: results_total (company records in Hunter Discover)

| Industry filter (Hunter ID) | EE 1-10 | EE 11-50 | EE 51-200 | LV 1-10 | LV 11-50 | LV 51-200 | LT 1-10 | LT 11-50 | LT 51-200 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ALL industries (no filter) | 8,368 | 3,562 | 1,113 | 4,250 | 2,359 | 909 | 8,427 | 4,367 | 1,749 |
| Transportation, Logistics, Supply Chain and Storage (116) | 142 | 107 | 37 | 116 | 110 | 47 | 231 | 199 | 97 |
| Wholesale (133) | 166 | 105 | 41 | 113 | 108 | 44 | 220 | 170 | 77 |
| Manufacturing (25) | 610 | 414 | 170 | 416 | 381 | 207 | 822 | 740 | 357 |
| Accounting (47) ⊂ Prof. Services | 78 | 19 | 6 | 46 | 17 | 4 | 89 | 37 | 5 |
| Professional Services (1810) | 2,639 | 945 | 230 | 1,285 | 534 | 123 | 2,414 | 855 | 206 |
| Business Consulting and Services (11) ⊂ Prof. Services | 706 | 164 | 34 | 285 | 88 | 26 | 594 | 147 | 40 |
| Administrative and Support Services (1912) | 338 | 118 | 38 | 198 | 104 | 27 | 412 | 166 | 40 |

| ALL industries | EE | LV | LT |
|---|---:|---:|---:|
| 201-500 employees | 317 | 252 | 510 |
| any size (country total, incl. unknown headcount) | 22,798 | 11,984 | 24,095 |
| 11-50 + 51-200 (returned by the technology queries; filter ignored) | 4,675 | 3,268 | 6,116 |

Notes:
* The size buckets do not add up to the country total. The total also includes 501+ employee companies and records with unknown headcount, which are excluded from every size-filtered query.
* The 11-50 + 51-200 totals equal the sum of the bucket rows (EE 3,562 + 1,113; LV 2,359 + 909; LT 4,367 + 1,749), which confirms that combined buckets work.

## Sub-industry mix inside the parents (from returned samples, indicative)

* **Logistics (116)** includes the parent tag itself and Truck Transportation, plus:
  * **Maritime Transportation** (≈11% of sampled rows): ship managers, crewing agencies, ferry and port fleets.
  * **Airlines and Aviation** (≈12%).
  * Warehousing and Storage, Freight and Package Transportation, Rail, Ground Passenger and bus.
* **Wholesale (133):** Wholesale Building Materials is large, and many of these are window, door or concrete *manufacturers* tagged as wholesale. Also Import and Export, Electrical, Food and Beverage, Motor Vehicles and Machinery.
* **Manufacturing (25):** industrial and other machinery, electrical and electronics, motor vehicles, **Printing Services**, furniture, and food and beverage.
* **Professional Services (1810):** **IT Services and IT Consulting is the largest sub-tag (≈1/3 of sampled rows)**, followed by Advertising, Legal, Business Consulting, Environmental, Architecture, HR, Research and Accounting.
* **Business Consulting and Services (11):** Marketing Services, Environmental Services (including waste management and utilities), HR Services, and Strategic Management and Outsourcing.
* **Administrative and Support Services (1912):** Events Services, Travel Arrangements, Staffing and Recruiting, Translation, Facilities and Janitorial, and Security.

### Maritime flag (Logistics rows): maritime rows / sample_n (of results_total)

| Logistics segment | EE | LV | LT |
|---|---:|---:|---:|
| 1-10 | 18 / 100 (of 142) | 14 / 100 (of 116) | 7 / 100 (of 231) |
| 11-50 | 18 / 100 (of 107) | 12 / 100 (of 110) | 0 / 100 (of 199) |
| 51-200 | 6 / 37 (of 37) | 6 / 47 (of 47) | 4 / 97 (of 97) |

**Operator action:** exclude shipowners, ship managers and crewing agencies from the Maritime-tagged rows, and decide separately on Airlines and Aviation.

## Technology adoption (CRM): filter not supported

`Find-Companies` never inferred a technology filter.
* **Six diagnostic phrasings were tried:** HubSpot four ways (including "whose technologies include hubspot", which returned no filters and 0 results), "Salesforce customers in Latvia", and the structured `technology: WordPress; location: Estonia; headcount: 11-50`.
* **The 21 canonical country × technology queries** were also run. Every one returned only the location and headcount filters, so it gave back the unfiltered country × 11-200 universe (EE 4,675; LV 3,268; LT 6,116).

The CSV technology rows therefore leave `results_total` and the sample fields blank rather than report unfiltered totals as adopters. The technology filter in Hunter's Discover web UI may allow this to be added by hand to the permalinks. That was not verified here.

**Fallback (indicative only):** technology slugs Hunter detected on the websites of the distinct 11-50 and 51-200 companies pooled from all machine-readable returned samples (83 result files, deduplicated by domain):

| Detected in pooled sample (11-50 + 51-200) | EE | LV | LT |
|---|---:|---:|---:|
| distinct sampled companies (n) | 924 | 904 | 1099 |
| HubSpot | 7 (0.8%) | 5 (0.6%) | 7 (0.6%) |
| Pipedrive | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) |
| Salesforce | 4 (0.4%) | 4 (0.4%) | 10 (0.9%) |
| Zoho (any zoho* slug) | 1 (0.1%) | 1 (0.1%) | 1 (0.1%) |
| Bitrix24 | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) |
| Kommo/amoCRM | 0 (0.0%) | 1 (0.1%) | 0 (0.0%) |
| ActiveCampaign | 2 (0.2%) | 1 (0.1%) | 0 (0.0%) |
| any target CRM | 12 (1.3%) | 9 (1.0%) | 14 (1.3%) |
| 1c-bitrix (CMS, not Bitrix24) | 4 (0.4%) | 4 (0.4%) | 1 (0.1%) |

Read these fallback figures with care:
* They are website-detectable traces only (scripts, chat widgets, forms). Back-office CRMs such as Pipedrive, Bitrix24 and Kommo are rarely visible, so 0 does not mean nobody uses them.
* The samples are mixed across industries and ranked by email count, so they are not representative.
* `1c-bitrix` is a CMS and is not counted as Bitrix24.
* 17 small segments came back inline (rather than as files), mostly 51-200 industry slices and Accounting, and were not parsed for technologies. A manual read of them found 3 more Salesforce detections (1 per country) and no other target CRM.

## Caveats

1. **This is a vendor database, not a register.** Hunter's coverage depends on companies having web domains. The counts are records or domains, not legal entities. Some firms appear under several domains (one EE aviation firm had 4), and some HQ countries are wrong (a few foreign firms were tagged EE, LV or LT). Treat the numbers as reachable-in-tool counts.
2. **Inference and classification noise.**
   * Filters come from NL inference. They were verified for every row here, but rephrasing can change them.
   * Industry tags are LinkedIn-style self or vendor classifications, with visible misclassifications (for example, a security firm tagged Accounting, a state audit office in Accounting, and manufacturers in Wholesale).
   * Parent filters pull in broad sub-industries: IT services sits inside Professional Services, and aviation and maritime sit inside Logistics.
3. **Headcount buckets are not statistical size classes.** Hunter's 1-10 / 11-50 / 51-200 / 201-500 are LinkedIn-style employee ranges, not registry employment. They do not align with the EU/SBS classes 0-9 / 10-49 / 50-249 / 250+. For example, 10 employees falls in "1-10" here but in "10-49" in statistics, and the 201-500 bucket straddles 250. Map them only approximately.
4. **Coverage bias.** The database over-represents firms with websites, LinkedIn or English presence, digital and service businesses, and capital-city firms. It under-represents micro firms and offline or traditional SMEs (for example, small hauliers). Coverage also differs by country (LT and EE are much larger than LV in this database). EE's count probably includes many internationally run companies registered in Estonia (for example, e-Residency start-ups and affiliate-marketing firms seen in the samples). Do not read the ratios between countries as economic structure.
5. **Email metrics.** `emails_count` is the number of addresses Hunter has indexed: "personal" means named individuals and "generic" means role addresses. The values for segments over 100 are upper bounds because of the email-count ranking (see Method).
6. **Operational notes.** A Hunter rate-limit error hit 1 of 7 parallel calls. That call (EE Pipedrive) was retried and succeeded, and the rest were run in batches of 3–4.
