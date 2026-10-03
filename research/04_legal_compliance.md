# WS4 — Legal & compliance for outbound lead generation and automation (EE / LV / LT)

**Scope.** This section covers the rules that apply to a one-person operator based in Estonia (invoicing as an FIE) who sells three services to B2B companies in Estonia, Latvia and Lithuania:
- **A** — CRM setup;
- **B** — AI/workflow automation;
- **C** — outbound lead generation.

It covers outreach law (e-mail, calls, LinkedIn), the GDPR legitimate-interest basis, data sources, the operator's obligations as a data processor and under the EU AI Act, and the "added beyond the brief" items: employee side business, sanctions, international transfers, LinkedIn terms, liability/insurance and language. **This is research, not legal advice.** Where the law is genuinely unsettled, the text says so and names what would resolve it.

**Legend**

| Label | Meaning |
|---|---|
| `[V:WS4-0xx]` | VERIFIED. The id points to `research/_work/sources_WS4.csv` (URL, quote of 25 words or fewer, date accessed). |
| `[E:A-WS4-01]` | ESTIMATE/judgement. The rubric is in `research/_work/assumptions_WS4.md`. |
| `UNKNOWN (resolve: …)` | Not established in this session. The cheapest resolution is given. |
| `UNKNOWN-P` | Not verified in this session. The analyst's prior reading of the law is given **for orientation only** and must be checked before anyone relies on it. It is not evidence and must not be scored as such. |
| `LEAD` | A source was found (title/URL) but its content could not be read. It is listed in the CSV with label LEAD. |

**Method note.** Evidence was gathered on 2026-10-03 from web-search extracts. Direct page fetching was blocked in this environment: vdai.lrv.lt and eur-lex.europa.eu both returned EGRESS_BLOCKED when tested.

The session-wide WebSearch budget, shared by six parallel workstreams, ran out after this workstream's first two dozen queries. As a result:
- **Verified:** the core outreach rules. These are the e-mail and outreach texts of EE ESS § 103¹, LV ISPL Art. 9 and LT ERĮ Art. 81, the positions of AKI, DVI and VDAI, and the April 2026 Lithuanian reform.
- **Not verified (`UNKNOWN-P`):** the EU-level layer (GDPR article content, the EU AI Act, sanctions, data transfers), LinkedIn terms, employment law, liability and language rules.
- **No Russian-language queries were run.**

The verification agent should treat every `UNKNOWN-P` as a claim still to be checked. A ready-made verification queue is in §7.

---

## 1. Key findings

1. **Lithuania changed its rules on 22 Apr 2026.** Direct marketing to *legal entities* no longer needs prior consent. ERĮ Art. 81 was amended by law `XV-815` [V:WS4-029] [V:WS4-031].
   - The mechanism is an exception to the consent rule where the subscriber or registered user is a legal entity [V:WS4-036]. Every message must offer a free opt-out [V:WS4-035].
   - Secondary sources say the exception also covers *named employees' work e-mails and work phone numbers* [V:WS4-034]. VDAI's own FAQ on this was not readable (UNKNOWN).
   - Before the change, VDAI required consent from the legal entity's manager [V:WS4-033]. Any Lithuanian guidance, vendor blog or agency claim written before April 2026 is therefore out of date.
2. **Estonia: opt-out regime for legal persons.**
   - ESS § 103¹ allows e-marketing to legal persons if every message offers a free, easy refusal, and it bans further use once someone refuses [V:WS4-001] [V:WS4-002].
   - AKI treats generic addresses (info@) as legal-person addresses. For addresses that identify a person (name.surname@), it weighs the recipient's position and the relevance of the product [V:WS4-004] [V:WS4-005].
   - AKI's guidance dates from 2015 (pre-2023 and pre-GDPR).
3. **Latvia: consent-based statute, read narrowly by the regulator.**
   - ISPL Art. 9 is a consent rule for e-mail, fax and automatic calling [V:WS4-011].
   - DVI says Art. 9's prohibitions apply to natural persons [V:WS4-019]. A *legal entity's* address may be e-mailed without consent if a valid stop-request address is given and stop requests are honoured (Art. 9(4)) [V:WS4-016] [V:WS4-015].
   - **Named-employee addresses are the least clear case of the three countries.** No DVI position was found (UNKNOWN).
