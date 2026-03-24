# Plan: Monkey Joe's — Two Core Offers Strategy

**Created:** 2026-03-20
**Status:** Draft
**Request:** From the MJ Project Kickoff meeting (March 16), create a plan for the 2 offers to test and launch

---

## Overview

### What This Plan Accomplishes

Defines and stages the two flagship offers for Monkey Joe's marketing pilot — a BOGO Admission weekday offer and a Frequent Jumper Card digital loyalty program. It maps out how each offer is structured, how they funnel together, how they are tracked, and what copy/landing page approach to use.

### Why This Matters

Michael Carter made it clear: if this pilot works for his two locations, it rolls out to the remaining 9 Monkey Joe's and then to Flying Biscuit and Cinnaholic (130+ Big Game Brands locations). These two offers are the engine of the pilot. Getting them right — trackable, compelling, easy to redeem — is the difference between a one-location deal and a franchise-wide retainer.

---

## Background (From Kickoff Meeting)

**Key insights from Michael Carter:**
- "Wacky Wednesday" BOGO has been running for 21 years — people know it, just not being pushed
- "Toddler Thursday" is consistently popular
- The problem isn't the offer — it's visibility. They're not "slapping people in the face with it" out in the wild
- Frequent Jumper Cards (10 admissions / $120 = $12 each) are a proven product but not sold online at all
- Michael wants promo codes, easy checkout, and a way to invalidate after use
- Corporate approved two conditions: stay on brand (font, monkey, colors) and follow all Florida privacy laws for minors
- Upcharge idea: BOGO weekday + $10 more for weekends

**Two Locations:**
- Pointe Orlando (higher waiver database: 20K+ contacts)
- Winter Park (16K contacts)

---

## Proposed Changes

### Summary

