# Plan: Monkey Joe's Legal Compliance — Marketing, SMS, Email, Waivers & Privacy

**Created:** 2026-03-23
**Status:** Draft
**Request:** Detail all legal requirements to run the MJ marketing strategy compliantly in Florida/Orlando, including whether waiver signatories can be SMS'd, what consent language is needed, what every email must include, what the waiver must say, and what to fix in GHL before launch.

---

## Overview

### What This Plan Accomplishes

This plan produces a complete legal compliance document for the Monkey Joe's marketing strategy — covering every touchpoint where data is collected, used, or communicated. It answers the key question (can you SMS people who signed the waiver?), provides exact copy-paste consent language, specifies every required email element, outlines the required waiver structure, and gives William and Michael a clear pre-launch checklist.

### Why This Matters

The MJ strategy involves SMS sequences, email automations, digital waivers, BOGO/discount offers, children's data, and Facebook/Google advertising — each carrying distinct legal risk in Florida. Running one SMS campaign without documented consent can cost $500–$1,500 per text under TCPA. Sending email to people who didn't opt in is a CAN-SPAM violation at $51,744 per email. Getting this right before launch protects Michael, protects William (as the implementing party), and protects the franchise scalability story for Big Game Brands.

---

## Current State

### Relevant Existing Structure

```
outputs/monkey-joes/
├── MASTER-STRATEGY.md          — North Star strategy doc
├── EMAIL-SEQUENCES.md          — 22 emails + 1 SMS, 7 sequences
├── WEEKLY-CAMPAIGN-TEMPLATES.md — 2 weekly send templates
├── GHL-LANDING-PAGE-BRIEF.md   — Build spec for William
├── KEYWORD-RESEARCH.md         — Google Ads keyword map
├── MJ-COMPLETE-PLAYBOOK.md     — Full combined presentation doc
.claude/skills/florida-legal-advisor/
├── SKILL.md                    — Legal advisor skill
├── references/florida-marketing-law.md
├── references/florida-waivers-privacy.md
```

### Gaps or Problems Being Addressed

1. **No consent language exists anywhere** — GHL forms, landing pages, and the Aluvii waiver form all currently lack legally compliant opt-in checkboxes for email AND SMS
2. **SMS sequences exist without a legal basis** — 10 SMS sequences are planned but there is currently no documented TCPA consent mechanism
3. **The waiver signing does NOT equal SMS consent** — this is the most common misunderstanding; must be clarified and a separate consent pathway created
4. **No privacy policy exists** for the landing pages or MJ website
5. **Email sequences have no physical address footer** — required by CAN-SPAM
6. **Birthday data collection** — current plan collects birthday info without clarifying COPPA limits
7. **"Florida residents only" restriction** is not clearly disclosed pre-checkout in the landing page spec
8. **No data processing agreement** documented for GHL or Aluvii

---

## The Key Question: Can You SMS People Who Signed the Waiver?

### Short answer: NO — not without a separate, explicit SMS opt-in.

Here is exactly why:

Signing a liability waiver is a **safety and legal document**. It is not a marketing consent form. The phone number (if collected) is collected for the purpose of operating the venue (emergency contact, booking confirmation). Under the **TCPA (47 U.S.C. § 227)**, sending a marketing text message requires **prior express written consent** — meaning the person must have been explicitly told they are consenting to receive marketing texts, and they must have agreed to that specifically.

The waiver says nothing about marketing. Therefore, using a waiver-collected phone number for marketing SMS is a TCPA violation. Each text = $500–$1,500 in statutory damages. Class actions are common.

### What about email from the waiver?

**Email is slightly different but still risky.** Under CAN-SPAM, the rule is more permissive — you CAN send one email if there is an existing business relationship (which signing a waiver establishes). However:
- It must be clearly identified as a commercial message
- It must have an unsubscribe link
- It must have a physical address
- The FTC has increasingly interpreted "existing business relationship" narrowly
- Best practice (and what avoids any dispute) is explicit email opt-in

