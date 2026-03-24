# Plan: Monkey Joe's — Complete Marketing Funnel (Messaging, Emails, Ads, Automations)

**Created:** 2026-03-20
**Status:** Draft
**Request:** Build the entire Monkey Joe's marketing funnel end-to-end — ad copy, email copy, automations, offer messaging, landing page content — ready to implement as soon as tracking and account access is confirmed.

---

## Overview

### What This Plan Accomplishes

Every piece of copy, every email, every automation sequence, and every ad for the Monkey Joe's 90-day pilot — written and ready to deploy. This is the complete operating manual for the funnel: two offers, two locations, four email sequences, Facebook ads, Google ads, and a competitor-informed creative strategy.

### Why This Matters

We have WordPress access, Facebook Pixel access, and a clear funnel structure. The only blockers are GA4 setup and Constant Contact authorization. This document means the moment those are resolved, implementation is same-day. No waiting. No "let me draft that" — it's already done.

---

## Ad Account Structure Decision

**Answer: Separate Meta ad accounts per location.**

| Structure | Pointe Orlando | Winter Park |
|-----------|---------------|-------------|
| Meta Business Manager | Shared (one) | Shared (one) |
| Ad Account | Separate | Separate |
| Facebook Pixel | Shared (one pixel, two events) | Shared |
| Budget tracking | Independent | Independent |
| Reporting | Per location | Per location |

**Why separate accounts:**
- Pointe Orlando has Florida resident restriction — different ad rules
- Different audience types (Pointe Orlando = tourist area, Winter Park = local families)
- Separate budgets: $750/month each (from $1,500/month total ad spend)
- Clean per-location reporting for Michael and corporate
- Easy to scale: when other locations come on, the model is already set

**Action needed:** In Meta Business Manager, create a second Ad Account named "Monkey Joe's Winter Park." The Pointe Orlando account already exists. Both sit under the same Business Manager.

---

## Current State

### Existing Plans (already created today)
- `plans/2026-03-20-monkey-joes-two-offers-strategy.md` — Offer structures
- `plans/2026-03-20-monkey-joes-full-project-plan.md` — Phase overview
- `plans/2026-03-20-monkey-joes-tracking-infrastructure.md` — GTM/GA4/Pixel setup
- `outputs/monkey-joes/logins.md` — Account credentials

### Gaps Being Addressed
- No written copy exists for any email, ad, or landing page
- No automation sequences defined
- No Constant Contact strategy mapped
- No Google ad copy written
- No Facebook ad copy written

---

## The Complete Funnel Map

```
COLD TRAFFIC FUNNEL
──────────────────
[FB/Google Ad]
    ↓
[Location-specific Landing Page: BOGO Offer]
    ↓
[Aloovy Checkout + Promo Code]
    ↓
[Confirmation Page]
    ↓
[Email: Welcome + How to Redeem] ← Constant Contact automation
    ↓
[VISIT: Family redeems BOGO at venue]
    ↓
[Day 1 Post-Visit SMS + Email: Frequent Jumper Card upsell]
    ↓
[Day 7 No Return: Re-engagement email]
    ↓
[Ongoing: Weekly campaigns (Wacky Wednesday, Toddler Thursday)]

BIRTHDAY REACTIVATION FUNNEL
─────────────────────────────
[Waiver database: 36K contacts with birthday data]
    ↓
[90-day trigger: "A birthday is coming!"]
    ↓
[45-day trigger: "Only 45 days — book now"]
    ↓
[Post-birthday: "Hope they had a blast — here's what's next"]

LEAD CAPTURE FUNNEL (Constant Contact Landing Page)
────────────────────────────────────────────────────
[FB Ad: Awareness / Value content]
    ↓
[CC Landing Page: "Get our weekly deals" opt-in]
    ↓
[Welcome sequence: 3 emails over 7 days]
    ↓
[Weekly campaign list: ongoing sends]
```

---

## SECTION 1: THE TWO OFFERS (Final Confirmed Structure)

### Offer 1: BOGO Weekday Admission

**Full name:** "Wacky Wednesday BOGO — Buy One Get One Free Admission"
**Valid:** Weekdays only (Monday–Friday)
**Who:** Kids ages 3–12
**Where:** Both locations (separate landing pages)
**Mechanic:** Promo code applied at Aloovy checkout — one use per family
**Weekend upgrade:** +$10 at checkout for full weekend validity
**Fine print (Pointe Orlando only):** "Valid for Florida residents only. Not valid with any other offer. One use per family."
**Fine print (Winter Park):** "Valid weekdays only. Not valid with any other offer. One use per family."

