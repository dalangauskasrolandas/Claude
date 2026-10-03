# WS4 — Legal & compliance for outbound lead generation and automation (EE / LV / LT)

**Scope.** This section covers the rules that apply to a one-person operator based in Estonia (invoicing as an FIE) who sells three services to B2B companies in Estonia, Latvia and Lithuania:
- **A** — CRM setup;
- **B** — AI/workflow automation;
- **C** — outbound lead generation.

It covers outreach law (e-mail, calls, LinkedIn), the GDPR legitimate-interest basis, data sources, the operator's obligations as a data processor and under the EU AI Act, and the "added beyond the brief" items: employee side business, sanctions, international transfers, LinkedIn terms, liability/insurance and language. **This is research, not legal advice.** Where the law is genuinely unsettled, the text says so and names what would resolve it.

**Legend**

| Label | Meaning |
|---|---|
| `[V:id]` (e.g. `WS4-001`) | VERIFIED. The id points to `research/_work/sources_WS4.csv` (URL, quote of 25 words or fewer, date accessed). |
| `[E:id]` (e.g. `A-WS4-01`) | ESTIMATE/judgement. The rubric is in `research/_work/assumptions_WS4.md`. |
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
    - **C (outbound lead generation):** LT 4 (provisional), EE 3, LV 3 (low confidence) [E:A-WS4-01].
    - **B (automation):** 3 in all three countries [E:A-WS4-01].
    - **A (CRM setup):** 4 in all three countries [E:A-WS4-01].

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
- The Law on Electronic Communications (Elektroninių ryšių įstatymas, ERĮ) is still act `IX-2135`. Law `XIV-635`, adopted 11 Nov 2021 and in force from 1 Dec 2021, restated it in full to transpose the European Electronic Communications Code [V:WS4-027] [V:WS4-026]. The edition history on e-TAR shows the act is still being amended in 2026 (LEAD [WS4-043]), so always check the consolidated version in force on the day.
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

Further Lithuanian commentary was found but not read: a member article published by the Kaunas Chamber of Commerce, Industry and Crafts, and a note by Ecovis Lithuania on VDAI's updated guidance (LEAD [WS4-044] [WS4-045]). Chamber-published compliance content may also interest WS6 as a channel signal.

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
- **LinkedIn's own terms:** see the LinkedIn User Agreement subsection under *Added beyond the brief*. Manual, personalised connection requests are the lowest-risk form. Automated sequences and data extraction are high risk (breach of contract plus GDPR).

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

### 3.5 Supervisory authorities and enforcement, 2020–2026

| Country | Who supervises e-marketing rules (evidence) | Verified cases / fines 2020–2026 | Cheapest resolution |
|---|---|---|---|
| EE | AKI publishes the ESS § 103¹ guidance [V:WS4-004]. It issued a precept-warning on use of electronic contact data in 2020, with the addressee anonymised (LEAD [WS4-007]). The ESS provision that gives AKI this competence was not extracted. | UNKNOWN: none verified. UNKNOWN-P: Estonia has historically punished GDPR breaches through misdemeanour procedure and penalty payments rather than administrative fines. Whether a 2025–2026 reform changed this is UNKNOWN. | AKI annual reports (aastaraamat) 2021–2025 and the precepts published on aki.ee |
| LV | DVI regularly receives complaints about commercial e-mail and SMS [V:WS4-018] and interprets ISPL Art. 9 [V:WS4-016]. The role of PTAC (consumer authority) in this area is UNKNOWN. | UNKNOWN. DVI decision documents appeared in search results but could not be read. The companies are deliberately not named, so as not to imply wrongdoing. | DVI decisions page ("Lēmumi") and DVI annual public reports 2021–2025 |
| LT | VDAI issues the Art. 81 guidance [V:WS4-031]. Two VDAI decisions of 2025 surfaced in direct-marketing searches (LEAD [WS4-039] [WS4-040]). VDAI's 2025 annual review was published on 2026-07-01 (LEAD [WS4-041]). The role of RRT (the communications regulator) under Art. 81 is UNKNOWN. | UNKNOWN: the subject and outcome of the 2025 decisions were not extracted. | Read the 2025 review [WS4-041] and the two decision PDFs |

**What this means:** with no verified enforcement data, legal risk cannot be calibrated against expected fines. The §8 scores therefore rest on how clear the rules are, not on how hard they are enforced [E:A-WS4-01].

### 3.6 Data sources for B2B prospecting

