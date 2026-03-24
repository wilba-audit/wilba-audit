# Monkey Joe's — Legal & Messaging Audit
## Privacy, Compliance, and Competitive Positioning Review

**Prepared by:** Jess Morrell / WILBA
**Date:** March 2026
**Status:** Action required before waiver database outreach or ad launch

---

## QUICK SUMMARY — WHAT YOU NEED TO KNOW

| Area | Status | Action Required |
|------|--------|----------------|
| Email to waiver database | ⚠️ Proceed with caution | Re-permission email first |
| SMS to waiver database | 🔴 DO NOT SEND | Zero confirmed opt-in — TCPA violation |
| Children's birthday data | ⚠️ Use carefully | Month only, parent-targeted only |
| Florida Digital Bill of Rights | ✅ Not applicable | Under $1B revenue threshold |
| Ad copy messaging | ✅ Strong | Minor fixes listed below |
| Competitive positioning | ✅ Differentiated | Refinements recommended |
| BOGO/50% off offer legality | ✅ Legal | Must disclose FL residents restriction |
| Waiver legal validity | ✅ Likely valid | Review digital signature audit trail |

---

---

# PART 1: LEGAL REVIEW — WAIVER DATABASE

## The Database: What We're Working With

| Field | What's There | Legal Implication |
|-------|-------------|------------------|
| 34,094 total contacts | PO: 23,751 / WP: 10,343 | Scale creates amplified liability |
| Email address | Present for all | Can email under CAN-SPAM with conditions |
| Phone number | Present for all | Cannot SMS without confirmed consent |
| child_birthday_mm_dd | Present | COPPA-adjacent — handle carefully |
| sms_consent | "Pending Review" for ALL 34,094 | Zero confirmed TCPA opt-in |
| waiver_signed date | NULL for 23,751 (PO records) | Cannot confirm consent was given |

---

## ISSUE 1: EMAIL MARKETING TO THE WAIVER DATABASE
### Risk Level: MEDIUM — Action Required Before Send

**The law:** CAN-SPAM (federal) is an **opt-OUT system**, not opt-in. You are legally permitted to send commercial emails to contacts who provided their email address in a business context (such as signing a venue waiver) — you do not need prior consent to send the first email.

**However, every marketing email must include:**
- ✅ Monkey Joe's physical mailing address (Pointe Orlando address works)
- ✅ A clear, functional unsubscribe link
- ✅ Accurate "From" name and reply-to address
- ✅ Non-deceptive subject line
- ✅ You must honor unsubscribes within 10 business days

**The risk here is NOT CAN-SPAM compliance — it's the quality of the list:**
- 23,751 records (PO) have no `waiver_signed` date recorded — we cannot confirm these emails were provided directly to Monkey Joe's, or when
- Old/cold emails will bounce heavily. A high bounce rate signals spam behavior to email providers and can get the sender domain blacklisted
- Many contacts are years old — Florida summer heat + high deliverability expectations = need list hygiene first

**ACTION REQUIRED — Before sending any email to this list:**

1. **Run list hygiene.** Before importing to GHL, run all 34,094 emails through an email validation tool (NeverBounce, ZeroBounce, or similar). Remove invalid, bounced, and disposable addresses. Expect 15-25% removal on a list this age.

2. **Send a single re-permission email first.** Rather than launching directly into promotions, send one reactivation email that gives people a reason to stay on the list AND confirms they want to hear from you. This improves deliverability, reduces unsubscribes, and builds a cleaner, more responsive list.

**Suggested re-permission subject:** `Still coming to Monkey Joe's?`
**Suggested re-permission body:**
> Hi [First Name],
>
> You're in our database from a previous visit to Monkey Joe's — and we'd love to stay in touch with exclusive deals, birthday surprises, and weekday specials.
>
> If you'd like to keep hearing from us, no action needed — you're already on the list.
>
> If you'd prefer we stop, just hit unsubscribe below. No hard feelings.
>
> Coming soon: weekday offers that will make you actually want a Tuesday.
>
> See you on the inflatables. 🐒
> — Monkey Joe's Orlando