**A/B Test:**
- Variant A: "Buy One Get One Free" framing
- Variant B: "50% Off All Kids Admissions" framing
(Same value. Test which converts better. Run both for 2 weeks, keep winner.)

---

### Offer 2: Frequent Jumper Card (Digital Loyalty)

**Full name:** "Frequent Jumper Card — 10 Jumps for $120"
**Value:** 10 admissions × $12 each = $120 (standard price, pre-paid convenience)
**Mechanic:** Digital card — QR code on phone, scanned at venue, auto-decrements
**Where sold:** Online via Aloovy (William to set up)
**Position in funnel:** Post-visit upsell ONLY — not a cold offer
**Commission:** Jess + William earn commission on every card sold online (confirm % with Michael)

---

## SECTION 2: EMAIL COPY (Constant Contact)

> **Tone guide:** Warm, fun, parent-friendly. Think "cool mum who also knows a deal." Not corporate. Short sentences. Emoji used sparingly. Subject lines: 6 words or fewer. Always mobile-first.

---

### EMAIL SEQUENCE A: Birthday Reactivation (from waiver database)

**Trigger:** Child's birthday in waiver database
**Send 1:** 90 days before birthday
**Send 2:** 45 days before birthday
**Send 3:** 7 days after birthday

---

#### A1: 90-Day Birthday Email

**Subject:** 🎉 A birthday's coming up...
**Preview text:** We've got the perfect plan.

**Body:**

> Hi [Parent First Name],
>
> Psst — we heard someone special has a birthday coming up in about 3 months.
>
> Whether you're planning a full party or just want to make the day extra fun, Monkey Joe's has you covered. We've been creating birthday memories in [Location] for over 20 years.
>
> **Here's what we do best:**
> - Party rooms (we have [4 at Pointe Orlando / 3 at Winter Park] — they book fast)
> - Unlimited bouncing, climbing, and sliding
> - A venue that handles the chaos so you don't have to
>
> **Start planning now → [Book a Party Room]**
>
> Or just want a fun day out? Our BOGO weekday deal means one kid gets in free. [Grab your spot here.]
>
> See you soon,
> The Monkey Joe's Team 🐒
>
> _Monkey Joe's [Location] | [Address]_

---

#### A2: 45-Day Birthday Email

**Subject:** Only 45 days — party rooms filling up
**Preview text:** Don't wait on this one.

**Body:**

> Hi [Parent First Name],
>
> The big day is 45 days away — and our party rooms are filling up fast.
>
> If a Monkey Joe's birthday party is on the cards, now's the time to lock it in. Kids go absolutely wild here (in the best way). You show up, we handle everything else.
>
> **🎂 Book your party room before it's gone → [Book Now]**
>
> Not doing a party this year? No worries — just bring them in for a bounce. Use our weekday BOGO deal and one kid gets in free.
>
> **→ [Grab the BOGO deal]**
>
> Either way, let's make it a birthday they talk about for months.
>
> See you soon,
> Monkey Joe's 🐒

---

#### A3: Post-Birthday Email (7 days after birthday)

**Subject:** Hope it was amazing 🎉
**Preview text:** Already planning the next one?

**Body:**

> Hi [Parent First Name],
>
> Hope the birthday celebrations were everything they dreamed of!
>
> If you came to see us — thank you. You're why we do this.
>
> If life got busy and you didn't make it in — no stress. We're here whenever you're ready.
>
> **Want to make it a regular thing?**
> Our Frequent Jumper Card gets you 10 admissions for $120 — that's $12 a visit, any day, any time.
>
> Perfect for the kids who can't get enough. 👇
>
> **→ [Get Your Frequent Jumper Card]**
>
> See you soon,
> Monkey Joe's 🐒

---

### EMAIL SEQUENCE B: Post-Purchase / Post-Visit (triggered from Aloovy)

**Trigger:** BOGO purchase confirmed in Aloovy
**Send 1:** Immediately post-purchase (confirmation + how to redeem)
**Send 2:** Day 1 after visit (Jumper Card upsell)
**Send 3:** Day 7 if no return visit

---

#### B1: Purchase Confirmation Email

**Subject:** You're in! Here's your free admission 🐒
**Preview text:** Save this — you'll need it at the door.

**Body:**

