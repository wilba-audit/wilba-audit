# Schoeman Growth OS — Claude Conversation Migration Pack (01)

**Purpose:** Faithful migration of everything produced in the originating Claude Code conversation, for the new `schoeman-growth-os` project. This document migrates existing work; it does not start a new strategy or redesign the system.

**Evidence legend (used inline throughout):**
- `[PRIMARY-SOURCE FACT]` — provided by the user or in an original clinic/source document.
- `[RAW DATA]` — actual numbers/records supplied.
- `[DERIVED METRIC]` — a calculation from supplied data.
- `[PREVIOUS CLAUDE INFERENCE]` — a conclusion Claude previously drew.
- `[HYPOTHESIS]` — proposed, not proven.
- `[RECOMMENDATION]` — a strategic/tactical suggestion made in the work.
- `[DECISION]` — something the user explicitly approved/chose/instructed.
- `[UNKNOWN]` — we do not actually have this.

**Provenance caveats:** Part of the originating conversation was context-compacted before this pack was written. Facts drawn from that earlier portion are labelled by their original source where known (e.g. user-pasted Telegram, proposal v3, the knowledge base). Where provenance cannot be established, it is marked `[UNKNOWN provenance]`.

---

## SECTION 1 — EXECUTIVE HANDOVER

- **Who is Dr Gina Schoeman:** `[PRIMARY-SOURCE FACT]` (team biographies) A longevity and functional medicine physician; Founder and Medical Director of The Schoeman Clinic London. MB ChB (Stellenbosch, 2001), MBA, Dip Derm (Cardiff), MRCGP, MBCAM, AFMCP. 20+ years clinical experience across emergency medicine, surgery, O&G, paediatrics, ENT, dermatology, then GP, practising functional medicine since 2004. Signature thesis: *"not what is wrong, but why."*
- **What The Schoeman Clinic is:** `[PRIMARY-SOURCE FACT]` (knowledge base) A UK private, CQC-registered clinic — "Your Specialist in Hormone, Longevity and Functional Medicine." Four-pillar methodology (GP medicine, bio-identical hormone therapy, functional medicine, longevity medicine), every clinician trained across all four ("one doctor, one picture"). Operates online + Harley Street and Wimbledon. Premium, high-ticket. Clinical records in Semble (EHR); GoHighLevel is the operational CRM.
- **What we were trying to accomplish (this conversation):** `[DECISION]` Primary focus shifted over the conversation from (a) finishing the GHL/WhatsApp operational build + patient-consent compliance, to (b) building a **social growth machine** for Dr Gina + the Clinic + the wider doctor faculty, as Phase 1 of a broader Schoeman Growth OS.
- **Current marketing/social situation:** `[DERIVED METRIC]` Instagram is the only channel with meaningful activity. A large paid-boost-driven spike in late May/June 2026 was followed by a ~99% collapse in weekly reach; follower counts flatlined. Facebook is negligible (clinic 13, Gina 6 followers). No lead magnet / funnel exists.
- **Major opportunities identified:** `[PREVIOUS CLAUDE INFERENCE]`/`[RECOMMENDATION]` A newly assembled **faculty of highly credentialled, media-worthy doctors** (each a distinct "attractive character" and content territory); Dr Gina's founder story as an unused asset; an existing referral network; the chance to convert reach into a list via a lead magnet + nurture.
- **Major problems identified:** `[DERIVED METRIC]`/`[PREVIOUS CLAUDE INFERENCE]` Reach collapse post-boost; vanity followers not seeing content; no funnel/lead-capture; effort split across two Instagram accounts; no measurement/learning loop.
- **Current stage of work:** `[DECISION]` Skills + audit complete; a **machine architecture was PROPOSED and is awaiting audit/approval** (the user explicitly instructed: audit existing skills and architecture first, do not build the 30-day system yet).
- **What has already been built:** four social/marketing skills + a compliance skill + a GHL inbox health-check skill; a data-backed social audit; a patient consent & privacy-notice pack; a Gina call-flow document; various knowledge-base captures. (Full list in Sections 12, 26, 30.)
- **What remains to be built:** the proposed new skills (`faculty-account-architect`, `content-performance-analyst`, `social-content-engine`), the "Social OS" memory files, skill extensions, and — only after architecture approval — the 30-day evidence-led social growth system.

---

## SECTION 2 — SOURCE MATERIAL INVENTORY

> Filenames preserved where known. Original uploaded CSV/DOCX arrived with hash-prefixed names in an ephemeral uploads folder; cleaned copies were saved into the working repo.

1. **Instagram export — The Schoeman Clinic**
   - NAME: `schoemanclinicinstagram.CSV` (uploaded as `2178a4f4-schoemanclinicinstagram.CSV`; saved to `outputs/schoeman-clinic/social-data/schoemanclinicinstagram.CSV`)
   - TYPE: CSV `[RAW DATA]`
   - CONTAINED: weekly Date, Views, Reach, Reposts, Followers (Aug 2026 back to Aug 2025; only May 31 2026 → Aug 2 2026 populated).
   - ANALYSIS: reach/views/follower trend; reach-collapse calculation; reach-as-%-of-followers.
   - EXTRACTED: see Section 3.
   - STILL NEEDED: yes (raw). RECOVERY PRIORITY: **CRITICAL**.
2. **Instagram export — Dr Gina Schoeman**
   - NAME: `drginaschoemaninstagram.CSV` (uploaded `3b71ff56-...`; saved `.../social-data/drginaschoemaninstagram.CSV`)
   - TYPE: CSV `[RAW DATA]`; same columns; May 24 2026 → Aug 2 2026 populated.
   - Same analysis/priority: **CRITICAL**.
3. **Facebook export — The Schoeman Clinic Page**
   - NAME: `TheSchoemanClinicFacebookPage.CSV` (uploaded `bc59588f-...`; saved `.../social-data/`)
   - TYPE: CSV `[RAW DATA]`; daily Date, Page Followers (May 1 → Aug 1 2026).
   - PRIORITY: **USEFUL** (values tiny).
4. **Facebook export — Dr Gina Schoeman Page**
   - NAME: `DrGinaSchoemanFacebookPage.CSV` (uploaded `d8b09382-...`; saved `.../social-data/`)
   - TYPE: CSV `[RAW DATA]`; daily Page Followers.
   - PRIORITY: **USEFUL**.
5. **Team biographies (fuller version)**
   - NAME: `Schoeman_Clinic_Doctor_Biographies_11.docx` (uploaded `9f55933c-...`; saved `outputs/schoeman-clinic/source-notes/Schoeman-Team-Biographies.docx`)
   - TYPE: DOCX `[PRIMARY-SOURCE FACT]`; one-liners, speaker intros, short + full bios for Gina + faculty + execs + admin.
   - EXTRACTED: Sections 5, 7. STILL NEEDED: yes. PRIORITY: **CRITICAL**.
