# Plan: Monkey Joe's — Step-by-Step Funnel Build (Both Locations)

**Created:** 2026-03-20
**Status:** Draft
**Request:** Clear step-by-step plan to build out both location funnels and automations, incorporating all meeting notes, with very clever marketing baked in.

---

## Overview

### What This Plan Accomplishes

A sequential, day-by-day build plan to take Monkey Joe's from zero marketing infrastructure to a fully live, two-location funnel by April 1, 2026. Every step is ordered by dependency — nothing is built until what it needs is in place. By the end, both Pointe Orlando and Winter Park have live ads, automated email sequences, a digital loyalty program, and full tracking.

### The Big Marketing Idea

**"Monkey Joe's is for regulars."**

Every competitor is chasing the birthday party booking. We're not. We're building a *weekly habit*. The family that comes every Wacky Wednesday. The toddler who drags their parent through the door every Thursday. The kid who's already counting down their 10th Jumper Card visit.

We're not competing on the birthday. We're winning the other 51 weeks of the year.

**Tone:** Warm, local, slightly cheeky. Not corporate. Not generic. Michael Carter has run this place for 20+ years and knows half his customers by name. That energy goes into every line of copy.

---

## Background (From Meeting Calls — Key Context)

From the **MJ Project Kickoff (March 16)**:
- **36K+ waiver database** (20K Pointe Orlando, 16K Winter Park) — warm audience, been in the door before
- **Wacky Wednesday BOGO has run for 21 years** — people know it, they're just not being reminded online
- **Toddler Thursday** — consistently popular, under-marketed digitally
- **No current organic social strategy** — "we don't have one"
- **15 reels incoming** from media shoot (within 2 weeks of March 16 = ~March 28)
- **Aloovy** handles booking + payments — promo codes and commission tracking need confirming
- **Constant Contact** — two accounts (mjstore135 / mjstore137), access authorization pending
- **Corporate rules:** Stay on brand (font, colors, monkey), follow Florida privacy laws for minors, weekly/bi-weekly updates
- **Phase 2 carrot:** 9 Monkey Joe's locations + Flying Biscuit + Cinnaholic (130+ locations) if this pilot works
- **Pointe Orlando** = tourist area, Florida-resident restriction on offers
- **Winter Park** = local family market, no resident restriction
- **Michael's biggest ask:** Easy to track, easy to pay, easy to redeem. "If you slap me in the face with it when I'm out in the wild, then it's not much better." = we need to get in front of them digitally.

**Competitor research findings (March 2026):**
- Chuck E. Cheese owns birthday but nobody owns the regular weekday visit
- Urban Air has the biggest budget (VaynerX-backed) but is corporate/national
- Sky Zone uses weekday discounts + email-gated offers — we borrow this
- **Nobody has a digital punch card** — Frequent Jumper Card is a genuine differentiator
- Short video (9:16 Reels) is the dominant format — media shoot timing is perfect

---

## The Funnel Architecture (Both Locations)

### Pointe Orlando Funnel
```
[Cold: FB/Google Ads — Florida residents, 10-mile radius]
    ↓
[Landing Page: BOGO Pointe Orlando]  ← "Florida residents only"
    ↓
[Aloovy checkout: PROMO-POL]
    ↓
[Email: Confirmation + how to redeem]
    ↓
[VISIT]
    ↓
[Day 1 SMS/Email: Frequent Jumper Card upsell]
    ↓
[Day 7: Re-engagement if no return]
    ↓
[Ongoing: Wacky Wednesday + Toddler Thursday weekly campaigns]
    ↓
[Birthday sequence: 90-day + 45-day triggers from waiver DB]
```

### Winter Park Funnel
```
[Cold: FB/Google Ads — local families, 10-mile radius]
    ↓
[Landing Page: BOGO Winter Park]  ← No resident restriction
    ↓
[Aloovy checkout: PROMO-WP]
    ↓
[Email: Confirmation + how to redeem]
    ↓
[VISIT]
    ↓
[Day 1 SMS/Email: Frequent Jumper Card upsell]
    ↓
[Day 7: Re-engagement if no return]
    ↓
[Ongoing: Wacky Wednesday + Toddler Thursday weekly campaigns]
    ↓
[Birthday sequence: 90-day + 45-day triggers from waiver DB]
```

---

## PRE-BUILD: Decisions & Access (Resolve First)

Before a single thing is built, these must be resolved:

| Item | Who | Status | Blocking |
|------|-----|--------|---------|
| Constant Contact access (both accounts) | Michael to authorize Jess | PENDING | All email |
| Aloovy promo code support | William to confirm | PENDING | Offer launch |
| Aloovy confirmation page URL | William to confirm | PENDING | Pixel Purchase event |
| Which CC account = which location | Michael to confirm | PENDING | List setup |
| Landing page domain (subdomain or separate?) | William to confirm | PENDING | GTM install |
| CallRail in/out of budget | Michael to confirm | PENDING | Phone tracking |
| Google My Business access (both locations) | Corporate via Michael | PENDING | GBP work |
| Google Ads access | William or Michael | PENDING | Google campaigns |