| Source | EE | LV | LT | Conditions in plain language | Evidence |
|---|---|---|---|---|---|
| Official business register (company data plus board members) | e-Business Register: **risky-low** | Register of Enterprises: **risky-low** | Registrų centras / JAR: **risky-low** | Company-level data is not personal data and is free to use. Board members' names *are* personal data: you need a legitimate-interest basis and an Art. 14 notice at first contact. Do not guess private e-mail addresses. Registers publish data for legal certainty, not marketing, so bulk reuse could be challenged. | UNKNOWN-P. LEADs: EE register-act translation [WS4-010]; DVI note on data published in the Register of Enterprises [WS4-022] |
| Commercial B2B databases (EE Inforegister/Teatmik; LV Lursoft/Firmas.lv; LT Rekvizitai/Creditinfo) | **risky** | **risky** | **risky**; read VDAI's note first | Once you import person-level data you become its controller. Check the vendor's lawful basis and what it tells data subjects, keep the source for your Art. 14 notice, and check accuracy. Company-only fields are low risk. | UNKNOWN-P. LEAD: VDAI note on offers to buy databases of legal entities [WS4-038] |
| Apollo/Hunter-type enrichment tools | **risky** | **risky** | **risky** | Third parties compiled the named-person data. You must disclose the source (Art. 14), keep it accurate and cover the non-EU transfer. EU precedents: France's DPA (CNIL) sanctioned the contact-extraction tool KASPR in 2024; Poland's DPA (UODO) ruled against Bisnode in 2019 (pre-2020) over Art. 14 notices for register-derived data. Details and amounts were not re-verified, so none are stated here. | UNKNOWN-P |
| Scraped data | **mixed** | **mixed** | **mixed** | Generic company addresses taken from company websites are lower risk (not personal data), subject to the site's terms. Scraping named individuals, especially from LinkedIn, breaches LinkedIn's contract and carries high GDPR risk. | UNKNOWN-P |

**Rule of thumb.** The national e-marketing rules (the e-mail subsection above) decide whether you may *contact* someone. The GDPR decides whether you may *hold and use* their data. Buying a list does not transfer the seller's compliance to you.

### 3.7 Obligations of a solo provider (A, B, and C when run for a client)

Everything in this subsection is EU-level law that could not be re-read this session (UNKNOWN-P), unless a source id is shown.

| Service | Operator's usual GDPR role | Main obligations | Status |
|---|---|---|---|
| A — CRM setup, clean-up, migration | Processor for the client | An Art. 28 data-processing agreement (DPA): act only on documented instructions, confidentiality, Art. 32 security, help with data-subject rights, return or delete data at the end, audits. If the client contracts with the CRM vendor directly, the vendor is the client's processor, not the operator's. | UNKNOWN-P |
| B — automation (n8n/Make, LLM APIs, e-mail tools) | Processor; vendors are the operator's sub-processors | Prior written authorisation of sub-processors and flow-down of terms (Art. 28(2) and (4)). A transfer basis for non-EU vendors (§4.3). A processor's record of processing (Art. 30(2)); the small-organisation exemption does not apply where processing is not occasional. Tell the client about a breach without undue delay (Art. 33(2)). | UNKNOWN-P |
| C — lead generation for a client | **Unsettled.** Processor if the client sets the target profile, sources and messages. Possibly a joint controller (Art. 26), or an independent controller if the operator builds and reuses its own prospect database. | The role decides who gives the Art. 14 notice, who answers objections and who is liable. Resolve by allocating roles in the contract; if material, ask AKI in writing. | UNKNOWN-P (genuinely unsettled) |

**Liability.**
- Under Art. 82(2) a processor is liable for damage only where it breached its own processor obligations or acted outside or against lawful instructions. Where both parties caused the damage, Art. 82(4) makes them jointly and severally liable, with recourse under Art. 82(5). UNKNOWN-P.
- An Estonian FIE trades in the owner's own name, so personal assets are exposed. UNKNOWN-P (resolve: RIK/EMTA guidance on FIE liability; WS5 covers the FIE setup).
- See also the liability-caps and insurance subsection under *Added beyond the brief*.

