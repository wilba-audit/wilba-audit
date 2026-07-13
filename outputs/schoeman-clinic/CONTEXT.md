# The Schoeman Clinic — Client Context

**Last updated:** 2026-07-13 · Built from Proposal v3, 6 meeting transcripts (Jun–Jul 2026, incl. the 13 Jul team training), the knowledge-base pack, and the WhatsApp thread with Griffin/Mati.

---

## ⭐ Tonight's team training — outcome (13 Jul 2026)

**Attended:** Zoey van Huyssteen, Isabell Drake, Lisa (joined under Zoom name "Megan Fensom-Turner"). Went well — team engaged and keen. Ran on Google Meet.

**Covered:** connected each PA's calendar + set their working hours; toured the Conversations tab (reply, mark read, assign, tasks, notes); confirmed WhatsApp messages flow in; appointments/payments stay in Semble for now.

**Staff questions raised (need Mati/Gina):**
- **⭐ Semble notes / double-entry (biggest one):** team currently copy important WhatsApp/email into the patient's Semble notes so Gina sees them. They asked if that stops now or continues. **Correct interim answer: KEEP copying to Semble** — WhatsApp→Semble sync is Phase 2 and the daily brief isn't live, so dropping it would leave Gina blind. ⚠️ *On the call Jess said they'd "move away from Semble entirely for notes" — needs gently resetting in the team follow-up.*
- Email sender identity — replies default to **info@**, with option to switch to personal (answered).
- "Do we book appointments in GHL now?" — **No, Semble** for now (answered, repeatedly).
- "From today do we use GHL not WhatsApp?" — get comfortable with the GHL inbox from today (answered).

**Action items (WILBA side):**
- **Dr Gina's calendar shows empty/unconnected** in GHL — Jess to fix.
- **Calendar display glitch** Lisa sees (text rendering vertically) — investigate.
- **Email list import + phone↔email matching** — in progress.
- **Holiday date-range blocking** — GHL changed the UI (one date at a time); Jess to set **Isabell's 4-week leave (from Mon 20 Jul → back 16 Aug)** on the backend; Isabell's workdays change on return (Mon–Fri → Tue–Fri, covering Lisa first week).
- Send team follow-up summary + set up WhatsApp group.

**Deliverables in this folder:** `mati-update-post-training.md` (message to Mati), `Schoeman-Clinic-Team-FollowUp.docx` (team hand-out), `team-guide.html` / `.docx` (fuller reference), `training-agenda.html` / `Schoeman-Clinic-GHL-Team-Training-Agenda.docx` (presenter run sheet), `Schoeman-Clinic-GoLive-Payment-Milestones.docx` (Mati payment note).

---

## 1. Who's who

| Person | Role |
|--------|------|
| **Dr Gina Schoeman** | The client. Premium hormone / longevity / functional-medicine doctor. Non-technical, very busy, camera-shy, gets "frantic/scattered," burnt by contractors before → needs trust and simplicity. |
| **Mati Simarro** (RobinHoodSolutions AI) | The intermediary who owns the Gina relationship. WILBA's proposal is *prepared for Mati*. He runs the **knowledge base, patient-journey copy, Semble, compliance/consent, and client comms**. Based in Spain. |
| **Jess (WILBA)** | Owns the **GoHighLevel + WhatsApp workstream and team training**. Strategy/face. In Bali (WITA, UTC+8). |
| **Griffin Guarino** | Jess's developer/partner (US). Builds the GHL/WhatsApp/automation side. |
| **The PA team** (remote, Mon–Fri 9–5 GMT, ~£20/hr) | **Lisa Roberts** — Lead Admin/Patient Liaison (30+ yrs, women's health; but Gina finds her replies blunt + spelling errors). **Zoey Van Huyssteen** — full-time. **Isabell Drake** — ~2 days/wk, temp-ish. **+ a 4th admin** started Mon 13 Jul. |
| **Marianne / Shelly / Samir** | Gina's *separate* social-media/marketing people. Not WILBA. (Jess is skeptical of this arrangement — parked until Gina can scale.) |

> **The clinic is growing fast:** new doctor starting this month, another in Sept, a health coach Aug/Sept, more doctors in the pipeline. This is *why* the automation matters — admin is overwhelmed and ~385 patients are behind on follow-up.

---

## 2. The deal (Proposal v3, 25 Apr 2026)

- **One-time build:** $10,000 USD — 50% on kickoff, 50% on go-live. Full refund promise if Gina isn't satisfied.
- **Retainer:** $1,000 USD/month — **minimum first 3 months** (Mati convinced her; needed to iterate the knowledge base from real conversations). After 3 months → reassess retainer vs hourly. Griffin nearly declined the job without a feedback/iteration retainer.
- **Note:** Gina must run **GHL on the HIPAA tier ($297/mo)**, not the $97 starter — this is a pass-through cost she pays, on top of the retainer.
- Total build = **103 hours across 9 stages** (Discovery → Foundation → WhatsApp Inbox → Recall/Nurture → Voice Agent → Inquiry Funnel → Daily Brief → Compliance Pack → Training/Handover → Hypercare).

## 3. Architecture — the one rule

**Clinical records STAY in Semble (their EHR).** GoHighLevel is operational only. The two talk via webhook. GHL is a marketing CRM with a HIPAA add-on — using it as a clinical record system would breach CQC Reg 17. Semble keeps notes, prescriptions, pathology, and the Heidi AI scribe.

**Stack:** GoHighLevel (HIPAA tier — inbox/CRM/workflows/forms/newsletter/payments/WhatsApp routing) · Meta WhatsApp Cloud API (storage region GB) · Twilio UK (voice number) · VAPI (voice orchestration) · ElevenLabs EU (voice) · AWS Bedrock Claude eu-west-2 (LLM) · Stripe (payments) · Semble (EHR).

---

## 4. Phase 1 scope (6 features)

1. **Unified WhatsApp shared inbox** — 3+ PAs work one inbox in GHL Conversations; assign, internal notes, hand off across days. Replaces "screenshot-and-forward" chaos. **← this is the piece going live first.**
2. **Recall / nurture / newsletter automation** — clear the ~55 (now ~385) overdue-follow-up backlog; 3- & 6-month recall; pre-appt reminders; payment + blood-test chasing; newsletter compose view; onboarding flow.
3. **After-hours voice agent** — Twilio UK number, operational queries only, hard escalation for anything medical ("if urgent hang up and call 999" / callback). Replaces after-hours Moneypenny (~£190/mo).
4. **Strategic patient-journey redesign** — paid-first funnel: short 6-field inquiry page → lead in GHL → long intake → blood-test order/pay → consult booking (£500) → post-consult summary → recall. Fixes the 20-field-form dropout problem.
5. **Dr Gina's daily-brief agent** — 7am UK WhatsApp brief: today's appts, new enquiries, overdue items, HITL queue, revenue. (Bonus, moved into Phase 1.)
6. **Replicable doctor-onboarding stack** — every workflow templated so each new doctor plugs in at ~zero build cost.

**Phase 2 (later, not priced):** Semble bidirectional integration, AI booking, lead-gen/landing pages, more doctors, Wilba Social, webinars, patient portal.

---

## 5. Where the build is AT (as of 13 Jul 2026)

**✅ Live / done**
- GHL account connected; everyone is admin.
- **WhatsApp connected to GHL** — messages flowing into the **Conversations** tab.
- **Shared inbox ready** — this is *tonight's* go-live for the PAs.
- Newsletter/email templates updated by Griffin. (Jess built one in HTML; wants the *visual* builder for Gina.)
- Inquiry-form fields agreed (6 fields: name, email, phone, sex-at-birth, reason [dropdown], referral source).

**🔧 In progress**
- **Knowledge base** — the big painstaking piece, feeds *both* WhatsApp AI and the voice agent. Mati is drafting Q&A with Claude (see `source-notes/knowledge-base-filled.md`); needs more live sessions with Gina to close open items. **AI runs in "suggestive mode" — a PA approves every draft before it sends.**
- **Post-consultation letter generation** — Mati implementing (~early Jul).
- **Patient portal** — Mati's roadmap, after the letter generation. Would let AI check a patient's file (e.g. "how much prescription is left", last consult date before allowing repeat scripts).
- **Marketing/GDPR consent wording** — WhatsApp needs *explicit* GDPR consent (email is near-free; WhatsApp ~£20/mo + consent required). Jess owns the *marketing-consent* copy; the *patient-level legal* sits with Gina's data person (Jess explicitly won't be the UK-legal author).