> Hi [First Name],
>
> You're all set! Here's everything you need for your visit.
>
> **Your BOGO Code:** `[PROMO CODE]`
>
> **How to use it:**
> 1. Head to Monkey Joe's [Location] on any weekday
> 2. Show this email (or your confirmation) at the door
> 3. One kid gets in free — it's that easy
>
> **📍 Find us:**
> Monkey Joe's [Location]
> [Address]
> [Hours: Mon–Fri X–Xpm, Weekends X–Xpm]
>
> **A few things to know:**
> - Valid weekdays only (Mon–Fri)
> - One use per family
> - Socks required — grab a pair at the door if you forget
> [Pointe Orlando only]: Valid for Florida residents only
>
> Questions? Call us: [Phone Number]
>
> Can't wait to see you,
> Monkey Joe's 🐒

---

#### B2: Post-Visit Day 1 Email (Frequent Jumper Card Upsell)

**Subject:** How was it? (and here's a little something...)
**Preview text:** For the kids who want to go back. Immediately.

**Body:**

> Hi [First Name],
>
> Hope the kids had an absolute blast yesterday!
>
> If the car ride home was full of "Can we go again??" — we have the perfect answer.
>
> **The Frequent Jumper Card.**
> 10 admissions for $120. That's $12 a jump, any day you want.
>
> No booking required. Just scan and bounce.
>
> **→ [Get Your Frequent Jumper Card — $120]**
>
> It's the move for families who just... get it. 🐒
>
> See you again soon,
> Monkey Joe's

---

#### B3: Day 7 No-Return Email

**Subject:** Miss you already 👀
**Preview text:** Come back this week — bring a friend.

**Body:**

> Hi [First Name],
>
> It's been a week since your last visit — the bounce houses are asking for you.
>
> If you're ready to come back, don't forget: **Wacky Wednesdays are BOGO every week.** Bring a friend and one gets in free.
>
> And if you want unlimited access? The Frequent Jumper Card gives you 10 visits for $120.
>
> **→ [Grab the Wednesday BOGO]**
> **→ [Get the Frequent Jumper Card]**
>
> See you soon,
> Monkey Joe's 🐒

---

### EMAIL SEQUENCE C: Welcome Series (new opt-ins from CC landing page)

**Trigger:** Someone opts in via Constant Contact landing page
**Send 1:** Immediately (welcome + best offer)
**Send 2:** Day 3 (story/social proof)
**Send 3:** Day 7 (Toddler Thursday feature)

---

#### C1: Welcome Email

**Subject:** Welcome to the Monkey Joe's fam 🐒
**Preview text:** Here's your first deal, on us.

**Body:**

> Hi [First Name],
>
> Welcome! You've officially joined the inner circle of parents who know the secret to a great day out.
>
> Here's your welcome gift:
>
> **This week: Buy One Get One Free admission on any weekday.**
> Use code `WELCOME` at checkout.
>
> **→ [Claim Your Free Admission]**
>
> We'll also be sending you our weekly deals — Wacky Wednesdays, Toddler Thursdays, and whatever else we've got cooking.
>
> Fair warning: the kids are going to love you for this.
>
> See you soon,
> Monkey Joe's 🐒

---

#### C2: Day 3 — Story Email

**Subject:** 20+ years of birthday memories
**Preview text:** And we're just getting started.

**Body:**

> Hi [First Name],
>
> Fun fact: Monkey Joe's [Location] has been making kids' birthday dreams come true for over 20 years.
>
> We've had families come back year after year — same kids, growing up, eventually bringing their own kids. (Yep. We have second-generation Monkey Joe's fans.)
>
> What keeps them coming back?
> - The bouncing (obviously)
> - The climbing walls, slides, and obstacle courses
> - Party rooms that take the stress out of birthdays completely
> - A place where kids just... run free
>
> **Have a birthday coming up? Book a party room now → [Book Here]**
>
> Or just swing by on a weekday and try the BOGO deal. First visit's basically on us.
>
> **→ [Get Your BOGO Admission]**
>
> See you soon,
> Monkey Joe's 🐒

---

#### C3: Day 7 — Toddler Thursday Feature

**Subject:** Toddler Thursday is kind of a big deal
**Preview text:** Designed for the little ones (and tired parents).

**Body:**

