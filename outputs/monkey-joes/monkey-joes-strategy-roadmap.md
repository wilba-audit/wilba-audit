# Monkey Joe's — Digital Marketing Strategy & Roadmap
**Prepared by:** Jess Morrell / WILBA for William Milner (Lanyu.ai)
**Client:** Michael Carter — Monkey Joe's, Pointe Orlando + Winter Park
**Date:** March 2026
**Engagement:** 3-Month Pilot → Phase 2: 9 locations → Phase 3: Big Game Brands (130+ locations)

---

## THE CORE PRINCIPLE: FIX THE LEAKY BUCKET FIRST

> "Don't pour more water into a leaky bucket."

**Month 1 = zero ad spend.** Every dollar of Michael's $1,500/month ad budget stays in the account until:
- Tracking is installed and verified
- Offers are built and assets are ready
- Landing pages are live
- Email automation is set up
- The attribution system is in place

Launching ads before this foundation exists wastes money and makes results impossible to prove. This is how we protect William's 10% revenue share model — and how we make a case that scales to 9 locations.

---

## PHASE 1: FOUNDATION (Weeks 1–4 — No Ad Spend)

### Week 1: Access & Audit

**Access needed from Michael/Nicole — get this list to William ASAP:**

| Platform | What We Need | Who Requests |
|---|---|---|
| Google Ads | Admin access | William → Michael |
| Google Analytics 4 (GA4) | Admin access | William → Michael |
| Google Business Profile | Owner/Manager access (both locations) | William → Michael |
| Facebook Business Manager | Admin access | William → Michael |
| Constant Contact | Admin or campaign manager access | William → Michael |
| WordPress | Editor or admin access | William → Michael |
| CallRail | Admin access | William → Michael |
| Aluvy (POS system) | Read/reporting access | William → Michael |

**Audit tasks while waiting for access:**
- Screenshot and document current GBP profiles for both locations (before state)
- Review current website: load time, mobile usability, offers, CTAs, booking flow
- Pull current Constant Contact list stats: total contacts, recent open rates, bounce rate, last send date
- Document all existing Facebook assets: pixel installed? Page followers (target: 30K), any active ads?
- Search Google for top 10 competitor keywords — document what ads are showing
- Pull existing Google Ads history if account exists (what's been spent, what's been running)

---

### Week 2: Tracking Installation

**This is the most critical week. Nothing launches until this is done.**

#### Step 1: Google Tag Manager (GTM)
Install GTM container on WordPress site first. ALL other tags fire through GTM. This means future changes don't require developer help.

- Install GTM container (one container, covers both location pages if on same domain)
- Verify GTM fires on all key pages: homepage, birthday party page, pricing page, contact/booking page, thank-you/confirmation page

#### Step 2: GA4 Setup
- Confirm or create GA4 property
- Add two data streams if Pointe Orlando and Winter Park have separate pages/subdomains
- Configure conversion events:
  - `birthday_party_inquiry` (form submission on party page)
  - `phone_call_click` (click on phone number)
  - `coupon_download` (PDF lead magnet download)
  - `email_signup` (pop-up or form email capture)
  - `directions_click` (links to Google Maps)