4. **Natural persons need prior consent in all three countries**, apart from the existing-customer "soft opt-in". This covers private e-mail addresses and arguably sole traders (FIE / IK / individual activity).
   - Verified for LV [V:WS4-011] and LT [V:WS4-028].
   - For EE this is inferred from the structure of § 103¹ and AKI's legal-person carve-out [V:WS4-004] (UNKNOWN-P for the exact natural-person clause).
5. **The national B2B exceptions do not switch off the GDPR.** A named work address is personal data [V:WS4-037] [V:WS4-017]. Each campaign therefore needs:
   - a documented legitimate-interest basis;
   - an Art. 14 notice (including where the data came from) no later than the first e-mail;
   - immediate honouring of objections.

   The detail of these GDPR articles is UNKNOWN-P (not re-read this session).
6. **Cold calling.**
   - **LV:** DVI material says companies may be called without prior consent (LEAD [WS4-020]). Other commercial communications to natural persons need prior, free and explicit consent [V:WS4-013].
   - **LT:** the 2026 opt-out reportedly also covers calls and SMS to work phone numbers assigned by the employer [V:WS4-034].
   - **EE:** UNKNOWN whether § 103¹ covers live voice calls.
   - In every country, calling needs daytime hours, which is a poor fit with the operator's availability (see WS6).
7. **No enforcement case or fine from 2020–2026 could be verified in EE, LV or LT (UNKNOWN).**
   - Leads: an AKI precept-warning of 2020 [WS4-007, LEAD], two VDAI decisions of 2025 [WS4-039, WS4-040, LEAD] and VDAI's 2025 annual review [WS4-041, LEAD].
   - DVI states that it regularly receives complaints about commercial e-mail and SMS [V:WS4-018].
8. **The highest-risk practices in component C are LinkedIn automation/scraping and US-style enrichment databases** (Apollo/Hunter type). No Baltic source on either was verified. UNKNOWN-P: LinkedIn's User Agreement bans bots and scraping, and EU DPAs have sanctioned contact-scraping tools.
9. **Components A and B are legally routine processor work**, but they need:
   - an Art. 28 data-processing agreement;
   - a sub-processor list;
   - a transfer basis for US AI/automation vendors.

   AI Act duties for this kind of service look light (AI literacy; telling people when they are talking to a chatbot). All of this is UNKNOWN-P, including the status of the Digital Omnibus amendments.
10. **Suggested legal-risk scores** (5 = lowest risk) [E:A-WS4-01]:
    - **C (outbound lead generation):** LT 4 (provisional), EE 3, LV 3 (low confidence).
    - **B (automation):** 3 in all three countries.
    - **A (CRM setup):** 4 in all three countries.

---

## 2. Legal architecture — two layers (EE, LV, LT)

1. **National unsolicited-communication rules.** These are national laws derived from the EU ePrivacy Directive (Directive 2002/58/EC). They decide *whether you may send at all* (prior consent vs opt-out):
   - EE: ESS § 103¹ [V:WS4-001];
   - LV: ISPL Art. 9 [V:WS4-011];
   - LT: ERĮ Art. 81 [V:WS4-028].
2. **GDPR.** It applies as soon as the recipient is identifiable (a named employee). It governs the lawful basis, transparency (Art. 14), the right to object (Art. 21) and security. DVI states explicitly that the ISPL and the GDPR must be applied together [V:WS4-017]. Lithuanian commentary on the 2026 reform says the same [V:WS4-037].

**Which country's rule applies to a campaign sent from Estonia to Latvian or Lithuanian recipients?** UNKNOWN-P.
- The analyst's prior view:
  - The ePrivacy-derived rules are national and are not covered by the GDPR's one-stop-shop.
  - The e-Commerce Directive's country-of-origin principle carves out the permissibility of unsolicited commercial e-mail.
  - Regulators therefore generally apply the **recipient's** country rule.