### The safe and compliant approach:

Add TWO separate opt-in checkboxes to the waiver form (and all GHL landing page forms), **unchecked by default**:

```
[ ] Yes, I'd like to receive news, offers and updates from Monkey Joe's by email.

[ ] Yes, I'd like to receive text message promotions from Monkey Joe's.
    Monkey Joe's, 9101 International Dr, Orlando FL 32819.
    Message & data rates may apply. Up to [X] msgs/month. Reply STOP to opt out,
    HELP for help. Consent is not a condition of purchase.
```

Anyone who checks the SMS box = you can SMS them.
Anyone who ONLY checks the email box = email only.
Anyone who checks neither = no marketing contact (waiver is still valid; this is a separate field).

---

## Proposed Changes

### Summary of Changes

- Create `outputs/monkey-joes/LEGAL-COMPLIANCE-GUIDE.md` — the master compliance document for Michael and William
- Create `outputs/monkey-joes/CONSENT-LANGUAGE-TEMPLATES.md` — copy-paste ready consent text for every form touchpoint
- Create `outputs/monkey-joes/PRIVACY-POLICY-TEMPLATE.md` — ready-to-use privacy policy for landing pages
- Create `outputs/monkey-joes/WAIVER-TEMPLATE.md` — complete liability waiver template meeting Florida standards
- Update `outputs/monkey-joes/GHL-LANDING-PAGE-BRIEF.md` — add consent checkboxes and CAN-SPAM requirements to every form spec
- Update `outputs/monkey-joes/EMAIL-SEQUENCES.md` — add physical address footer and unsubscribe note to all sequences
- Update `outputs/monkey-joes/MJ-COMPLETE-PLAYBOOK.md` — add Legal Compliance section

### New Files to Create

| File Path | Purpose |
|---|---|
| `outputs/monkey-joes/LEGAL-COMPLIANCE-GUIDE.md` | Master compliance doc — answers every legal question, risk-rated, with action items for Michael and William |
| `outputs/monkey-joes/CONSENT-LANGUAGE-TEMPLATES.md` | Copy-paste consent text for Aluvii waiver form, GHL landing page forms, GHL SMS opt-in, birthday form |
| `outputs/monkey-joes/PRIVACY-POLICY-TEMPLATE.md` | Full privacy policy ready to drop onto landing pages and MJ website |
| `outputs/monkey-joes/WAIVER-TEMPLATE.md` | Complete Florida-compliant liability waiver with embedded marketing consent section |

### Files to Modify

| File Path | Changes |
|---|---|
| `outputs/monkey-joes/GHL-LANDING-PAGE-BRIEF.md` | Add consent checkbox section to every form; add CAN-SPAM footer spec; add "Florida residents only" disclosure placement |
| `outputs/monkey-joes/EMAIL-SEQUENCES.md` | Add physical address and unsubscribe reminder note to all 22 email templates |

---

## Design Decisions

### Key Decisions Made

1. **Waiver ≠ SMS consent — always explicit opt-in:** This is non-negotiable under TCPA. The plan makes this crystal clear and provides the exact consent language rather than leaving interpretation to William or Michael.

2. **Email opt-in recommended even though CAN-SPAM technically allows existing business relationship:** The difference between "allowed" and "best practice" is class action risk. At franchise scale (56 locations), even a small percentage of complaints becomes a major exposure. We recommend explicit opt-in for email too.

3. **Four separate documents, not one big one:** Compliance guide, consent templates, privacy policy, and waiver are each a different deliverable used by a different person in a different context. Michael needs the waiver. William needs the consent templates for GHL. The privacy policy goes on the website. The compliance guide is the overview.

4. **Produce working copy-paste text, not legal theory:** The goal is for William to be able to build the forms correctly without needing a law degree. Every document produces exact text to use.