**⏸️ Not started / deferred / blocked**
- **AI suggested-reply mode + knowledge-base connection in the inbox** — NOT part of tonight. Comes when Jess + Mati are ready.
- **Voice agent + Twilio calling number** — pending Gina **topping up GHL**; involves spending money → left to Jess's side. Not urgent.
- **Meta Business Verification / WABA migration** — critical path, Meta-controlled.
- **Discovery-call calendar** in GHL — Jess's team to set up; loom for PAs on setting their hours.

**✅ Resolved dependencies**
- **Semble admin access — Griffin HAS it** (confirmed by Jess, 13 Jul). No longer a blocker; Griffin is pulling the patient list for the email/phone contact matching. *(Note: the go-live/milestone doc still lists this as a blocker — correct it before sending.)*

---

## 6. Key rules the AI (and PAs) must follow

- **Operational only. Never clinical.** No medical advice, no interpreting symptoms/results, no dosing. Anything clinical → escalate to a human.
- **Blood results go to Dr Gina, never straight to the patient.** Standard line: results discussed at an appointment.
- **Escalation path (current, manual):** PA copies the WhatsApp into an email to Gina *and* pastes it onto the patient's Semble file. Goal is to automate this. Escalations land in the **PA WhatsApp queue**; Gina still makes every clinical call.
- **Email rule:** patients get **2 short emails**; a page-long / complex query = a paid consultation (15 min £125 / 30 min £250).
- **Consent:** never add anyone to marketing or send WhatsApp without explicit per-channel consent. Identity must be human-verified before any patient-specific info.

## 7. Open items / watch-outs

- **☎️ WhatsApp number — CONFIRMED +44 7426 494321.** Griffin confirmed this is the correct inbox number ("Yes that is the correct number. No idea where u or Jess saw the other one"). ⚠️ The **website FAQ + footer still show +44 7426 292 321** — the *site* needs correcting so patients aren't sent to the wrong number. Not a training blocker.
- Semble limits: 3-day calendar view, weak consent fields, no native WhatsApp consent flag.
- Gina is trust-sensitive → **prove it works first, keep it simple, no tech overwhelm.** Marketing/social is parked until she can scale delivery.
- Time zones: Jess (Bali +8), Gina/PAs (UK +1), Mati (Spain), Griffin (US) → expect ~1-day round-trips.

## 8. Source docs

Distilled from files Jess uploaded 13 Jul 2026 (originals live outside the repo and won't persist):
- `source-notes/proposal-v3.txt` — full proposal
- `source-notes/knowledge-base-filled.md` — the 16-section KB questionnaire (blue = answered, italics = open)
- Transcripts referenced: *Wilba Catch Up – Dr Schoeman* (3 Jun), *Patient portal catch up* (5 Jun), *Catch up (Jess+Mati)* (16 Jun), *Knowledge base* (3 Jul), *Knowledge base 2* (4 Jul), plus the Griffin/Mati WhatsApp thread.