**EU AI Act (Regulation (EU) `2024/1689`).** All points are UNKNOWN-P unless marked otherwise.
- **Provider or deployer?**
  - A company that uses an AI system under its own authority in a professional capacity is a *deployer*. This covers the operator using Claude/GPT in its own work, and a client running an automation in its business.
  - The operator would become a *provider* only by developing an AI system and placing it on the market, or putting it into service, under its own name or trademark (for example a branded chatbot product).
  - A client-specific workflow that calls a third-party model most likely sits on the deployer/integration side. For custom builds sold to clients the line is unsettled (resolve: the Commission's guidelines on the AI-system definition and on roles; the AI Act service desk).
- **Art. 4 AI literacy:** applies to providers and deployers from 2 Feb 2025. The Digital Omnibus on AI, proposed in November 2025, would turn this into a duty to encourage literacy. Whether it has been adopted is UNKNOWN.
- **Art. 50 transparency, from 2 Aug 2026:**
  - People must be told when they are interacting with an AI system such as a chatbot, unless it is obvious.
  - Deployers must disclose AI-generated text published to inform the public on matters of public interest, unless a human reviewed it and takes editorial responsibility.
  - AI-drafted B2B sales e-mails that a human checks and sends carry no specific AI Act labelling duty in the analyst's reading.
- **High-risk systems (Annex III)** include AI used for recruitment and CV screening, worker management and creditworthiness. They carry heavy obligations and are best kept out of scope. When the Annex III obligations start, after the Digital Omnibus, is UNKNOWN (resolve: the Omnibus procedure file on EUR-Lex/OEIL).
- **National AI Act authorities:** LT reportedly RRT (LEAD [WS4-046]); EE and LV UNKNOWN.

---

## 3.8 Deliverable — allowed / risky / forbidden, per country (plain language)

Verdicts: **ALLOWED** (permitted if you meet the stated conditions), **RISKY** (defensible but unsettled, or depends on facts), **FORBIDDEN** (prohibited unless the stated exception applies). Each row's last column gives its evidence status.

### Estonia

| # | Activity | Verdict | What you must do / why | Citation / status |
|---|---|---|---|---|
| 1 | E-mail to a generic company address (info@, sales@) | ALLOWED | Offer a free, easy opt-out in every message; stop after a refusal; identify yourself | [V:WS4-001] [V:WS4-002] [V:WS4-004] [V:WS4-006] |
| 2 | E-mail to a named employee's work address, offer relevant to their role | RISKY (defensible) | AKI weighs the recipient's position and the product; add a GDPR legitimate-interest assessment, an Art. 14 notice in the first e-mail, and honour objections | [V:WS4-005]; GDPR layer UNKNOWN-P |
| 3 | E-mail to a named employee, offer unrelated to their role | FORBIDDEN without prior consent | Treated as marketing to a natural person | [V:WS4-005]; natural-person clause UNKNOWN-P |
| 4 | E-mail/SMS to private addresses or to FIE sole traders | FORBIDDEN without prior consent (except soft opt-in) | Natural persons | UNKNOWN-P (implied by [V:WS4-004]) |
| 5 | Marketing your own similar products to existing customers | ALLOWED | Offer an opt-out at collection and in each message | [V:WS4-003] |
| 6 | Cold call to a company's general number | ALLOWED (likely) | Keep a do-not-call list | UNKNOWN-P |
| 7 | Cold call to a named employee's work mobile | RISKY | GDPR legitimate interest; stop on objection | UNKNOWN (whether § 103¹ covers live calls) |
| 8 | Manual LinkedIn connection request or message | RISKY (unsettled) | Unclear whether this is "electronic mail" (ask AKI); GDPR applies | UNKNOWN |
| 9 | LinkedIn automation tools, or scraping profiles | FORBIDDEN by LinkedIn's contract; high GDPR risk | Account ban and data-protection exposure | UNKNOWN-P |
| 10 | Business-register data to identify decision-makers | RISKY-LOW | Legitimate interest plus Art. 14 notice | UNKNOWN-P; LEAD [WS4-010] |
| 11 | Bought lists or Apollo/Hunter enrichment | RISKY | Check the vendor; disclose the source; check accuracy and transfers | UNKNOWN-P |
| 12 | Handling client CRM data and automations | ALLOWED | Art. 28 DPA, sub-processor list, security | UNKNOWN-P |
| 13 | AI chatbot or AI-drafted replies built for a client | ALLOWED with disclosure | Chatbots must say they are AI (AI Act Art. 50, from 2 Aug 2026) | UNKNOWN-P |
| 14 | Clients established in Russia or Belarus; Baltic clients trading with them | FORBIDDEN / EXCLUDED | EU services bans (§4.2); hard exclusion in the brief | UNKNOWN-P |

### Latvia

| # | Activity | Verdict | What you must do / why | Citation / status |
|---|---|---|---|---|
| 1 | E-mail to a generic company address | ALLOWED | Give a valid address for stop requests; honour every stop request (Art. 9(4)) | [V:WS4-016] [V:WS4-015] [V:WS4-019] |
| 2 | E-mail to a named employee's work address, offer relevant to their role | RISKY (unsettled; no DVI position) | A named address identifies a natural person; DVI says Art. 9 protects natural persons. Ask DVI in writing before scaling. GDPR applies. | UNKNOWN; [V:WS4-019] [V:WS4-017] |
| 3 | E-mail to private addresses, or to sole traders (IK / self-employed) | FORBIDDEN without prior consent (except soft opt-in) | Natural persons | [V:WS4-011] [V:WS4-019] |
| 4 | Marketing your own similar products to existing customers | ALLOWED | The customer did not object at collection; opt-out in each message | [V:WS4-012] |
| 5 | Cold call to a company's general number | ALLOWED (per DVI material) | Keep a do-not-call list | LEAD [WS4-020]; UNKNOWN until the DVI text is read |
| 6 | Cold call to a named employee's mobile | RISKY | Commercial communications to natural persons through public e-comms services need prior explicit consent | [V:WS4-013] |
| 7 | Calls/SMS to private persons; automatic calling | FORBIDDEN without prior consent | | [V:WS4-011] [V:WS4-013] |
| 8 | Manual LinkedIn connection request or message | RISKY (unsettled) | Ask DVI whether it counts as e-mail; GDPR applies | UNKNOWN |
| 9 | LinkedIn automation tools, or scraping profiles | FORBIDDEN by LinkedIn's contract; high GDPR risk | | UNKNOWN-P |
| 10 | Register of Enterprises or Lursoft data to identify decision-makers | RISKY-LOW | Legitimate interest plus Art. 14 notice; read DVI's note on register data | UNKNOWN-P; LEAD [WS4-022] |
| 11 | Bought lists or Apollo/Hunter enrichment | RISKY | Check the vendor; disclose the source | UNKNOWN-P |
| 12 | Handling client CRM data and automations | ALLOWED | Art. 28 DPA, sub-processor list, security | UNKNOWN-P |
| 13 | AI chatbot or AI-drafted replies built for a client | ALLOWED with disclosure | AI Act Art. 50, from 2 Aug 2026 | UNKNOWN-P |
| 14 | Clients established in Russia or Belarus; Baltic clients trading with them | FORBIDDEN / EXCLUDED | §4.2; hard exclusion | UNKNOWN-P |

### Lithuania

| # | Activity | Verdict | What you must do / why | Citation / status |
|---|---|---|---|---|
| 1 | E-mail to a generic company address | **ALLOWED since 22 Apr 2026** (FORBIDDEN without consent before then) | Free opt-out in every message; stop immediately on opt-out; keep proof | [V:WS4-031] [V:WS4-035] [V:WS4-036]; old rule [V:WS4-033] |
| 2 | E-mail to a named employee's work address on the company domain | ALLOWED with opt-out (secondary sources); the employee can opt out personally | Plus GDPR legitimate interest and an Art. 14 notice; confirm against VDAI's FAQ | [V:WS4-034] [V:WS4-036] [V:WS4-037]; FAQ UNKNOWN |
| 3 | E-mail to private addresses / natural persons, including sole traders with individual-activity status | FORBIDDEN without prior consent (except soft opt-in) | The Art. 81 general rule | [V:WS4-028] |
| 4 | Marketing your own similar products to existing customers | ALLOWED | Clear, free opt-out | [V:WS4-028] |
| 5 | Cold call to a company's general number | ALLOWED with opt-out since 22 Apr 2026 | | [V:WS4-034] |
| 6 | Cold call to a work phone the employer assigned to an employee | ALLOWED with opt-out (secondary) | Confirm against VDAI's FAQ | [V:WS4-034]; FAQ UNKNOWN |
| 7 | Calls/SMS to private persons | FORBIDDEN without prior consent | | [V:WS4-028] |
| 8 | Manual LinkedIn connection request or message | RISKY (unsettled) | The account is registered to the individual, so the legal-entity exception probably does not apply if the message counts as e-mail | UNKNOWN; reasoning from [V:WS4-036] |
| 9 | LinkedIn automation tools, or scraping profiles | FORBIDDEN by LinkedIn's contract; high GDPR risk | | UNKNOWN-P |
| 10 | Registrų centras / JAR data to identify decision-makers | RISKY-LOW | Legitimate interest plus Art. 14 notice | UNKNOWN-P |
| 11 | Bought lists (Rekvizitai/Creditinfo) or Apollo/Hunter enrichment | RISKY | Read VDAI's note on buying databases of legal entities first | LEAD [WS4-038]; UNKNOWN-P |
| 12 | Handling client CRM data and automations | ALLOWED | Art. 28 DPA, sub-processor list, security | UNKNOWN-P |
| 13 | AI chatbot or AI-drafted replies built for a client | ALLOWED with disclosure | AI Act Art. 50; LT authority reportedly RRT | UNKNOWN-P; LEAD [WS4-046] |
| 14 | Clients established in Russia or Belarus; Baltic clients trading with them | FORBIDDEN / EXCLUDED | §4.2; hard exclusion | UNKNOWN-P |

---

## 4. Added beyond the brief

### 4.1 Running a side business while employed in Estonia (Employment Contracts Act, Töölepingu seadus)

All UNKNOWN-P: the section numbers come from the lead analyst's assignment and were not re-verified this session.
- **§ 23 and § 24 (non-compete agreements).** In the analyst's reading, an employee may run a side business unless:
  - a written non-compete agreement covers it, during or after employment, under the validity conditions of § 24; or
  - it breaches the general duties of loyalty and confidentiality.
- **No general duty to get the employer's consent** for non-competing side work was identified. This is UNKNOWN-P (resolve: read the consolidated text on riigiteataja.ee; the Labour Inspectorate's (Tööinspektsioon) free legal advice is a further cheap check).