- Define Offer 1: BOGO Admission (weekday) — copy, landing page brief, promo code logic
- Define Offer 2: Frequent Jumper Card — online store setup brief, digital punch card logic (William's build)
- Design the funnel connecting both offers (post-visit upsell flow)
- Confirm offer approval process with Michael before anything goes live

---

## The Two Offers

---

### OFFER 1: BOGO Weekday Admission

**What it is:**
Buy one admission (kids ages 3–12), get one free. Valid weekdays only. Option to upgrade to weekend validity for $10 more.

**Why it works:**
- Already well-known ("Wacky Wednesday" brand) — we're amplifying an existing behavior
- Weekday traffic boost = exactly what Michael needs (summer haymaking is weekends, but the rest needs filling)
- Easy to A/B test against a "50% off" version — same value, different framing

**Offer variants to A/B test:**
| Variant | Headline | Mechanic |
|---------|----------|---------|
| A | "Buy One, Get One Free — Weekdays Only" | BOGO admission, promo code at checkout |
| B | "50% Off All Kids Admissions (Ages 3–12)" | Half price, promo code at checkout |
| C (optional) | "3 Kids In, 1 Pays" | Group-friendly twist, for families with multiple kids |

**Pricing logic:**
- Standard admission: ~$12 (check current pricing in Aloovy)
- BOGO = effectively $6/child
- Weekend upgrade: +$10 for full weekend use

**Redemption flow:**
1. User sees ad (Google/Facebook/Email)
2. Clicks through to dedicated landing page (one offer only — no distractions)
3. Promo code pre-populated at checkout on Aloovy
4. Receipt/confirmation = proof of purchase
5. Code invalidated after use (William to confirm Aloovy supports this)
6. QR code backup if Aloovy doesn't support single-use codes

**Florida privacy compliance:**
- Do NOT reference child's name in any communications
- Use parent-addressed messaging only: "We hear someone special has a birthday coming up..."
- Review Florida COPPA/privacy laws for minors in marketing database use before launch

**Landing Page Brief:**
- Monkey Joe's branding: colors, font, monkey logo
- Hero: bold offer headline + countdown timer or "Limited Weekday Offer"
- Single CTA: "Claim Your Free Admission" → Aloovy checkout
- Minimal copy: 1 line of benefit, 1 line of social proof (e.g., "21 years of Wacky Wednesdays")
- Mobile-first (most click-throughs will be mobile)
- Location-specific: separate pages for Pointe Orlando and Winter Park

**Tracking:**
- Unique promo code per ad campaign/source (e.g., `BOGO-FB-POL`, `BOGO-GG-WP`)
- UTM parameters on all ad links
- FB Pixel + GA4 conversion event on Aloovy checkout confirmation page

---

### OFFER 2: Frequent Jumper Card (Digital Loyalty)

**What it is:**
10 admissions for $120 ($12 each — full price, but pre-paid convenience + loyalty positioning). Delivered as a digital punch card — scannable at the venue, automatically counts down remaining uses.

**Why it works:**
- Existing product, zero online presence — pure incremental revenue
- Drives repeat visits (the card itself is the retention mechanism)
- Commission-based: Jess and team get a cut on every card sold online
- Perfect upsell for first-time BOGO visitors: they've tried it, they loved it, here's how to come back for less

**Build requirements (William):**
- Aloovy integration for online purchase
- Digital punch card: scan at venue, decrements count, shows remaining entries
- Ideally: QR code on phone (no physical card needed)
- Single-use per visit, but reusable across multiple visits until exhausted

**Funnel position:**
- This is the **post-visit upsell** — NOT the lead-generation offer
- Trigger: after first BOGO visit, send automated follow-up (SMS or email next day)

**Post-visit follow-up sequence (draft):**
- **Day 1 after visit (SMS):** "Hey [Parent name], hope the kids had a blast at Monkey Joe's! 🐒 Want to come back? Grab a Frequent Jumper Card — 10 admissions for $120. That's just $12 a visit. [Link]"
- **Day 3 (Email):** More detail — what the card is, how to use it, link to purchase

**Landing Page Brief:**
- Positioned as "the regulars' card"
- Headline: "Come Back Any Time — 10 Jumps for $120"
- Show value: 10 admissions × $12 = $120 (vs. standard walk-in price)
- Digital card graphic/mockup
- CTA: "Get Your Jumper Card" → Aloovy
- Include: "Already used your BOGO? This is the next step."

**Tracking:**
- Unique product in Aloovy with commission tracking
- Source UTM for email vs SMS triggers
- Goal: track how many BOGO first-timers convert to Jumper Cards (this is the LTV metric)

---

## The Funnel (How Both Offers Work Together)

```
[Ad: Google/Facebook/Email]
         ↓
[Landing Page: BOGO Offer]
         ↓
[Checkout: Aloovy — promo code applied]
         ↓
[Visit: Family redeems BOGO at venue]
         ↓
[Day 1 SMS: "Loved it? Get 10 jumps for $120"]
         ↓
[Landing Page: Frequent Jumper Card]
         ↓
[Checkout: Aloovy — digital card purchased]
         ↓
[Repeat visits tracked, Google review requested]
```

This is a simple, proven funnel:
- Offer 1 = **acquisition** (get them in the door)
- Offer 2 = **retention** (keep them coming back)

---

## Step-by-Step Tasks

### Step 1: Confirm Offer Details with Michael

Before building anything, get sign-off on:
- Exact pricing for BOGO (standard admission price to confirm math)
- Whether Aloovy supports promo codes + single-use invalidation (William to check)
- Confirm "not available with any other offer" disclaimer required on all Pointe Orlando offers
- Florida-resident-only restriction on Pointe Orlando offers (not required for Winter Park)
- Brand assets received (15 reels within 2 weeks from media shoot)

**Actions:**
- Draft a 1-page "Offer Confirmation" doc with both offers, pricing, and conditions
- Send to Michael for approval before any copy or pages are built
- CC William

**Files affected:**
- `outputs/monkey-joes/offer-confirmation.md` (create)

---

### Step 2: Research — Audit Existing Ads + Competitors

Before writing a single word of ad copy:
- Audit existing Facebook Ad account (access confirmed during kickoff)
- Audit existing Google Ads account (access confirmed)
- Use ad spy tool (SEM Rush / AdSpy / SpyFu) to see what competitors are running
- Review Constant Contact account: look at past email designs that performed well

**Actions:**
- Log into Facebook Business Manager → Ad Library → note what ran, when, results
- Log into Google Ads → Campaigns → export performance history
- Note: no active campaigns, starting fresh is likely better than inheriting broken campaigns
- Identify 2–3 competitor offers running in Orlando kids entertainment space

**Files affected:**
- `outputs/monkey-joes/ads-audit.md` (create)

---

### Step 3: Write Offer Copy

Once audit is done and Michael has approved the offer structure:

**For Offer 1 (BOGO):**
- 3 × Google Ad headlines (30 chars each) + 2 descriptions (90 chars each)
- 3 × Facebook Ad primary text variants (short, punchy)
- 1 × Email subject line + preview text
- Landing page headline, subhead, CTA button text
- Fine print: "Valid weekdays only. Not valid with other offers. Florida residents only (Pointe Orlando). One use per household."

**For Offer 2 (Frequent Jumper Card):**
- SMS copy (160 chars max)
- Email subject + body (post-visit follow-up)
- Landing page copy

**Actions:**
- Draft all copy in `outputs/monkey-joes/offer-copy.md`
- Run copy past Michael for approval before campaign build

**Files affected:**
- `outputs/monkey-joes/offer-copy.md` (create)

---

### Step 4: Landing Page Briefs (for William to Build)

William builds the pages — Jess provides the briefs.

Create a brief for each page:
1. **BOGO Landing Page — Pointe Orlando**
2. **BOGO Landing Page — Winter Park**
3. **Frequent Jumper Card Landing Page** (shared across locations or location-specific TBD)

Each brief includes:
- Headline / subhead / body copy
- CTA text + destination URL (Aloovy)
- Branding notes: Monkey Joe's font, colors, monkey logo
- Mobile-first
- What tracking pixels to install (GA4, FB Pixel)
- Promo code to pre-populate

**Actions:**
- Create `outputs/monkey-joes/landing-page-briefs.md`
- Send to William to build

**Files affected:**
- `outputs/monkey-joes/landing-page-briefs.md` (create)

---

### Step 5: Aloovy Promo Code Setup

Work with William to confirm Aloovy supports:
- [ ] Promo code creation + assignment to specific products
- [ ] Single-use code invalidation after redemption
- [ ] Commission tracking for online sales
- [ ] QR code generation as backup redemption method

If Aloovy supports it: William sets up products and codes.
If not: explore alternative (custom landing page with separate payment + code delivery).

---

### Step 6: Pre-Launch Approval Run

Before going live:
- [ ] Michael reviews and approves all ad copy
- [ ] Michael reviews and approves landing pages
- [ ] Promo codes tested end-to-end (purchase → confirmation → redemption)
- [ ] Florida privacy compliance confirmed on all list-based sends
- [ ] Tracking confirmed: GA4 events firing, FB Pixel active, UTMs in all links

---

## Files to Create

| File Path | Purpose |
|-----------|---------|
| `outputs/monkey-joes/offer-confirmation.md` | One-page offer spec to send Michael for approval |
| `outputs/monkey-joes/ads-audit.md` | Notes from Google + Facebook account audits |
| `outputs/monkey-joes/offer-copy.md` | All copy: ads, emails, landing pages, SMS, fine print |
| `outputs/monkey-joes/landing-page-briefs.md` | Page briefs for William to build |

---

## Open Questions

1. **Aloovy promo codes:** Does Aloovy support single-use codes + commission tracking? (William to confirm)
2. **Admission pricing:** What is standard walk-in price today per child? (Check monkeyjoes.com)
3. **Pointe Orlando Florida-resident restriction:** How is this enforced at checkout? Address field? Honor system?
4. **Weekend upgrade:** Does Michael want this as an Aloovy upsell at checkout, or separate product?
5. **Google My Business access:** Still needs corporate to grant access to 2 location accounts
6. **Constant Contact access:** Confirmed? Need login or invite.

---

## Validation Checklist

- [ ] Michael has reviewed and approved both offer structures
- [ ] Aloovy capability confirmed (promo codes, single-use, commission)
- [ ] Florida privacy compliance reviewed
- [ ] Copy written and approved for both offers
- [ ] Landing page briefs delivered to William
- [ ] Tracking plan confirmed (GA4 + FB Pixel + UTMs)

---

## Success Criteria

1. Both offers approved by Michael and ready to deploy by April 1 launch
2. Landing pages built with unique promo codes, mobile-first, on-brand
3. Post-visit Frequent Jumper Card follow-up sequence built and tested
4. Tracking confirmed working before first dollar of ad spend goes live

---

## Notes

- Michael mentioned 15 reels from media shoot arriving within 2 weeks — use these in ads ASAP. Better creative = better ad performance, lower cost per click.
- The "Toddler Thursday" brand is proven and untapped digitally — consider making this a third offer in Phase 2 (email + social push to young parent segment)
- Long-term: if online store proves successful, Michael mentioned selling party packages and admissions ahead of time — this becomes a new revenue model for future phases
- Big picture: this pilot is the demo for 130+ franchise locations. Every asset we create should look polished enough to present to Big Game Brands corporate.