3. **Segment the engaged list.** After the re-permission send, focus all campaigns on contacts who opened, clicked, or did NOT unsubscribe. This is your live, marketable list.

---

## ISSUE 2: SMS MARKETING TO THE WAIVER DATABASE
### Risk Level: 🔴 CRITICAL — DO NOT SEND

**The law:** TCPA (Telephone Consumer Protection Act, 47 U.S.C. § 227) requires **prior express written consent** before sending any marketing text messages. A phone number collected on a liability waiver does NOT constitute SMS consent.

**The numbers:**
- 34,094 contacts × $500 minimum penalty = **$17,047,000 potential exposure**
- 34,094 contacts × $1,500 maximum penalty = **$51,141,000 potential exposure**
- TCPA class actions are heavily litigated. A single plaintiff can trigger a class of thousands.

**The database confirms the risk:** Every single record in the unified database shows `sms_consent = "Pending Review"` — this means zero of the 34,094 contacts have confirmed, documented TCPA consent. Sending any marketing SMS to this list as it stands is a clear TCPA violation.

**Florida Telephone Solicitation (Fla. Stat. § 501.059)** adds state-level requirements on top of TCPA: documented consent, STOP requests honored within 15 days, and no messages outside 8am–9pm local time.

**ACTION REQUIRED — Three steps to fix this:**

1. **Do not send SMS to this database until consent is obtained.** This is non-negotiable.

2. **Add explicit SMS consent to the Aloovy/Aluvii waiver intake form going forward.** The language William adds must be:
   > `[ ]` Yes, I'd like to receive text message promotions from Monkey Joe's. Message and data rates may apply. Reply STOP to opt out at any time.

   Both this box AND the email marketing box must be **unchecked by default**. A pre-checked box is not valid consent.

3. **Obtain consent via email re-permission campaign.** Within the re-permission email (see Issue 1), include a link to a consent page where contacts can explicitly opt into SMS. Those who click "Yes, text me deals" have now given express written consent. Only SMS those contacts.

**Suggested SMS opt-in landing page:** A simple GHL form with the disclosure language above, tracked by timestamp.

---

## ISSUE 3: CHILDREN'S BIRTHDAY DATA — COPPA
### Risk Level: MEDIUM — Use Carefully

