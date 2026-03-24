# Monkey Joe's — Master Strategy
### The Single Source of Truth. Everything Else Is Archive.

**Client:** Michael Carter — Monkey Joe's, Pointe Orlando + Winter Park
**Prepared by:** Jess Morrell / WILBA × William Milner / Lanyu
**Pilot period:** April 1 – June 30, 2026
**Upside:** 9 MJ locations → Big Game Brands (56 locations + Flying Biscuit, Cinnaholic — 130+ total)
**Last updated:** March 2026

> ⚠️ **This document supersedes all previous strategy, roadmap, and planning docs.**
> If something is not in here, it is not in scope for the pilot.

---

## The Mission (One Sentence)

Drive measurable weekday foot traffic to two Monkey Joe's locations using two proven offers, a clean Google → landing page → Facebook funnel, and automated email follow-up — then package the system to roll out to 54 more locations.

---

## The People

| Person | Role |
|---|---|
| **Michael Carter** | Franchise operator — Pointe Orlando + Winter Park. Approves offers, provides access, trains staff |
| **William Milner** (Lanyu) | Developer — builds GoHighLevel funnels, sets up tracking, manages Aloovy/Aluvii integration |
| **Jess Morrell** (WILBA) | Marketing lead — runs ads, writes all copy, manages email campaigns, delivers weekly reports |
| **Nicole** | Michael's venue manager — handles birthday party enquiries, trains staff on promo codes |

---

## The Platform: GoHighLevel

We are building this pilot in **GoHighLevel (GHL)**.

**Why GHL and not WordPress:**
- Build one landing page funnel → clone per location in minutes
- 56 locations means this is a franchise marketing system, not a one-off campaign
- GHL handles landing pages + email automation + SMS in one platform
- When we pitch Big Game Brands corporate, we hand them a turnkey system, not a collection of tools
- Replaces the need for Constant Contact (email) + WordPress landing pages + separate SMS tool

**William builds in GHL. Jess provides all copy and briefs.**
Refer to `GHL-LANDING-PAGE-BRIEF.md` for the full build specification.

---

## The Two Offers (Locked. No Changes Without Michael's Sign-Off.)

These are the only two offers in the pilot. Everything else — Coloring Pages, Spring Break Pack, Ten Tuesday — is Phase 2 once we have a winning offer.

### Offer A — BOGO Weekday Admission

| Field | Detail |
|---|---|
| **What it is** | Buy one kids admission, get one free |
| **Valid** | Weekdays only (Mon–Fri) |
| **Ages** | 3–12 |
| **Pointe Orlando code** | `WACKY-POL` |
| **Winter Park code** | `WACKY-WP` |
| **Restriction (POL only)** | Florida residents only |
| **Not combinable with** | Any other offer or daily deal |
| **One use per** | Household |

### Offer B — 50% Off Ages 3–12

| Field | Detail |
|---|---|
| **What it is** | 50% off all kids admissions, ages 3–12 |
| **Valid** | Weekdays only (Mon–Fri) |
| **Pointe Orlando code** | `KIDS50-POL` |
| **Winter Park code** | `KIDS50-WP` |
| **Not combinable with** | Any other offer or daily deal |
| **One use per** | Household |

**The A/B test:** Both offers run simultaneously at equal budget. After 2 weeks, compare cost per booking. Kill the loser. Scale the winner 20% per week.

---

## The Funnel (Locked)

```
STEP 1 — GOOGLE SEARCH ADS
  Intent-based. People actively searching for kids activities in Orlando.
  Two ad campaigns: Open Play + Birthday Party (separate budgets).
  Location-targeted: 10-mile radius from each store.
        ↓
STEP 2 — LOCATION-SPECIFIC LANDING PAGE (GoHighLevel)
  Pointe Orlando searchers → /bogo-orlando or /halfprice-orlando
  Winter Park searchers → /bogo-winterpark or /halfprice-winterpark
  Each page: one offer, one CTA, promo code pre-filled, no navigation.
        ↓
STEP 3 — ALOOVY/ALUVII CHECKOUT
  Promo code applied at checkout. Booking confirmed.
  Email address captured. Tracking event fired.
        ↓
STEP 4 — AUTOMATED EMAIL SEQUENCE BEGINS
  Confirmation → Day-Before Reminder → Post-Visit Review Request → Jumper Card Upsell.
  See EMAIL-SEQUENCES.md for full copy.
        ↓
STEP 5 — VISIT (family redeems offer at venue)
  Staff ask "Do you have a promo code?" at entry.
  Redemption logged in Aluvii — this is our walk-in attribution.
        ↓
STEP 6 — FACEBOOK/INSTAGRAM RETARGETING
  Pixel fires on all landing pages.
  Retarget: website visitors who didn't convert (BOGO offer ad).
  Retarget: purchasers (Jumper Card upsell ad).
  Upload 36K email list as custom audience.
  Lookalike audience (1%) from best customers — prospecting.
        ↓
STEP 7 — LOYALTY UPSELL: FREQUENT JUMPER CARD
  Day 1 post-visit SMS: "Come back — 10 jumps for $120"
  Day 3 email: Jumper Card explainer + purchase link.
  This is the LTV metric: BOGO first-timers who become regulars.
```