**What to check in your own contract** (no personal data involved):
1. Is there a non-compete clause, and how is its scope defined? Does "the employer's field of activity" stretch beyond maritime inspection to sales/BD consulting or CRM services?
2. Is there a clause requiring consent for other paid work or a side business, or an internal policy (handbook) that says so?
3. Does the confidentiality clause cover the employer's contact lists, CRM data, templates and know-how? None of these may be reused.
4. Who owns work created during working time or with employer equipment or accounts (IP / work-product clause)?
5. Are there conflict-of-interest rules covering the employer's clients and suppliers? Ship managers, shipowners and vessel brokering are already excluded by the brief.

If a non-compete exists, written consent from the employer removes the risk.

### 4.2 Sanctions compliance for a service provider

All UNKNOWN-P: EUR-Lex was blocked and the search budget was exhausted.
- **EU Regulation 833/2014, Art. 5n (as amended by successive packages)** prohibits providing a list of business services to the Russian government and to legal persons established in Russia. In the analyst's understanding the list includes:
  - business and management consulting, public relations, accounting and tax consulting;
  - IT consultancy, legal advisory, architectural and engineering services;
  - market research and advertising;
  - since the December 2023 package, software for enterprise management such as **CRM/ERP**.
  
  CRM setup, automation and lead generation therefore all map onto prohibited categories for Russian entities. The paragraph letters and the exemptions are UNKNOWN (resolve: consolidated Reg. 833/2014 on EUR-Lex).