> Hi [First Name],
>
> If you've got a little one under 5, Thursday is your day.
>
> **Toddler Thursday at Monkey Joe's** is built for the small but mighty — smaller crowds, the perfect pace, and all the bounce house joy without the chaos of a busy weekend.
>
> Parents love it. Toddlers go absolutely feral (in the best way).
>
> **→ [See This Week's Toddler Thursday Details]**
>
> And don't forget your weekday BOGO — it works on Thursdays too.
>
> See you Thursday,
> Monkey Joe's 🐒

---

### EMAIL SEQUENCE D: Dormant Re-engagement Campaign

**Target:** Contacts with zero opens in 6+ months
**Goal:** Re-engage or remove from list (clean list = better deliverability)
**Send 1:** Re-engagement offer
**Send 2:** 3 days later (non-openers): last chance
**Send 3:** Remove non-openers from active list (suppress)

---

#### D1: Re-engagement

**Subject:** It's been a while... 👀
**Preview text:** We've got something for you.

**Body:**

> Hi [First Name],
>
> We noticed it's been a while since we've seen you.
>
> We get it — life gets busy. Kids get busy. Parents definitely get busy.
>
> But we wanted to pop in with something to make it easy to come back:
>
> **One free admission — on us.**
> Use code `COMEBACK` at checkout. Valid weekdays only.
>
> **→ [Claim Your Free Admission]**
>
> No strings. Just bouncing. 🐒
>
> Hope to see you soon,
> Monkey Joe's

---

#### D2: Last Chance

**Subject:** Last one, we promise 🙏
**Preview text:** Free admission expires soon.

**Body:**

> Hi [First Name],
>
> This is the last email we'll send about your free admission offer.
>
> If bouncing around Monkey Joe's sounds fun, claim it now — code `COMEBACK`, weekdays only.
>
> **→ [Use My Free Admission]**
>
> If you'd rather we stop sending emails, no hard feelings — just unsubscribe below. We'll part as friends.
>
> Either way,
> Monkey Joe's 🐒

---

### WEEKLY CAMPAIGN TEMPLATES

**Cadence:** 2–3 per week
**Format:** Short subject, one image, one offer, one CTA

---

#### Weekly Template: Wacky Wednesday (send Tuesday evening)

**Subject:** Wednesday = BOGO 🐒 (as always)
**Preview text:** Buy one admission, get one free. Every Wednesday.

**Body:**
> Happy almost-Wednesday, [First Name]!
>
> Same deal as always — come in Wednesday and one kid bounces free. No code needed, just show up.
>
> **📍 [Location] | [Hours]**
>
> → [See Daily Specials] → [Book a Party Room]

---

#### Weekly Template: Toddler Thursday (send Wednesday evening)

**Subject:** Tomorrow: Toddler Thursday 🐒
**Preview text:** Perfect for the under-5 crowd.

**Body:**
> Tomorrow's Toddler Thursday at Monkey Joe's [Location].
>
> Little ones, big fun, relaxed vibe. Exactly what Thursday should be.
>
> **→ [See Details + Hours]**
>
> P.S. BOGO deal works tomorrow too — one gets in free on any weekday.

---

#### Weekly Template: Weekend Hype (send Friday morning)

**Subject:** Weekend plans sorted ✅
**Preview text:** Bounce houses, party rooms, and zero screen time.

**Body:**
> Hi [First Name],
>
> Looking for something to do with the kids this weekend?
>
> Monkey Joe's [Location] is open [Sat–Sun, Hours]. Party rooms available for walk-ins or advance booking.
>
> **→ [See This Weekend's Hours]**
> **→ [Book a Party Room]**

---

## SECTION 3: FACEBOOK AD COPY

> **Targeting notes:**
> - Pointe Orlando: Parents 25–45 within 10 miles. Interest: family activities, kids entertainment, birthday parties, Florida theme parks. Exclude tourists (target "local awareness" not "travel")
> - Winter Park: Parents 25–45 within 10 miles. Interest: local family activities, kids sports, parenting.
> - Both: Retargeting audiences from website visitors (Pixel required) + email list uploads

---

### FB AD SET 1: BOGO Offer — Cold Audience

**Campaign objective:** Conversions (Aloovy purchase)
**A/B test:** Run Variant A and Variant B simultaneously for 14 days

---

#### Variant A: BOGO Framing

**Primary text:**
> Wednesday just became the best day of the week.
>
> Monkey Joe's Wacky Wednesday: Buy one kid's admission, get one FREE. Every single Wednesday.
>
> Ages 3–12. Bounce houses, climbing walls, slides — the works.
>
> [Pointe Orlando: Florida residents only. Not valid with other offers.]
>
> 👉 Grab your spot before it fills up.

**Headline:** Buy One, Get One Free — Wednesdays Only

**Description:** Kids ages 3–12. Weekday deal. Book online now.

**CTA button:** Book Now

**Creative direction:** Video or carousel. Opening frame: kid launching into bounce house, huge smile. Text overlay: "BOGO WEDNESDAY 🐒". Use media shoot reels.

---

#### Variant B: 50% Off Framing

**Primary text:**
> Half price kids' admission — weekdays all week.
>
> 50% off for kids ages 3–12, Monday through Friday at Monkey Joe's [Location].
>
> Bounce houses. Climbing walls. Obstacle courses. And one happy parent.
>
> [Pointe Orlando: Florida residents only.]
>
> 👉 Book your weekday visit now — limited spots.

**Headline:** 50% Off Kids Admission — This Week

**Description:** Ages 3–12. Weekdays only. Grab your deal online.

**CTA button:** Get Offer

---

### FB AD SET 2: Birthday Party — Cold Audience

**Campaign objective:** Traffic / Lead generation

**Primary text:**
> Planning a birthday party that the kids actually talk about?
>
> Monkey Joe's [Location] has [4/3] party rooms, unlimited bouncing, and 20+ years of making birthday dreams happen.
>
> You show up. We handle everything else.
>
> 🎂 Party rooms book fast — especially on weekends.
>
> 👉 Check availability now.

**Headline:** Book a Birthday Party at Monkey Joe's

**Description:** Party rooms available. Book yours before it's gone.

**CTA button:** Book Now

---

### FB AD SET 3: Frequent Jumper Card — Retargeting (post-visit)

**Audience:** Custom audience — Aloovy purchasers (pixel event) + email list (BOGO buyers)
**Campaign objective:** Conversions

**Primary text:**
> If your kids said "Can we go again?" after their last visit — this one's for you.
>
> The Monkey Joe's Frequent Jumper Card.
> 10 admissions for $120. That's $12 a visit, any day you want.
>
> No booking needed. Just scan and bounce.
>
> 👇 Get yours online now.

**Headline:** 10 Visits for $120 — Frequent Jumper Card

**Description:** The smartest thing you'll buy this month.

**CTA button:** Shop Now

---

### FB AD SET 4: Awareness / Toddler Thursday — Cold Audience

**Primary text:**
> Toddler mums — this one's for you.
>
> Every Thursday at Monkey Joe's [Location]: smaller crowds, the perfect pace, and bounce houses designed for the little ones.
>
> Kids under 5 absolutely THRIVE here. And it's BOGO on weekdays — so one gets in free.
>
> 👉 See this Thursday's details.

**Headline:** Toddler Thursday at Monkey Joe's

**Description:** Perfect for little ones. Weekday BOGO included.

**CTA button:** Learn More

---

### FB AD CREATIVE BRIEF (for media shoot reels)

You have 15 reels incoming from the media shoot. Here's how to use them:

| Reel Type | Best Ad Set | Opening Hook |
|-----------|------------|-------------|
| Kid launching into bounce house | BOGO cold | "Watch this." |
| Group of kids on obstacle course | Birthday party | "What a birthday looks like." |
| Parent + toddler in bounce area | Toddler Thursday | "This is why we love Thursdays." |
| Party room setup / birthday cake | Birthday party | "No stress. Just celebrate." |
| Kid sliding / huge smile closeup | Retargeting | "They want to go back. You know it." |

**Hook rule:** First 3 seconds must stop the scroll. Kid laughing or doing something wild = best hook for this audience.

---

## SECTION 4: GOOGLE ADS COPY

### Campaign 1: Brand

**Ad Group: Brand Keywords**
Keywords: monkey joes orlando, monkey joes winter park, monkey joes pointe orlando, monkey joes birthday party

**RSA Headline options (30 chars each):**
1. Monkey Joe's Orlando
2. Book Online Today
3. Party Rooms Available Now
4. BOGO Wednesdays — Book Now
5. Kids 3–12 Love It Here
6. Weekday Deals Available

**Description options (90 chars each):**
1. Bounce houses, climbing walls & party rooms. BOGO weekday deal. Book online now.
2. Orlando's favourite kids' play venue. Party rooms available. Check availability now.

---

### Campaign 2: Category (non-brand)

**Ad Group: Kids Play Place**
Keywords: kids play place orlando, indoor play centre orlando, kids activities orlando, kids birthday party venue orlando, bounce house orlando

**RSA Headlines:**
1. Kids Indoor Play — Orlando
2. Bounce Houses + Party Rooms
3. Buy One Get One — Weekdays
4. Kids Ages 3–12
5. Book Online Today
6. 20 Years of Birthday Fun
7. Weekday BOGO Admission Deal

**Descriptions:**
1. Bounce houses, climbing walls & slides for kids 3–12. BOGO weekdays. Book your visit now.
2. Party rooms, obstacle courses & unlimited fun. Orlando's go-to kids' play venue. Book now.

---

### Campaign 3: Competitor

**Ad Group: Competitor Keywords**
Keywords: chuck e cheese orlando, indoor play place near me, kids entertainment orlando, alternatives to chuck e cheese

**RSA Headlines:**
1. More Bounce. Less Noise.
2. Monkey Joe's — Try It Today
3. BOGO Weekday Deal On Now
4. Kids 3–12 Go Absolutely Wild
5. Party Rooms Still Available
6. Book Online — Easy + Fast

**Descriptions:**
1. Skip the tokens and queues. Monkey Joe's: pure bounce house fun for kids 3–12. BOGO weekdays.
2. Kids love the bounce houses. Parents love the price. BOGO weekdays at Monkey Joe's Orlando.

---

## SECTION 5: LANDING PAGE CONTENT BRIEFS

### Landing Page 1: BOGO — Pointe Orlando

**URL:** (William to set — e.g., offers.monkeyjoes.com/bogo-orlando)
**Headline:** Buy One Kid In, Get One FREE
**Subhead:** Weekday BOGO at Monkey Joe's Pointe Orlando — ages 3–12
**Body (short):**
> Wacky Wednesdays just got even better. Bring two kids, pay for one. Valid any weekday at our Pointe Orlando location.
>
> ✅ Ages 3–12
> ✅ Weekdays only (Mon–Fri)
> ✅ One use per family
> ✅ Florida residents only

**CTA:** Claim Your Free Admission →
**Destination:** Aloovy Pointe Orlando checkout with promo code pre-filled
**Fine print:** "Valid weekdays only. For Florida residents only. Not valid with any other offer. One use per family."
**Tracking:** GTM (GA4 ViewContent + FB Pixel ViewContent on page load)
**Pixel event on CTA click:** InitiateCheckout

---

### Landing Page 2: BOGO — Winter Park

**URL:** (William to set — e.g., offers.monkeyjoes.com/bogo-winterpark)
**Headline:** Buy One Kid In, Get One FREE
**Subhead:** Weekday BOGO at Monkey Joe's Winter Park — ages 3–12
**Body:**
> Same deal. Different location. Monkey Joe's Winter Park — bring two kids, pay for one on any weekday.
>
> ✅ Ages 3–12
> ✅ Weekdays only (Mon–Fri)
> ✅ One use per family

**CTA:** Claim Your Free Admission →
**Fine print:** "Valid weekdays only. Not valid with any other offer. One use per family."

---

### Landing Page 3: Frequent Jumper Card

**URL:** (e.g., offers.monkeyjoes.com/jumper-card)
**Headline:** Come Back Any Time. 10 Jumps for $120.
**Subhead:** The Monkey Joe's Frequent Jumper Card — your digital pass to unlimited fun
**Body:**
> Your kids want to go back. You know it.
>
> The Frequent Jumper Card gives you 10 admissions for $120 — that's $12 a visit, any day, any time.
>
> **How it works:**
> 1. Buy online — takes 2 minutes
> 2. Get your digital card (QR code on your phone)
> 3. Scan at the door — we handle the rest
> 4. 10 visits. Use them whenever. They won't expire.
>
> **The maths:**
> Standard admission: [price]
> Jumper Card: $12/visit ✅
> Worth it: obviously.

**CTA:** Get My Frequent Jumper Card — $120 →
**Destination:** Aloovy product page for Jumper Card
**Pixel event on CTA click:** InitiateCheckout

---

### Constant Contact Landing Page: Email Opt-In

**Purpose:** Lead capture from awareness ads — NOT a conversion page
**Headline:** Get the Best Monkey Joe's Deals Straight to Your Inbox
**Subhead:** Weekly specials, BOGO alerts, and Toddler Thursday reminders — free.
**Form fields:** First name, Email address
**CTA button:** Send Me the Deals
**Post-submit:** "You're in! Check your inbox for your welcome deal."
**Pixel event:** Lead (FB) + generate_lead (GA4)

---

## SECTION 6: AUTOMATION SETUP (Constant Contact)

### Automation 1: Birthday Reactivation

**Trigger:** Contact has a birthday date within the next 90 days (from waiver database upload)
**Entry:** Rolling — contacts enter continuously as their 90-day window opens

| Step | Delay | Email | Notes |
|------|-------|-------|-------|
| 1 | Immediately at 90-day mark | A1: "A birthday's coming up" | Book a party or BOGO |
| 2 | 45 days later | A2: "Only 45 days — party rooms filling up" | Urgency |
| 3 | Birthday +7 days | A3: "Hope it was amazing" | Jumper Card upsell |

**Segment:** Contacts with birthday field populated. Exclude anyone who has booked a party in last 30 days (if Aloovy data is available).

---

### Automation 2: Post-Purchase Welcome

**Trigger:** New contact added to "BOGO Purchasers" list (manual upload from Aloovy weekly, or Zapier if available)
**Entry:** One-time per contact

| Step | Delay | Email |
|------|-------|-------|
| 1 | Immediately | B1: Confirmation + promo code |
| 2 | 24–48 hrs post-expected visit | B2: Day 1 post-visit upsell |
| 3 | 7 days post-purchase | B3: Day 7 re-engagement |

**Note on trigger:** Until Zapier/API is set up between Aloovy and Constant Contact, export Aloovy purchasers weekly and import to CC manually. Tag with "BOGO-Purchaser-[Date]".

---

### Automation 3: New Opt-In Welcome Series

**Trigger:** New subscriber via Constant Contact opt-in form

| Step | Delay | Email |
|------|-------|-------|
| 1 | Immediately | C1: Welcome + `WELCOME` promo code |
| 2 | Day 3 | C2: 20 years of birthday memories |
| 3 | Day 7 | C3: Toddler Thursday feature |
| 4 | Day 10 | → Move to weekly campaign list |

---

### Automation 4: Dormant Re-engagement

**Trigger:** Manual — run this campaign against the dormant segment (no opens in 6+ months)
**Run once:** Before main campaign launches to clean the list

| Step | Delay | Email |
|------|-------|-------|
| 1 | Day 1 | D1: "It's been a while" + `COMEBACK` code |
| 2 | Day 3 (non-openers only) | D2: "Last one, we promise" |
| 3 | Day 5 | Remove non-openers from active list |

---

### Weekly Campaign Schedule (ongoing from April 1)

| Day | Time | Campaign | Segment |
|-----|------|---------|---------|
| Tuesday | 6pm | Wacky Wednesday BOGO reminder | All active subscribers |
| Wednesday | 6pm | Toddler Thursday preview | Parents of under-5s (if segmented) / All |
| Friday | 9am | Weekend hype | All active subscribers |

---

## SECTION 7: PROMO CODES NEEDED FROM ALOOVY

Request William to create these codes in Aloovy before launch:

| Code | Offer | Restriction | Location |
|------|-------|-------------|---------|
| `WACKYWED-POL` | BOGO weekday | FL residents, 1x use | Pointe Orlando |
| `WACKYWED-WP` | BOGO weekday | 1x use | Winter Park |
| `WELCOME` | BOGO weekday | 1x use (new opt-ins) | Both |
| `COMEBACK` | BOGO weekday | 1x use (re-engagement) | Both |

**FB/Google ad tracking codes (UTM, not Aloovy):** Each campaign gets a unique UTM link — the promo code at Aloovy is separate from tracking.

---

## SECTION 8: UTM NAMING CONVENTION

All links in all ads and emails must include UTM parameters.

**Builder:** ga-dev-tools.google.com/campaign-url-builder

| Campaign | utm_source | utm_medium | utm_campaign | utm_content |
|----------|-----------|------------|-------------|------------|
| FB BOGO Variant A | facebook | cpc | bogo-weekday | variant-a |
| FB BOGO Variant B | facebook | cpc | bogo-weekday | variant-b |
| FB Birthday Party | facebook | cpc | birthday-party | — |
| FB Jumper Card | facebook | cpc | jumper-card | retargeting |
| Google Brand | google | cpc | brand | — |
| Google Category | google | cpc | category-kids-play | — |
| Email Birthday 90d | email | email | birthday-reactivation | 90day |
| Email Birthday 45d | email | email | birthday-reactivation | 45day |
| Email Welcome | email | email | welcome-series | day-1 |
| Email Wacky Wed | email | email | weekly-wacky-wednesday | — |
| SMS Jumper Card | sms | sms | jumper-card-upsell | — |

---

## Files to Create During Implementation

| File Path | Purpose |
|-----------|---------|
| `outputs/monkey-joes/email-copy.md` | All email copy (Sequences A, B, C, D + weekly templates) |
| `outputs/monkey-joes/ad-copy-facebook.md` | All FB ad copy with targeting notes |
| `outputs/monkey-joes/ad-copy-google.md` | All Google Ads copy (RSAs + descriptions) |
| `outputs/monkey-joes/landing-page-briefs.md` | 4 landing page briefs for William |
| `outputs/monkey-joes/automation-setup.md` | CC automation setup instructions |
| `outputs/monkey-joes/promo-codes.md` | Code list for William to set up in Aloovy |
| `outputs/monkey-joes/utm-guide.md` | UTM naming convention + link builder |
| `outputs/monkey-joes/competitor-research.md` | Competitor ad research (running in background) |

---

## Implementation Order (What to Do First)

### This Week (Before April 1)

**Day 1 (today):**
- [ ] Get Constant Contact authorization — email Michael/William requesting invite to both CC accounts
- [ ] Log into WordPress, check admin level, install GTM4WP plugin
- [ ] Create GTM account
- [ ] Create second Meta Ad Account for Winter Park
- [ ] Send William landing page briefs + GTM container ID

**Day 2:**
- [ ] Add GA4 as GTM tag (create GA4 property first)
- [ ] Add FB Pixel as GTM tag (you already have pixel access)
- [ ] Publish GTM container
- [ ] Verify Pixel firing with Pixel Helper
- [ ] Request Aloovy promo codes from William

**Day 3–5:**
- [ ] Set up Constant Contact automations (once access granted)
- [ ] Upload/segment waiver database lists in CC
- [ ] Build Facebook ad campaigns (both ad accounts)
- [ ] Build Google Ads campaigns
- [ ] Brief William on landing pages

**March 28:**
- [ ] Full tracking verification checklist
- [ ] All campaigns in draft/review state, ready to activate

**April 1:**
- [ ] Everything goes live

---

## Open Questions

1. **Constant Contact access:** When will Michael send the invite? This is blocking all email setup.
2. **Aloovy promo code support:** William to confirm before codes are listed in any emails or ads
3. **Aloovy confirmation page URL:** Needed to fire the Purchase conversion event
4. **Which CC account is which location?** mjstore135 vs mjstore137 — confirm with Michael
5. **Budget split:** $750/location/month confirmed? Or different split?
6. **CallRail:** In or out? Confirm budget with Michael (~$45/month)
7. **Landing page domain:** William's pages — subdomain of monkeyjoes.com or separate?

---

## Validation Checklist

- [ ] All email copy sequences written (A, B, C, D + weekly templates)
- [ ] All Facebook ad copy written with targeting notes
- [ ] All Google ad RSAs written
- [ ] All 4 landing page briefs complete and ready for William
- [ ] Promo code list sent to William
- [ ] UTM guide documented
- [ ] Automation triggers and sequences defined in detail
- [ ] Competitor research complete and incorporated into copy

---

## Success Criteria

1. Every piece of copy is written, approved, and ready to deploy — zero drafting needed at implementation time
2. William can take landing page briefs and build immediately with no back-and-forth
3. As soon as Constant Contact access is granted, automations can be built same day
4. Ad campaigns can go live the moment tracking is confirmed (April 1 target)
5. The full document is presentable to Michael for review and sign-off

---

## Notes

- **Tone check before sending anything to Michael:** copy should feel like a fun local business, not a corporate chain. If it sounds like a press release, rewrite it.
- **Florida resident restriction is on every Pointe Orlando offer** — this must appear in all ad fine print, all emails mentioning that location, and the Aloovy checkout flow. William needs to build this into the promo code logic.
- **Media shoot reels (15 incoming):** As soon as these arrive, brief the ad creative direction to William and start running video ads. Video almost always outperforms static in family/kids entertainment.
- **AI content angle (Phase 2):** Michael expressed interest in AI-generated TikTok/Reels commercials. This is a WILBA Content Generation Machine case study opportunity. Flag for Phase 2 conversation.
- **Competitor research:** Running in background via AIOS — findings will be incorporated into a revised copy brief once complete.