**Why Google first, Facebook second:**
Google Search captures people who are ACTIVELY looking right now. Facebook/Instagram is passive — great for retargeting warm audiences but expensive for cold prospecting against a venue. Start with intent, follow up with display.

---

## GoHighLevel Sub-Account Structure

Each location gets its own GHL sub-account:

| Sub-Account | Location | Promo Codes | Landing Page URLs |
|---|---|---|---|
| MJ — Pointe Orlando | 9101 International Dr, Orlando | `WACKY-POL`, `KIDS50-POL` | /bogo-orlando, /halfprice-orlando |
| MJ — Winter Park | TBC (William to confirm address) | `WACKY-WP`, `KIDS50-WP` | /bogo-winterpark, /halfprice-winterpark |

When pilot succeeds: clone each sub-account for new locations. Change address, phone, promo codes, Google reviews. Done in under an hour per location.

---

## Ad Budget Allocation ($1,500/month Michael's budget)

### Google Ads — $900/month total
| Campaign | Budget | Goal |
|---|---|---|
| Search — Open Play (both locations) | $400 | Weekday foot traffic, BOGO/50% off conversions |
| Search — Birthday Party (both locations) | $400 | High-value party bookings |
| Reserve / testing | $100 | New ad variants, performance max (Month 3) |

### Facebook/Meta Ads — $600/month total
| Campaign | Audience | Budget |
|---|---|---|
| Retargeting — website visitors | 30-day pixel audience | $200 |
| Email list custom audience | 36K uploaded list | $200 |
| Lookalike prospecting | 1% lookalike from best customers | $150 |
| Birthday page retargeting | 14-day birthday page visitors | $50 |

---

## Tracking Infrastructure (William to Build)

Before any dollar of ad spend goes live:

| Tool | Purpose | Status |
|---|---|---|
| Google Tag Manager (GTM) | All tags fire through here — no future dev needed | ⬜ |
| Google Analytics 4 | Conversion tracking — form submits, phone clicks, bookings | ⬜ |
| Meta Pixel | Landing page visits, checkout starts, purchases | ⬜ |
| Google Ads conversion import | Pull GA4 conversions into Google Ads for bidding | ⬜ |
| GHL pipeline | Track leads from landing page through to visit | ⬜ |
| UTM parameters | Every ad link tagged — see utm-guide.md | ⬜ |
| Promo code redemption in Aluvii | Walk-in attribution — this proves ROI to Michael | ⬜ |

**Gate rule:** Ads do not go live until every item above is checked and verified with a test booking.

---

## Email & Automation Strategy

**Platform:** GoHighLevel (replaces Constant Contact)

**Two types of emails:**

### 1. Automated Sequences (build once, fire automatically)
All copy in `EMAIL-SEQUENCES.md`. Sequences:
1. New Subscriber Welcome (3 emails)
2. Post-BOGO Purchase (3 emails)
3. Post-50%-Off Purchase (3 emails)
4. Birthday Party Inquiry Follow-Up (3 emails)
5. Win-Back / Reactivation for lapsed list (5 emails over 8 weeks)
6. Jumper Card Post-Visit Upsell (2 emails + 1 SMS)
7. Birthday Month Reminder (3 emails, triggered by age data)

### 2. Weekly Broadcast Campaigns (Jess drafts, sends weekly)
Templates in `WEEKLY-CAMPAIGN-TEMPLATES.md`:
- **Campaign 1 — Tuesday evening:** Wacky Wednesday BOGO push
- **Campaign 2 — Friday morning:** Weekend preview + birthday party angle

