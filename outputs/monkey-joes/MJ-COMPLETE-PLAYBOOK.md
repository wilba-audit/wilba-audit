# Monkey Joe's — Complete Marketing Playbook v2.0
## The Automation System That Runs While You Sleep

**Prepared by:** Jess Morrell / WILBA
**For:** Michael Carter + William Milner (Lanyu)
**Locations:** Pointe Orlando + Winter Park
**Pilot period:** April – June 2026
**Version:** 2.0 — Full rewrite. This supersedes v1.0.
**Platform:** GoHighLevel (GHL)

---

> *"The best marketing is the kind that feels like it was written by a friend who happened to have the best deal in town."*
> — Inspired by Joe Polish & Dean Jackson

---

## HOW TO READ THIS DOCUMENT

**Section 1 — The Automation System**
Every email. Every SMS. Every trigger. Every tag. Built once in GHL — runs day and night without you touching it. This is the engine.

**Section 2 — Weekly Campaign Templates**
What Jess sends manually each week. Wacky Wednesday push. Friday weekend preview. Completely rewritten hooks.

**Section 3 — Legal Compliance Reference**
Every automation has compliance built in. This section explains why and gives the exact language for SMS opt-in, unsubscribe, and Florida-specific restrictions.

---

---

# SECTION 1: THE AUTOMATION SYSTEM

---

## PHILOSOPHY

Stop marketing to strangers. Start marketing to people who already raised their hand.

The moment someone enters their email and phone number on one of our landing pages, they are not a stranger. They want the offer. They're interested in Monkey Joe's. They just need a little nudge to actually book — and then, once they've been, they need a reason to come back.

This system handles all of it. Automatically. Every time. For every contact. At every location.

**The system does six things:**
1. **Delivers the offer** the moment they opt in — with their promo code, clear instructions, and excitement
2. **Follows up** if they don't book — short, personal, not pushy
3. **Recovers abandoned checkouts** — three texts and an email before they slip away
4. **Welcomes them back** after their visit — asks for a review, introduces birthday parties and the Jumper Card
5. **Re-engages the quiet ones** — automated at 180 days, personalised, uses the offer as a hook
6. **Exploits weather** — rainy days are our best walk-in opportunity. The system sends automatically.

---

## THE MASTER TAG MAP

Every contact in GHL gets tagged based on their behaviour. Tags control which sequences fire and which get suppressed. **Never send an acquisition offer to someone already tagged as a customer.**

### Offer & Lead Tags
| Tag | When Applied | What It Does |
|---|---|---|
| `BOGO-POL-LEAD` | Opts in via BOGO Pointe Orlando page | Starts Sequence 1A |
| `BOGO-WP-LEAD` | Opts in via BOGO Winter Park page | Starts Sequence 1B |
| `50OFF-POL-LEAD` | Opts in via 50% Off Pointe Orlando page | Starts Sequence 1C |
| `50OFF-WP-LEAD` | Opts in via 50% Off Winter Park page | Starts Sequence 1D |
| `SMS-CONSENT` | Checks SMS opt-in box on landing page form | Required before any SMS fires |

### Booking & Customer Tags
| Tag | When Applied | What It Does |
|---|---|---|
| `BOGO-POL-BOOKED` | WACKY-POL code redeemed in Aluvii | Removes from offer sequence, starts Sequence 2 |
| `BOGO-WP-BOOKED` | WACKY-WP code redeemed | Removes from offer sequence, starts Sequence 2 |
| `50OFF-POL-BOOKED` | KIDS50-POL code redeemed | Removes from offer sequence, starts Sequence 3 |
| `50OFF-WP-BOOKED` | KIDS50-WP code redeemed | Removes from offer sequence, starts Sequence 3 |
| `CUSTOMER` | Any booking confirmed (BOGO or 50% Off, either location) | All acquisition offer sequences stop |
| `VISITED` | Visit date has passed (from Aluvii export via Zapier) | Triggers post-visit sequences |

### Behaviour Tags
| Tag | When Applied | What It Does |
|---|---|---|
| `ABANDONED-CHECKOUT` | Started Aluvii checkout, no purchase within 2 hours | Starts Sequence 4 |
| `BIRTHDAY-DRIP` | Completes offer sequence without booking + 14 days on list | Starts birthday party drip |
| `BIRTHDAY-INQUIRY` | Submits birthday party enquiry form | Starts Sequence 7 |
| `BIRTHDAY-BOOKED` | Birthday party confirmed | Stops birthday sequences |
| `WEEKLY-LIST` | Added after offer sequence ends | Gets weekly broadcasts |
| `LAPSED-180` | No email open or click in 180 days | Starts Sequence 5 (Win-Back) |
| `WIN-BACK-ACTIVE` | Clicks offer code in win-back sequence | Restarts Sequence 1 (appropriate variant) |
| `RAINY-DAY-SENT` | Received rainy day trigger (reset weekly) | Prevents duplicate sends |
| `NO-RETURN-7` | No visit 7 days after first visit | Starts 7-day no-return email |
| `UNSUBSCRIBED-SMS` | Replies STOP | Removes from all SMS sequences permanently |
| `UNSUBSCRIBED-EMAIL` | Clicks unsubscribe | Removes from all email sequences |
| `POL` | Pointe Orlando contact | Location targeting for broadcasts |
| `WP` | Winter Park contact | Location targeting for broadcasts |

### The If/Then Decision Logic (Master Flow)