**Send William and Michael a single "access request" email covering all of the above today.**

---

## PHASE 0: Infrastructure (Days 1–3)

### STEP 0.1 — Create Second Meta Ad Account (Winter Park)

**Why:** Separate budgets, separate reporting, different audience rules per location.

**Actions:**
1. Log into Meta Business Manager (you already have access)
2. Business Settings → Accounts → Ad Accounts → Add → Create New Ad Account
3. Name: "Monkey Joe's Winter Park"
4. Currency: USD, Time zone: Eastern
5. Assign payment method (Michael's card — he pays separately for ad spend)
6. Confirm existing account = "Monkey Joe's Pointe Orlando"

**Result:** Two ad accounts, one Business Manager. ✓

---

### STEP 0.2 — Set Up Facebook Pixel (Both Accounts)

**Why:** You have pixel access. This unblocks all conversion tracking and audience building — even before GA4 is set up.

**Actions:**
1. Meta Business Manager → Events Manager → Data Sources → Connect → Facebook Pixel
2. Create pixel: "Monkey Joe's Pixel"
3. Copy Pixel ID → save to `outputs/monkey-joes/logins.md`
4. Share pixel with BOTH ad accounts (Pointe Orlando + Winter Park) — one pixel, two ad accounts using it

**For now (without GTM):**
- Ask William to install the pixel base code directly on his landing pages (paste into `<head>`)
- You'll install it on the WordPress site via GTM once that's set up

**Events to fire (tell William to implement on his pages):**
- `ViewContent` — on landing page load
- `InitiateCheckout` — when user clicks the Aloovy CTA button
- `Purchase` — on Aloovy confirmation page (if possible)

---

### STEP 0.3 — Install GTM on WordPress

**Why:** One plugin = permanent home for all tracking tags. Faster than installing pixels manually.

**Actions:**
1. Log into WordPress: monkeyjoes.com/store-admin (STORE137@monkeyjoes.com)
2. **First:** Check what's already installed — Plugins → Installed Plugins. Look for any Google Analytics, pixel, or tag manager plugin already running.
3. **Also check:** BuiltWith.com → paste monkeyjoes.com → see what tracking exists
4. If nothing found: Plugins → Add New → search "GTM4WP" → Install → Activate
5. Create GTM account: tagmanager.google.com (sign in with WILBA Google account)
6. New container: "monkeyjoes.com" → Web
7. Copy Container ID (GTM-XXXXXXX)
8. GTM4WP Settings → paste Container ID → Save
9. Verify: Chrome DevTools → Network → search "gtm.js" → should load ✓

**Save:** GTM Container ID to `outputs/monkey-joes/logins.md`

---

### STEP 0.4 — Add FB Pixel Tag in GTM

**Actions:**
1. GTM → Tags → New → Custom HTML (or Meta Pixel template if available)
2. Paste FB Pixel base code (from Meta Events Manager → Manual Install)
3. Replace pixel ID with your actual Pixel ID
4. Trigger: All Pages
5. Name: "FB Pixel — Base Code"
6. Add ViewContent tag: trigger on landing page URL patterns
7. Publish container (version name: "Initial — FB Pixel")

**Verify:** Facebook Pixel Helper Chrome extension → green on monkeyjoes.com ✓

---

### STEP 0.5 — Create GA4 Property

**Actions:**
1. analytics.google.com → Create Property → "Monkey Joe's"
2. Platform: Web → URL: monkeyjoes.com → timezone: Eastern → currency: USD
3. Copy Measurement ID (G-XXXXXXXXXX)
4. Add as GTM tag (GA4 Configuration tag → All Pages trigger)
5. Publish GTM update
6. Give Michael "Viewer" access to GA4 (Admin → Access Management → add his email)

**Save:** GA4 Measurement ID to `outputs/monkey-joes/logins.md`

---

### STEP 0.6 — Give William GTM Container ID

**Message William:**

> "For every Monkey Joe's landing page you build, add this GTM snippet in the `<head>` — it automatically installs our Facebook Pixel and GA4. Here's the container ID: GTM-XXXXXXX. Let me know if you need the full snippet code."

---

## PHASE 1: Offer Setup (Days 2–4)

### STEP 1.1 — Send Offer Confirmation to Michael

Before any copy goes live, get written sign-off. Create `outputs/monkey-joes/offer-confirmation.md` and send.

**Offer 1: BOGO Weekday Admission**
- Buy one admission (kids 3–12), get one free
- Valid Monday–Friday
- Weekend upgrade available: +$10
- Pointe Orlando: Florida residents only, not valid with other offers, one use per family
- Winter Park: weekdays only, not valid with other offers, one use per family
- Mechanic: promo code at Aloovy checkout

**Offer 2: Frequent Jumper Card**
- 10 admissions for $120 ($12/visit)
- Digital card, QR scan at door, auto-decrements
- Commission paid to Jess + William on each card sold online
- Not a cold offer — post-visit upsell only

**Questions to confirm with Michael:**
1. Current standard admission price per child?
2. Can Aloovy do single-use promo codes? (William checking)
3. Weekend upgrade — separate Aloovy product or upsell at checkout?
4. Commission % on Frequent Jumper Card sales?
5. Which CC account (135/137) is which location?

---

### STEP 1.2 — Request Aloovy Promo Codes from William

**Codes needed:**

| Code | Offer | Location | Restriction |
|------|-------|---------|------------|
| `WACKY-POL` | BOGO weekday | Pointe Orlando | FL residents, 1x per family |
| `WACKY-WP` | BOGO weekday | Winter Park | 1x per family |
| `WELCOME` | BOGO weekday | Both | New opt-ins, 1x use |
| `COMEBACK` | BOGO weekday | Both | Dormant re-engagement, 1x use |

**Also request from William:**
- Frequent Jumper Card set up as purchasable product in Aloovy
- Commission tracking enabled
- Confirmation page URL after successful purchase

---

### STEP 1.3 — Build UTM Link System

Create all campaign links with UTM parameters. Save to `outputs/monkey-joes/utm-guide.md`.

**Build links using:** ga-dev-tools.google.com/campaign-url-builder

| Campaign | Base URL | UTM Tags |
|----------|---------|---------|
| FB BOGO POL (Variant A — BOGO framing) | [William's POL landing page] | source=facebook, medium=cpc, campaign=bogo-weekday, content=variant-a |
| FB BOGO POL (Variant B — 50% off framing) | [William's POL landing page] | source=facebook, medium=cpc, campaign=bogo-weekday, content=variant-b |
| FB BOGO WP (Variant A) | [William's WP landing page] | source=facebook, medium=cpc, campaign=bogo-weekday, content=variant-a |
| FB BOGO WP (Variant B) | [William's WP landing page] | source=facebook, medium=cpc, campaign=bogo-weekday, content=variant-b |
| Google Brand POL | [William's POL page] | source=google, medium=cpc, campaign=brand |
| Google Brand WP | [William's WP page] | source=google, medium=cpc, campaign=brand |
| Email Birthday 90d | [BOGO landing page] | source=email, medium=email, campaign=birthday-reactivation, content=90day |
| Email Birthday 45d | [BOGO landing page] | source=email, medium=email, campaign=birthday-reactivation, content=45day |
| Email Welcome | [BOGO landing page] | source=email, medium=email, campaign=welcome-series |

---

## PHASE 2: Email & Automations (Days 3–6, once CC access granted)

> **Prerequisite:** Constant Contact access confirmed. If not received within 48 hours of kickoff, escalate to Michael directly.

### STEP 2.1 — Audit Both CC Accounts

Log into each CC account (mjstore135 and mjstore137):

**For each account:**
- What lists exist? How many contacts?
- What's the overall health? (open rates, bounce rates)
- Are there existing automations running? (DON'T delete anything until understood)
- What emails have been sent? What performed best?
- Does the birthday field exist on contact records? (essential for automation)
- What segments already exist?

**Document in:** `outputs/monkey-joes/email-audit.md`

---

### STEP 2.2 — Prepare & Import Waiver Database

**Source:** Waiver database — 20K Pointe Orlando contacts + 16K Winter Park contacts

**Before importing:**
- [ ] Review Florida privacy laws for marketing to minors (addresses are adult parents — confirm)
- [ ] Scrub for: duplicates, invalid emails, obvious data errors
- [ ] Confirm birthday field is formatted consistently (MM/DD/YYYY or similar)
- [ ] Do NOT address any child by name in any campaign

**Import structure per account:**
- List name: "Waiver Database — [Location] — March 2026"
- Tag: "waiver-import"
- Custom field: ChildBirthday (if not already existing)

**Create segments immediately after import:**
- Active (opened email in last 90 days — if applicable)
- Warm (opened 90–180 days ago)
- Dormant (no opens in 6+ months or never opened)
- Birthday in next 90 days (for automation trigger)

---

### STEP 2.3 — Build Automation 1: Birthday Reactivation

**In Constant Contact → Automations → Create Automation**

**Trigger:** Contact's ChildBirthday field = 90 days from today (rolling)

**Sequence:**

| Step | Timing | Email | Subject |
|------|--------|-------|---------|
| 1 | Day 0 (90 days out) | A1: Birthday coming up | "🎉 A birthday's coming up..." |
| 2 | 45 days later | A2: Only 45 days | "Only 45 days — party rooms filling up" |
| 3 | Birthday + 7 days | A3: Hope it was amazing | "Hope it was amazing 🎉" |

**Email A1 body:**
> Hi [First Name],
>
> Psst — we heard someone special has a birthday coming up in about 3 months.
>
> Whether you're planning a full party or just want to make the day extra fun, Monkey Joe's has you covered. We've been creating birthday memories in [Location] for over 20 years.
>
> **Here's what we do best:**
> - Party rooms (booking up fast — especially weekends)
> - Unlimited bouncing, climbing, and sliding
> - A venue that handles the chaos so you don't have to
>
> **Start planning now → [Book a Party Room]**
>
> Or just want a fun day out first? Our BOGO weekday deal means one kid gets in free. → [Grab your spot]
>
> See you soon,
> The Monkey Joe's Team 🐒

**Email A2 body:**
> Hi [First Name],
>
> The big day is 45 days away — and our party rooms are filling up fast.
>
> If a Monkey Joe's birthday is on the cards, now's the time to lock it in. You show up, we handle everything else.
>
> **🎂 Book your party room → [Book Now]**
>
> Not doing a party this year? No worries. Our weekday BOGO deal means one kid bounces free any Monday–Friday.
>
> **→ [Grab the BOGO deal]**
>
> Either way — let's make it a birthday they talk about for months.
>
> Monkey Joe's 🐒

**Email A3 body:**
> Hi [First Name],
>
> Hope the birthday celebrations were everything they dreamed of!
>
> If you came to see us — thank you. You're why we do this.
>
> If life got in the way — no stress. We're here whenever you're ready.
>
> **Want to make it a regular thing?**
>
> The Frequent Jumper Card: 10 admissions for $120. That's $12 a visit, any day, any time. Just scan and bounce.
>
> **→ [Get Your Frequent Jumper Card — $120]**
>
> See you soon,
> Monkey Joe's 🐒

---

### STEP 2.4 — Build Automation 2: Post-Purchase Welcome

**Trigger:** New contact added to list "BOGO Purchasers — [Location]"
(Manual weekly import from Aloovy export until Zapier/API set up)

| Step | Timing | Email | Subject |
|------|--------|-------|---------|
| 1 | Immediately | B1: Confirmation | "You're in! Here's your free admission 🐒" |
| 2 | 48 hours post-purchase | B2: Post-visit upsell | "How was it? (and here's a little something...)" |
| 3 | Day 7 | B3: Come back | "Miss you already 👀" |

**Email B1 body:**
> Hi [First Name],
>
> You're all set! Here's everything you need.
>
> **Your BOGO Code:** `[WACKY-POL or WACKY-WP]`
>
> **How to use it:**
> 1. Head to Monkey Joe's [Location] any weekday (Mon–Fri)
> 2. Show this email at the door
> 3. One kid gets in free
>
> **📍** [Location address] | Open [hours]
>
> **A few things to know:**
> - Valid weekdays only
> - One use per family
> - Socks required (grab a pair at the door for $2 if needed)
> [Pointe Orlando only]: Valid for Florida residents only
>
> Questions? Call us: [phone]
>
> Can't wait to see you,
> Monkey Joe's 🐒

**Email B2 body:**
> Hi [First Name],
>
> Hope the kids had an absolute blast!
>
> If the car ride home was full of "Can we PLEASE go again??" — we have the perfect answer.
>
> **The Frequent Jumper Card.**
> 10 admissions. $120. That's $12 a jump, any day you want. No booking needed. Just scan and bounce.
>
> It's basically the smartest thing you'll buy this month. 🐒
>
> **→ [Get Your Frequent Jumper Card]**
>
> See you again soon,
> Monkey Joe's

**Email B3 body:**
> Hi [First Name],
>
> It's been a week since your last visit — the bounce houses are asking for you.
>
> Don't forget: **Wacky Wednesdays are BOGO every single week.** Bring a friend, one gets in free. Every Wednesday.
>
> And if you're ready to make it a habit — the Frequent Jumper Card gives you 10 visits for $120.
>
> **→ [Grab Wednesday's BOGO]** → **[Get the Jumper Card]**
>
> See you soon,
> Monkey Joe's 🐒

---

### STEP 2.5 — Build Automation 3: New Opt-In Welcome Series

**Trigger:** New subscriber via CC opt-in form or landing page

| Step | Timing | Email | Subject |
|------|--------|-------|---------|
| 1 | Immediately | C1: Welcome | "Welcome to the Monkey Joe's fam 🐒" |
| 2 | Day 3 | C2: The story | "20+ years of birthday memories" |
| 3 | Day 7 | C3: Toddler Thursday | "Toddler Thursday is kind of a big deal" |
| 4 | Day 10 | → Move to weekly list | — |

**Email C1 body:**
> Hi [First Name],
>
> Welcome! You've officially joined the inner circle of parents who know the secret to a great day out.
>
> Here's your welcome gift:
>
> **Buy One Get One Free admission — this week, any weekday.**
> Use code `WELCOME` at checkout.
>
> **→ [Claim Your Free Admission]**
>
> We'll keep you posted on Wacky Wednesdays, Toddler Thursdays, and anything else we've got cooking.
>
> Fair warning: the kids are going to love you for this.
>
> See you soon,
> Monkey Joe's 🐒

---

### STEP 2.6 — Build Automation 4: Dormant Re-engagement

**Run once:** Before main campaigns launch — clean the list.

**Trigger:** Manual — apply to "Dormant" segment (no opens in 6+ months)

| Step | Timing | Email | Subject |
|------|--------|-------|---------|
| 1 | Day 1 | D1: It's been a while | "It's been a while... 👀" |
| 2 | Day 3 (non-openers) | D2: Last chance | "Last one, we promise 🙏" |
| 3 | Day 5 | Suppress non-openers from active list | — |

**Email D1 body:**
> Hi [First Name],
>
> We noticed it's been a while since we've seen you.
>
> We get it — life gets busy. But we've got something to make coming back easy:
>
> **One free admission — on us.**
> Code `COMEBACK` at checkout. Weekdays only.
>
> **→ [Claim Your Free Admission]**
>
> No strings. Just bouncing. 🐒
>
> Hope to see you soon,
> Monkey Joe's

---

### STEP 2.7 — Set Up Weekly Campaign Calendar

**Schedule in Constant Contact from April 1:**

| Day | Send Time | Campaign | List |
|-----|-----------|---------|------|
| Tuesday | 6:00pm | Wacky Wednesday BOGO reminder | All active |
| Wednesday | 6:00pm | Toddler Thursday preview | All active |
| Friday | 9:00am | Weekend hype | All active |

**Tuesday email template:**
- Subject: "Wednesday = BOGO 🐒 (as always)"
- Preview: "Buy one admission, get one free. Every Wednesday."
- Body: 3 lines max. One image. One CTA → landing page.

---

## PHASE 3: Facebook Ads (Days 4–7)

> **Prerequisite:** Landing pages from William live. Promo codes confirmed in Aloovy. Pixel firing.

### STEP 3.1 — Set Up Both Ad Accounts

For each account (Pointe Orlando + Winter Park):
1. Payment method confirmed (Michael's card for ad spend)
2. Business Manager access confirmed
3. Pixel shared and assigned
4. Correct timezone (Eastern), currency (USD)

---

### STEP 3.2 — Build Custom Audiences

For each ad account:

| Audience | Source | Size est. |
|---------|--------|---------|
| Website visitors (30 days) | Pixel | Grows over time |
| Email list upload | CC export → custom audience | 16K–20K |
| 1% Lookalike of email list | Lookalike from above | Large |
| 1% Lookalike of website visitors | Lookalike from pixel | Grows |

**Email list upload:**
1. Export list from Constant Contact (CSV)
2. Meta Business Manager → Audiences → Create → Customer List
3. Upload CSV → match on email + first name
4. Repeat for each location's list

---

### STEP 3.3 — Build Campaign Structure

**Pointe Orlando Ad Account:**

| Campaign | Objective | Budget | Audience |
|---------|-----------|--------|---------|
| BOGO — Cold Traffic | Conversions | $500/month | Interest: local parents, Florida geo, 10mi radius |
| BOGO — Retargeting | Conversions | $150/month | Website visitors + email list |
| Birthday Party — Awareness | Traffic | $100/month | Cold interest-targeted |

**Winter Park Ad Account:**

| Campaign | Objective | Budget | Audience |
|---------|-----------|--------|---------|
| BOGO — Cold Traffic | Conversions | $500/month | Interest: local parents, 10mi radius |
| BOGO — Retargeting | Conversions | $150/month | Website visitors + email list |
| Birthday Party — Awareness | Traffic | $100/month | Cold interest-targeted |

**Total monthly ad spend: $1,500 (split $750/$750 per location)**

---

### STEP 3.4 — Build Ad Sets: BOGO Cold Traffic

**Ad Set: Pointe Orlando — Cold Parents**
- Location: 10-mile radius, Pointe Orlando, Florida residents only
- Age: 25–45
- Gender: All (skew female — moms are primary decision-maker per Urban Air research)
- Detailed targeting: Parents (Facebook parenting interest), Family activities, Kids entertainment, Birthday party planning

**Ad Set: Winter Park — Cold Parents**
- Location: 10-mile radius, Winter Park
- Age: 25–45
- Same interest targeting, no resident restriction

---

### STEP 3.5 — Create The Ads (BOGO Campaign)

**Variant A — BOGO framing:**

*Primary text:*
> Wednesday just became the best day of the week.
>
> Monkey Joe's Wacky Wednesday: buy one kid's admission, get one FREE. Every single Wednesday.
>
> Ages 3–12. Bounce houses, climbing walls, slides — the works.
>
> 21 years of Wacky Wednesdays. Still going strong. 🐒
>
> [Pointe Orlando only: Florida residents only. Not valid with other offers.]
>
> 👉 Book your free admission before spots fill up.

*Headline:* Buy One Get One Free — Wednesdays Only
*Description:* Kids ages 3–12. Weekday deal. Book online.
*CTA button:* Book Now
*Destination:* UTM-tagged landing page URL

**Variant B — 50% off framing:**

*Primary text:*
> Half price kids' admission — weekdays all week long.
>
> 50% off for kids ages 3–12, Monday–Friday at Monkey Joe's [Location].
>
> Bounce houses. Climbing walls. Obstacle courses. One very happy parent.
>
> [Pointe Orlando: Florida residents only.]
>
> 👉 Book your visit now.

*Headline:* 50% Off Kids Admission — This Week
*CTA button:* Get Offer

**Creative direction (for media shoot reels):**
- Video 1: Kid launching into bounce house, huge smile → text overlay "BOGO WEDNESDAY 🐒" → offer reveal
- Video 2: Group of little kids racing through obstacle course → "The chaos they love. The break you need." → offer
- Video 3: Parent watching kids bounce, relieved/happy expression → "Wacky Wednesday. One gets in free. Every week." → CTA

**Hook rule:** First 3 seconds = kid face doing something joyful/chaotic. No voiceover needed. Let the energy sell it.

---

### STEP 3.6 — Create Retargeting Ads (Frequent Jumper Card)

**Audience:** Website visitors who did NOT purchase + email list (Pointe Orlando and Winter Park separately)

*Primary text:*
> If your kids said "Can we go again?" on the way home — this one's for you.
>
> The Monkey Joe's Frequent Jumper Card.
> 10 admissions. $120. That's $12 a visit, any day you want.
>
> No booking needed. Just scan and bounce.
>
> The regulars swear by it. 🐒
>
> 👇 Get yours online.

*Headline:* 10 Visits for $120 — Frequent Jumper Card
*CTA button:* Shop Now

---

### STEP 3.7 — Create Toddler Thursday Ad

**Audience:** Parents of toddlers (ages 0–4 Facebook parenting interest) + existing list

*Primary text:*
> Toddler mums — this one's for you.
>
> Every Thursday at Monkey Joe's [Location]: smaller crowds, the right pace, bounce houses built for little ones.
>
> Kids under 5 absolutely thrive here. And it's BOGO on weekdays — one gets in free.
>
> 👉 See this Thursday's details.

*Headline:* Toddler Thursday at Monkey Joe's
*CTA:* Learn More

---

## PHASE 4: Google Ads (Days 5–8)

> **Prerequisite:** Google Ads account access confirmed.

### STEP 4.1 — Account Structure

| Account | Location | Monthly budget |
|---------|---------|--------------|
| Pointe Orlando | Geo: Pointe Orlando + surrounds | $375 search + $125 display |
| Winter Park | Geo: Winter Park + surrounds | $375 search + $125 display |

---

### STEP 4.2 — Campaign 1: Brand Search

**Ad Group: Brand Keywords**
- Keywords: `monkey joes orlando`, `monkey joes pointe orlando`, `monkey joes winter park`, `monkey joe's birthday party`, `monkeyjoes.com`

**RSA Headline options:**
1. Monkey Joe's Orlando
2. BOGO Wednesdays — Book Now
3. Party Rooms Available
4. Kids 3–12 Go Wild Here
5. 20 Years of Birthday Fun
6. Book Online Today
7. Weekday BOGO Deal

**Descriptions:**
1. Bounce houses, climbing walls & party rooms. Buy one kid in, get one free on weekdays. Book now.
2. Orlando's favourite kids' play venue for 20+ years. BOGO weekday deal. Party rooms available now.

---

### STEP 4.3 — Campaign 2: Category Search

**Keywords:**
- `kids indoor play place orlando`
- `indoor bounce house orlando`
- `kids activities orlando weekday`
- `kids birthday party venue orlando`
- `indoor play area for toddlers orlando`
- `things to do with kids orlando`

**RSA Headlines:**
1. Kids Indoor Play — Orlando
2. Bounce Houses + Party Rooms
3. Buy One Get One — Weekdays
4. Kids Ages 3–12
5. Toddler Thursday Every Week
6. Book Online — Fast & Easy
7. [Location] — Open Now

**Descriptions:**
1. Bounce houses, climbing walls & obstacle courses for kids 3–12. BOGO weekdays. Book your visit online.
2. [Location]'s go-to kids' play venue. Party rooms still available. Weekday BOGO deal running now.

---

### STEP 4.4 — Campaign 3: Competitor

**Keywords:**
- `chuck e cheese orlando`
- `urban air orlando`
- `sky zone orlando`
- `indoor play near me`
- `alternative to chuck e cheese`

**RSA Headlines:**
1. More Bounce. Less Noise.
2. Try Monkey Joe's Instead
3. BOGO Every Weekday
4. Kids Go Absolutely Wild
5. Simpler. More Fun. Less $$$
6. Pure Bounce House Energy 🐒

**Descriptions:**
1. Skip the tokens. Monkey Joe's: pure bounce house fun for kids 3–12. BOGO weekdays at both Orlando locations.
2. Kids love it. Parents love the BOGO deal. Weekday buy one get one at Monkey Joe's [Location].

---

### STEP 4.5 — Campaign 4: Display Remarketing

**Audience:** GA4 website visitors (30 days) — served across Google Display Network
**Budget:** $125/month per location
**Creative:** Static banner ads — same offer messaging as Facebook

---

## PHASE 5: Landing Pages (Brief to William — Days 3–5)

### STEP 5.1 — BOGO Landing Page: Pointe Orlando

**Deliverable to William:**
- Headline: "Buy One Kid In, Get One FREE"
- Subhead: "Weekday BOGO at Monkey Joe's Pointe Orlando — ages 3–12"
- Body:
  > Wacky Wednesdays — it's been running for 21 years for a reason. Bring two kids, pay for one. Any weekday at our Pointe Orlando location.
  >
  > ✅ Ages 3–12  ✅ Weekdays only (Mon–Fri)  ✅ One use per family  ✅ Florida residents only
- CTA: "Claim Your Free Admission →"
- Below CTA: Fine print text
- Install: GTM container ID (one snippet) — covers GA4 + Pixel automatically
- Design: On-brand (Monkey Joe's colors, font, monkey logo). Mobile-first. No site navigation. One offer, one button.

---

### STEP 5.2 — BOGO Landing Page: Winter Park

Same structure. Change location name, remove Florida resident restriction from fine print. Separate Aloovy promo code (`WACKY-WP`).

---

### STEP 5.3 — Frequent Jumper Card Landing Page

- Headline: "Come Back Any Time. 10 Jumps for $120."
- Subhead: "The Monkey Joe's Frequent Jumper Card — your digital pass to unlimited fun"
- Value prop section:
  > Your kids want to go back. You know it.
  >
  > 10 admissions. $120. $12 a visit, any day.
  >
  > Digital card → scan at door → visit counted. No fuss.
- CTA: "Get My Frequent Jumper Card — $120 →"
- No Florida resident restriction needed (loyalty product, not acquisition)

---

### STEP 5.4 — Constant Contact Opt-In Landing Page

Built inside Constant Contact (no William needed):
- Headline: "Get the Best Monkey Joe's Deals Straight to Your Inbox"
- Fields: First name + Email
- CTA: "Send Me the Deals"
- Post-submit: "You're in! Check your inbox for your first exclusive deal."
- Embed FB Pixel + GA4 snippet manually in CC page HTML

---

## PHASE 6: Google My Business (Days 1–4, parallel)

> **Prerequisite:** GBP access from corporate (Michael to chase)

### STEP 6.1 — Profile Audit Both Locations

- Photos: last updated? (replace with media shoot assets)
- Reviews: quantity, recency, response rate
- Business hours, description, categories — all accurate?
- Posts section: when was last post? (should be weekly)
- Q&A section: any unanswered questions?

---

### STEP 6.2 — Photo Refresh

As soon as media shoot reels arrive (~March 28):
- Extract stills from reels for GBP photos
- Upload 10–15 new photos per location
- Cover photo: best "kids going wild in bounce house" image
- Remove any dark/blurry/outdated photos

---

### STEP 6.3 — Weekly GBP Posts

Post every Tuesday (same time as email sends):
- Same content as Wacky Wednesday email — short, visual, CTA to landing page
- GBP posts are indexed in Google → free local search visibility
- Tag posts with offer details (Google sometimes displays in search results)

---

## PHASE 7: Reporting Dashboard (Days 5–8)

### STEP 7.1 — Google Looker Studio Setup

1. studio.google.com → Blank Report
2. Connect data sources:
   - Google Analytics (GA4)
   - Facebook Ads (use third-party connector: Supermetrics or Porter Metrics — free tier available)
   - Google Ads (native connector)
3. Build pages:
   - Page 1: Executive summary (top KPIs)
   - Page 2: Pointe Orlando (all channels)
   - Page 3: Winter Park (all channels)
   - Page 4: Email (Constant Contact — manual export weekly if no connector)

**Key metrics per page:**
- Ad spend vs revenue (if Aloovy purchase events fire)
- Cost per click, cost per conversion
- Email: open rate, click rate, unsubscribes
- BOGO codes redeemed (from Aloovy report)
- Phone calls (from CallRail if set up)

---

### STEP 7.2 — Share Dashboard with Michael

1. Publish dashboard → share link with Michael (View access)
2. He can check live results any time
3. Brief him on how to read it in the first weekly report

---

### STEP 7.3 — Weekly Report Format

Send every Monday via email:

**Template:**
```
Subject: Monkey Joe's Weekly Report — Week of [Date]

Hi Michael,

Here's your weekly snapshot:

📊 AD SPEND THIS WEEK
- Pointe Orlando: $XXX spent → X clicks, X conversions
- Winter Park: $XXX spent → X clicks, X conversions

📧 EMAIL
- Campaigns sent: X  |  Open rate: X%  |  Clicks: X

🛒 ONLINE STORE (Aloovy)
- BOGO codes redeemed: X
- Frequent Jumper Cards sold: X

🏆 WIN OF THE WEEK
[One specific result or insight]

📋 NEXT WEEK PLAN
[One action we're taking based on this week's data]

See the full dashboard here: [link]

Jess
```

---

## FULL LAUNCH CHECKLIST (April 1 Target)

### Infrastructure
- [ ] GTM installed on WordPress and firing
- [ ] FB Pixel base code live on WordPress + William's landing pages
- [ ] GA4 property created, tag firing via GTM
- [ ] Second Meta Ad Account created (Winter Park)
- [ ] Both ad accounts have Pixel assigned

### Accounts
- [ ] Constant Contact access confirmed (both accounts)
- [ ] Which CC account = which location confirmed
- [ ] Google Ads access confirmed
- [ ] GBP access confirmed (both locations)
- [ ] Aloovy promo codes created and tested

### Landing Pages
- [ ] BOGO Pointe Orlando page live + GTM installed + Pixel firing
- [ ] BOGO Winter Park page live + GTM installed + Pixel firing
- [ ] Frequent Jumper Card page live + Pixel firing
- [ ] CC opt-in landing page live + manual Pixel embed confirmed

### Email
- [ ] Waiver database imported (both locations)
- [ ] Segments created (active / warm / dormant / birthday-soon)
- [ ] Automation 1 (Birthday Reactivation) built + tested
- [ ] Automation 2 (Post-Purchase Welcome) built + tested
- [ ] Automation 3 (New Opt-In Welcome) built + tested
- [ ] Automation 4 (Dormant Re-engagement) sent + suppressions applied
- [ ] Weekly campaign calendar scheduled

### Ads
- [ ] Facebook: BOGO campaign live (Pointe Orlando)
- [ ] Facebook: BOGO campaign live (Winter Park)
- [ ] Facebook: Retargeting campaign live (Frequent Jumper Card)
- [ ] Facebook: Toddler Thursday ad live
- [ ] Google: Brand campaign live (both locations)
- [ ] Google: Category campaign live (both locations)

### Copy & Approvals
- [ ] Michael has reviewed and approved all ad copy
- [ ] Michael has reviewed and approved all email copy
- [ ] Michael has reviewed and approved both landing pages
- [ ] Fine print correct on all Pointe Orlando materials (FL residents only)

### Reporting
- [ ] Looker Studio dashboard live
- [ ] Michael has View access to dashboard
- [ ] Weekly report template ready
- [ ] Review meeting booked: May 3–5

---

## Files in This Project

| File | Purpose |
|------|---------|
| `plans/2026-03-20-monkey-joes-two-offers-strategy.md` | Offer structures and funnel logic |
| `plans/2026-03-20-monkey-joes-full-project-plan.md` | Phase overview |
| `plans/2026-03-20-monkey-joes-tracking-infrastructure.md` | GTM/GA4/Pixel setup |
| `plans/2026-03-20-monkey-joes-complete-funnel.md` | All copy written out |
| `plans/2026-03-20-monkey-joes-funnel-build-stepbystep.md` | This file — the build order |
| `outputs/monkey-joes/logins.md` | All credentials |
| `outputs/monkey-joes/competitor-research.md` | Competitor intel |

---

## Notes & Clever Marketing Angles to Bake In

1. **"21 years of Wacky Wednesdays"** — this is a story. Use it. Competitors can't say they've been doing BOGO for 21 years. Lead with it in ad copy.

2. **Michael as the owner** — in Phase 2, a 30-second "meet your host" video from Michael is worth 100 polished brand ads. Real people, real story.

3. **The Jumper Card as identity** — position it not just as a product but as joining something. "Monkey Joe's regulars." Make people feel like they're in a club.

4. **Toddler Thursday as a cult classic** — it's already beloved. Make it feel like an event, not just a discount. "Toddler Thursday is kind of a big deal" gives it personality.

5. **The waiver database is gold** — 36K families who've already been through the door. They don't need convincing Monkey Joe's is good. They just need reminding it exists. Re-engagement cost per conversion will be a fraction of cold traffic.

6. **Phase 2 pitch to Michael (May review):** Once summer hits — propose the "Summer Jumper Pass" (unlimited weekday visits, $79/child). Urban Air proved the pass model works. Monkey Joe's can do it better locally.

7. **The franchise play:** Document everything beautifully. Every report, every result, every creative. This is the pitch deck for 130 locations.