- Practical reading: run each country's campaign to that country's rule. For a solo FIE the GDPR lead authority would be AKI.
- Resolve:
  - a written enquiry to AKI asking which national rule it applies to an Estonian sender's campaigns to LV/LT recipients;
  - checking the e-Commerce Directive annex derogations on EUR-Lex.

---

## 3. Outreach rules by channel

### 3.1 Unsolicited B2B commercial e-mail

#### Estonia (EE)

**The statute: Electronic Communications Act (Elektroonilise side seadus, ESS) § 103¹ — "use of electronic contact details for direct marketing".**
- **Legal persons:** marketing use is allowed if *each* use gives a clear, distinct, free and easy opportunity to refuse, and the refusal can be made over an electronic communications network [V:WS4-001].
- **After a refusal:** use is prohibited once the user, subscriber or buyer has refused [V:WS4-002].
- **Existing customers (soft opt-in):** contact data obtained from a buyer (natural or legal person) in a sale may be used for the seller's own *similar* products. An opt-out must be offered when the data is collected and in every message [V:WS4-003]. The search returned this text from an older consolidated version, and the current wording was not re-confirmed.
- **Subsection numbering inside § 103¹:** not verified. The search extracts gave the content but not the subsection numbers (UNKNOWN; resolve: open § 103¹ on riigiteataja.ee and record which subsection covers legal persons, natural persons, the soft opt-in and sender identification).
- **Natural persons:** prior consent required. UNKNOWN-P. This is implied by the legal-person carve-out and by AKI's guidance [V:WS4-004], but the natural-person clause itself was not extracted.

**Generic vs named-employee addresses — AKI guidance.** This is Andmekaitse Inspektsioon's guidance on electronic contact data in direct marketing, last updated 2015 (pre-2023, pre-GDPR).
- A legal entity's contact details may be used without prior consent, but the entity must be able to prohibit further use [V:WS4-004].
- **info@company.ee / company@company.ee** count as legal-entity addresses [V:WS4-005].
- **name.surname@company.ee, salesman@company.ee:** the recipient's position in the company and the nature of the product decide the case [V:WS4-005].
- **Plain-language reading:**
  - An offer that plainly fits the person's job (for example a CRM offer to a head of sales) can be treated like a legal-person address under the opt-out regime.
  - An offer unrelated to the person's role should be treated as marketing to a natural person, which needs consent.
- Natural and legal persons must both be given an opt-out every time [V:WS4-006].

**Information Society Services Act (Infoühiskonna teenuse seadus).** Its identification and transparency rules for commercial communications were not extracted. Riigi Teataja hosts a 2014 English translation (LEAD [WS4-009]). UNKNOWN (resolve: read the current consolidated text on riigiteataja.ee).

#### Latvia (LV)

**The statute: Information Society Services Law (Informācijas sabiedrības pakalpojumu likums, ISPL) Art. 9.**
- Commercial communications by automatic calling systems, fax or e-mail are prohibited unless the "service recipient" gave prior consent [V:WS4-011].
- Soft opt-in for existing customers: similar products, no initial objection, and a free opt-out in each message [V:WS4-012].
- Other commercial communications through publicly available electronic communication services need the recipient's prior, free and explicit consent [V:WS4-013].
- **Art. 9(4):** a commercial communication is prohibited if it uses an invalid address to which the recipient could send a stop request, or if a stop request is ignored [V:WS4-015].
- Art. 1 defines a "commercial communication" broadly: any electronic message advertising goods, services or a merchant's image [V:WS4-014].

**DVI's interpretation (Datu valsts inspekcija, the Latvian DPA).**
- Art. 9's prohibitions apply to commercial communications sent to **natural persons** [V:WS4-019].
- Commercial communications **may be sent to a legal entity's e-mail address without prior consent**, provided Art. 9(4) is observed: a valid stop-request address and honoured stop requests [V:WS4-016]. (DVI note of 2021.)
- Sending to identified or identifiable persons is personal-data processing, so the ISPL and the GDPR apply together [V:WS4-017].