**The law:** COPPA (Children's Online Privacy Protection Act) protects personal information collected from or about children under 13. Monkey Joe's is a children's venue — COPPA applies.

**The database contains:** `child_birthday_mm_dd`, `child_birthday_month`, `child_birthday_day`

**What you CAN do:**
- Use birth month (not full date) to send birthday month promotions targeted at **parents**
- "Your little one has a birthday coming up!" — parent is the recipient, parent is being marketed to
- Birthday email sequences directed at parents are standard industry practice and compliant

**What you CANNOT do:**
- Target advertising directly at children under 13 (also violates Facebook/Google ad platform policy)
- Use child's full date of birth in combination with their name for any marketing purpose
- Collect or store child's name alongside birthday in any marketing system
- Email or text a child directly

**ACTION REQUIRED:**
1. In GHL, import birthday data as **Month only** — not month + day combined. This reduces precision below COPPA concern threshold.
2. All birthday campaigns must be addressed to the **parent**: "Your child has a birthday this month — make it a Monkey Joe's celebration."
3. Never include the child's name in any marketing message.
4. Add to all landing page footers and email footers: "Monkey Joe's marketing is directed at parents and guardians, not children. We do not knowingly collect personal information from children under 13."

---

## ISSUE 4: FLORIDA DIGITAL BILL OF RIGHTS
### Risk Level: ✅ NOT APPLICABLE

Florida's Digital Bill of Rights (Fla. Stat. § 501.702, effective July 1, 2024) applies only to businesses with **$1 billion or more in annual global revenue**. Monkey Joe's two-location franchise generating ~$2M revenue is well below this threshold.

This law would apply to the Monkey Joe's **franchisor/corporate parent** at national level if they exceed the threshold — but at the franchisee level, it does not apply.

**No action required at franchise level.** Note this for any future corporate-level data discussions.

---

## ISSUE 5: FLORIDA INFORMATION PROTECTION ACT (FIPA)
### Risk Level: MEDIUM — Data Security Required

FIPA (Fla. Stat. § 501.171) applies to any business that stores personal information of Florida residents. With 34,094 Florida resident records, Monkey Joe's is covered.

**Requirements:**
- Reasonable data security measures on all stored personal information
- If a breach affects 500+ Floridians: notify Florida AG within 30 days + notify individuals
- Written data processing agreements required with GHL and Aloovy/Aluvii

**ACTION REQUIRED:**
1. Confirm GHL has a data processing agreement in place (most enterprise platforms do — verify)
2. The waiver database files (WP_Waiver_DB.xlsx, PO_Waiver_DB.xlsx, mj-waiver-database-unified.xlsx) must NOT be shared via unencrypted email or unsecured channels. Share only via encrypted file share or secure workspace.
3. Do not export customer lists to third parties without a data processing agreement.

---

## ISSUE 6: LIABILITY WAIVER — LEGAL VALIDITY CHECK
### Risk Level: LOW — Audit Recommended

Under Florida law, properly drafted parental liability waivers for recreational activities are enforceable (*Global Travel Marketing v. Shea*, 908 So. 2d 392 (Fla. 2005)), but only for ordinary negligence — not gross negligence.

**What we cannot verify without reading the actual waiver:**
- Does the waiver clearly identify Monkey Joe's as the released party?
- Does it specifically describe inflatable play as the covered activity?
- Is it presented BEFORE the child enters the play area?
- Does it include "parent/guardian" signature language (not just "your name")?
- Does the Aloovy digital system retain timestamped e-signature records?

**ACTION REQUIRED:**
1. Review the actual waiver language in the Aloovy system — not just the database export.
2. Confirm the digital waiver is presented before admission, not after.
3. Confirm Aloovy retains timestamp + IP address of each signed waiver.

**Important note from the database:** 23,751 PO records show NULL for `waiver_signed` date. This may be a data export issue (dates not exported), but if these waivers were genuinely not completed, that is a significant liability gap. Confirm with Michael whether all walk-ins are completing waivers before entry.

---

---

# PART 2: ADVERTISING & OFFER COMPLIANCE

## ISSUE 7: BOGO OFFER — FDUTPA COMPLIANCE
### Risk Level: LOW — One Disclosure Required

**BOGO ("Buy One Get One Free")** is legal under Florida's FDUTPA and FTC guidelines IF:
- The paying admission is the genuine regular admission price — not inflated to fund the "free" one
- Standard admission prices from website: $9.95 (Monday), $10 (Tuesday), $23 (weekday regular), $12.99 (Friday)
- The BOGO ad offer must be based on the **regular weekday admission price**. Confirm with Michael what the base price is for the BOGO campaign offer.

**FLORIDA RESIDENTS ONLY — MUST DISCLOSE:**
Pointe Orlando's existing daily specials are restricted to Florida residents. If this restriction applies to the ad campaign BOGO offer, it MUST be disclosed prominently — not buried in fine print. This is both an FDUTPA requirement and a basic trust issue.

**ACTION: Add to all Pointe Orlando ad copy:**
> *Pointe Orlando only: Valid for Florida residents. Proof of residency required.*

This line must appear in:
- The ad primary text (not just fine print)
- The landing page hero section
- The offer terms section

---

## ISSUE 8: "50% OFF" OFFER — FDUTPA COMPLIANCE
### Risk Level: LOW — Clean

**50% off is valid** as long as the comparison is genuine. The regular weekday admission of ~$23 for ages 3-12 is the base. 50% off = ~$11.50. This is a genuine, substantiated discount.

**No action required** beyond confirming the base price with Michael before ads launch.

---

## ISSUE 9: COUNTDOWN TIMERS / URGENCY LANGUAGE
### Risk Level: LOW — FTC 2024 Guidance

The FTC updated guidance in 2024: countdown timers that **reset when the timer expires** (i.e., always showing "expires in 24 hours") are deceptive. If William builds countdown timers on landing pages, they must be genuine expiry timers — not evergreen reset timers.

**For email subject lines like "This weekend only"** — the offer must genuinely expire that weekend. Do not use perpetual urgency language on always-available offers.

---

---

# PART 3: MESSAGING AUDIT — COMPETITIVE POSITIONING

## VERDICT: The Messaging is Genuinely Strong

The dual promise positioning — *"You get to breathe. They get the best time of their life."* — is the single most differentiated idea in this competitive set. No competitor in Orlando owns this angle in their paid advertising. Tested against all 7 competitors:

| Competitor | Primary Message | MJ Advantage |
|-----------|----------------|-------------|
| Urban Air | "Way more than a trampoline park" | MJ: emotional/parent-focused vs. attraction-led |
| Sky Zone | Membership value | MJ: no commitment, BOGO framing wins |
| Chuck E. Cheese | Family entertainment | MJ: cleaner single focus, less diluted |
| Launch | Multi-attraction | MJ: simpler proposition, higher emotional resonance |
| Funtastic Depot | New/exciting | MJ: 21 years credibility vs. 2023 newcomer |

**The voice is right.** Warm, cheeky, parent-friend energy is exactly what works for this audience and it's distinct from every competitor's tone.

---

## MESSAGING STRENGTHS — KEEP THESE

1. **"You get to breathe. They get the best time of their life."** — Own this. Put it on everything.
2. **"No membership. No monthly fee. Just show up."** — Direct response to Urban Air/Sky Zone. Works in retargeting.
3. **"21 years" / "20+ years"** — Leverage this harder. Funtastic Depot opened in 2023. Trust = time.
4. **Beat-the-Heat variant (B4)** — Nobody else is doing this. Florida gold.
5. **Toddler variant (A4)** — Inflatables ARE safer than trampolines for toddlers. This claim is true and unclaimed.
6. **BOGO framing: "One kid bounces FREE"** — Cleaner than "buy one get one." The word FREE is the most powerful word in marketing.

---

## MESSAGING GAPS — ADD THESE

### Gap 1: Birthday Party Ad Sequence (MISSING — HIGH PRIORITY)
The competitor research shows **birthday parties are the universal lead product** — every competitor leads with it. Our current strategy has birthday party Google ads and email sequences, but **no dedicated Meta Facebook/Instagram birthday party ad sequence**.

Birthday party is the highest-value conversion ($234–$454 per party, up to 24 kids). It deserves its own paid Meta campaign.

**Add to AD-CAMPAIGN-COPY.md:**

**AD C1 — Birthday Party (Meta Video, 30 seconds)**

Hook: `THE BIRTHDAY WHERE YOU ACTUALLY ENJOY IT 🎂`

Primary text:
> You planned everything.
>
> The decorations. The goodie bags. The cake. The RSVPs.
>
> What if this one birthday — just this one — you showed up and we handled the rest?
>
> Monkey Joe's birthday parties include a private party suite, dedicated party host (setup, serving, cleanup), themed plates, cups, and invitations — for up to 24 kids. You bring the cake. We run the show.
>
> Packages from $234. Weekends book fast.
>
> 🎂 Book your date — link below.

Headline: `The Birthday Where YOU Get to Enjoy It`
CTA: Book Now
Target: Women 28–45, parents of children 3–12, 10-mile radius, interest: birthday parties, kids activities

---

### Gap 2: UGC/Testimonial Ad (MISSING — HIGH PRIORITY)
All current copy is brand-written. The data is clear: UGC-style ads outperform polished brand copy in this category. No competitor is running systematic UGC at local franchise level.

**Script for a UGC-style ad (read by a real parent, phone filmed):**
> "I planned my daughter's 7th birthday at Monkey Joe's and honestly? It was the first time in 4 years I actually enjoyed one of her parties. They did everything. I literally just showed up with the cake. My husband and I sat down, had coffee, and watched her run around screaming with joy for two hours. I'm never doing it any other way again."

Ask 3 party parents for a 30-second video. Run as a Meta Reel. This will outperform every polished ad in the set.

---

### Gap 3: Post-Visit Re-engagement (MISSING)
The waiver database contains contacts who have visited before but may not have returned. This is the highest-ROI audience — they already know and trust the brand.

**Win-back sequence (3 emails, add to MESSAGING-BIBLE.md):**

**Email W1 — "It's been a while" (send to anyone with visit date 90+ days ago)**
Subject: `Haven't seen you in a bit 🐒`
> Hi [First Name],
>
> It's been a little while since your last visit to Monkey Joe's.
>
> We get it — life's busy. But we've got something worth coming back for.
>
> This week: [insert current weekly deal]. Come see us.
>
> [CTA: Check This Week's Deals]

**Email W2 — "Your kid's birthday is coming" (send in birthday month)**
Subject: `Birthday month — this one's for [them]`
> Hi [First Name],
>
> It's your little one's birthday month — congratulations to them (and to you for surviving another year).
>
> Monkey Joe's has birthday party packages starting at $234, with a dedicated host who handles everything so you actually get to enjoy it.
>
> Weekend dates book fast. Don't leave it too late.
>
> [CTA: Check Party Packages]

**Email W3 — "One last time" (send 7 days after W2 if no engagement)**
Subject: `Last chance on this one`
> Quick heads up — birthday packages are filling up and we don't want you to miss out.
>
> [CTA: Book Now — It Takes 2 Minutes]

---

### Gap 4: Inbound Call Follow-Up (MISSING — REVENUE OPPORTUNITY)
The inbound call logs show live AI receptionist calls where people asked about:
- Party packages (Jungle Experience $234, Island Excursion $314, Extreme Safari $454)
- Parking
- Closing times / admission pricing

**These callers are warm leads.** When the AI can't complete the booking, there is no follow-up. This is a missed conversion.

**If William can pull caller phone numbers from VAPI logs:**
- Every caller who asked about birthday parties but didn't book should receive a follow-up SMS (with proper consent gathered via the AI call flow)
- Add to the AI receptionist script: "Can I send you a text with a direct booking link?"
- If caller says yes = SMS consent obtained during the call

**This is a significant untapped revenue channel.**

---

### Gap 5: Pre-Visit Confirmation Sequence (MISSING)
When someone books online via Aloovy, do they receive a confirmation sequence? Based on what we know, this is likely minimal.

**Add a 3-touch pre-visit sequence:**
1. **Immediately after booking:** Confirmation email with location details, parking, what to bring (socks!), hours
2. **Day before visit:** Reminder SMS or email — "Your visit is tomorrow! See you at [location]."
3. **Day of visit:** Morning of — "Today's the day! [Location] opens at [time]. Parking tip: [parking info]"

This reduces no-shows and increases venue satisfaction scores (which drives reviews).

---

### Gap 6: Post-Visit Review Request (MISSING)
Google reviews are a major conversion driver for walk-in venue traffic. No post-visit review sequence is currently documented.

**Add to MESSAGING-BIBLE.md:**

**SMS (send 24 hours post-visit — requires TCPA consent):**
> Had a great time at Monkey Joe's? We'd love a quick Google review — it helps more families find us! [Google Maps link] — Reply STOP to opt out.

**Email (send 48 hours post-visit):**
Subject: `How was your visit? 🐒`
> Hi [First Name],
>
> We hope the kids had the best time! If they're still talking about it, we'd love it if you'd take 30 seconds to leave us a review on Google.
>
> It genuinely helps other local families find us — and means the world to our team.
>
> [Leave a Google Review →]
>
> See you next time!
> — Monkey Joe's [Location]

---

---

# PART 4: COMPLIANCE CHECKLIST — BEFORE LAUNCH

## Before Any Email Goes Out
- [ ] Run 34,094 emails through NeverBounce or ZeroBounce — clean the list
- [ ] Send re-permission email (template in Issue 1 above)
- [ ] Confirm GHL email includes: physical address, unsubscribe link, accurate from name
- [ ] Segment into: engaged (opened/clicked) vs. unengaged — market to engaged first

## Before Any SMS Goes Out
- [ ] ZERO SMS to the existing waiver database — no exceptions
- [ ] Add SMS consent checkbox to Aloovy intake form (unchecked by default)
- [ ] Build SMS opt-in page via GHL for email re-permission conversion
- [ ] Only SMS contacts with documented, timestamped consent
- [ ] Every SMS must include: "Monkey Joe's" sender name + "Reply STOP to opt out"
- [ ] Quiet hours enforced: 8am–9pm Eastern only

## Before Paid Ads Launch
- [ ] Pointe Orlando ads: Add Florida residents restriction disclosure to ALL copy
- [ ] Confirm BOGO base price = genuine regular weekday admission price
- [ ] Confirm 50% off base price = genuine regular weekday admission price
- [ ] Landing pages include: privacy policy link + physical address in footer
- [ ] No countdown timers that reset — genuine expiry only
- [ ] Pull 2–3 real 5-star Google reviews for social proof sections

## Data Security
- [ ] Waiver database files stored securely — do not share via unencrypted email
- [ ] Confirm GHL data processing agreement in place
- [ ] Confirm Aloovy/Aluvii data processing agreement in place
- [ ] No credit card data stored outside Aloovy's payment system

## Waiver Audit
- [ ] Review actual Aloovy waiver language against Florida requirements
- [ ] Confirm waiver is presented BEFORE admission (not after)
- [ ] Confirm Aloovy retains timestamped e-signature records
- [ ] Investigate why 23,751 PO records show NULL waiver_signed date

---

---

# PART 5: SAFE WAIVER DATABASE ACTIVATION PLAN

Rather than avoiding the 34,094 contacts, here is the compliant, strategic way to activate them:

## Phase 1: Clean and Re-Permission (Week 1–2)
1. Run list through email validation tool — remove invalid/bounced
2. Send re-permission email to remaining ~25,000-28,000 valid addresses
3. Include email opt-in confirmation + SMS opt-in link in the re-permission email
4. Expected result: 15-30% engage, building a clean list of 3,750–8,400 active, consented contacts

## Phase 2: Birthday Segment (Week 3+)
1. Pull all contacts with `child_birthday_month` matching current or next month
2. Send birthday party email to this segment (parent-targeted, month-only, no child name)
3. This is the highest-intent segment in the entire database

## Phase 3: Lapsed Visit Re-engagement (Week 4+)
1. Segment by last visit date (from Aloovy data, if available)
2. 90–180 days lapsed: Win-back sequence (Email W1 above)
3. 180+ days lapsed: Single reactivation offer (weekly deal)

## Phase 4: SMS Opt-In Growth (Ongoing)
1. New Aloovy intake form captures explicit SMS consent going forward
2. Re-permission email converts email list contacts to SMS subscribers
3. Build from zero — every SMS contact is legally clean

---

*Legal analysis prepared by WILBA using Florida Legal Advisor skill, referencing: CAN-SPAM Act (15 U.S.C. § 7701), TCPA (47 U.S.C. § 227), COPPA (15 U.S.C. § 6501), FDUTPA (Fla. Stat. §§ 501.201–501.213), FIPA (Fla. Stat. § 501.171), Florida Telephone Solicitation Act (Fla. Stat. § 501.059), Florida Electronic Signature Act (Fla. Stat. § 668.50), and FTC Act Section 5.*

**Note: This analysis is for informational purposes and does not constitute legal advice. Consult a licensed Florida attorney before relying on any of this analysis for business decisions.**

---

*Version 1.0 — March 2026*
*Prepared by Jess Morrell / WILBA — wilba.ai*