- **Belarus:** Reg. 765/2006 contains parallel services restrictions; the article number is UNKNOWN.
- **National law:**
  - EE: International Sanctions Act (Rahvusvahelise sanktsiooni seadus);
  - LV: Law on International Sanctions and National Sanctions of the Republic of Latvia;
  - LT: Law on the Implementation of Economic and Other International Sanctions.
  
  All three countries criminalise sanctions violations. These names and points are UNKNOWN-P (resolve: Riigi Teataja, likumi.lv, e-tar.lt).
- **Practical screening:**
  - check client entities and their owners (EU ownership/control test) against the EU consolidated sanctions list and the EU Sanctions Map;
  - ask clients, especially in freight forwarding and wholesale, whether they sell to, buy from or route through Russia or Belarus;
  - avoid supporting trade that could amount to circumvention.
  
  This matches the brief's hard exclusion.

### 4.3 International transfers and the sub-processor chain (B, and C tooling)

All UNKNOWN-P.
- **EU–US Data Privacy Framework (DPF):**
  - The adequacy decision was adopted in July 2023.
  - The EU General Court dismissed the Latombe challenge (T-553/23) in September 2025.
  - An appeal to the Court of Justice was reported; its status in October 2026 is UNKNOWN (resolve: curia.europa.eu case search "Latombe").
  - DPF-certified US vendors can rely on the adequacy decision. For others, use the Standard Contractual Clauses plus a transfer impact assessment.
- **The chain to disclose in each client DPA:**
  - CRM vendor (where the operator contracts with it);
  - automation platform (Make cloud, or n8n cloud vs self-hosted on an EU server);
  - LLM APIs (for example Anthropic, OpenAI);
  - e-mail sending, warm-up and verification tools;
  - enrichment tools;
  - hosting and logging.
- **For each entry, state:** legal entity, location, transfer basis, purpose, retention, any use of data for model training (check the API data-use terms), and how the client is told about changes and can object.
- **Data minimisation:** do not send special-category data, or more personal data than needed, to LLM prompts.

### 4.4 LinkedIn User Agreement — automation and scraping

All UNKNOWN-P: linkedin.com was blocked and no search quota remained.
- In the analyst's reading, LinkedIn's User Agreement ("Dos and Don'ts") prohibits:
  - software, scripts, bots, crawlers or browser plug-ins that scrape or copy profiles or other data;
  - unauthorised automated methods for adding or downloading contacts or sending messages;
  - fake profiles.
- LinkedIn enforces through account restriction and termination, and has sued scrapers in the US.
- Sales Navigator is LinkedIn's own sanctioned prospecting product, but its data-export limits apply.
- Using LinkedIn data is also GDPR processing (see the LinkedIn outreach subsection).
- Resolve: read the current User Agreement and Professional Community Policies at linkedin.com/legal and note the section numbers and their effective date.

### 4.5 Liability caps and professional-indemnity insurance for a solo provider in Estonia

- **Liability caps:** the Law of Obligations Act (Võlaõigusseadus) § 106 governs excluding and limiting liability. In the analyst's reading:
  - B2B caps are generally possible;
  - a clause cannot exclude or limit liability for intentional breach, or where that would be contrary to good faith;
  - standard-terms control also applies to pre-formulated B2B terms.
  
  UNKNOWN-P (resolve: VÕS § 106 and the standard-terms provisions on riigiteataja.ee).