5. **Birthday data — collect month/year only, never child's name + DOB together:** This keeps MJ out of COPPA grey zone. "What month is your child's birthday?" is safe. "Child's full name and date of birth" used for targeted marketing crosses into collecting children's personal information.

### Open Questions (Needs Input from Michael Before Implementation)

1. **Does Monkey Joe's currently have a liability waiver system in Aluvii?** The waiver template assumes digital delivery via Aluvii. Need to confirm: (a) is Aluvii collecting waivers today, and (b) can Michael's team modify the Aluvii waiver form to add the opt-in checkboxes?

2. **What phone number will MJ SMS from?** TCPA requires identifying the sender in every message. Need the GHL phone number or Twilio number that will be used.

3. **Does Big Game Brands corporate have existing legal documents** (waiver, privacy policy) that must be used instead of new ones? If so, those docs need review against this plan rather than replacement.

4. **Is MJ currently sending any email marketing?** If they have an existing list, we need to understand how those contacts were collected before importing them to GHL.

---

## Step-by-Step Tasks

### Step 1: Create the Master Legal Compliance Guide

Create `outputs/monkey-joes/LEGAL-COMPLIANCE-GUIDE.md` — a plain-English document structured for Michael and William. Covers all 7 compliance areas with risk ratings and action items.

**Structure:**
- Executive Summary: The 5 things that must be done before launch
- Section 1: The Waiver Question (can you SMS waiver signatories?) — with definitive answer
- Section 2: Email Compliance (CAN-SPAM requirements)
- Section 3: SMS Compliance (TCPA requirements — marked HIGH RISK throughout)
- Section 4: COPPA — children's data rules
- Section 5: Promotional offer compliance (BOGO, 50% off, "Florida residents only")
- Section 6: Ad platform rules (Facebook/Google age-targeting restrictions)
- Section 7: Privacy & data security (FIPA, GHL/Aluvii vendor agreements)
- Pre-Launch Checklist — every item that must be ticked before going live
- Legal disclaimer

**Actions:**
- Write the full document with specific, actionable items at each section
- Include exact statutory references (TCPA, CAN-SPAM, FDUTPA, COPPA, FIPA)
- Use a risk matrix table: Area | Risk Level | What Could Go Wrong | What To Do

**Files affected:**
- `outputs/monkey-joes/LEGAL-COMPLIANCE-GUIDE.md` (create)

---

### Step 2: Create the Consent Language Templates

Create `outputs/monkey-joes/CONSENT-LANGUAGE-TEMPLATES.md` — copy-paste ready text for every form in the MJ tech stack.

**Templates to include:**

**A. Aluvii Waiver / Intake Form — Email + SMS consent checkboxes**
```
[ ] Yes, I'd like to receive special offers, news and promotions from Monkey Joe's by email.

[ ] Yes, I'd like to receive text message promotions from Monkey Joe's.
    Monkey Joe's | [Location Address]. Message & data rates may apply.
    Up to 4 msgs/month. Reply STOP to opt out, HELP for help.
    Consent is not a condition of purchase or service.
```

**B. GHL Landing Page Form (BOGO / 50% Off)**
```
By entering your email, you agree to receive marketing emails from Monkey Joe's.
You can unsubscribe at any time.

[ ] I also consent to receive text message promotions from Monkey Joe's at the number
    provided above. Message & data rates may apply. Up to 4 msgs/month.
    Reply STOP to unsubscribe. Consent is not required to receive the offer.
```

**C. Birthday Party Enquiry Form**
```
By submitting this form, you agree to receive follow-up communications about your
birthday party enquiry by email and phone. We will not share your information with
third parties.

[ ] I also consent to receive SMS updates about my enquiry and future promotions
    from Monkey Joe's. Reply STOP at any time to opt out.
```