```
CONTACT OPTS IN (landing page)
        ↓
Apply: [OFFER]-[LOCATION]-LEAD + SMS-CONSENT (if checked) + [POL or WP]
        ↓
IF tagged CUSTOMER already → STOP. Do not start offer sequence.
IF not tagged CUSTOMER → Start Sequence 1 (appropriate variant)
        ↓
SEQUENCE 1 RUNNING
        ↓
IF code redeemed within 48hrs → Apply BOOKED tag → STOP Seq 1 → Start Seq 2/3
IF NOT booked by Email 3 → STOP Seq 1 → Apply WEEKLY-LIST tag → Start birthday drip (14 days later)
        ↓
CONTACT STARTS ALUVII CHECKOUT
        ↓
IF purchase completes → Apply BOOKED tag (as above)
IF purchase NOT completed within 2 hours → Apply ABANDONED-CHECKOUT → Start Seq 4
        ↓
CONTACT VISITS (VISITED tag applied via Aluvii export)
        ↓
48 hours after visit → Start post-visit sequence (Seq 2 Email 3 / Seq 3 Email 3)
        ↓
7 days after visit → IF no second visit (no new BOOKED tag) → Apply NO-RETURN-7 → Day 7 email
        ↓
180 days no activity → Apply LAPSED-180 → Start Seq 5 (Win-Back)
        ↓
RAINY DAY (manual or Zapier weather trigger)
        ↓
Send to: all contacts tagged CUSTOMER + WEEKLY-LIST, NOT tagged RAINY-DAY-SENT this week
Apply RAINY-DAY-SENT (reset Monday 6am each week)
```

---

---

## SEQUENCE 1A — BOGO OFFER CLAIM · POINTE ORLANDO
**Trigger:** Contact opts in via `/bogo-orlando` landing page
**Tags applied on entry:** `BOGO-POL-LEAD` + `POL` + `SMS-CONSENT` (if checked)
**Goal:** Deliver the code. Make them feel like they just scored something real. Get them to book.
**Stop condition:** `BOGO-POL-BOOKED` tag applied at any point → remove from sequence immediately

---

### EMAIL 1A.1 — Immediate
**Subject:** Your free admission is right here 🐒
**Preview:** Save this. Use it this week.
**Tags:** Applied on send: none | Remove from sequence if: BOOKED

---

Hey [First Name]!

You just did something smart.

Here's your code — save it, screenshot it, tattoo it on your arm if you need to:

---
**YOUR CODE: `WACKY-POL`**
Buy One Kid's Admission, Get One FREE
Valid Monday–Friday | Ages 3–12 | Pointe Orlando only
Florida residents only | One use per household
---

👉 **[BOOK YOUR VISIT NOW →]** *(link to Aluvii checkout with code pre-filled)*

**Here's how it works:**
1. Click the link above — your code is already in there
2. Pick a weekday that works for your family
3. Show up, let the kids go absolutely feral on the bounce houses
4. You sit down. Drink something. Breathe.