- **GDPR damages:** liability to data subjects under Art. 82 cannot be contracted away. Indemnities and caps *between* operator and client can be negotiated. UNKNOWN-P.
- **Professional-indemnity insurance** ("ametivastutuskindlustus" / professional liability): it is UNKNOWN whether Estonian insurers cover an FIE doing IT, automation or marketing services, and at what premium (resolve: ask several insurers active in Estonia, such as If, ERGO, Salva and BTA, for a quote; WS5 would cost it).

### 4.6 Language requirements for commercial communications (cross-check with WS1)

- UNKNOWN for EE, LV and LT: this session did not search language law; WS1 owns it.
- UNKNOWN-P: in the analyst's reading, private B2B correspondence (e-mails and proposals between businesses) is not language-regulated in any of the three countries. Public-facing advertising and consumer information must be in the state language under:
  - EE: Language Act (Keeleseadus);
  - LV: State Language Law (Valsts valodas likums);
  - LT: Law on the State Language and Law on Advertising.
- For the operator: cold B2B e-mails in English, Russian or Lithuanian face no statutory bar that was identified. Any public advertising or website aimed at the market would need checking.

---

## 5. Conflicts between sources

| # | Topic | Source A | Source B | Trusted | Why |
|---|---|---|---|---|---|
| 1 | LT: is consent needed for e-mail to legal entities? | VDAI 2022 seminar: yes, the manager's consent [V:WS4-033] | VDAI 2026 news: rules simplified from 22 Apr 2026 [V:WS4-031]; secondary sources: no prior consent, opt-out instead [V:WS4-034] [V:WS4-036] | **B** | A later statutory amendment (`XV-815`) [V:WS4-029] supersedes the earlier guidance. All pre-April-2026 LT material is obsolete for legal entities. |
| 2 | LT: date of the change | e-Seimas/tagidas: law `XV-815` dated 16 April 2026; tagidas calls it "effective" from that date [V:WS4-029] [V:WS4-030] | VDAI: in force 22 Apr 2026 [V:WS4-031] | **B** (in-force date) | 16 April is most likely the adoption date and 22 April the entry into force. VDAI is the regulator. Which date is which in the official gazette is UNKNOWN (resolve: e-TAR publication record of `XV-815`). |
| 3 | LV: is B2B e-mail consent-based? | Statute: consent of the "service recipient" [V:WS4-011]; DLA Piper: "prior express consent", no B2B distinction [V:WS4-025] | DVI: Art. 9 prohibitions apply to natural persons; a legal entity's e-mail needs no consent if Art. 9(4) is met [V:WS4-016] [V:WS4-019] | **B**, with residual risk | The regulator's interpretation governs enforcement in practice. However, the statutory definition of "service recipient" (ISPL Art. 1) was not extracted, and guidance does not bind courts (UNKNOWN). |
| 4 | EE: how authoritative is the guidance? | AKI guidance dates from 2015, before the GDPR [V:WS4-004] | ESS § 103¹, current English translation [V:WS4-001] | **Both, consistent** | They agree on opt-out for legal persons. AKI's named-address test predates the GDPR, so GDPR duties must be added on top. |
| 5 | LT: named employees' work addresses | Pre-2026 VDAI: consent from the legal entity or the specific employee [V:WS4-033] | Post-2026 secondary sources: covered by the legal-entity opt-out [V:WS4-034] [V:WS4-036] | **B, provisionally** | It matches the stated purpose of the amendment [V:WS4-032]. Confirm against VDAI's FAQ (UNKNOWN). |

---

## 6. Search-language log

| Language | Example queries | Found | Not found |
|---|---|---|---|
| ET | "Elektroonilise side seadus § 103¹ elektroonilise kontaktandmete kasutamine otseturustuseks juriidiline isik"; "Andmekaitse Inspektsioon otseturustus juriidilise isiku e-post nõusolek ESS 103¹ juhend" | ESS § 103¹ text (legal persons; soft opt-in) [V:WS4-003]; AKI 2015 guidance [V:WS4-004]; AKI 2020 precept (LEAD) | Current subsection numbering; any post-GDPR AKI e-marketing guidance; enforcement or fines |
| LV | "Informācijas sabiedrības pakalpojumu likums 9. pants komercpaziņojumu sūtīšana…"; "Datu valsts inspekcija komercpaziņojumi juridiskām personām e-pasts…" | ISPL Art. 9 / Art. 9(4) / Art. 1 [V:WS4-011] [V:WS4-015]; DVI 2021 note [V:WS4-016]; DVI explainer [V:WS4-019]; telemarketing leads | The Art. 1 definition of "service recipient"; a DVI position on named-employee addresses; enforcement |
| LT | "naujas Elektroninių ryšių įstatymas tiesioginė rinkodara…"; "Pokyčiai: tiesioginė rinkodara juridinių asmenų atžvilgiu…"; "XV-815 … 81 straipsnio…" | The 2026 Art. 81 reform [V:WS4-031]; the `XIV-635` restatement [V:WS4-027]; the RRT news item [V:WS4-026]; ExpertLab commentary [V:WS4-034]; VDAI 2025 decisions (LEAD) | The amended Art. 81 wording verbatim; the text of VDAI's 2026 FAQ |
| EN | "Electronic Communications Act Estonia § 103¹ 'Use of electronic contact details for direct marketing'…"; "Lithuania electronic communications law amendment April 2026…"; "Electronic marketing Latvia legal persons…" | ESS English translation [V:WS4-001]; emailexpert.com [V:WS4-036]; DLA Piper LV [V:WS4-025] | EU-level texts (EUR-Lex blocked); the LinkedIn User Agreement (blocked) |
| RU | none run | — | **Gap:** the search budget ran out before any Russian-language queries. Russian-language compliance guidance and community practice remain unsearched (UNKNOWN). |