**Email list segmentation (do this before sending anything):**
| Segment | Criteria | Action |
|---|---|---|
| Active | Opened/clicked in last 90 days | Weekly campaigns immediately |
| At-Risk | 90–180 days inactive | Re-engagement sequence first |
| Lapsed | 180+ days inactive | Win-back sequence first |

Do NOT blast all 36K at once. Start with Active, warm up At-Risk and Lapsed.

---

## Competitive Positioning (Use This in All Copy)

**Two advantages that no competitor can match. Lead with these everywhere.**

| Monkey Joe's | Kidiverse | Pump It Up | Rebounderz | Funtastic Depot |
|---|---|---|---|---|
| Kids $12.99–$13.99 | ~$20.49 all-in | ~$9 open play | ~$20/hour | $14.95–$24.95 |
| **Adults FREE** | Varies | Included | Included | Included |
| **Walk-in, no booking** | Required | Required | Required | Walk-in OK |

**Tagline for all ads and copy:** "Adults always free. Walk in anytime."

**Secondary angle:** 21 years of Wacky Wednesday — not a flash-in-the-pan discount, it's a two-decade tradition. That's credibility.

---

## Keyword Strategy

Full keyword map in `KEYWORD-RESEARCH.md`. Priority campaigns:

**Google — Open Play:**
- "indoor playground Orlando"
- "indoor play center Winter Park FL"
- "toddler indoor playground Orlando"
- "kids activities rainy day Orlando" ← underpriced, high intent
- "inflatable play center Orlando"

**Google — Birthday Party:**
- "kids birthday party venue Orlando"
- "indoor birthday party Orlando FL"
- "birthday party with inflatables Orlando"
- "birthday party venue Winter Park FL"

**Negative keywords (add Day 1):**
jobs, hiring, outdoor, park, equipment for sale, daycare, preschool, Disney, Universal, water park, Miami, Tampa, Jacksonville, Gainesville, adult

---

## Reporting Cadence

| Report | Who | When |
|---|---|---|
| Weekly performance update | Jess → William | Every Monday by 9am |
| Monthly report (full) | Jess → William → Michael | By 3rd of each month |
| Michael receives report | William → Michael | By 5th of each month |
| Michael pays | Michael | By 15th (5-day window to contest) |

Weekly report template: `weekly-report-template.md`

---

## Phase Timeline

| Phase | Dates | Focus | Ad Spend |
|---|---|---|---|
| **Phase 1 — Foundation** | April 1–14 | GHL setup, tracking, promo codes, email list segmented | $0 |
| **Phase 2 — Launch** | April 15–30 | Google Ads live, email sequences live, first weekly campaigns | $1,500/mo begins |
| **Phase 3 — Retargeting** | May 1–15 | Facebook retargeting live, A/B test results → scale winner | $1,500/mo |
| **Phase 4 — Prove & Pitch** | May 15–June 30 | Optimize, build case study, prepare 9-location pitch to Michael + corporate | $1,500/mo |

---

## What Wins This Pilot

1. **Provable walk-in revenue via promo code redemptions** — Michael sees the code, he sees the conversion
2. **Cost per booking under $15** — if Google Ads brings in bookings for <$15 each, that's a clear positive ROI
3. **Birthday party inquiries up** — this is the highest-value conversion in the business
4. **Email list grows** — 36K → 38K+ by end of pilot
5. **The system looks scalable** — every landing page, every automation, every report is documented well enough to pitch to corporate

---

## Files in This Project

| File | What It Is |
|---|---|
| `MASTER-STRATEGY.md` | **THIS FILE** — the North Star |
| `EMAIL-SEQUENCES.md` | All 7 automation sequences, fully written copy |
| `WEEKLY-CAMPAIGN-TEMPLATES.md` | Two weekly send templates for Jess to use each week |
| `GHL-LANDING-PAGE-BRIEF.md` | GoHighLevel build brief for William — full specs |
| `KEYWORD-RESEARCH.md` | Full keyword map, CPC estimates, competitor intel |
| `AD-CAMPAIGN-COPY.md` | Ad headlines, descriptions, all variants |
| `MESSAGING-BIBLE.md` | Brand voice, all channel copy (reference) |
| `ROLLOUT-CHECKLIST.md` | Task-level launch checklist (now secondary to this doc) |
| `weekly-report-template.md` | Monday report template |
| `utm-guide.md` | UTM naming convention for all links |
| `promo-codes.md` | Full promo code list |

---

*Strategy v2.0 — March 2026*
*WILBA × Lanyu × Monkey Joe's*
*Questions: jess@wilba.ai | william@lanyu.ai*