- Set up internal IP filters (exclude Michael's office, William's office, Jess's IP)
- Link GA4 to Google Ads account

#### Step 3: Facebook Pixel
- Install Meta Pixel via GTM
- Configure standard events:
  - `PageView` — all pages
  - `ViewContent` — birthday party page visits
  - `Lead` — form submissions
  - `Contact` — phone number clicks
- Verify with Facebook Pixel Helper Chrome extension
- Upload 20K email list as Customer List Custom Audience (segment before upload — see email section)

#### Step 4: CallRail
- Create two tracked numbers: one per location
- Create third tracked number for Google Ads call extensions
- Connect CallRail to Google Ads (import calls 60+ seconds as conversions)
- Connect CallRail to GA4 via UTM parameters

#### Step 5: Google Ads Conversion Import
- Import GA4 conversions into Google Ads
- Set primary conversion actions: `birthday_party_inquiry`, `phone_call_60sec`
- Set secondary conversions: `email_signup`, `coupon_download`

#### Step 6: Promo Code System (Walk-In Attribution)
This is how we prove walk-in revenue to Michael — the hardest attribution problem.

**System:**
- Create unique promo codes for each marketing channel:
  - `EMAIL10` — email campaigns
  - `FB10` — Facebook ads
  - `GOOGLE10` — Google Ads
  - `SMS10` — text message campaigns
  - `COLORING` — coloring pages lead magnet
- Train Michael/Nicole to ask customers at POS: "Do you have a promo code today?"
- Match promo code redemptions in Aluvy against campaign sends
- This creates the "provable revenue" chain William needs for his 10% model

**Note for kickoff call with Michael:** This only works if staff actually ask. This is a process change that needs to be trained and reinforced. Flag this explicitly.

---

### Week 3: Offers, Assets & Website

#### OFFERS STRATEGY — ASSETS REQUIRED FOR EACH

Before any campaign can launch, each offer needs its assets built. Do not run campaigns without these in place.

---

**OFFER 1: "Kids Come Free" — Primary Acquisition Offer**
Best for: Email reactivation, Facebook retargeting, Google Ads
What it is: One child free with paying adult admission (first-time family visit)

Assets needed:
- [ ] Landing page (dedicated URL — not homepage)
- [ ] Email capture form on landing page (Name + Email + Child age range)
- [ ] Confirmation email automated in Constant Contact (delivers the offer + venue info)
- [ ] Digital coupon or unique promo code: `KIDFREE`
- [ ] Staff training: how to redeem and log in Aluvy
- [ ] Social media graphic (1080x1080 for Instagram, 1200x628 for Facebook)
- [ ] Email banner image

What Michael needs to confirm: Is this offer approved? Max redemptions per family? Expiry date?

---

**OFFER 2: Wacky Wednesday BOGO — Weekly Deal Amplifier**
Best for: Email campaigns, Facebook organic posts, retargeting, SMS
What it is: Buy one get one free admission, Wednesdays only (already exists — amplify it)

Assets needed:
- [ ] Dedicated landing page or at minimum a clear webpage for Wednesday deal
- [ ] Weekly email template (can be reused every Wednesday)
- [ ] Social media graphic (branded, Wednesday-specific)
- [ ] SMS template (see SMS section)
- [ ] Promo code: `BOGO` or `WED2FOR1`
- [ ] GBP post (publish every Tuesday evening for Wednesday)

Why it's important: This is already Monkey Joe's best deal. Most people don't know it exists. The job is distribution, not invention.

---

**OFFER 3: Ten Tuesday — $10 + $10 Game Card**
Best for: Email, SMS, Google Ads promotion extension
What it is: $10 admission + $10 arcade game card (exceptional value)

Assets needed:
- [ ] Email template (standalone Tuesday deal email)
- [ ] SMS template
- [ ] Google Ads promotion extension (active Tuesdays only — schedule in advance)
- [ ] Social post graphic
- [ ] GBP post (publish Monday evening)

---

**OFFER 4: Birthday Party Booking — High-Value Conversion**
Best for: Google Ads (dedicated campaign), Facebook retargeting, email sequence
What it is: Reserve a private party room — setup to cleanup included

Assets needed:
- [ ] Dedicated birthday party landing page (NOT the general website page)
  - Hero: photo of a decorated party suite with happy kids
  - Headline: "Orlando's Most Fun Kids Birthday Party — We Handle Everything"
  - Includes: what's in each package, max headcount, price range, what parents don't have to do
  - CTA: "Reserve Your Party Date" (links to booking form or calendar)
  - Trust signals: Google star rating, photo reviews, safety callouts
  - Mobile-first: click-to-call, directions button, form max 4 fields
- [ ] Party inquiry form (Name, Email, Phone, Preferred Date)
- [ ] Automated confirmation email (Constant Contact): "We got your inquiry — here's what happens next"
- [ ] Follow-up call script for Nicole (what to say when she calls back)
- [ ] Party booking availability calendar (or clear process for Nicole to manage inquiries)
- [ ] 5–8 high-quality photos of party rooms, decorated setups, kids celebrating

What Michael needs to provide: Current package names, prices, headcount limits, what's included, available party time slots.

---

**OFFER 5: Coloring Pages PDF — Lead Magnet / Email Growth**
Best for: Facebook organic + paid (lead gen ads), website pop-up, email capture
What it is: Free printable kids coloring pages — instant download, email required

Assets needed:
- [ ] PDF coloring pages (8–12 pages minimum): Monkey Joe's characters + kid-friendly themes
  - Every page must include: Monkey Joe's logo, both location addresses, weekly deal schedule, website URL
  - Seasonal versions: "Rainy Day Activity Pack" (launch June), "Spring Break Fun Pack" (launch March)
- [ ] Dedicated landing page: "Free Printable Coloring Pages — Download Instantly"
  - Mockup image of the coloring book cover
  - 3-field form: Name + Email + Child's age range (Under 3 / 3–6 / 7–12)
- [ ] Automated delivery email in Constant Contact (fires immediately on form submit)
- [ ] 3-email welcome sequence (see email section)
- [ ] Facebook lead gen ad creative (image of coloring pages + headline)
- [ ] Promo code inside PDF: `COLORING` — 10% off next visit

Who creates the PDF: William to confirm — can be designed by Jess's team or sourced. AI image generation possible for illustrations.

---

**OFFER 6: Spring Break Pack — Seasonal Bundle**
Best for: Email campaign (mid-March), Google Ads (April)
What it is: 5 visits for $55 (saves ~$10 vs. full price), valid during school holidays

Assets needed:
- [ ] Physical or digital punch card / bundle voucher
- [ ] Landing page section or dedicated page
- [ ] Email campaign (deploy last week of March)
- [ ] Social graphic
- [ ] Promo code: `SPRING26`

What Michael needs to confirm: Is this bundle approved? How is it tracked/redeemed in Aluvy?

---

**OFFER 7: "Rainy Day Rate" — Seasonal Conversion**
Best for: Weather-triggered email + SMS (William's weather API integration)
What it is: Discounted weekday afternoon admission when rain is forecast

Assets needed:
- [ ] Email template (short, punchy — deploy same day as rain forecast)
- [ ] SMS template (see SMS section — this is ideal for SMS)
- [ ] Weather API connection (William's domain — Jess to provide email/SMS content)
- [ ] Promo code: `RAINDAY`

This is one of the highest-upside ideas in the whole campaign — Florida's rainy season runs June–September. Families are actively looking for indoor options when it's pouring at 3pm.

---

#### Website Improvements (Week 3)

**Priority changes — do not touch design, focus on conversion:**

1. **Homepage hero:** Add clear headline ("Orlando's Best Indoor Inflatable Play Center — Adults Always FREE"), add admission pricing with the deals visible, add a "Book a Birthday Party" CTA button above the fold
2. **Exit-intent pop-up:** Trigger when visitor is about to leave. Offer: "Before you go — get 10% off your first visit" → email capture form → delivers promo code via Constant Contact automation
3. **Sticky mobile header:** Phone number (click-to-call) + "Book a Party" button always visible on mobile scroll
4. **Birthday party page:** Rebuild per the landing page spec in Offer 4 above
5. **Add weekly deals prominently:** Monday Madness, Ten Tuesday, Wacky Wednesday need to be visible on the homepage, not buried in a menu
6. **Page speed:** Run through Google PageSpeed Insights — target under 2 seconds on mobile. Compress any images above 200KB.

**William to confirm:** Does Jess have WordPress editor access? Or does William need to brief a developer?

---

#### Google Business Profile Optimization (Week 3)

Both locations — do this before ads run. GBP is free traffic.

**Pointe Orlando + Winter Park — each profile:**

- [ ] Primary category: "Amusement center" → add secondary: "Children's party service", "Indoor playground", "Arcade"
- [ ] Description (750 chars): Lead with price point, adults free, daily deals, birthday parties, both locations
- [ ] Hours: Verify current and add special hours for school holidays, spring break
- [ ] Attributes: Wheelchair accessible, good for kids, good for groups, Wi-Fi, parking, credit cards
- [ ] Photos: Upload minimum 25 per location (kids in action, party rooms, staff, exterior, toddler zone)
  - William to request updated photos from Michael at kickoff — this was discussed on the call
  - File name format: `monkey-joes-orlando-birthday-party-room.jpg` (keywords in filename)
- [ ] Add all weekly deals as GBP Posts (schedule: Mon for Monday deal, Tue for BOGO preview, Fri for weekend)
- [ ] Q&A section: Pre-populate with 5 common questions (age range, birthday party process, parking, pricing, toddler zone)
- [ ] Review response: Respond to every existing review this week — signals responsiveness to Google

---

### Week 4: Email Setup & SMS Foundation

#### EMAIL LIST PREPARATION (Constant Contact)

Before sending a single email, segment the 20K list:

| Segment | Criteria | Size (est.) | First Campaign |
|---|---|---|---|
| Active | Opened/clicked in last 90 days | ~3–5K | Weekly deal emails |
| At-Risk | 90–180 days inactive | ~4–6K | Re-engagement sequence |
| Lapsed | 180+ days no activity | ~8–12K | Win-back sequence |
| Birthday Inquirers | Clicked birthday content (if trackable) | Varies | Birthday party drip |

**Do not blast all 20K at once.** Start with Active segment, then warm up At-Risk, then Lapsed. Sending to a cold list damages deliverability and can get the Constant Contact account flagged.

#### EMAIL AUTOMATIONS TO BUILD IN WEEK 4

**Automation 1: Website Pop-Up Welcome Series (3 emails)**
Triggered by: Exit-intent pop-up form submission

- Email 1 (immediate): Promo code delivery + "Here's everything you need to know about Monkey Joe's"
  - Weekly deal schedule (Mon/Tue/Wed specials)
  - Both locations + links to directions
  - "We can't wait to meet your family"
- Email 2 (Day 3): Highlight the deals — "Did you know Wednesdays are BOGO?"
  - Wacky Wednesday explainer, Monday Madness, Ten Tuesday
  - CTA: "Plan your visit"
- Email 3 (Day 7): Birthday party pitch — "Is a birthday coming up?"
  - "We handle everything — setup, cleanup, party host, invitations"
  - CTA: "Check party date availability"

**Automation 2: Coloring Pages Download Welcome Series (3 emails)**
Triggered by: Coloring pages landing page form submission

- Email 1 (immediate): PDF delivery + "Your coloring pages are here!"
  - Attach/link PDF
  - Quick intro to Monkey Joe's + weekly deals
- Email 2 (Day 3): "Your kids will love this" — venue walkthrough with photos
  - Toddler zone, inflatables, arcade, party rooms
  - First visit offer: `KIDFREE` promo code
- Email 3 (Day 7): Birthday party angle — "Next time could be their birthday party"

**Automation 3: Birthday Party Follow-Up (post-inquiry)**
Triggered by: Birthday party inquiry form submission

- Email 1 (immediate): "We got your enquiry! Here's what happens next"
  - Expected response time
  - What's included in each package (brief)
  - "Nicole will call you within 24 hours"
- Email 2 (if no booking in 5 days): "Still thinking about it?"
  - Party dates fill up fast (genuine urgency)
  - Social proof: recent party reviews
  - CTA: "Grab your date before it's gone"

#### REACTIVATION SEQUENCE — LAPSED LIST (8-week drip)

For the 180+ day inactive segment. Run this before any promotional emails to this group.

| Week | Subject Line | Content | CTA |
|---|---|---|---|
| 1 | "It's been a while… we saved something for you 🎈" | Warm, personal. Here's what you've been missing. Offer: BOGO coupon | Claim your BOGO |
| 3 | "Best way to beat the Orlando heat this [month]" | Seasonal hook. New photos. Toddler zone highlight | Plan a visit |
| 5 | "370 parents gave us 5 stars this month — here's why" | Pull real Google reviews. Ten Tuesday highlight | Come see for yourself |
| 7 | "Is your child's birthday coming up soon?" | Birthday party pitch. We handle everything | Check availability |
| 9 | "Last one from us — unless you want to stay 👋" | Acknowledge absence. Final offer: Kids Come Free. Opt-down option | Claim your offer |

After Week 9: Remove non-responders from active marketing list. This is standard list hygiene — do not skip this step.

---

#### SMS / TEXT MESSAGE STRATEGY

SMS is William's domain (AI-powered via Lanyu.ai) but Jess provides the content strategy and message copy. Include this in the kickoff briefing for William.

**Why SMS before advertising:**
- Average SMS open rate: 98% (vs. ~32% email)
- 90% of SMS messages are read within 3 minutes
- The existing audience (email list, FB followers) is warm — SMS reactivation will outperform cold ads
- Zero media spend required

**SMS Campaign Types to Build:**

**1. Reactivation Campaign (Week 4–8)**
Target: Lapsed customers whose phone numbers are in the Constant Contact list or Aluvy POS

Message 1 (Day 1):
> "Hey [First Name]! It's Monkey Joe's — we miss your family 🐒 It's been a while and we want you back. Here's a BOGO admission for your next visit: BOGOBACK. Expires [date]. Both locations: Pointe Orlando + Winter Park. Reply STOP to opt out."

Message 2 (Day 7, if no redemption):
> "Last chance [First Name] — your BOGO code BOGOBACK expires [date]. Kids love Tuesdays here: $10 admission + $10 game card. Come see us! [link] Reply STOP to opt out."

**2. Weekly Deal Alerts (Ongoing — Active Subscribers)**
Monday evening:
> "🐒 Monday Madness is BACK! $9.95 + $5 game card — today only at Monkey Joe's. Walk-ins welcome, no booking needed. [address links]"

Tuesday morning:
> "It's Ten Tuesday! $10 admission + $10 game card. Best deal of the week 👊 Monkey Joe's, Orlando + Winter Park."

**3. Birthday Party Reminder (Triggered by Age Data)**
If you have child age/birthday data from the coloring pages form or POS:
> "Hey [First Name]! [Child's name]'s birthday is coming up 🎂 Monkey Joe's birthday parties are fully handled — we do setup, cleanup, and the fun. Limited dates left this month. Grab yours: [link]"

**4. Weather-Triggered Campaign (William's Weather API — implement Month 2)**
Trigger: Rain forecast >70% probability in Orlando area
Send time: 6am same day

> "☔ Rain forecast today in Orlando! Perfect day to head to Monkey Joe's — 40+ inflatables, arcade, toddler zone. Walk in anytime. $9.95 Mondays, BOGO Wednesdays. Both locations open from 11am. [link]"

This is the highest-upside SMS campaign in the entire strategy. A rainy afternoon in summer = every parent in Orlando searching for indoor activities simultaneously. Being the first SMS in their phone that morning wins visits.

**5. Birthday Party Follow-Up SMS (Post-Inquiry)**
Send 48 hours after inquiry if no booking confirmed:
> "Hi [First Name], it's Monkey Joe's 🎉 Just checking in on [child's name]'s party! Party dates are filling up for [month]. Want to lock in your spot? Call us: [number] or book: [link]"

**SMS Platform Note:** William is handling the AI SMS infrastructure via Lanyu.ai. Jess to provide all message copy. Confirm with William: what platform (e.g., Attentive, Klaviyo, custom)? What opt-in mechanism for existing contacts? Compliance: TCPA opt-in required for all SMS recipients.

---

## PHASE 2: LAUNCH (Month 2 — Weeks 5–8)

**Conditions to meet before Phase 2 begins:**
- [ ] GA4, Pixel, CallRail all verified and tracking
- [ ] Promo codes set up in Aluvy, staff trained
- [ ] Birthday party landing page live
- [ ] At least one automated email sequence active
- [ ] GBP profiles updated and photos uploaded
- [ ] Michael has confirmed all offers and pricing

### Google Ads — Launch Structure

**Budget:** $1,500/month ($50/day) — Michael's budget, managed by Jess

| Campaign | Budget | Keywords |
|---|---|---|
| Search — Birthday Party | $600/month | Birthday party venue Orlando, kids birthday party near me, indoor birthday party Orlando |
| Search — Open Play | $500/month | Indoor playground Orlando, indoor play center Orlando, kids activities Orlando rainy day |
| Display Retargeting | $250/month | Website visitors (30-day), birthday page visitors (14-day) |
| Reserve | $150/month | Hold for testing / Performance Max in Month 3 |

**Campaign settings:**
- Location: 20-mile radius around each location (Central Florida)
- Language: English + Spanish (Orlando has large Spanish-speaking community — create Spanish ad variants Month 2)
- Bid strategy: Start with Maximize Clicks (CPC cap $3.00) → switch to Target CPA after 30 conversions
- Ad schedule: 6am–10pm daily; bid +20% Friday–Sunday; bid +20% 11am–7pm
- Device: +25% mobile bid adjustment

**Top Keywords to Launch With:**

*Birthday Party Campaign:*
- "birthday party venue Orlando" (phrase)
- "kids birthday party places near me" (phrase)
- "indoor birthday party Orlando" (phrase)
- "birthday party with inflatables Orlando" (phrase)
- [monkey joe's competitors] — Kidiverse, Pump It Up, Funtastic Depot (exact)

*Open Play Campaign:*
- "indoor playground Orlando" (phrase)
- "indoor play center Orlando FL" (phrase)
- "activities for kids rainy day Orlando" (phrase) ← low competition, HIGH intent
- "toddler indoor playground Orlando" (phrase)
- "things to do with kids Orlando" (broad — monitor closely)

**Negative keywords (add day 1):**
jobs, hiring, careers, outdoor playground, park, Disney, Universal, daycare, preschool, for sale, buy, DIY, dog park, adult, Miami, Tampa, Jacksonville

**Ad copy — 3 variations per ad group:**

Birthday Party:
1. "Orlando's Best Kids Birthday Party | We Handle Setup to Cleanup | Private Rooms + Party Host"
2. "Only [X] Party Dates Left | Inflatables, Arcade + Private Suite | Book Your Child's Birthday"
3. "Birthday Party Stress? We've Got It | $0 Cleanup. Zero Stress. 100% Fun | See Packages"

Open Play:
1. "Indoor Play Center Orlando | 40+ Inflatables, Toddler Zone, Arcade | Adults Always FREE"
2. "Rainy Day Sorted ☔ | $12.99 Kids, Adults Free | Walk In Anytime — No Booking Needed"
3. "Wacky Wednesday BOGO | Kids Play From $9.95 | Orlando's #1 Inflatable Play Center"

**Ad extensions — all active day 1:**
- Sitelinks: "Birthday Parties" / "Daily Deals" / "Toddler Zone" / "Directions"
- Callouts: "Adults Always Free" / "No Booking Required" / "Private Party Rooms" / "Clean & Safe"
- Call extensions: CallRail tracked numbers for each location
- Location extensions: Linked to both GBP profiles
- Promotion extensions: Active for Monday, Tuesday, Wednesday deals (scheduled by day)

### Facebook — Launch Structure

**Week 5 (1 week after Google Ads):**

Launch order:
1. Retargeting campaigns first (cheapest, warmest audience)
2. Email list custom audience (upload 20K → Facebook matches ~40–70%)
3. Prospecting (lookalike) campaigns — Week 6

| Campaign | Audience | Creative | Budget |
|---|---|---|---|
| Retargeting — website visitors | 30-day website visitors | BOGO Wednesday offer | $150/month |
| Retargeting — birthday page visitors | 14-day birthday page visitors | "Reserve your party date" | $100/month |
| Email list retargeting | 20K customer list custom audience | Kids Come Free offer | $150/month |
| Prospecting — lookalike | 1% lookalike of best customers | Venue walkthrough video | $300/month |
| Lead gen — coloring pages | Broad (parents, 25–45, Orlando) | Coloring pages download | $100/month |

**Ad formats:**
- Video (15–30 sec, vertical): Kids playing on inflatables — highest conversion for venue marketing
- Carousel: "5 reasons families love Monkey Joe's" — one card per reason
- Static with offer overlay: "BOGO Wednesday — Tag someone to bring along"
- Facebook lead gen ad: Coloring pages download (no landing page needed — native form)

---

## PHASE 3: OPTIMIZE (Month 3 — Weeks 9–12)

- Review all search term reports — expand winners, kill losers, add negatives
- Transition Google Ads to Target CPA bidding (requires 30+ conversions)
- Add Performance Max campaign ($150 budget — needs conversion history to work)
- Launch Spanish-language ad variants
- Add membership offer to email sequence for active visitors
- Introduce Spring Break Pack campaign (if April timing aligns)
- Scale Facebook lookalike audience (move from 1% to 2% if CPA holds)
- Birthday party follow-up SMS automation live
- Weather API SMS campaign live (William's infrastructure)
- Analyze which promo codes are redeeming most — double down on those channels

---

## TRACKING & ATTRIBUTION FRAMEWORK

**The challenge:** Walk-in traffic is the primary KPI but the hardest to attribute.

**Our multi-signal attribution model:**

| Signal | What It Proves | Tool |
|---|---|---|
| Promo code redemption in Aluvy | Direct revenue attribution by channel | Aluvy POS |
| Party bookings with UTM source | Full online-to-booking attribution | GA4 + Booking form |
| Phone calls (60+ sec) | Inbound interest driven by marketing | CallRail |
| Email opens → foot traffic correlation | Week-on-week traffic vs. campaign timing | Constant Contact + Aluvy |
| GA4 conversion events | Online actions tied to campaigns | GA4 |
| GBP direction requests | Local intent from search | GBP Insights |
| Facebook Pixel events | Ad impressions → website → visit | Meta Ads Manager |
| Website traffic trend vs. revenue trend | Macro correlation | GA4 + Aluvy |

**For William's 10% model:** Provable revenue = promo code redemptions + trackable party bookings. The other signals are supporting evidence, not primary proof. This needs to be agreed with Michael at kickoff — set expectations that walk-in attribution is imperfect but this model is industry standard.

**The live dashboard (Jess builds, William shares with Michael):**

Recommended: Looker Studio (free, connects GA4 + Google Ads + CallRail)

| Dashboard Page | What It Shows |
|---|---|
| Executive Summary | Monthly spend, conversions, cost per result, email stats |
| Google Ads | Campaign performance, top keywords, location split |
| Email Marketing | Open rates, click rates, list growth, reactivation progress |
| Phone Calls | Call volume by source, missed calls, call duration |
| Local Presence | GBP impressions, direction requests, reviews |
| Revenue Attribution | Promo code redemptions by channel, party bookings by source |

**Reporting cycle (as agreed on call):**
- Jess delivers report → William by **3rd of each month**
- William delivers to Michael by **5th of each month**
- Michael has until **15th to pay**, with 5-day window to contest

---

## COMPETITIVE LANDSCAPE — QUICK REFERENCE

| Venue | Child Admission | Adults | Strength | Monkey Joe's Edge |
|---|---|---|---|---|
| Kidiverse | ~$20.49 all-in | Varies | Ninja course, escape room | $7+ cheaper per child |
| Funtastic Depot | $14.95–$24.95 | Included | Live DJ weekends | Opens earlier, cheaper |
| Pump It Up | ~$9 open play | Included | Fully private parties | Walk-ins welcome daily |
| Rebounderz | ~$20/hour | Included | Trampolines, older kids | Toddler-friendly, cheaper |
| Millie Moo's | Varies | Included | Under-5 specialist | Larger, more activities |

**Monkey Joe's two biggest advantages — lead with these in all copy:**
1. **Adults always free** — most competitors charge adults
2. **Walk-in friendly, no reservations required** — Pump It Up requires booking; MJ is open door

---

## KEYWORD MASTER LIST

### Birthday Party (High Intent, $2–$4 CPC)
- birthday party venue Orlando
- kids birthday party places near me Orlando
- indoor birthday party Orlando FL
- birthday party with inflatables Orlando
- private birthday party rooms Orlando
- birthday party venue Winter Park FL

### Open Play (Volume, $1–$2.50 CPC)
- indoor playground Orlando
- indoor play center Orlando FL
- indoor play center Winter Park
- toddler indoor playground Orlando
- family fun center Orlando
- inflatable playground Orlando
- children's entertainment center Orlando

### Rainy Day / Situational (Low CPC, High Intent)
- activities for kids on rainy day Orlando ← William flagged this specifically as underpriced
- indoor activities for kids Orlando rain
- rainy day family fun Orlando
- what to do with kids today Orlando
- indoor fun for kids Central Florida

### Local Modifiers (Add to all campaigns)
Winter Park, Pointe Orlando, International Drive, Altamonte Springs, Maitland, Oviedo, Casselberry, Lake Mary, Longwood, Kissimmee, Doctor Phillips, Hunter's Creek

### Negative Keywords (Add Day 1)
jobs, hiring, careers, outdoor, park, equipment for sale, buy bounce house, daycare, preschool, Disney, Universal, water park, dog park, adult, Miami, Tampa, Jacksonville, Gainesville

---

## ASSET ACQUISITION CHECKLIST

Everything needed before a single dollar of ad spend:

**From Michael/Nicole (request at kickoff):**
- [ ] Login credentials / admin access for all platforms (see Week 1 list)
- [ ] 30–50 high-quality photos of each venue (kids playing, party rooms, exterior, toddler zone, staff)
- [ ] Video footage of kids on inflatables (even iPhone video is fine — vertical preferred)
- [ ] Confirmation of all offer approvals (Kids Come Free, promo codes, Spring Break Pack)
- [ ] Birthday party package details (names, prices, inclusions, headcount limits, time slots)
- [ ] Aluvy reporting access for promo code tracking
- [ ] Staff agreement to ask "do you have a promo code?" at POS
- [ ] Confirmation of Constant Contact access and current list state
- [ ] Any existing brand guidelines (logo files, colors, fonts)

**To Build (Jess/William):**
- [ ] Coloring pages PDF (Monkey Joe's branded, 8–12 pages)
- [ ] Birthday party landing page
- [ ] Open play landing page
- [ ] Coloring pages lead magnet landing page
- [ ] Exit-intent pop-up for website
- [ ] Email automation sequences (3 automations, see Week 4)
- [ ] Reactivation email sequence (5 emails)
- [ ] SMS message copy (all templates)
- [ ] Ad creative (social graphics, ad images)
- [ ] Looker Studio dashboard

---

## WHAT SUCCESS LOOKS LIKE

**End of Month 1 (Foundation):**
- All tracking installed and verified
- All offers approved and assets built
- GBP profiles optimized, 25+ photos per location
- Email list segmented, automations live
- Reactivation sequence deployed to lapsed segment

**End of Month 2 (Launch):**
- Google Ads running — tracking 50+ clicks/day
- Facebook retargeting live, email list uploaded as custom audience
- 500+ new email subscribers from coloring pages lead magnet
- First promo code redemptions tracked in Aluvy
- Birthday party inquiries generating via landing page

**End of Month 3 (Proof):**
- Provable revenue via promo codes = $X (establish baseline for William's 10% model)
- Party bookings attributed to ads/email = Y bookings
- Google Ads cost per birthday inquiry < $40
- Email list grown from 20K to 22K+
- GBP direction requests up 30% vs. baseline

---

## QUICK WINS TO DO THIS WEEK

1. Send William the access list — get all platform logins before kickoff
2. Request photos from Michael at kickoff — can't optimize GBP or run ads without them
3. Screenshot current GBP profiles and website (before state for reporting)
4. Start the coloring pages PDF design — this is the lead magnet that costs nothing to distribute
5. Confirm all offers with Michael at kickoff — no campaigns launch without approved offers

---

*Next document: Kickoff presentation / strategy overview for Michael and Nicole*
*Roadmap version: 1.0 — March 2026*
*Built by Jess Morrell / WILBA for Lanyu.ai × Monkey Joe's*