The LT-language queries were the most productive: they surfaced the decisive 2026 reform. The LV-language queries were the only route to DVI's B2B position. The EN queries mainly duplicated these findings.

---

## 7. UNKNOWNs and the cheapest way to resolve each

1. **The amended LT Art. 81 wording, and whether VDAI's FAQ confirms that named employees' work e-mails and phones are covered.** Resolve with WebSearch `allowed_domains ["vdai.lrv.lt","e-seimas.lrs.lt"]`, query `DUK 81 straipsnio pakeitimai juridiniai asmenys darbuotojo darbo el. pašto adresas atsisakymas`. Or ask VDAI in writing (free).
2. **LV named-employee work addresses.** Send a written enquiry to DVI (the question drafted in the Latvia e-mail subsection). A search alternative: `["dvi.gov.lv"]` "darbinieka e-pasta adrese komercpaziņojums juridiskai personai".
3. **EE § 103¹ subsection numbering, the natural-person clause, and whether live voice calls are covered.** Resolve on Riigi Teataja (current ESS) plus the phone-call section of AKI's guidance; WebSearch `["riigiteataja.ee"]` `103¹ füüsilisest isikust kliendi elektrooniliste kontaktandmete kasutamine otseturustuseks eelneval nõusolekul`.
4. **Enforcement cases and fines, 2020–2026, in all three countries.**
   - AKI annual reports 2021–2025 (`["aki.ee"]` "aastaraamat otseturustus rikkumine").
   - DVI decisions and annual reports (`["dvi.gov.lv"]` "lēmums komercpaziņojumi sods").
   - VDAI 2025 review [WS4-041] and decisions [WS4-039] [WS4-040].
5. **Whether a LinkedIn message counts as "electronic mail" under each national rule.** Ask AKI, DVI and VDAI the same written question (drafted in the LinkedIn outreach subsection).
6. **The AI Act timeline and Digital Omnibus status in October 2026.** EUR-Lex/OEIL procedure file for the "Digital Omnibus on AI"; WebSearch `["eur-lex.europa.eu","europarl.europa.eu"]`.
7. **The DPF appeal status.** curia.europa.eu case search "Latombe".
8. **The exact services prohibited by sanctions.** Consolidated Reg. 833/2014 Art. 5n and the Belarus equivalent in Reg. 765/2006, on EUR-Lex.
9. **Employment Contracts Act § 23 and § 24 text, plus the operator's own contract.** Riigi Teataja, and the contract checklist in the side-business subsection.
10. **Professional-indemnity insurance: availability and premium for an IT/marketing FIE.** Quotes from insurers active in Estonia.
11. **Which national rule applies to cross-border campaigns** (EE sender, LV/LT recipients), and which authority acts. Written enquiry to AKI, plus the e-Commerce Directive annex on EUR-Lex.
12. **Whether register and commercial-database data may lawfully be used for prospecting.** Read DVI's note on register data [WS4-022] and VDAI's note on buying databases [WS4-038]; CNIL's KASPR decision for the enrichment-tool comparison.
13. **The GDPR layer** (Art. 6(1)(f), Recital 47, Art. 14, Art. 21, Art. 28, Art. 30, Art. 33, Art. 82), **CJEU C-621/22**, and **whether EDPB Guidelines `1/2024` are final.** Re-read on EUR-Lex, curia.europa.eu and edpb.europa.eu. These are stable texts, so a single check confirms them.
14. **Russian-language sources.** Not searched; run at least two RU queries, e.g. "прямой маркетинг e-mail юридическим лицам Литва 2026 согласие" and "коммерческие сообщения DVI Латвия юридические лица".
15. **Language law for commercial communications.** Defer to WS1.

**Note for the verifier.** The WebSearch budget for this session is exhausted. Re-verifying anything requires the lead analyst to raise `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION`. Items one to four matter most for decisions.

---

## 8. Synthesis inputs

### 8.1 Legal-risk score per country × component (scale one to five; five = lowest risk)