**Named-employee work addresses (vārds.uzvārds@uzņēmums.lv): no DVI position found.** UNKNOWN.
- A cautious reading: a named address identifies a natural person, and DVI frames Art. 9 around natural persons [V:WS4-019]. Treat these addresses as **risky**.
- Resolve (cheap and free): a written enquiry to DVI: *"Does the ISPL Art. 9 prior-consent requirement apply to a commercial e-mail sent to a named employee's work address at a legal entity, where the offer concerns that employee's job function?"*

**A conflicting secondary summary.** A widely used law-firm summary describes Latvia simply as "prior express consent", with no B2B distinction [V:WS4-025]. DVI's position is trusted here (see §5), but DVI guidance does not bind the courts.

**Electronic Communications Law (Elektronisko sakaru likums).** The current text is on likumi.lv (LEAD [WS4-024]). Any direct-marketing provisions in it were not extracted (UNKNOWN).

#### Lithuania (LT)

**The statute and its numbering.**
- The Law on Electronic Communications (Elektroninių ryšių įstatymas, ERĮ) is still act `IX-2135`. Law `XIV-635`, adopted 11 Nov 2021 and in force from 1 Dec 2021, restated it in full to transpose the European Electronic Communications Code [V:WS4-027] [V:WS4-026].
- The direct-marketing article is now **Art. 81** [V:WS4-028]. Older material cites the pre-restatement number, Art. 69(1) (LEAD [WS4-047]). Do not rely on guidance that cites Art. 69.

**General rule (Art. 81):** using electronic communications services, including e-mail, for direct marketing needs the **prior consent of the subscriber or registered user**. There is a soft opt-in for the sender's own customers and similar goods [V:WS4-028].

**The 2026 reform.**
- Law `XV-815` (dated 16 April 2026) amended Art. 81 [V:WS4-029], together with other ERĮ articles [V:WS4-030].
- VDAI (Valstybinė duomenų apsaugos inspekcija) says the amended Art. 81 took effect on **22 Apr 2026** and *simplifies the conditions for direct marketing to legal entities* [V:WS4-031]. The stated aim is to encourage competition and make it easier to tell legal entities about goods and services. VDAI prepared an FAQ [V:WS4-032].
- **How it works:** consent remains the general rule, with an exception where the subscriber or registered user is a legal entity [V:WS4-036].
- **Duties under the exception:** every message must offer a clear, free opt-out; sending must stop immediately after an opt-out; proof should be kept; and an employee who has been assigned a contact address can opt out personally [V:WS4-035].
- **Scope (secondary sources only):** the exception covers general company contacts (info@) **and employees' work e-mail addresses and phone numbers assigned for work functions** [V:WS4-034] [V:WS4-036]. The new statutory wording and VDAI's FAQ were not readable. UNKNOWN (resolve: read the consolidated Art. 81 on e-seimas.lrs.lt and the FAQ linked from the VDAI news item [WS4-031]).

**Before 22 Apr 2026:** VDAI held that legal entities are "subscribers", so e-mail marketing to a legal entity needed the prior consent of its manager or an authorised person [V:WS4-033]. That position is superseded for legal entities. Older guidance (2019 FAQ, 2020 leaflet; LEAD [WS4-042]) should no longer be used for B2B campaigns.

**The GDPR still applies to named employees** [V:WS4-037].

### 3.2 B2B cold calling

| Country | Call to a company's general line | Call to a named employee's work phone | Call / SMS to a private person | Evidence |
|---|---|---|---|---|
| EE | Likely allowed; keep a do-not-call list | Risky: GDPR legitimate interest; stop on objection | Consent required for automated calls and SMS; live calls unclear | UNKNOWN whether ESS § 103¹ covers live voice calls (resolve: full text of AKI guidance [WS4-004], phone-call section; or a written enquiry to AKI). The rest is UNKNOWN-P |
| LV | Allowed without prior consent, per DVI telemarketing material | Risky: a named mobile identifies a natural person | **Forbidden without prior, free and explicit consent** for commercial communications via public e-comms services | LEAD [WS4-020]; [V:WS4-013]; DVI explainer on calling auto-generated numbers without consent (LEAD [WS4-021]) |
| LT | Allowed since 22 Apr 2026 with opt-out (legal-entity exception) | Allowed with opt-out if the number is assigned by the employer for work (secondary) | **Forbidden without prior consent** (Art. 81 general rule) | [V:WS4-034] [V:WS4-028] |