**A few things worth knowing:**
👟 Socks required for all jumpers (grab a pair at the venue for $2 if needed)
👨‍👩‍👧 Adults always get in free — every visit, no exceptions
🎮 40+ inflatables, arcade, toddler zone, air conditioning (you're welcome, Florida summer)
📍 Monkey Joe's Pointe Orlando — 9101 International Dr, Orlando FL 32819

**Walk-in specials while you're there:**
Monday Madness: $9.95 + $5 game card
Wacky Wednesday: Buy one, get one free (BOGO) — every single week for 21 years
Toddler Thursday: Reduced price for ages 2–5

Questions? Call us: [phone]

Can't wait to see you,
The Monkey Joe's Team 🐒

*Not valid with any other offer. Florida residents only. One use per household. Weekdays only (Mon–Fri).*
*[Unsubscribe] | Monkey Joe's Pointe Orlando | 9101 International Dr, Orlando FL 32819*
*You received this because you requested an offer at monkeyjoes.com/bogo-orlando.*

---

### SMS 1A.1 — Immediate (only if SMS-CONSENT tagged)
> Monkey Joe's: Hey [First Name]! Your BOGO code is WACKY-POL — one kid gets in FREE any weekday. Book now: [link] Reply STOP to opt out.

---

### EMAIL 1A.2 — Day 2 (IF not BOOKED)
**Subject:** Still got your free admission waiting 👀
**Preview:** Just checking — did you get a chance to use it?
**Trigger condition:** Contact NOT tagged BOGO-POL-BOOKED

---

Hey [First Name],

Did you get a chance to book?

Your code is still active: **`WACKY-POL`** — buy one kid's admission, get one free, any weekday.

👉 **[GRAB YOUR SPOT →]** *(Aluvii link)*

Fair warning: this is the kind of deal kids remember.

"Why did we wait so long to go back?" — said by approximately every parent who's ever brought their kids to Monkey Joe's.

See you soon,
The Monkey Joe's Team 🐒

*Code expires [expiry date if applicable]. One use per household. FL residents only. Weekdays Mon–Fri.*
*[Unsubscribe] | Monkey Joe's Pointe Orlando | 9101 International Dr, Orlando FL 32819*

---

### SMS 1A.2 — Day 2 (IF not BOOKED + SMS-CONSENT)
> Monkey Joe's: Hey [First Name] — your free admission code WACKY-POL is still waiting! Any weekday works. Book here: [link] Reply STOP to opt out.

---

### EMAIL 1A.3 — Day 5 (IF not BOOKED)
**Subject:** Last check-in 🐒
**Preview:** Just one quick thing before I leave you alone.
**Trigger condition:** Contact NOT tagged BOGO-POL-BOOKED

---

Hey [First Name],

Last one, I promise.

Your **Buy One, Get One Free (BOGO) code — `WACKY-POL`** — is still sitting here waiting for you.

I won't keep nudging you after this. But if you've been thinking about it and life just got in the way — here's the link:

👉 **[USE YOUR CODE →]**

The bounce houses will be there. The kids' smiles will be there. The hot coffee you finally get to finish in peace — also there.

Whenever you're ready,
The Monkey Joe's Team 🐒

*[Unsubscribe] | Monkey Joe's Pointe Orlando | 9101 International Dr, Orlando FL 32819*

---

### SMS 1A.3 — Day 5 (IF not BOOKED + SMS-CONSENT)
> Monkey Joe's: Final reminder — BOGO code WACKY-POL, one kid FREE any weekday. Book: [link] We'd love to see your family! Reply STOP to opt out.

---

**→ After Email 3 (no booking): Remove BOGO-POL-LEAD tag. Apply WEEKLY-LIST + POL tags. Enrol in weekly broadcast list. Start BIRTHDAY-DRIP after 14 days.**

---
---

## SEQUENCE 1B — BOGO OFFER CLAIM · WINTER PARK
**Trigger:** Contact opts in via `/bogo-winterpark` landing page
**Tags applied on entry:** `BOGO-WP-LEAD` + `WP` + `SMS-CONSENT` (if checked)
**Stop condition:** `BOGO-WP-BOOKED` tag applied → remove from sequence immediately

*Identical structure to Sequence 1A. Change only:*
- Promo code: `WACKY-WP`
- Location: Winter Park | [address]
- Remove "Florida residents only" restriction
- Phone: [Winter Park phone]
- Aluvii link: Winter Park checkout URL

---
---

## SEQUENCE 1C — 50% OFF OFFER CLAIM · POINTE ORLANDO
**Trigger:** Contact opts in via `/halfprice-orlando` landing page
**Tags applied on entry:** `50OFF-POL-LEAD` + `POL` + `SMS-CONSENT` (if checked)
**Stop condition:** `50OFF-POL-BOOKED` tag applied → remove from sequence immediately

---

### EMAIL 1C.1 — Immediate
**Subject:** 50% off is officially yours 🎉
**Preview:** Here's your code — use it any weekday this week.

---

Hey [First Name]!

Boom. You just cut your kids' admission in half.

Here's your code:

---
**YOUR CODE: `KIDS50-POL`**
50% Off Kids' Admissions — Ages 3–12
Valid Monday–Friday | Pointe Orlando only
Florida residents only | One use per household
---

👉 **[BOOK YOUR VISIT →]** *(Aluvii link with code pre-filled)*

**How to use it:**
1. Hit the link — code is already loaded
2. Pick any weekday
3. Show up, watch the kids disappear into a cloud of joy
4. Sit down. Actually relax. You've earned it.

**What's waiting at Monkey Joe's Pointe Orlando:**
🐒 40+ inflatable bounce houses, slides, and obstacle courses
🎮 Arcade zone with prizes
👶 Dedicated toddler area (ages 2–5)
❄️ Full air conditioning — essential, let's be honest
📍 9101 International Dr, Orlando FL 32819
👨‍👩‍👧 Adults always free — always

Questions? [Phone]

See you soon!
The Monkey Joe's Team 🐒

*Not valid with any other offer. Florida residents only. One use per household. Valid weekdays Mon–Fri.*
*[Unsubscribe] | Monkey Joe's Pointe Orlando | 9101 International Dr, Orlando FL 32819*

---

### SMS 1C.1 — Immediate (SMS-CONSENT required)
> Monkey Joe's: [First Name], your 50% off code is KIDS50-POL. Half price any weekday! Book now: [link] Reply STOP to opt out.

---

### EMAIL 1C.2 — Day 2 (IF not BOOKED)
**Subject:** Your 50% off code is still alive 👀
**Preview:** Quick check-in on that deal you grabbed.

---

Hey [First Name],

Just popping in — have you had a chance to use your code yet?

**`KIDS50-POL`** — 50% off kids' admission, any weekday.

Here's the thing about this deal: it's genuinely half price. That's not "slightly discounted" or "BOGO-if-you-squint." It's half. Off.

For 40+ inflatables, an arcade, a toddler zone, and approximately one hour of pure, glorious chaos (for them) and peace (for you).

👉 **[GRAB YOUR SPOT →]**

The kids won't forget it. And neither will you — mostly because you'll be the one who finally got to sit down.

See you soon,
Monkey Joe's 🐒

*[Unsubscribe] | Monkey Joe's Pointe Orlando | 9101 International Dr, Orlando FL 32819*

---

### SMS 1C.2 — Day 2 (SMS-CONSENT)
> Monkey Joe's: [First Name] — 50% off code KIDS50-POL is still good! Any weekday, ages 3–12. Book here: [link] Reply STOP to opt out.

---

### EMAIL 1C.3 — Day 5 (IF not BOOKED)
**Subject:** Honest question, [First Name] 🐒
**Preview:** One thing I should probably mention.

---

Hey [First Name],

Honest question: is anything stopping you from booking?

Sometimes it's timing. Sometimes it's life. Sometimes the code just gets buried under 47 other emails and you forget it exists.

Your code: **`KIDS50-POL`** — 50% off kids' admission, any weekday.

👉 **[BOOK HERE →]**

This is my last check-in — I won't keep nudging you after this. But if there's something you need to know, or a question I can answer, just reply to this email and I'll get back to you.

Otherwise — whenever you're ready, we're here. The bounce houses aren't going anywhere.

The Monkey Joe's Team 🐒

*[Unsubscribe] | Monkey Joe's Pointe Orlando | 9101 International Dr, Orlando FL 32819*

---

### SMS 1C.3 — Day 5 (SMS-CONSENT)
> Monkey Joe's: Last reminder — 50% off code KIDS50-POL. Any weekday, ages 3–12, Pointe Orlando. Book: [link] Reply STOP to opt out.

---

**→ After Email 3 (no booking): Remove 50OFF-POL-LEAD. Apply WEEKLY-LIST + POL. Birthday drip starts in 14 days.**

---
---

## SEQUENCE 1D — 50% OFF OFFER CLAIM · WINTER PARK
**Trigger:** `/halfprice-winterpark` opt-in
**Tags:** `50OFF-WP-LEAD` + `WP` + `SMS-CONSENT`
**Stop condition:** `50OFF-WP-BOOKED`

*Identical to Sequence 1C. Change only:*
- Code: `KIDS50-WP`
- Location: Winter Park | [address]
- Remove Florida residents restriction
- Phone: [WP phone]

---
---

## SEQUENCE 2 — POST-BOGO PURCHASE
**Trigger:** `BOGO-POL-BOOKED` or `BOGO-WP-BOOKED` tag applied
**Tags on entry:** Add `CUSTOMER`
**Goal:** Perfect visit experience → review → welcome them back → introduce Jumper Card + birthday parties
**Stop conditions throughout:** If contact re-books → suppress Day 7 no-return email

---

### EMAIL 2.1 — Immediate (Booking Confirmed)
**Subject:** You're booked! Here's everything you need 🎟️
**Preview:** Pack socks. Adults are free. The kids are going to lose it.

---

Hey [First Name]!

You're all set. The kids are going to absolutely love this.

**Your booking:**
🎟️ Offer: Buy One Kid's Admission, Get One FREE
📍 Location: [location name + address]
💳 Your code: [`WACKY-POL` or `WACKY-WP`]

No need to print anything — just show this email at the door (or screenshot it).

**Before you arrive:**
👟 Socks are required for all jumpers — bring a pair each, or grab some at the door ($2/pair)
👨‍👩‍👧 Adults are always free — bring all the adults, every time, no exceptions
🕙 Open weekdays [hours — Michael to confirm]
🚗 Parking at [location-specific note]

📍 [Full address + Google Maps link]
📞 Questions? [Location phone]

The bounce houses are waiting. See you soon!
The Monkey Joe's Team 🐒

*Code is one use per household. FL residents only (Pointe Orlando). Valid weekdays Mon–Fri.*
*[Unsubscribe] | [Location address]*

---

### SMS 2.1 — Immediate (SMS-CONSENT)
> Monkey Joe's: You're booked, [First Name]! 🐒 See you at [location] — bring socks! Adults are FREE. Reply STOP to opt out.

---

### EMAIL 2.2 — Day of Visit (Send at 8am on visit date)
**Subject:** Today's the day! 🐒
**Preview:** Quick checklist before you head in.
**Trigger:** Visit date field in GHL (populated from Aluvii booking)

---

Hey [First Name]!

It's Monkey Joe's day! 🎉

Quick checklist before you head in:

📍 [Location address + Google Maps link]
🕙 Open today: [hours]
👟 Socks for every jumper (this is the #1 thing families forget — you're welcome)
💳 Your code: [`WACKY-POL` / `WACKY-WP`] — just show this email
👨‍👩‍👧 Adults are FREE — bring whoever wants to come

**Pro tip from parents who've been before:** grab a spot near the toddler zone if you've got little ones — the view is great and the seating is comfortable.

See you today,
The Monkey Joe's Team 🐒

*[Unsubscribe] | [Location address]*

---

### SMS 2.2 — Day of Visit (8am)
> Monkey Joe's: Today's the day, [First Name]! 🐒 See you at [address]. Bring socks! Adults FREE. Reply STOP to opt out.

---

### EMAIL 2.3 — 48 Hours After Visit Date
**Subject:** Hope it was absolutely incredible 🙌
**Preview:** (And a tiny favour, if you have 30 seconds.)
**Trigger:** 48 hours after visit date in GHL

---

Hey [First Name]!

We hope your family had the BEST time at Monkey Joe's!

We love hearing how it went. If you got a chance to enjoy a hot coffee in peace while the kids went absolutely feral on the bounce houses — that's exactly what we're here for.

**If you had a great time, could you do us a quick favour?**

A Google review takes about 30 seconds and makes a massive difference for a family-owned business like ours. It helps other local parents find us when they're Googling for a rainy day activity or a birthday venue.

👉 **[Leave a Google Review →]** *(location-specific Google review link)*

Thank you — it genuinely means the world to us.

---

**Ready to come back?**

Here are two ways regulars keep the fun going:

**🎟️ The Frequent Jumper Card — 10 visits for $120 ($12 each)**
No codes. No booking. Just scan your phone at the door. Perfect for families who visit more than once (which, after yesterday, is probably you).
👉 **[Get Your Jumper Card →]**

**🎂 Planning a birthday party?**
Monkey Joe's birthday parties are the ones kids talk about for *months.* Private party room. Dedicated host. We handle setup AND cleanup. You just show up and look like a hero.
Party dates go fast — especially weekends.
👉 **[Check Party Room Availability →]**

See you again soon,
The Monkey Joe's Team 🐒

*[Unsubscribe] | [Location address]*

---

### SMS 2.3 — 48 Hours After Visit (SMS-CONSENT)
> Monkey Joe's: Hope your fam had a blast [First Name]! 🐒 Come back anytime — Jumper Card = 10 visits for $120. Get yours: [link] Reply STOP to opt out.

---

### EMAIL 2.4 — Day 7 (IF no return visit — NO-RETURN-7 tag applied)
**Trigger condition:** 7 days after visit date AND no new BOOKED tag applied
**Subject:** The bounce houses have been asking about you 👀
**Preview:** (They haven't. But the offer I've got for you is real.)

---

Hey [First Name]!

It's been a week since your Monkey Joe's visit — and we noticed you haven't been back yet.

Totally fine. Life happens. But here's a gentle nudge:

**Wacky Wednesday is every week.** Buy one kid's admission, get one FREE. It's been running for 21 years. It'll run this Wednesday too.

And if you want to skip the booking and just show up whenever — the **Frequent Jumper Card** (10 visits, $120) is made for you.

👉 **[Book This Wednesday →]**
👉 **[Get the Jumper Card →]**

The kids remember. They'll ask again. This is your head start.

See you soon,
The Monkey Joe's Team 🐒

*[Unsubscribe] | [Location address]*

---
---

## SEQUENCE 3 — POST-50%-OFF PURCHASE
**Trigger:** `50OFF-POL-BOOKED` or `50OFF-WP-BOOKED` tag applied
**Tags on entry:** Add `CUSTOMER`

*Identical structure to Sequence 2. Change only:*
- Email 2.1: "50% Off Kids' Admissions" instead of "Buy One Get One Free"
- Code references: `KIDS50-POL` or `KIDS50-WP`
- All other emails (day-of, post-visit, day 7) are identical

---
---

## SEQUENCE 4 — ABANDONED CHECKOUT RECOVERY
**Trigger:** GHL pixel fires `ViewContent` on Aluvii checkout page but NOT `Purchase` within 2 hours
**Tags on entry:** `ABANDONED-CHECKOUT`
**Goal:** Recover the booking before they forget or go elsewhere
**Stop condition:** `BOOKED` tag applied at any point → stop all abandoned checkout messages immediately

---

### SMS 4.1 — 30 Minutes After Abandonment (SMS-CONSENT required)
> Monkey Joe's: Hey [First Name] — looks like you didn't finish booking! Your code [CODE] is still good. Grab your spot: [link] Reply STOP to opt out.

---

### SMS 4.2 — 4 Hours After Abandonment
> Monkey Joe's: Still thinking about it? 🐒 Your [offer] code [CODE] is waiting. The kids are going to love it — finish booking: [link] Reply STOP to opt out.

---

### SMS 4.3 — Day 2 After Abandonment
> Monkey Joe's: Last chance on this one, [First Name]. Your [Buy One Get One Free / 50% off] code [CODE] — any weekday. Book here: [link] Reply STOP to opt out.

---

### EMAIL 4.1 — Day 1 After Abandonment (8 hours after)
**Subject:** Did something go wrong? 🐒
**Preview:** Your booking didn't go through — here's how to fix it.

---

Hey [First Name],

We noticed you started booking your Monkey Joe's visit but didn't quite finish.

Totally happens — checkout can be finicky sometimes, or life interrupted. Either way, your code is still valid:

**Code: [PROMO CODE]**
[Buy One Kid's Admission, Get One FREE / 50% Off Kids' Admission]
Valid weekdays (Mon–Fri) | Ages 3–12 | One use per household

👉 **[COMPLETE YOUR BOOKING →]**

If you hit a snag at checkout, just reply to this email and we'll sort it out.

The kids are waiting (metaphorically). We've got the bounce houses covered.

The Monkey Joe's Team 🐒

*[Unsubscribe] | [Location address]*

---

**→ After SMS 4.3 + Email 4.1 (no booking): Remove ABANDONED-CHECKOUT. Contact remains on WEEKLY-LIST if already tagged, or returns to standard offer sequence follow-up.**

---
---

## SEQUENCE 5 — 180-DAY WIN-BACK (Automated)
**Trigger:** Contact has NO email open, NO click, NO purchase for 180 consecutive days
**Tags on entry:** `LAPSED-180`
**Goal:** Bring them back with an irresistible offer + emotional hook
**If they click an offer:** Apply `WIN-BACK-ACTIVE` → restart relevant Sequence 1 variant

---

### EMAIL 5.1 — Day 1
**Subject:** It's been a while. We miss your family. 🐒
**Preview:** Something to make coming back ridiculously easy.

---

Hey [First Name],

It's been about 6 months since we've seen you at Monkey Joe's.

We get it — life moves fast. Kids get into new things. The calendar fills up before you've even had a chance to think.

But here's what doesn't change: the moment kids step into Monkey Joe's, they light up. Every time. First visit or fiftieth.

We'd love to see your family again. So here's something to make it easy:

**A Buy One, Get One Free (BOGO) admission — on us.**
Code: `COMEBACK-POL` *(or `COMEBACK-WP` for Winter Park)*
Valid any weekday. Ages 3–12. One use.

👉 **[CLAIM YOUR WELCOME BACK VISIT →]**

You get to breathe. They get the best time. Just like you remember.

See you soon,
The Monkey Joe's Team 🐒

*[Unsubscribe] | [Location address]*

---

### EMAIL 5.2 — Day 5 (IF no click on Email 5.1)
**Subject:** One more thing before I leave you alone 🙏
**Preview:** (It's a short one. I promise.)
**Trigger condition:** No click on Email 5.1

---

Hey [First Name],

I'm going to keep this short.

Your **BOGO code is still active** — `COMEBACK-POL` / `COMEBACK-WP`. Buy one kid in, get one free. Any weekday. Ages 3–12.

👉 **[USE IT HERE →]**

If you'd rather we stopped emailing you, just click unsubscribe below and we'll part as friends. No hard feelings at all.

But if there's even a small chance your family would enjoy an afternoon at Monkey Joe's — use the code. It costs nothing to try.

The Monkey Joe's Team 🐒

*[Unsubscribe] | [Location address]*
*After this email: contacts who do not open or click are moved to suppressed list. They stay subscribed but receive only monthly newsletters, not automations.*

---
---

## SEQUENCE 6 — RAINY DAY TRIGGER
**Trigger:** Manual (Jess activates on days with heavy rain/storm forecast) OR Zapier + Weather API (automated — trigger when rain >70% probability in Orlando/Winter Park)
**Audience:** Contacts tagged `CUSTOMER` or `WEEKLY-LIST` and NOT tagged `RAINY-DAY-SENT` this week
**Tags on send:** Apply `RAINY-DAY-SENT` (auto-reset every Monday 6am)
**If/then:** IF tagged CUSTOMER → use `COMEBACK-POL/WP` code as bonus gift. IF tagged as LEAD only → use their existing offer code.

---

### EMAIL 6.1 — Rainy Day
**Subject:** The forecast is basically free admission for your kids ⛈️
**Preview:** Stuck inside? We've got 10,000 sq ft of inflatable chaos with your name on it.

---

Hey [First Name]!

Big news: it's raining. Again.

Here's the upside: Monkey Joe's has 10,000 square feet of inflatables, a full arcade, a toddler zone, and air conditioning so powerful it'll make you forget it's Florida outside.

The kids bounce. You breathe. The rain does whatever it wants.

And because the weather is being dramatic, here's a little something from us:

**Use code `COMEBACK-POL` / `COMEBACK-WP`** for a buy one, get one free (BOGO) admission on your next weekday visit.

👉 **[PLAN YOUR RAINY DAY ESCAPE →]**

📍 [Location] | [Address] | Walk-ins welcome

See you on the other side of the puddles,
The Monkey Joe's Team 🐒

*Valid weekdays (Mon–Fri). Ages 3–12. Not valid with other offers. One use per household.*
*[Unsubscribe] | [Location address]*

---

### SMS 6.1 — Rainy Day (SMS-CONSENT)
> Monkey Joe's: ⛈️ Rain = perfect Monkey Joe's day. 10,000 sq ft of inflatables + AC. BOGO code COMEBACK-[POL/WP] for today! Book: [link] Reply STOP to opt out.

---
---

## SEQUENCE 7 — BIRTHDAY PARTY INQUIRY FOLLOW-UP
**Trigger:** Birthday party enquiry form submitted in GHL
**Tags on entry:** `BIRTHDAY-INQUIRY` + location tag
**Goal:** Close the party booking within 7 days. This is the highest-value conversion in the business.
**Stop condition:** `BIRTHDAY-BOOKED` tag applied → stop all birthday inquiry emails

---

### EMAIL 7.1 — Immediate
**Subject:** We got your party enquiry — here's what happens next 🎂
**Preview:** [Location] has [X] party rooms. Here's how to lock yours in.

---

Hey [First Name]!

We got your birthday party enquiry — and we're SO excited to help you make this one special.

Here's what happens next:

Our party coordinator, [Nicole / team], will be in touch within [24 hours / 1 business day] to walk you through everything. But here's a sneak peek at what you're signing up for:

**What Monkey Joe's does for birthday parties:**
🎉 Private party room — just your group, your vibe
🐒 Unlimited bounce time on all 40+ inflatables (the whole venue)
🎂 Dedicated party host — we manage the room so you can actually enjoy it
🧹 We handle setup AND cleanup — you show up, we handle the rest
👨‍👩‍👧 Adults always free — every adult guest gets in without paying
🏆 The birthday child gets a special welcome (they feel like royalty, and they should)

**Party rooms go fast — especially April through June and any weekend.**

If you have specific dates in mind, let Nicole know when she reaches out, and she'll check availability for you.

We can't wait to be part of [child's name / your family's] big day.

The Monkey Joe's Team 🐒

📞 Questions right now? Call [phone] | Or reply to this email

*[Unsubscribe] | [Location address]*

---

### EMAIL 7.2 — Day 3 (IF not BIRTHDAY-BOOKED)
**Subject:** Party room update — dates are filling up 📅
**Preview:** A few things worth knowing before you decide.
**Trigger condition:** No BIRTHDAY-BOOKED tag

---

Hey [First Name],

Just checking in on your birthday party enquiry!

We have [X] party rooms available at [location], and the popular weekend dates — especially in April and May — do go fast.

**Here's what we need from you to hold a date:**
1. Your preferred date + a backup date
2. Approximate number of guests
3. Any special requests or dietary needs we should know about

Just reply to this email or call [phone] and Nicole will sort the rest.

We promise: this is the birthday party where you'll actually get to enjoy it too.

The Monkey Joe's Team 🐒

*[Unsubscribe] | [Location address]*

---

### EMAIL 7.3 — Day 7 (IF not BIRTHDAY-BOOKED)
**Subject:** Last check-in on the birthday party 🎂
**Preview:** We want to make this happen for your family.

---

Hey [First Name],

One more check-in on the birthday party — I want to make sure we haven't dropped the ball on our end.

If you've decided to go another direction, absolutely no hard feelings. But if you're still thinking about Monkey Joe's and just need a nudge or an answer to a question, here we are:

📞 Call or text: [phone]
📧 Reply to this email
👉 **[Book Your Party Room Directly →]**

Weekends in [month] are filling fast. If you've got a date in mind, now's the moment.

We'd love to be part of it.

The Monkey Joe's Team 🐒

*[Unsubscribe] | [Location address]*

---
---

## SEQUENCE 8 — BIRTHDAY PARTY DRIP (Post-Offer, No-Book Contacts)
**Trigger:** 14 days after contact is added to `WEEKLY-LIST` tag (i.e., after completing offer sequence without booking)
**Tags on entry:** `BIRTHDAY-DRIP`
**Goal:** Introduce birthday parties to people who haven't visited yet — warm them up, not sell them hard
**Stop condition:** `BIRTHDAY-INQUIRY` or `BIRTHDAY-BOOKED` applied

---

### EMAIL 8.1 — Day 1 of Drip
**Subject:** One question before the next school holidays 🎂
**Preview:** (It's a good one. Especially if there's a birthday coming up.)

---

Hey [First Name],

Quick question: **is there a birthday coming up in the next 90 days?**

Because Monkey Joe's birthday parties are the ones kids literally cannot stop talking about. Private party room. 40+ inflatables. A dedicated host who runs the whole show. Setup and cleanup handled.

You show up. You feel like the best parent alive. Your kid thinks you're basically magic.

**→ [Tell Us About the Birthday →]** *(birthday party enquiry link)*

Even if the birthday's a little further out, it's worth checking dates now — weekends fill faster than you'd think.

And hey — your [BOGO / 50% off] offer code still works for a visit before the party, too. Great way for the kids to scope it out first.

The Monkey Joe's Team 🐒

*[Unsubscribe] | [Location address]*

---

### EMAIL 8.2 — Day 10 (IF no BIRTHDAY-INQUIRY tag)
**Subject:** What 7-year-olds say in the car on the way home 🚗
**Preview:** (It's always the same. Always.)
**Trigger condition:** No BIRTHDAY-INQUIRY tag

---

Hey [First Name],

You know that moment in the car on the way home from a really great outing?

The kids are in the back, completely spent — that deep, happy, wide-eyed tired that only happens after they've run themselves absolutely ragged.

And then one of them says it: *"Can we go back?"*

That's Monkey Joe's. Every time.

If there's a birthday coming up and you want that energy — but with a private room, a party host, cake, and zero cleanup for you — we'd love to make it happen.

👉 **[Check Birthday Party Availability →]**

Party rooms: [X] at Pointe Orlando / [X] at Winter Park. Weekends are popular.

The Monkey Joe's Team 🐒

*[Unsubscribe] | [Location address]*

---

**→ After Email 8.2 (no action): Remove BIRTHDAY-DRIP tag. Contact remains on WEEKLY-LIST for ongoing broadcasts.**

---
---

# SECTION 2: WEEKLY CAMPAIGN TEMPLATES

---

## THE PHILOSOPHY

Weekly emails go to everyone on the `WEEKLY-LIST` tag.
**Key rule:** Contacts tagged `CUSTOMER` get the standard weekly email. Contacts NOT tagged `CUSTOMER` still get the weekly email BUT include their offer code reminder in the P.S. — nudging them to finally book.

Weekly sends:
- **Tuesday 5pm:** Wacky Wednesday push ← rewritten hooks below
- **Friday 9am:** Weekend preview + birthday angle

---

## CAMPAIGN 1 — WACKY WEDNESDAY (Tuesday 5pm)
**Audience:** `WEEKLY-LIST` + location tag (`POL` or `WP`)
**Subject line rotation (5-week cycle — never repeat back-to-back):**

**Week 1:** Tomorrow = free. (Kind of.) 🐒
**Week 2:** 21 years and they're still doing this.
**Week 3:** The deal that's been running since [year they were born, probably].
**Week 4:** One kid in free. Every. Single. Wednesday.
**Week 5:** Quick — Wacky Wednesday is tomorrow 👀

---

**EMAIL TEMPLATE — Wacky Wednesday**
*(Swap subject line weekly per rotation above. Body stays consistent.)*

---

Hey [First Name]!

Just a quick heads-up before tomorrow:

**Wacky Wednesday at Monkey Joe's = Buy One Kid's Admission, Get One FREE.**

Every Wednesday. No code needed. Been running for 21 years. Still going strong.

You relax. They have the best time. That's it.

👉 **[BOOK YOUR WEDNESDAY VISIT →]** *(Aloovy link — location specific)*

📍 [Location] | [Address] | Open [hours]
👟 Don't forget socks for the jumpers!
👨‍👩‍👧 Adults always free

See you tomorrow,
The Monkey Joe's Team 🐒

*P.S. — [IF contact NOT tagged CUSTOMER]: Your exclusive code **[CODE]** for [Buy One Get One Free / 50% Off] is still active on top of this. Weekdays only, one use per household.*

*[Unsubscribe] | [Location address]*

---

### SMS — Wacky Wednesday (Tuesday 5pm, SMS-CONSENT)
> Monkey Joe's: Tomorrow = BOGO Wednesday 🐒 One kid bounces FREE. Book your spot: [link] Every Wednesday, 21 years running. Reply STOP to opt out.

---

## CAMPAIGN 2 — WEEKEND PREVIEW (Friday 9am)
**Audience:** `WEEKLY-LIST` + location tag

---

**Subject:** This weekend sorted ✅
**Preview:** Party rooms + bounce houses. Walk-ins welcome.

---

Hey [First Name]!

Weekend plans: handled.

Monkey Joe's [Location] is open [Saturday–Sunday, hours]. Walk-ins welcome — no booking needed for open play.

**Party rooms:** Still have availability this weekend if you're planning something last minute. [Book here →]

**Birthday coming up?** Weekend party room slots for [month] are going fast. Grab yours now before the good dates disappear.

👉 **[PLAN YOUR WEEKEND VISIT →]**
👉 **[CHECK PARTY ROOM AVAILABILITY →]**

You relax. They have the best weekend. 🐒

The Monkey Joe's Team

*[Unsubscribe] | [Location address]*

---
---

# SECTION 3: LEGAL COMPLIANCE REFERENCE
## Florida + Federal. Every Email. Every SMS.

---

## WHY THIS MATTERS

Every email and SMS in this system must comply with:
- **CAN-SPAM Act (Federal)** — email commercial messaging rules
- **TCPA (Federal)** — text message rules, including explicit opt-in
- **FDUTPA (Florida)** — Florida Deceptive and Unfair Trade Practices Act — no misleading offers
- **COPPA (Federal)** — no data collection from children under 13 (all forms go to parents only)
- **Florida Minors Privacy** — we never name, photo, or identify a child in communications

---

## EMAIL COMPLIANCE CHECKLIST
Every email in this system must include:

- [x] **Physical address** of Monkey Joe's location in footer
- [x] **Unsubscribe link** — one click, no friction, no "are you sure?" loop
- [x] **"You received this because..."** notice at bottom of automated welcome emails
- [x] **From name** clearly identifies Monkey Joe's (not Jess, not WILBA)
- [x] **No deceptive subject lines** — no "RE:" or "FWD:" prefixes, no false urgency about codes expiring unless they actually do
- [x] **Offer terms in footer** — valid days, age restrictions, Florida resident restriction (Pointe Orlando BOGO), one use per household

---

## SMS COMPLIANCE CHECKLIST (TCPA)
SMS is heavily regulated. These rules are non-negotiable:

- [x] **Explicit opt-in required** — landing page form must have a SEPARATE checkbox for SMS (not bundled with email opt-in). Example checkbox text: *"Yes, I'd also like to receive text message reminders and offers from Monkey Joe's. Message & data rates may apply. Reply STOP to opt out at any time."*
- [x] **Business name first** — every SMS starts with "Monkey Joe's:" or "MJ:"
- [x] **Reply STOP** — every SMS ends with "Reply STOP to opt out." No exceptions.
- [x] **Frequency** — no more than [3 per week] per contact. This system sends max 2–3 SMS per sequence.
- [x] **No SMS without SMS-CONSENT tag** — GHL conditional: if contact does NOT have SMS-CONSENT tag, skip all SMS steps
- [x] **Unsubscribe honoured immediately** — STOP reply must remove SMS-CONSENT tag and add UNSUBSCRIBED-SMS tag instantly
- [x] **No SMS to purchased lists** — the 20K Constant Contact / waiver database does NOT auto-qualify for SMS. SMS consent must be collected separately for those contacts.

---

## OFFER TERMS (Use in All Email Footers)
**BOGO — Pointe Orlando:**
*Valid weekdays only (Monday–Friday). For Florida residents only. Ages 3–12. Buy one admission, get one admission of equal or lesser value free. Not valid with any other offer or daily deal. One use per household. Admission pricing subject to change. See venue for current pricing.*

**BOGO — Winter Park:**
*Valid weekdays only (Monday–Friday). Ages 3–12. Buy one admission, get one admission of equal or lesser value free. Not valid with any other offer or daily deal. One use per household. Admission pricing subject to change.*

**50% Off — Pointe Orlando:**
*Valid weekdays only (Monday–Friday). For Florida residents only. Ages 3–12. 50% discount applies to standard admission. Not valid with any other offer or daily deal. One use per household.*

**50% Off — Winter Park:**
*Valid weekdays only (Monday–Friday). Ages 3–12. 50% discount applies to standard admission. Not valid with any other offer or daily deal. One use per household.*

---

## LANDING PAGE FORM — REQUIRED FIELDS + CONSENT LANGUAGE
*(William to implement in GHL)*

**Fields:**
1. First Name (required)
2. Email Address (required)
3. Phone Number (optional but encouraged — explain why: "So we can text you your code instantly")

**Consent checkboxes (separate — cannot be pre-checked):**

☐ *I agree to receive marketing emails from Monkey Joe's, including offers and updates. I can unsubscribe at any time. [Privacy Policy link]*

☐ *Yes, I'd also like to receive text message reminders and deals from Monkey Joe's at the number I provided. Message and data rates may apply. Message frequency varies. Reply STOP to opt out at any time. [Terms link]*

**Below form:**
> *Your information is kept private and never sold. Florida residents only for Pointe Orlando offer. See full offer terms [link].*

---
---

# APPENDIX: PROMO CODE MASTER LIST

| Code | Offer | Location | Restriction | Sequences |
|---|---|---|---|---|
| `WACKY-POL` | Buy One Get One Free (BOGO) weekday admission | Pointe Orlando | FL residents only, 1× per household | Seq 1A, Seq 5, Seq 6 |
| `WACKY-WP` | Buy One Get One Free (BOGO) weekday admission | Winter Park | 1× per household | Seq 1B, Seq 5, Seq 6 |
| `KIDS50-POL` | 50% Off Kids Admission | Pointe Orlando | FL residents only, 1× per household | Seq 1C |
| `KIDS50-WP` | 50% Off Kids Admission | Winter Park | 1× per household | Seq 1D |
| `COMEBACK-POL` | Buy One Get One Free (BOGO) re-engagement | Pointe Orlando | FL residents, 1× per household, win-back and rainy day only | Seq 5, Seq 6 |
| `COMEBACK-WP` | Buy One Get One Free (BOGO) re-engagement | Winter Park | 1× per household, win-back and rainy day only | Seq 5, Seq 6 |

**All codes to be created in Aluvii by William. Set to single-use per household. Confirm expiry dates with Michael.**

---

*MJ Complete Playbook v2.0 | Prepared by Jess Morrell / WILBA | wilba.ai | March 2026*
*Platform: GoHighLevel | For: Michael Carter + William Milner (Lanyu)*