| Country | A — CRM setup | B — AI/workflow automation | C — outbound lead generation | Main reason (C) | Key citations |
|---|---|---|---|---|---|
| EE | 4 [E:A-WS4-01] | 3 [E:A-WS4-01] | 3 [E:A-WS4-01] | Opt-out for legal persons is in the statute. Named addresses depend on AKI's role/product test (2015 guidance). Natural persons and FIEs need consent. LinkedIn is unsettled. | [V:WS4-001] [V:WS4-004] [V:WS4-005] |
| LV | 4 [E:A-WS4-01] | 3 [E:A-WS4-01] | 3, low confidence (could be 2) [E:A-WS4-01] | Legal-entity e-mail is allowed per DVI. There is no position on named employees. Calls to natural persons need consent. The statute is consent-based. | [V:WS4-016] [V:WS4-019] [V:WS4-013] [V:WS4-011] |
| LT | 4 [E:A-WS4-01] | 3 [E:A-WS4-01] | 4, provisional (3 if VDAI's FAQ narrows the employee scope) [E:A-WS4-01] | The 2026 statutory opt-out for legal entities reportedly includes work contacts. The rule is new and there is no enforcement practice yet. | [V:WS4-031] [V:WS4-034] [V:WS4-036] |

- **A and B scores are the same in all three countries** because they rest on EU-level processor and AI Act duties (UNKNOWN-P this session).
- **B scores one point below A** because of the sub-processor chain, US transfers and the uncertain Digital Omnibus timing (UNKNOWN-P).

### 8.2 Allowed / risky / forbidden summary matrix

| Activity | EE | LV | LT | Evidence |
|---|---|---|---|---|
| E-mail to a generic company address | ALLOWED (opt-out) | ALLOWED (valid stop-address; honour requests) | ALLOWED since 22 Apr 2026 (opt-out) | [V:WS4-001] [V:WS4-016] [V:WS4-031] |
| E-mail to a named employee's work address | RISKY (role/product test) | RISKY (unsettled) | ALLOWED with opt-out (secondary) | [V:WS4-005] [V:WS4-019] [V:WS4-034] |
| E-mail/SMS to natural persons or sole traders | FORBIDDEN without consent (UNKNOWN-P) | FORBIDDEN without consent | FORBIDDEN without consent | [V:WS4-011] [V:WS4-028] |
| Cold call to a company line | ALLOWED, likely (UNKNOWN-P) | ALLOWED (LEAD [WS4-020]) | ALLOWED (opt-out) | [V:WS4-034] |
| Call to a named person's mobile | RISKY (UNKNOWN) | RISKY | ALLOWED if a work phone (secondary) | [V:WS4-013] [V:WS4-034] |
| Manual LinkedIn message | RISKY (UNKNOWN) | RISKY (UNKNOWN) | RISKY (UNKNOWN) | — |
| LinkedIn automation or scraping | FORBIDDEN (contract; UNKNOWN-P) | FORBIDDEN (UNKNOWN-P) | FORBIDDEN (UNKNOWN-P) | — |
| Register data for targeting | RISKY-LOW (UNKNOWN-P) | RISKY-LOW (UNKNOWN-P) | RISKY-LOW (UNKNOWN-P) | LEAD [WS4-010] [WS4-022] |
| Bought lists or enrichment tools | RISKY (UNKNOWN-P) | RISKY (UNKNOWN-P) | RISKY (UNKNOWN-P) | LEAD [WS4-038] |
| Processing client data (A/B) | ALLOWED with Art. 28 DPA (UNKNOWN-P) | same | same | — |
| Russia/Belarus clients | FORBIDDEN (UNKNOWN-P) | FORBIDDEN (UNKNOWN-P) | FORBIDDEN (UNKNOWN-P) | — |

### 8.3 Notes for other workstreams

- **WS3 (competitors) and WS6 (channels).** Any agency, vendor or blog claim about Lithuanian B2B e-mail dated before 22 Apr 2026 describes the old consent regime [V:WS4-033]. Since that date, Lithuania is arguably the *most permissive* of the three for e-mail and calls to company contacts [V:WS4-031] [V:WS4-034].
- **WS6.** Cold calling is legally feasible to company lines in all three countries (with caveats; §3.2), but it needs daytime hours. LinkedIn outreach is legally unsettled at the national level, and its automation is barred by LinkedIn's contract (UNKNOWN-P).
- **WS1.** Language-law constraints on B2B communication were not verified here (see the language subsection under *Added beyond the brief*). Please confirm or correct them from WS1's own sources.
- **WS5.** Budget for compliance overheads:
  - a DPA template and sub-processor register;
  - a suppression/opt-out list that works across all clients;
  - privacy notices in each outreach language;
  - possibly professional-indemnity insurance (UNKNOWN cost).
  
  These are time costs rather than tool costs, except insurance.
- **All workstreams.** The shared WebSearch budget is exhausted. The brief's verification step cannot run until it is raised.