6. **Team biographies (second version)**
   - NAME: `Schoeman_Clinic_Doctor_Biographies.docx` (uploaded `64a21a57-...`)
   - TYPE: DOCX `[PRIMARY-SOURCE FACT]`; a second/earlier biographies file (content not separately extracted; assumed subset/variant of #5). PRIORITY: **USEFUL** (compare against #5).
7. **Google Drive folder "Knowledge base"** (owner `mati@robinhoodsolutions.ai`, folder id `1Zdq-ax7hkcX9zFV37kYcdpTAeeZ95XYt`) — read during the conversation. Contained `[PRIMARY-SOURCE FACT]`:
   - `Schoeman_Clinic_Knowledge_Base_Trimmed (1).docx` — Gina's confirmed KB answers (escalation, clinic, services, consultations, bloods, payments, prescriptions, journey, appointments, team, positioning). **CRITICAL**.
   - `Consultations type and prices` (Google Doc) — full consultation menu + prices. **CRITICAL**.
   - `BLOOD_TEST_TYPES_with_prices.docx` — panels GS1–GS13 with prices + fasting flags (draft). **CRITICAL**.
   - `Our_Partners_updated.pdf` — pharmacies/supplements/testing partners; Gut Map code `TSC10`. **CRITICAL**.
   - `Current_Automations.docx` — automation register + redundancy review. **USEFUL**.
   - `Schoeman_Clinic_Knowledge_Base_Filled.docx` — earlier filled KB (site-sourced). **USEFUL**.
   - `Post Consultation Patient Letter.docx`, `ourpartners.docx`, `Barcode email copy updated.docx`, `Post_Consultation_Letter_Example_Automation.docx`, `Example blood test invoice.pdf`. **OPTIONAL–USEFUL**.
   - Related Google Docs seen in Drive search: `Schoeman-Knowledge-Base-Session` (two copies), `Schoeman Clinic - Knowledge Base`. **OPTIONAL**.
8. **User-pasted Telegram messages** (Mati / Griffin / Dr Gina group) `[PRIMARY-SOURCE FACT]`:
   - Launch-timing thread (~late Jul 2026): website live ~5 Aug, new-doctor announcement 7 Aug, social intros w/c 10 Aug (Dr Nathan → Sonia → Nikita), newsletter w/c 24 Aug; post-consultation email copy; Mati/Griffin exchange on inactive patients + post-consult email. Preserved verbatim in `outputs/schoeman-clinic/telegram-thread-log.md`.
   - Later batch: "Prices sent"; "Semble sends appointment reminders"; "new website with another company, ETA beginning of August"; "Mati replaced 3 docs in the knowledge base folder (updated by Gina)"; "Griffin … email copy and PDF … post-consultation letter … switch off the n8n automation."
   - Earlier (compacted) Telegram: Twilio caller-ID + GHL wallet top-up; ~815-patient Semble→GHL migration; double-messaging; consent form request. RECOVERY: **USEFUL** (originals in Telegram).
9. **Boost fact** `[PRIMARY-SOURCE FACT]` (user statement): "she boosted a post in June, using the standard boost." No screenshot/campaign export supplied.
10. **Website** `theschoemanclinic.com` — referenced; **could not be fetched** (network egress blocked in the session). `[UNKNOWN]` current live content beyond KB-captured copy. PRIORITY to recover: **USEFUL**.
11. **Patient/Website Privacy Policies + enquiry-form fields** — pasted earlier (compacted) and used to build the consent pack. RECOVERY: **USEFUL**.
12. **Proposal v3** — `outputs/schoeman-clinic/source-notes/proposal-v3.txt` (pre-existing in repo) — WILBA/RobinHood build proposal. **USEFUL**.
13. **WILBA brand assets (NOT Schoeman)** — `outputs/brand/brand-positioning.md`, `social-media-intelligence.md`, `30-day-instagram-calendar.md`. Present in repo; **belong to WILBA/Jess's own brand**, not the clinic. Flagged to avoid cross-contamination. PRIORITY: **OPTIONAL** for Schoeman.

---

## SECTION 3 — SOCIAL DATA

All figures below are `[RAW DATA]` unless marked `[DERIVED METRIC]`. Instagram data is **weekly**; Facebook is **daily follower count only**. No engagement, saves, comments, profile-visit, geographic, or website/lead data was included in the exports.

### DR GINA SCHOEMAN — Instagram (@drginaschoeman, handle inferred from filename)
Columns: Date, Views, Reach, Reposts, Followers.
| Week | Views | Reach | Reposts | Followers |
|---|---|---|---|---|
| Aug 2 2026 | 99 | 4 | 0 | 2356 |
| Jul 26 | 2448 | 34 | 0 | 2350 |
| Jul 19 | 3830 | 53 | 0 | 2346 |
| Jul 12 | 2507 | 42 | 3 | 2344 |
| Jul 5 | 2877 | 172 | 2 | 2338 |
| Jun 28 | 6911 | 268 | 2 | 2328 |
| Jun 21 | 5182 | 117 | 4 | 2319 |
| Jun 14 | 17011 | 1423 | 4 | 2293 |
| Jun 7 | 8786 | 429 | 2 | 2259 |
| May 31 | 9540 | 133 | 4 | 2204 |
| May 24 | 17 | 1 | 0 | 2170 |
(Weeks before May 24 2026: blank.)

### DR GINA SCHOEMAN — Facebook Page
`[RAW DATA]` daily Page Followers grew from 1 (May 2026) to **6** (Jul 31 2026); Aug 1 blank.

### DR GINA — LinkedIn / other
`[UNKNOWN]` — not provided. (A LinkedIn profile URL surfaced via web search: `linkedin.com/in/dr-gina-schoeman-...`; no data analysed.)

### THE SCHOEMAN CLINIC — Instagram (@schoemanclinic, inferred)
| Week | Views | Reach | Reposts | Followers |
|---|---|---|---|---|
| Aug 2 2026 | 105 | 20 | 0 | 1516 |
| Jul 26 | 2075 | 68 | 6 | 1515 |
| Jul 19 | 2190 | 117 | 0 | 1508 |
| Jul 12 | 2939 | 233 | 3 | 1499 |
| Jul 5 | 1803 | 84 | 4 | 1496 |
| Jun 28 | 6501 | 511 | 5 | 1451 |
| Jun 21 | 7529 | 671 | 12 | 1270 |
| Jun 14 | 23945 | 2268 | 6 | 987 |
| Jun 7 | 20484 | 1551 | 10 | 429 |
| May 31 | 8447 | 1494 | 2 | 269 |
(May 24 2026 and earlier: blank — account likely began ~May 2026.)

### THE SCHOEMAN CLINIC — Facebook Page
`[RAW DATA]` daily Page Followers grew from ~1–2 (May 2026) to **13** (Aug 1 2026).

### THE SCHOEMAN CLINIC — LinkedIn / other
`[UNKNOWN]` — not provided.

### Derived metrics `[DERIVED METRIC]`
- Clinic IG reach: peak Jun 14 = 2268 → Aug 2 = 20 → **−99.1%**.
- Gina IG reach: peak Jun 14 = 1423 → Aug 2 = 4 → **−99.7%**.
- Clinic IG followers: 269 (May 31) → 1516 (Aug 2) = +1247; the bulk (269→1270) landed by Jun 21; +20 only in the last month (Jul 5 1496 → Aug 2 1516).
- Reach as % of current followers (Aug 2): clinic ≈ 1.3%; Gina ≈ 0.2%.
- Clinic peak-fortnight views (Jun 7 + Jun 14) = 44,429.

### NOT AVAILABLE in the data `[UNKNOWN]`
impressions (only "views"), engagement/engagement rate, shares/saves/comments, profile visits, follows-from-content, per-post/format performance, top/weak posts, audience demographics/geography (for social), paid-vs-organic split within the exports, website activity, lead activity.

---

## SECTION 4 — JUNE PERFORMANCE / BOOST FORENSICS

**KNOWN FACTS**
- `[PRIMARY-SOURCE FACT]` The user stated Dr Gina **boosted a post in June using the standard ("Boost Post") option**.
- `[RAW DATA]` Late-May/June spike then July collapse (see Section 3). Clinic followers jumped 269→1270 between May 31 and Jun 21; clinic views peaked 23,945 (Jun 14); reach then fell to 20 (Aug 2).

**PREVIOUS CLAUDE INTERPRETATION**
- `[PREVIOUS CLAUDE INFERENCE]` The June spike was driven by the boost (paid), not organic growth; the boost likely brought low-intent followers.
- `[PREVIOUS CLAUDE INFERENCE]` The subsequent reach collapse is *consistent with* a boost ending and/or an unengaged follower base depressing organic distribution.

**HYPOTHESES (explicitly unproven)**
- `[HYPOTHESIS]` The boost *caused* Instagram to "throttle" organic reach because boosted followers didn't engage. **CAUSAL UNCERTAINTY — DO NOT TREAT AS FACT.** We have no engagement data, no per-post data, no boost campaign export. The reach decline is equally consistent with reduced/lower-quality posting after June, seasonal effects, content-market mismatch, or normal post-spike regression. Causation is not established.

**UNKNOWN about the boost** `[UNKNOWN]`: which post, budget, duration, objective, target audience, geography, resulting paid reach/impressions, paid-vs-organic follower split, posting cadence change after June, content/theme changes after June.

---

## SECTION 5 — DR GINA (marketing-relevant)

All `[PRIMARY-SOURCE FACT]` from the team biographies + knowledge base unless marked.
- **Credentials:** MB ChB (Stellenbosch, 2001), MBA, Dip Derm (Cardiff University), MRCGP, MBCAM, AFMCP. CQC-registered clinic.
- **Background:** primary→tertiary care; emergency medicine, surgery, O&G, paediatrics, ENT, dermatology; GP; practising functional medicine since 2004 (before mainstream in the UK).
- **Memberships/quals:** Oxford Society of Ageing and Longevity; British Society of Ecological Medicine; Longevity Docs; Independent Doctors Federation; Academy for Preventive and Innovative Medicine; GMC; Institute for Functional Medicine; WorldLink Medical (advanced bio-identical hormone programme).
- **Specialist areas:** bio-identical hormone therapy (women + men), hormone/longevity/functional medicine, whole-person/systems medicine.
- **Founder story / philosophy:** *"not what is wrong, but why."* Conviction that clinical markers for conditions including dementia and cardiovascular decline can be visible up to ~20 years before onset; conventional medicine is structured to treat illness rather than prevent it. Personal turning point: her own health declined despite following conventional protocols she'd trained in.
- **Voice / positioning (from bio one-liners):** "a longevity and functional medicine physician … at the frontier of preventative and whole-person medicine"; regular international conference speaker.
- **Topics she can credibly own** `[RECOMMENDATION]`: root-cause/"why not what" medicine; why "normal" bloods miss the picture; hormones/perimenopause/menopause; longevity/prevention; the four-pillar method.
- **Media / thought-leadership potential** `[PREVIOUS CLAUDE INFERENCE]`: high — founder narrative + speaking + credentials.
- **Existing content performance:** see Section 3 (Gina IG 2356 followers, reach collapsed to 4). No per-post content was viewable (IG not accessible).
- **Existing personal-brand strategy:** `[UNKNOWN]` beyond the two Instagram accounts and Facebook page.
- `[RECOMMENDATION]` (Claude) Lead with Dr Gina as the primary "attractive character"; her founder story is an unused asset. **Not user-approved as a decision.**

---

## SECTION 6 — THE SCHOEMAN CLINIC

`[PRIMARY-SOURCE FACT]` (knowledge base / website copy captured in KB) unless marked.
- **Positioning:** "Your Specialist in Hormone, Longevity and Functional Medicine." Four-pillar methodology; "one doctor, one picture"; whole-patient systems approach vs siloed specialists.
- **Services:** hormonal health (perimenopause, menopause, PCOS, endometriosis, PMDD, male hormone optimisation/andropause/TRT, adrenal, thyroid); longevity & functional (biological-age testing, nutrigenomics/epigenetics, mitochondrial/cellular, brain health); diagnostics (advanced bloods, genetic testing, gut testing, IV nutrient therapy, cardiology partnership, imaging). Also gut health, mental health/brain optimisation, MCAS, hypermobility, multi-system presentations.
- **Consultations & prices:** Initial concise 45 min £350; standard 60 min £500; comprehensive 90 min £750. Follow-ups: 30 min £250; 15 min brief £125; 45 min £350. (Hormone + Functional Medicine follow-up variants.)
- **Locations / days:** Video Tue & Thu; Wimbledon (Edition Clinic) Wed ×3/month; Harley Street (Creo) Mon ×3/month. Addresses: 96 Harley Street, London W1G 7HY; 4 St Marks Place, Wimbledon SW19 7NP.
- **Clinical philosophy:** functional/root-cause + longevity/prevention; every clinician trained across all four pillars.
- **Patient journey / consultation process:** enquiry form → registration → mandatory bloods (TDL, ~1 month before consult; menstruating days 18–22) → consultation → post-consultation letter within 5 working days. Free discovery call (10–15 min, all PAs) as low-friction entry.
- **Blood panels:** GS1–GS13 (£79–£489) + add-ons (some prices "TBC"); fasting column marked draft.
- **Team:** see Section 7.
- **Differentiators:** four-pillar, whole-patient, one-doctor-one-picture, prevention 20 years ahead.
- **Target market:** `[PRIMARY-SOURCE FACT]` avg age 49; core 46–65 (46.8%); 74% female; hormone entry 76.7%, gut 14.7%, skin 12.7%; London-dominant (49% by registered address), notable international base (South Africa, Kuwait, Saudi Arabia, Jersey, US).
- **Business model:** `[PRIMARY-SOURCE FACT]` (proposal v3) private, high-ticket. WILBA build deal: **$10,000 USD one-time (50/50 kickoff/go-live) + $1,000/mo retainer (min 3 months)**; Gina pays GHL HIPAA tier ~$297/mo.
- **Current marketing:** boosted-post-led social (see Sections 3–4); newsletter planned (w/c 24 Aug, moving MailChimp→GHL).
- **Current funnel:** enquiry form + discovery call; **no lead magnet**. See Section 18.
- **Website:** `theschoemanclinic.com`; new website being rebuilt with another provider, ETA ~beginning of August 2026. Site FAQ/footer showed WhatsApp `+44 7426 292 321` (mismatch vs operational inbox `+44 7426 494321`).
- **Lead capture:** minimal (enquiry form + discovery call). `[DERIVED METRIC]`/`[PREVIOUS CLAUDE INFERENCE]` no funnel to capture social reach.
- **CRM:** GoHighLevel (HIPAA tier) operational; Semble = clinical EHR. See Section 15.
- **Email:** MailChimp (being retired) → GHL. See Section 19.
- **Paid media:** June boost only known. See Section 20.
- **Referral channels:** existing referral network (Section 22).
- **Commercial objectives:** `[PRIMARY-SOURCE FACT]` scale a differentiated longevity clinic; grow to five doctors by end of 2026 (stated in KB); Mary-Anne Russell (CCO) leads commercial strategy/positioning/new revenue.
- **Unknowns:** `[UNKNOWN]` current website analytics, exact patient volumes, revenue figures, ad account state.

---

## SECTION 7 — DOCTOR / FACULTY INFORMATION

All biography facts `[PRIMARY-SOURCE FACT]` (team biographies). Content-territory notes are `[RECOMMENDATION]`/`[PREVIOUS CLAUDE INFERENCE]` and clearly marked.

**Dr Gina Schoeman — Founder & Medical Director.** (See Section 5.) Content territory `[RECOMMENDATION]`: root-cause thesis, hormones/longevity, founder story.

**Dr Nikita Grover — Longevity & Functional Medicine Specialist.** MBBS, MRCP, MRCGP, IFMCP. 30 yrs. Read History of Medicine & History of Art at UCL before medicine. Decade in hospital medicine; 25 yrs NHS GP (20 as partner, Highgate Group Practice); GP Clinical Tutor in Culinary Medicine (UCLH). Board cert IFM (2019); Mayr Medicine (Austria); PGCert Genomics (distinction, Cambridge); Dip Clinical Dermatology (distinction, QMUL); Dip Clinical Nutrition. Most recently **Head of Functional Medicine at Lanserhof at The Arts Club**. Content territory `[RECOMMENDATION]`: gut healing/Mayr, genomics, culinary/food-as-medicine, "came the long way round" story.

**Dr Sonia Tsukagoshi — Longevity & Functional Medicine Specialist.** MBBS, MRCGP, MA, AFMCP, DRCOG (+ Dip Fertility/Sexual/Reproductive Medicine). ~20 yrs NHS. **MA Medical Anthropology (SOAS).** Founded & chaired the WONCA World Special Interest Group for Integrative Medicine; exec member WONCA Europe; RCGP leadership. Certified health coach; training in coaching, psychology, yoga. Interests: midlife health, metabolic wellbeing, stress-related illness, sustainable behaviour change. Content territory `[RECOMMENDATION]`: culture/behaviour change, midlife, why the same symptom means different things per person.

**Dr Zia Knippenberg-Stratos — Longevity & Functional Medicine Specialist.** MD, RNutr, IFM, WALSH. Trained Georgetown + UCL. Registered nutritionist; certified FM practitioner; WALSH advanced nutrient therapy; intuitive eating counsellor. UCL MSc Clinical & Public Health Nutrition; published research on diet & autoimmunity. **Founder of "Food as Medicine."** Focus: gut microbiome, gut-brain axis, nutritional psychiatry, early-life nutrition (first 1,000 days). Fluent in six languages (English, French, Greek, Spanish, Portuguese, Dutch). Contributions to WHO, UNICEF, The Trussell Trust. Content territory `[RECOMMENDATION]`: gut-brain, food-as-medicine, mental health/nutrition, family/early-life.

**Dr Nathan Curran — Longevity & Functional Medicine Specialist.** MB ChB (Hons Genetics), Dip Nutr Med (Surrey), DOccMed. Stellenbosch (medical + intercalated honours Human Genetics). 20 yrs in the City of London serving blue-chip institutions (Google, Deutsche Bank, Bank of America Merrill Lynch, BNP Paribas). Multi-omic diagnostics (genomics, epigenomics, proteomics, metabolomics, microbiomics); hormone optimisation; immune restoration; geroprotective/regenerative therapies (peptides, photobiomodulation, stem cells, plasmapheresis, EBOO). **Press: Financial Times, British Vogue, Tatler 2025 Address Book, Harper's Bazaar, The Telegraph.** Worked with elite athletes (Premier League football, pro cycling, weightlifting). Content territory `[RECOMMENDATION]`: cutting-edge longevity/regenerative, executive performance/burnout, the media-magnet/premium angle.

**Mary-Anne Russell — Chief Commercial Officer.** Founder of **Trinity Square** (commercial strategy consultancy). 25 yrs commercial/GTM leadership (PE-backed + scale-ups; SaaS, cybersecurity, consulting, legal, tech-enabled services). **Marketing Week Top 100 most effective marketers.** CIM AI & Marketing (mini MBA). Proprietary GTM Diagnostic tool. At the clinic leads commercial strategy, positioning, marketing, referral strategy, new revenue. **Note (important for lane):** she owns clinic marketing strategy; WILBA's proposed role was positioned as execution/intelligence under her strategy — see Sections 10, 27, 28.

**Mati Simarro — Chief Digital Officer.** Founder of an AI consultancy. PRINCE2/Agile/Scrum/MSP. Practising acupuncturist & naturopath. `[PRIMARY-SOURCE FACT]` (earlier context) Mati owns the client relationship / knowledge base / patient-journey copy / Semble / compliance; primary WILBA contact.

**Cécile Vallée — Longevity & Functional Medicine Health Coach.** `[PRIMARY-SOURCE FACT]` **STRICTLY EMBARGOED UNTIL 1 SEPTEMBER 2026** — do not publish before then.

**Zoey Van Huyssteen — Patient services & admin (PA).** **Isabell Drake — Patient services & admin (PA).**

**Other people referenced (earlier context / KB):** `[PRIMARY-SOURCE FACT]` **Lisa Roberts** — Lead Admin/Patient Liaison, **resigned effective 13 Aug 2026 (CONFIDENTIAL — keep out of team-facing comms).** **Louise** — PA. **Griffin** — the developer building the GHL system (WILBA side). **Nadia Babar** — social media scheduling (clinic side). **Jess Morrell** — WILBA founder (the user); owns GHL + WhatsApp workstream + team training.

**Existing audience/content per doctor:** `[UNKNOWN]` — only the two Instagram accounts + two Facebook pages have data (Section 3); no individual-doctor social data provided.

---

## SECTION 8 — AUDIENCE INTELLIGENCE

**Evidence-backed (from KB patient data)** `[PRIMARY-SOURCE FACT]`:
- Avg age 49; core 46–65 (46.8%); 74% female.
- Entry points: hormone therapy 76.7%; gut health 14.7%; skin 12.7%.
- Geography: London-dominant (49% by registered address); international base (SA, Kuwait, Saudi, Jersey, US) — some London addresses are secondary residences for international patients.
- Two personas described in the positioning material: (1) the "diagnostic-odyssey" patient (seen multiple specialists, told results are "normal," out of options); (2) the proactive "future-proofer" (40–55) wanting advanced diagnostics before symptoms.
- Mindset: evidence-led, sceptical of wellness "fluff," wants real medicine + advanced diagnostics.
- Not-a-good-fit (from KB): single-issue/one-off seekers, unwilling-to-engage-with-diagnostics, price-sensitive, seekers of unregulated protocols.

**Claude-created strategic framing (not evidence)** `[RECOMMENDATION]`/`[PREVIOUS CLAUDE INFERENCE]`:
- "ELF" ideal-client framing (Easy/Lucrative/Fun) applied to the two personas.
- Language angles ("your bloods came back normal but you still feel terrible"), problem/desire mapping. These are proposed, not validated against audience research.

**Unknown** `[UNKNOWN]`: social-audience demographics/geography, psychographics beyond the above, explicit fears/objections/questions in patients' own words, awareness levels, content preferences, social behaviour.

---

## SECTION 9 — POSITIONING & BRAND

**Source-derived** `[PRIMARY-SOURCE FACT]`:
- Clinic positioning: "Your Specialist in Hormone, Longevity and Functional Medicine"; four-pillar; one-doctor-one-picture; prevention/root-cause.
- Dr Gina thesis: "not what is wrong, but why."
- **Tone/voice rules confirmed by Gina (from KB / gina-kb-answers):** warm, patient-centred, polished/premium; **avoid negative words** ("unfortunately", "cannot"); **no emojis** (patient-facing); **never mention/compare competitors**; sign-off "Best wishes, The Schoeman Clinic Team"; first names OK. **Gina dislikes em dashes — keep them out of all patient-facing copy.**
- Commercial strategy/positioning is owned by Mary-Anne Russell (CCO) `[PRIMARY-SOURCE FACT]`.

**Claude-proposed (not user-approved)** `[RECOMMENDATION]`:
- Lead with Dr Gina as "attractive character"; faculty-as-content-engine; content pillars (root-cause education, founder/philosophy, patient transformations, myth-busting, behind-the-method).
- These pillars were proposed in the audit/strategy discussion; the user did **not** formally approve them as final brand pillars.

**User-approved** `[DECISION]`: the tone rules above are Gina's (source), not Claude's. Phase-1 accounts to grow = Dr Gina + The Schoeman Clinic + faculty (Section 27).

---

## SECTION 10 — EXISTING SOCIAL STRATEGY (migrated, not improved)

The following was **proposed by Claude** during the conversation (via the `social-growth-strategist` lens). It is `[RECOMMENDATION]` unless a `[DECISION]` is noted. It has **not** been fully approved; the user instructed an architecture-first audit before building.

- **Core insight (proposed):** not a followers problem — a reach + funnel problem. Capture the not-ready-yet majority with a low-friction lead magnet and nurture them (Dean Jackson), lead with an irresistible offer/value ladder (Brunson), lead with relationships/right-clients (Polish).
- **Account architecture (proposed):** consolidate around Dr Gina as the face; clinic + Gina as hubs; doctors as recurring "faculty features." `[DECISION]` The user confirmed Phase-1 growth spans Dr Gina + Clinic + faculty (which accounts/how they interrelate = still open).
- **Platform strategy (proposed):** reach = Reels/TikTok/YouTube Shorts; authority/high-ticket trust = LinkedIn + long-form YouTube; nurture = Instagram Stories/Facebook. Deprioritise Facebook organically; hold for paid/retargeting. Pick 2–3 and dominate.
- **Value ladder (proposed):** lead magnet (missing) → free discovery call (exists) → consults £350–£750 → ongoing/premium.
- **Lead magnet (proposed):** a 2-minute self-assessment quiz (e.g. "Is it hormonal?") to capture email + segment → discovery call.
- **Content pillars (proposed):** root-cause education; Dr Gina's story/philosophy; patient transformations (compliant); evidence-led myth-busting; behind-the-method.
- **Formats/cadence:** per platform-playbook; tied to real capacity; monthly "capture day" for the faculty (batch-record short answers). `[RECOMMENDATION]`
- **CTAs / lead capture / repurposing / capture / editing / distribution:** covered by the proposed "machine" (Section 26).

---

## SECTION 11 — CONTENT INTELLIGENCE

**Evidence-limited.** Instagram content itself was **not viewable** (network blocked). What exists:
- `[RAW DATA]` The June boosted post (unidentified) coincided with the only high-reach period.
- `[PREVIOUS CLAUDE INFERENCE]` "What worked in June" cannot be attributed to content vs paid boost without per-post data.
- `[RECOMMENDATION]` (Claude) hook-first production; one-idea-per-post; save/send-worthy formats; carousels for saves, Reels for reach, Stories for nurture; captions with a hook line; editing for retention (first-frame hook, captions on, value <3s, one CTA); repurpose one idea across platforms.
- **Winning/failing themes, doctor/topic combinations, audience language, visual style:** `[UNKNOWN]` — no per-post/creative data was available. Any such claim would be unproven.

**Limitation to preserve:** all content-performance conclusions here are based on **weekly aggregate reach/views/followers only**, plus one user-stated boost. No creative, caption, hashtag, or per-post data exists in this migration.

---

## SECTION 12 — EXISTING SKILLS

Skills live in the repo at `.claude/skills/<name>/SKILL.md`. Full text is in the repo; the frontmatter `description` (the trigger config) is reproduced faithfully; bodies are summarised faithfully (not rewritten). This list is believed complete for this conversation but is not guaranteed exhaustive.

### 1. `marketing-comms-counsel` — STATUS: **CREATED** (committed earlier in the conversation)
- PURPOSE: senior international marketing/comms compliance counsel — consent wording, opt-in flows, privacy notices, sub-processor registers, DPIA, data-flow, per-channel opt-in; UK GDPR/PECR/EU GDPR/CAN-SPAM/CASL/Meta-WhatsApp; strong for healthcare special-category data.
- TRIGGER (verbatim description keywords): "consent form", "opt-in", "marketing consent", "privacy notice", "GDPR", "PECR", "can we email/WhatsApp patients", "cookie banner", "DPIA", "unsubscribe", "data flow", "sub-processor".
- RESPONSIBILITIES: produce review-ready drafts; always state qualified local legal sign-off required before go-live; pin jurisdiction/data/systems/channels/purposes/controller-processor; apply consent standard; per-channel unticked opt-in.
- OUTPUTS: consent copy, form consent blocks, privacy-notice inserts, lawful-basis tables, sub-processor register, DPIA outline, comms rulebook, data-flow review.
- DEPENDENCIES: used by the consent pack build. OVERLAPS: compliance guardrails referenced by the social skills.

### 2. `ghl-inbox-health-check` — STATUS: **CREATED**
- PURPOSE: guided, non-technical diagnostic for a GoHighLevel shared inbox (WhatsApp/SMS/email) — connection, wallet/billing, Meta verification, inbound webhooks, 24-hour window + templates, user access, double-messaging.
- TRIGGER: "inbox not working", "messages not coming through", "can't reply", "WhatsApp not connected", "conversations not loading", "double messaging", "shared inbox audit", "is the inbox working", "GHL health check".
- RESPONSIBILITIES: pin symptom (inbound/outbound/both/when/who) → walk 7-link pipeline → triage table → health report + prioritised fixes → drafted developer hand-off → go-live checklist. Notes an optional automated layer if GHL API creds are provided (mirroring the Monkey Joe's `mj_ghl_audit` GitHub Action pattern).
- NOTE: relevant to Schoeman ops, not the social machine.

### 3. `social-growth-strategist` — STATUS: **CREATED**
- PURPOSE: growth strategy combining Russell Brunson (offers/value ladder/funnels/hook-story-offer/Dream 100/attractive character), Joe Polish (relationship & referral marketing/ELF clients/market to the affluent/value-first), Dean Jackson (low-friction lead capture/list-building/8 profit activators/before-during-after/nurture).
- TRIGGER: "social media strategy", "content plan", "social audit", "grow my audience", "personal brand", "lead magnet", "funnel", "offer", "nurture sequence", "email marketing", "Instagram", "how do I get more clients".
- RESPONSIBILITIES: ELF/goal anchoring; seven-lens audit (positioning/attractive character; offer/value ladder; lead capture; content/story; nurture; Dream 100; metrics); foundation-before-fancy; funnel map; content pillars; nurture; Dream 100/referral; 90-day roadmap; real KPIs; healthcare-compliance guardrail (defer to marketing-comms-counsel).
- OUTPUTS: audit scorecard, positioning, offer/lead magnet, funnel map, content pillars/calendar, nurture sequence, Dream 100 plan, KPI scoreboard.

### 4. `social-platform-playbook` — STATUS: **CREATED** (later **MODIFIED** — boost-trap section added)
- PURPOSE: per-platform optimisation on durable feed mechanics (hook, watch-time/dwell, saves/sends, comments, early velocity, keep-on-platform, consistency, profile-as-landing-page) + a "verify current specifics" step; LinkedIn, Instagram, Facebook, TikTok, YouTube (long + Shorts); platform selection; **paid: the boost-button trap** (spike-then-collapse = rented vanity reach; use Ads Manager conversion campaigns not boosts).
- TRIGGER: "algorithm", "reach", "go viral", "Reels", "Shorts", "LinkedIn post", "posting schedule", "best time to post", "which platform", "profile optimisation", "hashtags", "hook", "why is my reach down".
- MODIFICATION: a "Paid reach: the boost-button trap" section was appended after building the audit (informed by the June boost finding).

### 5. `content-studio` — STATUS: **CREATED**
- PURPOSE: create/edit/repurpose content — turn an idea/voice note/transcript/long video into finished, platform-shaped, on-brand posts and atomise one asset across channels; video (short-form scripts, edit direction, captions/subtitles), copy (hooks, captions, carousels), repurposing.
- TRIGGER: "write a post", "caption", "hook", "video script", "reel", "edit this", "repurpose", "turn this into content", "content calendar", "carousel", "make this into a video".
- RESPONSIBILITIES: rule-zero strategy-first + hook-first; production method (anchor → hook → structure → shape per platform → edit for retention → on-brand + compliant); video editing checklist; copy editing checklist; atomisation engine; compliance guardrails (human review before publishing for regulated accounts).

### PROPOSED skills (NOT built) — `[RECOMMENDATION]`, awaiting approval
- `faculty-account-architect` — which doctor/account says what; expertise matrix; per-doctor capture questions; account architecture. (Answers "which doctor/account" + capture sourcing.)
- `content-performance-analyst` — metric definitions, analytics reading, performance memory, experiment tracking, the learn-loop. (Answers "how measured" + "what did we learn".)
- `social-content-engine` — orchestrator running the 12-question pipeline across the other skills + the Social OS memory files.
- Plus proposed **extensions** to existing skills: audience-intelligence depth, "why now"/timeliness, content-calendar logic (into strategist); hook-intelligence library (into content-studio/playbook).

**Overlaps to watch:** strategist ↔ platform-playbook (both touch hooks/pillars); content-studio ↔ playbook (formatting). Compliance is centralised in marketing-comms-counsel.

---

## SECTION 13 — AGENTS / SUBAGENTS

- **None created.** `[UNKNOWN]`/N/A — no Claude subagents/agents were created, proposed, or configured for Schoeman in this conversation. (The proposed `social-content-engine` is an orchestration *skill*, not a subagent; it was described as calling other skills + reading/writing memory files, not as an autonomous agent with its own tools/permissions/memory.)

---

## SECTION 14 — COMMANDS / WORKFLOWS / AUTOMATIONS

- **No new slash commands or scripts were created for the social machine.** The proposed `social-content-engine` (a "12-question pipeline") is `[RECOMMENDATION]`/PROPOSED, not implemented.
- **Clinic-side automations already exist (developer-owned, not in this repo)** `[PRIMARY-SOURCE FACT]` (`Current_Automations.docx`): Patient Letter Generator (Lovable → new AWS); Blood Test Payment Notifications; Blood Test Form Email to Patient (fasting/no-fasting); Post-Consultation Letter (auto, by 8pm Mon–Fri); Blood Results Not Ready Alert (moved to email); Patient Reactivation Report (Hostinger dashboard); Digital Tracker. An **n8n** post-consult automation is being replaced by a GHL-driven post-consultation email (Griffin).
- **Repo automations (WILBA/Monkey Joe's, unrelated to Schoeman):** existing GitHub Actions + scripts (`mj_ghl_audit.py`, etc.) — referenced only as a *pattern* for a possible future GHL audit.

---

## SECTION 15 — GHL / CRM

Separate **current state** from **proposed**. Detailed GHL configuration lives in the developer's environment, not this repo.

**CURRENT STATE** `[PRIMARY-SOURCE FACT]` (user-pasted Telegram + KB, some via compacted context):
- GoHighLevel (HIPAA tier) is the operational CRM; Semble is the clinical EHR (clinical records never migrate to GHL).
- GHL + WhatsApp connected; shared inbox live for the PA team.
- ~815 patients migrated Semble → GHL; **no "inactive" patients migrated**; all workflows currently **OFF** until launch.
- WhatsApp runs via **Coexistence**; operational number **+44 7426 494321**.
- Post-consultation email built in GHL (Griffin), tested, switched off; goes live at launch and replaces the old/n8n letter automation.
- Semble sends appointment reminders (GHL/AI must not duplicate).
- Patient consent + privacy notice pack built (see Section 23), delivered for the clinic's data team to sign off.
- **Known problems:** double-messaging (Coexistence mirroring — team answering in both the phone WhatsApp app and GHL) — unresolved `[HYPOTHESIS]` for cause; an Aug inbox outage where the owner **reconnected WhatsApp by re-scanning the QR from the phone** `[PRIMARY-SOURCE FACT]` (indicates a phone-linked session that can drop) — `[PREVIOUS CLAUDE INFERENCE]` the connection is phone-linked rather than hosted Cloud API; robustness fix not yet done.
- Twilio caller-ID: 494321 approach; landline verification failed; GHL wallet top-up was owed by Gina (per earlier Telegram).

**PROPOSED / OPEN** `[RECOMMENDATION]`/not-built:
- Discovery-call booking calendar: **not built** — spec: all PAs (Zoey, Louise, Isabell), M–F 10:00–16:30, round-robin by availability, remove Griffin (test user), block leave, embedded on the website next to the enquiry form.
- Confirm connection type (hosted Cloud API vs phone-linked) + add a disconnect alert.
- `[UNKNOWN]`: full detail of pipelines, opportunities, custom fields, tags, forms/surveys, calendars, attribution config in GHL.

---

## SECTION 16 — IHF DATA

**IHF marketing data was NOT provided in this conversation.** `[UNKNOWN]`
- The user stated an intention to "integrate the IHF strategy and details" and to "give more information," but **no IHF lead volume, lead sources, Symptoms Evaluation results, survey data, call bookings, show rates, conversion, workflow/email/SMS performance, revenue, cohorts, channels, or funnel data was actually supplied.**
- Background only `[PRIMARY-SOURCE FACT]` (workspace context): IHF = Integrated Health Foundation, an online health program for dysautonomia/POTS/MCAS/chronic illness, 4-pillar approach (Limbic, Lifestyle, Nutrition, Accountability); Jess Morrell was Head of Operations/Marketing/Strategy; the role was winding down (revenue had dropped from ~USD $5,000/mo to ~$1,500/mo). This is **historical, external** background — **do not treat IHF audience/correlations as Schoeman evidence or clinical evidence.**
- ACTION: IHF material must be recovered from the user (Section 29).

---

## SECTION 17 — SYMPTOMS EVALUATION SURVEY

**Not provided.** `[UNKNOWN]`
- The "Symptoms Evaluation" was named **only** in the user's Phase-1 brief as a downstream system the social architecture should later connect to.
- **No purpose detail, questions, structure, fields, completion/drop-off data, results, symptom categories, response patterns, conversion, nurture, segmentation, scoring, CRM integration, or proposed Schoeman adaptation was supplied or created.**
- Everything about the Symptoms Evaluation is currently unknown and must be recovered from the user / IHF (Section 29).

---

## SECTION 18 — FUNNEL

**Current (exists today)** `[PRIMARY-SOURCE FACT]`:
- Social attention (Instagram, underperforming) → website/enquiry form OR free discovery call (10–15 min, PAs) → registration → mandatory bloods → consultation → post-consultation letter. Recall at 6 weeks for planned follow-ups.
- **No lead magnet, no email opt-in from social, no nurture sequence.**

**Proposed (not built)** `[RECOMMENDATION]`:
- Social/Dream 100 → lead magnet (self-assessment quiz) → email capture → nurture → discovery call → consult → referral loop.
- Downstream connection points named by the user (not built): Symptoms Evaluation, GHL, nurture, consultation conversion, attribution, paid media, partnerships, SEO, email.

---

## SECTION 19 — EMAIL / NURTURE

**Existing** `[PRIMARY-SOURCE FACT]`:
- Newsletter planned for **w/c 24 Aug 2026**; email is **moving from MailChimp to GoHighLevel**.
- Consent pack built to enable compliant marketing (per-channel opt-in) — required before mass newsletter send.
- `[UNKNOWN]`: existing email list size, past campaign performance, segmentation, open/click rates.

**Proposed (not built)** `[RECOMMENDATION]`:
- Post-lead-magnet nurture sequence (value-first → story → proof → soft CTA to discovery call) + long-term newsletter nurture.

---

## SECTION 20 — PAID MEDIA

- `[PRIMARY-SOURCE FACT]` One known paid action: a **standard "Boost Post"** in June 2026 (Dr Gina). See Section 4.
- `[UNKNOWN]`: budget, duration, objective, audience, creative, results split, retargeting, any other campaigns, ad-account state.
- `[RECOMMENDATION]`: replace boosting with proper Ads Manager conversion campaigns targeting the lead magnet; organic + funnel first, paid amplifies.

---

## SECTION 21 — WEBSITE / SEARCH / SEO

- `[PRIMARY-SOURCE FACT]` Website `theschoemanclinic.com`; a **new website is being rebuilt with a different provider (ETA ~beginning of Aug 2026)**; developer "Giedrius" to have a review link by end of a Friday (per Telegram).
- `[PRIMARY-SOURCE FACT]` Website FAQ/footer showed WhatsApp `+44 7426 292 321` (mismatch vs operational `+44 7426 494321`) — needs correcting.
- **Website could not be fetched in-session (network egress blocked).** `[UNKNOWN]`: traffic, landing pages, conversion, SEO, Google Search Console, GA4, search demand, keywords, articles, AI-search, YouTube search.

---

## SECTION 22 — DREAM 100 / PARTNERSHIPS / PR

**Existing referral network** `[PRIMARY-SOURCE FACT]` (KB): Edition Clinic (Dr Zunaid Ali/"Alli", Dr Unnati Desai — aesthetics/intimate health); Dr Niraj Singh (neurodevelopmental psychiatry); One Heart Clinic / Dr Deven Patel (cardiology); Jackie McCusker & Mays Al-Ali (nutrition); Miss Claire Mellon (gynaecology); Dr Sasha Usiskin (breast imaging/radiology); Dr Sarmed Sami (gastroenterology); Rainford Hall & Steps Together (addiction/rehab).

**Faculty press assets** `[PRIMARY-SOURCE FACT]`: Dr Nathan Curran featured in FT, British Vogue, Tatler, Harper's Bazaar, The Telegraph; Dr Nikita Grover ex-Lanserhof; Dr Gina international speaker.

**Proposed (categories, not researched targets)** `[RECOMMENDATION]`/`[HYPOTHESIS]`: menopause/longevity podcasters, women's-health voices, private members' clubs, corporate wellness, JV/audience-borrowing, patient referral loop with recognition rewards (priority access, named liaison, invite-only events — matches a KB note that Gina prefers recognition over vouchers). **No specific Dream 100 targets were researched or listed.**

---

## SECTION 23 — COMPLIANCE

**Created** `[PRIMARY-SOURCE FACT]`/built:
- Skill `marketing-comms-counsel` (Section 12).
- **Patient Consent & Privacy Notice pack** (`outputs/schoeman-clinic/Schoeman-Clinic-Consent-DataProtection-Pack.{docx,pdf,html}`): Part A = short tick-box form copy (enquiry + registration, explicit health-data consent, separate marketing opt-in, per-channel, unticked); Part B = 12-section privacy notice (controller, data, purposes, lawful bases Art 6 + Art 9(2)(a)/9(2)(h), sharing, international transfers/UK IDTA, retention, security, rights, marketing choices, ICO complaint, changes). Iterated heavily per user feedback (see Section 27). Grounded partly in web research (ICO guidance, GDPR consent examples).
- Key compliance flags captured: replace "EU GDPR" → "UK GDPR" across Semble forms + policies; Semble auto-marking SMS/email consent is **not valid consent**; add GHL + WhatsApp/Meta as processors; MailChimp being retired; remove retargeting-ads clause from website policy (ads not currently run); DPIA recommended (special-category + new CRM + international transfer).
- Tone/claims guardrails for social (in the social skills): no medical claims/cures/guarantees, no health-anxiety bait, ASA/CQC awareness, testimonials/patient-story caution, human review before publishing for a clinic.
- `[UNKNOWN]`: final legal sign-off status (pack was for the clinic's data team to review).

---

## SECTION 24 — MEASUREMENT & ATTRIBUTION

**Actually tracked today** `[RAW DATA]`: weekly IG Views/Reach/Reposts/Followers; daily FB Page Followers. Nothing else.

**Proposed (not built)** `[RECOMMENDATION]`:
- KPIs: reach, saves, sends, profile visits, leads (email opt-ins), discovery calls booked, enquiry→consult conversion, list growth — not vanity followers.
- A `content-performance-analyst` skill + `performance-log.md` + `experiments.md` memory files (learn-loop).
- Downstream (deferred): UTMs, first/last touch, content/campaign IDs, GHL conversion ingestion, dashboards, weekly reporting.
- **No attribution, UTM scheme, or dashboard was built.**

---

## SECTION 25 — EXPERIMENTS & LEARNINGS

- **The June boost "experiment" (observed, not designed):** hypothesis — boosting grows the account; result — a spike then a ~99% reach collapse and flatlined followers; interpretation `[PREVIOUS CLAUDE INFERENCE]` — boosting bought vanity reach that evaporated; **confidence: causal link to organic throttling is LOW (no engagement/per-post data)**; decision `[RECOMMENDATION]` — stop boosting, use proper conversion campaigns + build a funnel. (Also folded as a lesson into `social-platform-playbook`.)
- **Audit finding (learning):** the account has reach + funnel problems, not a followers problem `[DERIVED METRIC]`/`[PREVIOUS CLAUDE INFERENCE]`.
- No other formal experiments/tests were run. `[UNKNOWN]` per-content experiments.

---

## SECTION 26 — CURRENT CAPABILITY MAP

| Capability | Status | Where it lives / was discussed | What it does | Maturity | Known gaps |
|---|---|---|---|---|---|
| Growth strategy | Built | `.claude/skills/social-growth-strategist` | Offers, funnel, Dream 100, nurture, 7-lens audit | Medium | audience depth, "why now", calendar logic |
| Platform optimisation | Built | `.claude/skills/social-platform-playbook` | Feed mechanics, formats, platform choice, boost-trap | Medium | hook library; live-verify specifics |
| Content production/editing | Built | `.claude/skills/content-studio` | Create/edit/repurpose, atomisation | Medium | hook intelligence depth |
| Compliance | Built | `.claude/skills/marketing-comms-counsel` + consent pack | Consent, privacy, claims guardrails | Higher | legal sign-off pending |
| GHL inbox diagnostics | Built | `.claude/skills/ghl-inbox-health-check` | Inbox health check (ops) | Medium | automated layer needs API creds |
| Social audit (data-backed) | Done | `outputs/schoeman-clinic/SOCIAL-AUDIT.md` + `social-data/` | IG/FB analysis, 7-lens scores | One-off | needs per-post + analytics |
| Faculty/account architecture | Proposed | conversation only | which doctor/account says what | Not built | — |
| Performance memory / analyst | Proposed | conversation only | measurement + learn-loop | Not built | — |
| Orchestration (12-question engine) | Proposed | conversation only | runs the pipeline | Not built | — |
| Social OS memory files | Proposed | conversation only | persistent state | Not built | — |
| 30-day social system | Proposed (gated) | conversation only | the first production milestone | **Do NOT build until architecture approved** | — |

---

## SECTION 27 — DECISION LOG

`[DECISION]` (explicit user choices/instructions):
1. **Target of the marketing machine = The Schoeman Clinic** (chosen via a direct question).
2. **"Edit the content" scope = all three** (video, copy, repurposing) — full content studio.
3. **Platform-skill structure = delegated to Claude's expertise** → Claude chose **one combined `social-platform-playbook`** (not separate per-platform skills).
4. **Phase 1 priority = SOCIAL GROWTH → CONTENT INTELLIGENCE → LEAD CAPTURE → MEASUREMENT**; do **not** build the entire Growth OS at once; build the social system with downstream conversion in mind but don't implement downstream now.
5. **Accounts to grow in Phase 1 = Dr Gina + The Schoeman Clinic + the wider doctor/faculty content.**
6. **Audit the existing skills and architecture FIRST; do NOT create the 30-day system until architecture is approved.**
7. **Migrate to a new Claude Code project `schoeman-growth-os`;** produce this migration pack; **stop after the pack + Source Recovery List — do not begin implementing.**

Consent-pack decisions `[DECISION]`:
8. Rejected the heavy DPO-style pack ("this looks so basic"/"this is wrong"/"doesn't look good"); wanted **just the checkbox + the regulation detail**; then wanted it **comprehensive**; final = tick-box form copy + full 12-section privacy notice.
9. **No em dashes** in patient-facing copy (Gina's preference).
10. Ads: **don't treat retargeting as an open question — remove the clause** (clinic doesn't run ads); fold DPIA into one pack.
11. Rejected use of the Artifact publishing tool earlier; preferred files delivered directly.

Not-yet-decided / merely proposed (do **not** treat as approved): the specific content pillars, lead-magnet quiz, account-consolidation, the new skills, the 30-day system.

---

## SECTION 28 — OPEN QUESTIONS

1. `[UNKNOWN]` **WILBA's lane vs Mary-Anne Russell (CCO/Top-100 marketer) and Nadia (scheduling)** — is WILBA the full social engine, or a specific execution/intelligence slice under Mary-Anne's strategy? Unresolved.
2. `[UNKNOWN]` **IHF material** — promised but not provided.
3. `[UNKNOWN]` **Symptoms Evaluation survey** — named only; no detail/data.
4. `[UNKNOWN]` **Account architecture specifics** — do individual doctors get their own accounts, or feature on Gina/clinic hubs?
5. `[UNKNOWN]` **Boost specifics** (post, budget, duration, objective, audience) and whether it was one-off or ongoing.
6. `[UNKNOWN]` **Who currently creates content** (Nadia schedules; creator unknown).
7. `[UNKNOWN]` **Analytics access** (Meta Business Manager, GA4, Search Console) — not granted/seen.
8. `[UNKNOWN]` **Per-post / creative / engagement data** — needed to validate any content or June-causation conclusions.
9. `[UNKNOWN]` **LinkedIn / YouTube / TikTok presence** — not provided.
10. `[UNKNOWN]` **Second biographies file** — whether `Schoeman_Clinic_Doctor_Biographies.docx` differs from the `_11` version.
11. `[UNKNOWN]` **Architecture approval** — the proposed machine (new skills, Social OS, orchestrator) is awaiting the user's audit/approval.
12. **Contradiction to resolve:** Gut Map discount code — older KB notes say `DRGINA`; the finalised partners PDF says `TSC10`. WhatsApp number mismatch (site 292 321 vs inbox 494321).

---

## SECTION 29 — SOURCE RECOVERY LIST

**CRITICAL**
1. **The four social exports** (`schoemanclinicinstagram.CSV`, `drginaschoemaninstagram.CSV`, `TheSchoemanClinicFacebookPage.CSV`, `DrGinaSchoemanFacebookPage.CSV`) — WHY: the only hard performance data. Enables all trend/audit verification. *Partially preserved* here (values + in `social-data/`). Recover originals to add engagement/geography if the platform allows richer exports.
2. **Team biographies** (`Schoeman_Clinic_Doctor_Biographies_11.docx`) — WHY: the faculty content engine + positioning depend on it. *Partially preserved* (facts in Sections 5, 7; full docx saved to `source-notes/`).
3. **The Google Drive "Knowledge base" folder** (esp. `Schoeman_Clinic_Knowledge_Base_Trimmed`, `Consultations type and prices`, `BLOOD_TEST_TYPES_with_prices.docx`, `Our_Partners_updated.pdf`) — WHY: services/prices/journey/partners; ground truth for content + compliance. *Partially preserved* (summaries here; originals in Drive folder id `1Zdq-ax7hkcX9zFV37kYcdpTAeeZ95XYt`).
4. **IHF marketing data + the Symptoms Evaluation survey** — WHY: required to "integrate IHF" and to design the assessment lead magnet/funnel; currently entirely absent. *Not preserved — must be supplied.*
5. **Richer social analytics + per-post/creative data** (Meta Business Suite export, Instagram Insights per post, saves/shares/profile visits/link clicks) — WHY: to validate the June-boost causation and identify winning content. *Not preserved.*

**USEFUL**
6. **Boost campaign details** (Ads Manager/boost receipt: post, budget, duration, objective, audience, results) — WHY: to confirm Section 4 and set a paid baseline. *Not preserved.*
7. **Website + analytics** (new site once live; GA4; Search Console) — WHY: funnel/SEO baseline. *Not preserved (site was egress-blocked).*
8. **Email/MailChimp export + list state** — WHY: nurture + newsletter baseline before the GHL migration. *Not preserved.*
9. **The consent pack + privacy policies + enquiry-form fields** — WHY: compliance for the funnel/newsletter. *Partially preserved* (pack built in `outputs/schoeman-clinic/`).
10. **Proposal v3** (`source-notes/proposal-v3.txt`) — WHY: deal scope/commercial context. *Preserved in repo.*
11. **Telegram thread (Mati/Griffin/Gina)** — WHY: launch timeline + operational decisions. *Partially preserved* (`telegram-thread-log.md`).

**OPTIONAL**
12. Second biographies file; the other Drive KB docs (post-consult letter, barcode email, blood invoice, KB session docs); Current_Automations.docx (ops, not social).
13. WILBA's own brand assets (`outputs/brand/*`) — only if intentionally reusing WILBA methodology; **do not confuse with clinic brand.**

---

## SECTION 30 — RECOMMENDED FILE MIGRATION (mapping only — do not create)

- `source-material/` → team biographies docx; consent pack (docx/pdf/html); proposal v3; KB source docs (from Drive); privacy policies.
- `context/` → this migration pack; the Schoeman `CONTEXT.md`; decision log; open questions; tone/brand rules.
- `data/social/` → the four CSVs; `SOCIAL-AUDIT.md`; derived-metrics notes.
- `data/ghl/` → GHL current-state notes; `Current_Automations.docx`; inbox/health notes.
- `data/ihf/` → (empty until IHF data supplied) — placeholder + recovery note.
- `data/surveys/` → (empty until Symptoms Evaluation supplied) — placeholder + recovery note.
- `research/` → web-research citations (ICO/GDPR; platform best-practice to be verified).
- `strategy/` → the proposed social strategy (Section 10); the proposed machine architecture; positioning/pillars (marked proposed).
- `content/transcripts/` → (empty) capture-day transcripts once produced.
- `content/production/` → future scripts/carousels/captions (content-studio outputs).
- `content/published/` → future published assets + IDs.
- `experiments/` → the boost learning; `experiments.md` scaffold.
- `reports/` → `SOCIAL-AUDIT.md`; future weekly reports; `gina-call-final.*`.
- `.claude/skills/` → `marketing-comms-counsel`, `ghl-inbox-health-check`, `social-growth-strategist`, `social-platform-playbook`, `content-studio` (built) + proposed skills (once approved).
- `.claude/agents/` → (none yet).

---

## SECTION 31 — MACHINE-READABLE HANDOVER INDEX

```yaml
project: schoeman-growth-os
migration_pack: schoeman-claude-history-01.md
entities:
  - Dr Gina Schoeman (Founder & Medical Director)
  - The Schoeman Clinic (UK, CQC-registered, hormone/longevity/functional medicine)
faculty:
  - Dr Gina Schoeman
  - Dr Nikita Grover
  - Dr Sonia Tsukagoshi
  - Dr Zia Knippenberg-Stratos
  - Dr Nathan Curran
  - Mary-Anne Russell (CCO)
  - Mati Simarro (CDO)
  - Cecile Vallee (health coach; EMBARGOED until 2026-09-01)
  - Zoey Van Huyssteen (PA), Isabell Drake (PA)
other_people:
  - Lisa Roberts (Lead Admin; resigned eff 2026-08-13; CONFIDENTIAL)
  - Louise (PA), Griffin (developer), Nadia Babar (social scheduling), Jess Morrell (WILBA)
accounts:
  instagram: ["@schoemanclinic (~1516 followers)", "@drginaschoeman (~2356 followers)"]
  facebook: ["Schoeman Clinic page (13)", "Dr Gina page (6)"]
  linkedin: unknown
  tiktok: unknown
  youtube: unknown
platforms_with_data: [instagram_weekly, facebook_daily_followers]
datasets:
  - schoemanclinicinstagram.CSV
  - drginaschoemaninstagram.CSV
  - TheSchoemanClinicFacebookPage.CSV
  - DrGinaSchoemanFacebookPage.CSV
source_documents:
  - Schoeman_Clinic_Doctor_Biographies_11.docx
  - Schoeman_Clinic_Doctor_Biographies.docx
  - "Google Drive 'Knowledge base' folder (id 1Zdq-ax7hkcX9zFV37kYcdpTAeeZ95XYt)"
  - Schoeman-Clinic-Consent-DataProtection-Pack.{docx,pdf,html}
  - proposal-v3.txt
  - telegram-thread-log.md
skills_built: [marketing-comms-counsel, ghl-inbox-health-check, social-growth-strategist, social-platform-playbook, content-studio]
skills_proposed: [faculty-account-architect, content-performance-analyst, social-content-engine]
agents: none
workflows_built: none_for_social
integrations:
  crm: GoHighLevel (HIPAA tier) [current]
  ehr: Semble [current]
  whatsapp: Coexistence, +44 7426 494321 [current]
  email: MailChimp -> GoHighLevel [in transition]
strategies:
  - "Reach+funnel over followers (proposed, not approved)"
  - "Faculty-as-content-engine (proposed)"
  - "Lead-magnet quiz -> list -> nurture (proposed)"
experiments:
  - "June boost -> spike then ~99% reach collapse (observed)"
major_findings:
  - "[DERIVED] IG reach collapsed ~99% from June peak; followers flatlined"
  - "[PRIMARY] June spike driven by a standard Boost Post"
  - "[PRIMARY] No lead magnet / funnel exists"
  - "[PRIMARY] A faculty of highly credentialled, media-worthy doctors now exists"
major_hypotheses:
  - "[LOW CONFIDENCE] Boosting caused organic-reach throttling (unproven; no engagement/per-post data)"
major_decisions:
  - "Target=Schoeman Clinic; scope=social growth first; audit architecture before building; migrate to schoeman-growth-os"
critical_missing_sources:
  - IHF marketing data
  - Symptoms Evaluation survey (structure + results)
  - Per-post/engagement social analytics
  - Boost campaign details
  - Website analytics (GA4/Search Console)
open_causal_flags:
  - "Do NOT assert boost->throttle causation as fact"
  - "Do NOT equate IHF audience with Schoeman audience"
```

---

*End of migration pack `schoeman-claude-history-01.md`. No implementation was performed after this document. Next step is for the new `schoeman-growth-os` Claude Code project to independently audit this material.*