**D. GHL Pop-Up / Exit Intent Form**
```
[ ] Yes, send me the offer plus future deals by email. I can unsubscribe anytime.
```

**E. First SMS message in every sequence — mandatory opener**
```
Monkey Joe's: [Message content]. Reply STOP to unsubscribe, HELP for help.
Msg & data rates may apply.
```

**F. Email footer — required in every GHL email**
```
Monkey Joe's | [Location: Pointe Orlando / Winter Park]
9101 International Drive, Orlando FL 32819 (and/or Winter Park address)

You're receiving this because you subscribed at [monkeyjoes.com / landing page].
[Unsubscribe] | [Privacy Policy]
```

**Actions:**
- Write every template with exact placeholder markers in [brackets]
- Note which template applies to which touchpoint
- Include a "do not do" section — things that look compliant but aren't (e.g., pre-checked boxes)

**Files affected:**
- `outputs/monkey-joes/CONSENT-LANGUAGE-TEMPLATES.md` (create)

---

### Step 3: Create the Privacy Policy Template

Create `outputs/monkey-joes/PRIVACY-POLICY-TEMPLATE.md` — a working privacy policy for MJ landing pages and website.

**Required sections (based on COPPA + FIPA + FTC requirements):**

1. **Who We Are** — Monkey Joe's, operator, contact info
2. **What Information We Collect**
   - Name, email address, phone number (from opt-in forms)
   - Birthday month (for birthday promotion — NOT child's DOB)
   - Technical data (IP address, browser, cookies — standard)
   - Payment info (processed by Aluvii — not stored by us)
3. **How We Use Your Information**
   - To send marketing emails you subscribed to
   - To send SMS promotions you explicitly opted into
   - To process birthday party inquiries
   - To improve our services
4. **Who We Share It With**
   - GoHighLevel (email/SMS platform — acts as data processor)
   - Aluvii (booking/POS system)
   - Google/Meta (anonymized/aggregated ad targeting only)
   - No sale of personal data
5. **Children Under 13**
   - "This website is directed to adults (parents and guardians). We do not knowingly collect personal information from children under 13. If you believe a child has submitted information to us, contact us at [email] and we will delete it."
6. **Your Rights**
   - Unsubscribe from emails at any time (link in every email)
   - Opt out of SMS by replying STOP
   - Request deletion of your data: [contact email]
7. **Data Security** — FIPA-compliant statement
8. **Contact Information**
9. **Last Updated date**

**Actions:**
- Write the full policy using plain English (not legal jargon)
- Insert [PLACEHOLDER] markers where MJ-specific info is needed (address, contact email, etc.)
- Note that this template should be reviewed by a licensed Florida attorney before publishing

**Files affected:**
- `outputs/monkey-joes/PRIVACY-POLICY-TEMPLATE.md` (create)

---

### Step 4: Create the Waiver Template

Create `outputs/monkey-joes/WAIVER-TEMPLATE.md` — a Florida-compliant liability waiver with embedded marketing consent, ready for Aluvii digital delivery.

**Required waiver elements (Florida law — *Global Travel Marketing v. Shea*):**

```
MONKEY JOE'S — LIABILITY RELEASE, WAIVER AND INDEMNIFICATION AGREEMENT

PLEASE READ THIS ENTIRE AGREEMENT CAREFULLY BEFORE SIGNING.

1. PARTIES
   This Agreement is between [Parent/Guardian Name] ("Participant" or "I/We") and
   [MJ Entity Name], operating as Monkey Joe's at [Location Address] ("Monkey Joe's").

2. ACTIVITY DESCRIPTION
   I am signing this Agreement in connection with my child's/children's participation
   in inflatable play activities, arcade games, and related recreational activities at
   Monkey Joe's ("Activities").

3. ACKNOWLEDGMENT OF RISKS
   I understand and acknowledge that the Activities involve physical activity and
   inherent risks, including but not limited to: falls, collisions with other
   participants or equipment, physical exertion, and minor injuries. I voluntarily
   accept these risks on behalf of myself and my minor child(ren).

4. RELEASE OF LIABILITY
   In consideration of being permitted to participate in the Activities, I, on behalf
   of myself, my minor child(ren), my heirs, executors, administrators, and assigns,
   hereby RELEASE, WAIVE, DISCHARGE AND COVENANT NOT TO SUE Monkey Joe's, its parent
   company, affiliates, subsidiaries, officers, directors, employees, agents,
   volunteers, and successors (collectively "Released Parties") from any and all
   liability, claims, demands, actions and causes of action whatsoever arising out of
   or relating to any loss, damage, or injury (including death) that may be sustained
   while participating in the Activities, WHETHER OR NOT CAUSED BY THE NEGLIGENCE OF
   THE RELEASED PARTIES, to the fullest extent permitted by Florida law.

   This release does not apply to gross negligence or intentional misconduct.

5. INDEMNIFICATION
   I agree to indemnify and hold harmless the Released Parties from any loss,
   liability, damage, or cost (including attorney's fees) they may incur arising out of
   my or my child's participation in the Activities.

6. GOVERNING LAW
   This Agreement shall be governed by the laws of the State of Florida.
   Any dispute arising hereunder shall be resolved in Orange County, Florida.

7. ACKNOWLEDGMENT
   I am 18 years of age or older. I am the parent or legal guardian of the minor
   child(ren) listed below. I have read this Agreement carefully and understand its
   contents. I am signing this Agreement freely and voluntarily.

CHILD(REN) INFORMATION:
Child's Name: ____________________   Date of Birth: ____________________
Child's Name: ____________________   Date of Birth: ____________________
(Add more as needed)

Parent/Guardian Signature: ____________________   Date: ________________
Parent/Guardian Printed Name: ____________________

---

OPTIONAL — MARKETING COMMUNICATIONS
(Separate from the waiver above — your signature above is valid regardless of
whether you check the boxes below)

[ ] Yes, I'd like to receive special offers, news and promotions from Monkey Joe's
    by email.

[ ] Yes, I'd like to receive text message promotions from Monkey Joe's at the mobile
    number I provide. Monkey Joe's | [Address]. Message and data rates may apply.
    Up to 4 messages/month. Reply STOP at any time to opt out. Reply HELP for help.
    Consent is not a condition of purchase.

Email address: ____________________
Mobile phone: ____________________   (required only if SMS box checked)
```

**Key design principles reflected:**
- Marketing consent is PHYSICALLY SEPARATED from the waiver with a clear visual break and explicit "Separate from the waiver above" label
- Both marketing checkboxes are unchecked by default
- The "Consent is not a condition of purchase" language is required by FTC guidance
- Child DOB is in the waiver only (for age verification) — NOT in the marketing section
- The waiver covers both locations — include addresses for both or use a location selector

**Actions:**
- Write the full waiver template in `WAIVER-TEMPLATE.md`
- Include a "Notes for Aluvii implementation" section explaining how William should configure the digital version
- Mark sections that MJ's attorney should review before live use

**Files affected:**
- `outputs/monkey-joes/WAIVER-TEMPLATE.md` (create)

---

### Step 5: Update GHL Landing Page Brief

Update `outputs/monkey-joes/GHL-LANDING-PAGE-BRIEF.md` to add legal compliance requirements to every form specification.

**Changes to make:**

1. **Add a "Legal Requirements" section** near the top of the brief, before the page specs, covering:
   - Every form must have the email consent checkbox (unchecked by default)
   - Every form with a phone field must have the SMS consent checkbox (unchecked by default)
   - Every landing page must link to the privacy policy
   - "Florida residents only" disclosure must appear above the CTA button, not only in fine print
   - No countdown timers that reset on expiry (FTC deceptive practice)

2. **Update the form field spec** in each landing page section to include:
   - Email opt-in checkbox with exact consent text
   - SMS opt-in checkbox with exact TCPA disclosure text
   - Privacy policy link

3. **Update the Tracking section** — add a note that GHL must be configured to tag contacts by consent type (email-only vs. SMS-consented) so sequences fire correctly

**Files affected:**
- `outputs/monkey-joes/GHL-LANDING-PAGE-BRIEF.md` (modify)

---

### Step 6: Update Email Sequences with CAN-SPAM Footer Note

Update `outputs/monkey-joes/EMAIL-SEQUENCES.md` — add a universal footer note and CAN-SPAM compliance reminder.

**Add at the top of the file (after the overview):**

```
## LEGAL REQUIREMENTS — APPLY TO ALL 22 EMAILS

Every email sent via GHL must include the following in the footer.
William to configure this as the default GHL email footer template.

--- REQUIRED FOOTER ---
Monkey Joe's
Pointe Orlando: 9101 International Drive, Orlando FL 32819
Winter Park: [Address — confirm with Michael]

You're receiving this email because you subscribed at [source].
[Unsubscribe from all emails]  |  [Privacy Policy]

This message was sent by Monkey Joe's. To stop receiving emails, click Unsubscribe.
--- END FOOTER ---

SUBJECT LINE RULE: Every subject line must accurately reflect the email content.
"Free admission" subject for a BOGO email = compliant.
"You've been selected" subject for a promotional email = not compliant (deceptive).

SEND TO CONFIRMED OPT-INS ONLY. Never import a purchased list or any list where
explicit email consent was not captured.
```

**Files affected:**
- `outputs/monkey-joes/EMAIL-SEQUENCES.md` (modify — add section at top)

---

### Step 7: Pre-Launch Legal Checklist

This is embedded in the LEGAL-COMPLIANCE-GUIDE.md created in Step 1, but also summarised here as a standalone quick-reference.

**Must be completed before any paid ads or email/SMS sequences go live:**

**Waiver & Consent (Michael + William):**
- [ ] Aluvii waiver form updated with separate email + SMS opt-in checkboxes (unchecked by default)
- [ ] Aluvii configured to tag contacts by consent type (email, SMS, or neither)
- [ ] New waiver reviewed by a licensed Florida attorney before going live
- [ ] Existing Aluvii contact list audited — identify which contacts have documented marketing consent

**GHL / Landing Pages (William):**
- [ ] Every GHL form has email consent checkbox (unchecked by default)
- [ ] Every GHL form with phone field has SMS consent checkbox with full TCPA disclosure
- [ ] Privacy policy page created and linked from every landing page footer
- [ ] "Florida residents only" disclosure on Pointe Orlando offer appears above the CTA button
- [ ] No countdown timers that reset on expiry
- [ ] GHL unsubscribe is enabled on all email sends
- [ ] GHL email footer template includes physical address for both locations
- [ ] GHL contact tags set up: `email-consent`, `sms-consent`, `no-marketing-consent`
- [ ] SMS sequences only fire to contacts tagged `sms-consent`

**Ad Platforms (Jess/William):**
- [ ] Facebook/Meta: Age targeting set to 18+ on all campaigns (parents, not children)
- [ ] Google Ads: No ad copy directed at children; all keywords target parents
- [ ] No ad claims that cannot be substantiated (e.g., no "lowest price" without evidence)
- [ ] "21 years of Wacky Wednesdays" verified as factually accurate with Michael

**Pricing & Offers:**
- [ ] Confirm that BOGO paying admission = regular price (not inflated to fund the free)
- [ ] Confirm that 50% off is calculated from the genuine regular price
- [ ] "Florida residents only" restriction live and clearly disclosed pre-checkout for Pointe Orlando

**Data Security:**
- [ ] GHL data processing agreement (DPA) reviewed — GHL provides this in their terms; confirm with William
- [ ] Aluvii data processing agreement confirmed
- [ ] No customer data exported to unencrypted spreadsheets or shared via email

---

## Connections & Dependencies

### Files That Reference This Area

- `outputs/monkey-joes/MASTER-STRATEGY.md` — strategy doc; will reference the compliance guide
- `outputs/monkey-joes/GHL-LANDING-PAGE-BRIEF.md` — being updated in Step 5
- `outputs/monkey-joes/EMAIL-SEQUENCES.md` — being updated in Step 6
- `outputs/monkey-joes/MJ-COMPLETE-PLAYBOOK.md` — the presentation doc for Michael/William; will benefit from a brief compliance summary section

### Impact on Existing Workflows

- **Email sequences:** All 22 emails need the CAN-SPAM footer. William configures this once as a GHL template footer.
- **SMS sequences:** Cannot fire without documented TCPA consent. GHL workflow must check for `sms-consent` tag before sending any SMS.
- **Landing page forms:** Every form gains 1–2 new fields (consent checkboxes). William to implement in GHL form builder.
- **Aluvii intake:** The waiver form gains a marketing consent section. Michael to coordinate with Aluvii support or configure in the admin panel.

---

## Validation Checklist

- [ ] `LEGAL-COMPLIANCE-GUIDE.md` created with all 7 compliance areas, risk ratings, and pre-launch checklist
- [ ] `CONSENT-LANGUAGE-TEMPLATES.md` created with copy-paste text for all 5 form touchpoints
- [ ] `PRIVACY-POLICY-TEMPLATE.md` created with all required COPPA + FIPA + FTC sections
- [ ] `WAIVER-TEMPLATE.md` created with Florida-compliant structure and separated marketing consent section
- [ ] `GHL-LANDING-PAGE-BRIEF.md` updated with legal requirements section and updated form specs
- [ ] `EMAIL-SEQUENCES.md` updated with CAN-SPAM footer template at the top
- [ ] All new files are cross-referenced correctly
- [ ] The key question (waiver = SMS consent?) answered definitively in the compliance guide

---

## Success Criteria

The implementation is complete when:

1. Michael and William can read `LEGAL-COMPLIANCE-GUIDE.md` and know exactly what they need to do before launch, without needing to ask further questions
2. William can copy-paste directly from `CONSENT-LANGUAGE-TEMPLATES.md` into GHL forms without writing any consent language himself
3. The waiver template in `WAIVER-TEMPLATE.md` is ready to send to a Florida attorney for final review — not a starting-from-scratch exercise
4. Every email in `EMAIL-SEQUENCES.md` has a CAN-SPAM-compliant footer note
5. GHL landing page brief is updated so the build spec produces legally compliant forms

---

## Notes

**On the SMS question specifically:** Many businesses make the mistake of assuming that "they gave us their phone number" = "we can text them." This is the most litigated area of marketing law in the US right now. TCPA class actions are common, and the plaintiffs' bar actively targets small-to-medium businesses. The $500–$1,500 per text statutory damages means a 500-person SMS list sent without documented consent = up to $750,000 in exposure. This is not a theoretical risk. Fix it first.

**On the waiver and attorney review:** The waiver template produced here is based on Florida case law and standard industry practice. However, the *Global Travel Marketing v. Shea* ruling specifically noted that enforceability depends on how well the waiver is drafted. Before going live with this waiver, Michael should have a Florida-licensed attorney review it. Cost: typically $300–$600 for a waiver review. Worth every dollar.

**On franchise scale:** Every decision made here for 2 locations should be made with 56 locations in mind. The consent infrastructure, the waiver design, the GHL template footer — if it's correct here, it scales to the whole franchise without rework.

**Legal disclaimer:** All content in this plan and its output documents is for informational purposes only and does not constitute legal advice. Monkey Joe's and Big Game Brands should consult a licensed Florida attorney before relying on any of this content for legal compliance purposes.