Calling needs business hours. That is an operational, not a legal, constraint for this operator (cross-reference WS6).

### 3.3 LinkedIn outreach (EE, LV, LT)

- **No Baltic DPA guidance on LinkedIn messaging was found** for EE, LV or LT. UNKNOWN (resolve: one written question to each of AKI, DVI and VDAI: *"Is a LinkedIn connection note or InMail with a commercial offer 'electronic mail' under ESS § 103¹ / ISPL Art. 9 / ERĮ Art. 81?"*).
- **Genuinely unsettled point.** It is unclear whether an in-platform message counts as "electronic mail" in the ePrivacy sense. Two analyst readings (UNKNOWN-P):
  - If it does count, a LinkedIn account is registered to an **individual**, not to the employer. The Lithuanian legal-entity exception (subscriber or registered user is a legal entity [V:WS4-036]) would then probably **not** cover it.
  - Estonia's role-relevance test [V:WS4-005] might.
- **GDPR (UNKNOWN-P):** using profile data to prospect is processing personal data. It needs a legitimate-interest basis, an Art. 14 notice and respect for objections.
- **LinkedIn's own terms:** see §4.4. Manual, personalised connection requests are the lowest-risk form. Automated sequences and data extraction are high risk (breach of contract plus GDPR).

### 3.4 GDPR legitimate interest — the shared EU layer (EE, LV, LT)

None of the GDPR text could be re-read this session (UNKNOWN-P). The analyst's reading, to be verified:

- **Lawful basis:** Art. 6(1)(f) (legitimate interests). Recital 47 states that direct marketing *may* be regarded as a legitimate interest. A documented three-part test is needed (legitimate purpose → necessity → balancing against the person's interests and reasonable expectations), plus accountability under Art. 5(2).
- **CJEU C-621/22 (Koninklijke Nederlandse Lawn Tennisbond), judgment of 4 Oct 2024:** a purely commercial interest can be a legitimate interest, but necessity and the balancing test are applied strictly. UNKNOWN-P.
- **EDPB Guidelines `1/2024` on Art. 6(1)(f):** adopted for public consultation in October 2024. Whether they were finalised by October 2026 is UNKNOWN (resolve: the EDPB guidelines page).
- **Art. 14 (data not obtained from the person):** the notice must cover the controller, purpose, legal basis, categories and **source** of the data. Where the data is used to contact the person, it must be given no later than the first communication (Art. 14(3)(b)). The "disproportionate effort" exemption (Art. 14(5)(b)) is narrow. UNKNOWN-P.
- **Art. 21(2)–(3):** the right to object to direct marketing is absolute; processing for that purpose must stop. Under Art. 21(4) the right must be brought to the person's attention explicitly, no later than the first communication. UNKNOWN-P.
- **National DPA material found:**
  - EE: AKI's guidance on e-marketing [V:WS4-004] and its general guide for controllers (LEAD [WS4-008]).
  - LV: DVI's note on how the ISPL and GDPR interact [V:WS4-017] and its SME guide (LEAD [WS4-023]).
  - LT: VDAI's 2026 Art. 81 FAQ (not read) [V:WS4-032] and older direct-marketing FAQs (LEAD [WS4-042]).
- **What this means per named prospect:** (1) the offer is relevant to the person's role; (2) only minimal data is used (name, title, work e-mail, company); (3) the first e-mail says who you are, where the data came from, why you are writing and how to object; (4) one suppression list is kept across all clients and campaigns; (5) data is deleted after a set period. Items (3) and (4) reflect requirements verified at national level ([V:WS4-006] [V:WS4-015] [V:WS4-035]); the GDPR-specific parts are UNKNOWN-P.
