# 🐒 Monkey Joe's — Digital Marketing Strategy & Roadmap

**Client:** Michael Carter — Monkey Joe's, Pointe Orlando + Winter Park
**Prepared by:** Jess Morrell / WILBA × Lanyu.ai
**Engagement:** 3-Month Pilot | March–June 2026
**Upside:** 9 MJ locations → Big Game Brands (130+ locations)

---

## ⚠️ The Core Rule: Fix the Leaky Bucket First

> **Month 1 = zero ad spend.**
> Every dollar of the $1,500/month ad budget stays in the account until tracking is installed, offers are built, and the attribution system is live.
> Launching ads before this foundation exists wastes money and makes results impossible to prove.

---

## 📋 Phase Overview

| Phase | Timeline | Focus | Ad Spend |
|---|---|---|---|
| **Phase 1: Foundation** | Weeks 1–4 | Tracking, offers, assets, email setup | $0 |
| **Phase 2: Launch** | Weeks 5–8 | Google Ads, Facebook, email campaigns live | $1,500/mo |
| **Phase 3: Optimise** | Weeks 9–12 | Scale what works, prove revenue for William | $1,500/mo |

---

# Phase 1: Foundation (Weeks 1–4)

## 🔑 Week 1 — Access & Audit

> Get every login before the kickoff call. Nothing can be built without access.

**Access needed from Michael/Nicole:**

- [ ] Google Ads — Admin access
- [ ] Google Analytics 4 (GA4) — Admin access
- [ ] Google Business Profile — Owner/Manager (both locations)
- [ ] Facebook Business Manager — Admin access
- [ ] Constant Contact — Admin or campaign manager access
- [ ] WordPress — Editor or admin access
- [ ] CallRail — Admin access
- [ ] Aluvy (POS system) — Read/reporting access

**Audit tasks (no access needed):**

- [ ] Screenshot current GBP profiles — both locations (before state)
- [ ] Review website: load speed, mobile usability, offers, booking flow
- [ ] Pull Constant Contact stats: total contacts, recent open rates, last send date
- [ ] Check if Facebook Pixel is already installed
- [ ] Search competitor keywords in Google — screenshot what ads are showing
- [ ] Pull existing Google Ads history if account exists

---

## 📡 Week 2 — Tracking Installation

> **Nothing launches until every item below is checked and verified.**

### Install order:

**1. Google Tag Manager (GTM)**
Install GTM on WordPress first. All other tags (GA4, Pixel, CallRail) fire through GTM — no developer needed for future changes.

- [ ] GTM container installed on website
- [ ] GTM fires on all key pages: homepage, birthday party page, pricing, contact, thank-you

**2. GA4 Setup**

- [ ] GA4 property confirmed or created
- [ ] Two data streams if locations have separate pages
- [ ] Conversion events configured:
  - [ ] `birthday_party_inquiry` — party form submissions
  - [ ] `phone_call_click` — clicks on phone numbers
  - [ ] `coupon_download` — PDF lead magnet downloads
  - [ ] `email_signup` — pop-up or form captures
  - [ ] `directions_click` — Google Maps links
- [ ] Internal IP filters (exclude Michael's office, William's office, Jess's IP)
- [ ] GA4 linked to Google Ads account

**3. Facebook Pixel**

- [ ] Meta Pixel installed via GTM
- [ ] Standard events configured: `PageView`, `ViewContent` (birthday page), `Lead`, `Contact`
- [ ] Verified with Facebook Pixel Helper extension
- [ ] 20K email list uploaded as Customer List Custom Audience

**4. CallRail**

- [ ] Tracked number created for Pointe Orlando
- [ ] Tracked number created for Winter Park
- [ ] Third number for Google Ads call extensions
- [ ] CallRail connected to Google Ads (import 60+ sec calls as conversions)
- [ ] CallRail connected to GA4

**5. Promo Code Attribution System**

> This is how we prove walk-in revenue to Michael. Staff must ask "do you have a promo code?" at the POS — this needs to be trained at kickoff.

| Code | Channel |
|---|---|
| `EMAIL10` | Email campaigns |
| `FB10` | Facebook ads |
| `GOOGLE10` | Google Ads |
| `SMS10` | Text message campaigns |
| `COLORING` | Coloring pages lead magnet |
| `KIDFREE` | Kids Come Free offer |
| `BOGO` | Wacky Wednesday |
| `RAINDAY` | Rainy day campaigns |

- [ ] All codes created in Aluvy
- [ ] Staff trained to ask for code at POS
- [ ] Redemption reporting confirmed in Aluvy

---

## 🎁 Week 3 — Offers & Assets

> **No campaign launches without its assets complete. Build before you spend.**

---

### Offer 1: Kids Come Free 🆓
*Primary acquisition offer — removes all barriers for first-time families*

**What it is:** One child free with paying adult admission (first-time visit only)
**Best for:** Email reactivation, Facebook retargeting, Google Ads, SMS

**Assets needed:**

- [ ] Dedicated landing page (not the homepage)
- [ ] Email capture form: Name + Email + Child age range
- [ ] Automated confirmation email in Constant Contact (delivers offer + venue info)
- [ ] Promo code: `KIDFREE`
- [ ] Staff redemption process confirmed in Aluvy
- [ ] Social media graphic (1080×1080 Instagram, 1200×628 Facebook)
- [ ] Email banner image

**Confirm with Michael:** Approved? Max redemptions per family? Expiry date?

---

### Offer 2: Wacky Wednesday BOGO 🎟️
*Already exists — the job is distribution, not invention*

**What it is:** Buy one get one free admission — Wednesdays only
**Best for:** Email, Facebook organic, retargeting, SMS

**Assets needed:**

- [ ] Dedicated landing page or clear webpage
- [ ] Weekly email template (reusable every Wednesday)
- [ ] Social media graphic (Wednesday-specific)
- [ ] SMS template
- [ ] Google Ads promotion extension (scheduled Wednesdays only)
- [ ] GBP post (publish Tuesday evening each week)
- [ ] Promo code: `BOGO`

---

### Offer 3: Ten Tuesday 🎮
*Exceptional value — $10 admission + $10 game card*

**Best for:** Email, SMS, Google Ads promotion extension

**Assets needed:**

- [ ] Email template (standalone Tuesday deal)
- [ ] SMS template
- [ ] Google Ads promotion extension (active Tuesdays only)
- [ ] Social post graphic
- [ ] GBP post (publish Monday evening)

---

### Offer 4: Birthday Party Booking 🎂
*Highest conversion value in the entire campaign*

**What it is:** Reserve a private party room — setup to cleanup included, party host provided
**Best for:** Google Ads (dedicated campaign), Facebook retargeting, email sequence

**Landing page requirements:**

- [ ] Hero: Photo of decorated party suite with happy kids
- [ ] Headline: "Orlando's Most Fun Kids Birthday Party — We Handle Everything"
- [ ] Package details: names, inclusions, prices, max headcount
- [ ] Single CTA: "Reserve Your Party Date" → booking form
- [ ] Trust signals: Google star rating, safety callouts, real parent photos (not stock)
- [ ] Mobile: click-to-call, directions button, max 4-field form
- [ ] Inquiry form: Name + Email + Phone + Preferred Date

**Assets needed:**

- [ ] Birthday party landing page (spec above)
- [ ] Party inquiry form
- [ ] Automated confirmation email: "We got your enquiry — Nicole will call within 24 hours"
- [ ] Birthday party follow-up email (if no booking in 5 days)
- [ ] 5–8 high-quality photos of party rooms and decorated setups
- [ ] Nicole's call-back script

**Get from Michael:** Current package names, prices, headcount limits, available time slots.

---

### Offer 5: Coloring Pages PDF 🖍️
*Free lead magnet — email capture, costs nothing to distribute*

**What it is:** Free printable kids coloring pages — instant download, email required
**Best for:** Facebook organic + paid lead gen, website pop-up, email list growth

**Why it works:** Every parent who downloads a children's coloring PDF has a child — exactly the audience needed. The PDF lives in their home as marketing collateral.

**PDF requirements:**

- [ ] 8–12 pages minimum (Monkey Joe's characters + kid themes)
- [ ] Every page includes: MJ logo, both location addresses, weekly deal schedule, website URL
- [ ] Seasonal versions: "Rainy Day Activity Pack" (June), "Spring Break Fun Pack" (now)
- [ ] Promo code on back page: `COLORING` — 10% off next visit

**Assets needed:**

- [ ] PDF designed and approved
- [ ] Dedicated landing page: "Free Printable Coloring Pages — Download Instantly"
  - Mockup image of coloring book cover
  - 3-field form: Name + Email + Child's age range (Under 3 / 3–6 / 7–12)
- [ ] Automated delivery email in Constant Contact (fires immediately on submit)
- [ ] 3-email welcome sequence (see email section)
- [ ] Facebook lead gen ad creative

---

### Offer 6: Spring Break Pack 🌊
*Seasonal bundle — 5 visits for $55 (saves ~$10)*

**Best for:** Email campaign (deploy now), Google Ads April

**Assets needed:**

- [ ] Bundle voucher or punch card mechanism
- [ ] Landing page section
- [ ] Email campaign (deploy last week of March)
- [ ] Social graphic
- [ ] Promo code: `SPRING26`

**Confirm with Michael:** Approved? How is it tracked/redeemed in Aluvy?

---

### Offer 7: Rainy Day Rate ☔
*Weather-triggered — highest upside campaign in the whole strategy*

**What it is:** Targeted message when rain is forecast in Orlando (Florida rainy season = June–September)
**Best for:** Weather-triggered SMS (William's weather API) + email

**Why it matters:** Florida's wet season brings afternoon storms almost daily. Parents are actively searching for indoor options. Being first in their SMS at 6am wins the visit.

**Assets needed:**

- [ ] Email template (short, urgent — same-day deployment)
- [ ] SMS template (see SMS section)
- [ ] Weather API connection (William's infrastructure — Jess provides copy)
- [ ] Promo code: `RAINDAY`

---

### Website Quick Wins (Week 3)

- [ ] **Homepage hero:** Clear headline + admission price + deals visible above the fold
- [ ] **Exit-intent pop-up:** "Before you go — 10% off your first visit" → email capture
- [ ] **Sticky mobile header:** Click-to-call + "Book a Party" button always visible on scroll
- [ ] **Birthday party page:** Rebuild to spec (see Offer 4)
- [ ] **Weekly deals prominent:** Monday Madness, Ten Tuesday, BOGO visible on homepage
- [ ] **Page speed:** Run Google PageSpeed Insights — target under 2 seconds mobile

---

### Google Business Profile (Week 3)

*Do this before any ads. Free traffic.*

**Both locations:**

- [ ] Primary category: "Amusement center"
- [ ] Secondary categories: "Children's party service", "Indoor playground", "Arcade"
- [ ] Description updated (lead with price, adults free, daily deals, birthday parties)
- [ ] Hours verified + special holiday hours added
- [ ] 25+ photos uploaded per location (kids, party rooms, staff, exterior, toddler zone)
- [ ] Weekly GBP posts scheduled (Mon/Tue/Fri + seasonal)
- [ ] Q&A section pre-populated (5 common questions)
- [ ] All existing reviews responded to

---

## 📧 Week 4 — Email & SMS Setup

### Email List Segmentation

> Do not blast all 20K at once — it damages deliverability and can flag the account.

| Segment | Criteria | Est. Size | First Action |
|---|---|---|---|
| Active | Opened/clicked last 90 days | ~3–5K | Weekly deal emails |
| At-Risk | 90–180 days inactive | ~4–6K | Re-engagement sequence |
| Lapsed | 180+ days no activity | ~8–12K | Win-back sequence |
| Birthday Inquirers | Clicked birthday content | Varies | Birthday party drip |

---

### Email Automations to Build

**Automation 1: Website Pop-Up Welcome (3 emails)**

| Email | Timing | Content |
|---|---|---|
| Email 1 | Immediate | Promo code delivery + venue intro + weekly deal schedule |
| Email 2 | Day 3 | "Did you know Wednesdays are BOGO?" — deals explainer |
| Email 3 | Day 7 | Birthday party pitch — "we handle everything" |

**Automation 2: Coloring Pages Welcome (3 emails)**

| Email | Timing | Content |
|---|---|---|
| Email 1 | Immediate | PDF delivery + intro to Monkey Joe's |
| Email 2 | Day 3 | Venue walkthrough with photos + `KIDFREE` code |
| Email 3 | Day 7 | Birthday party angle — "Next time could be their birthday" |

**Automation 3: Birthday Party Inquiry Follow-Up**

| Email | Timing | Content |
|---|---|---|
| Email 1 | Immediate | "We got your enquiry — Nicole will call within 24 hours" |
| Email 2 | Day 5 (if no booking) | "Still thinking about it? Party dates are filling up" |

---

### Lapsed List Reactivation Sequence (8 weeks)

| Week | Subject Line | Offer |
|---|---|---|
| 1 | "It's been a while… we saved something for you 🎈" | BOGO coupon |
| 3 | "Best way to beat the Orlando heat this [month]" | New photos + Ten Tuesday |
| 5 | "370 parents gave us 5 stars this month — here's why" | Reviews + deals |
| 7 | "Is your child's birthday coming up soon?" | Birthday party pitch |
| 9 | "Last one from us — unless you want to stay 👋" | Kids Come Free — final offer |

> After Week 9: Remove non-responders from the active list. Non-negotiable list hygiene step.

---

### 📱 SMS / Text Message Strategy

> Average SMS open rate: **98%** vs ~32% email. 90% read within 3 minutes. Zero media spend.
> **William handles the infrastructure (Lanyu.ai). Jess provides all copy.**

---

**SMS 1: Reactivation Campaign (Weeks 4–8)**

*Target: Lapsed customers in Constant Contact or Aluvy with phone numbers*

> Hey [First Name]! It's Monkey Joe's — we miss your family 🐒 It's been a while and we want you back. Here's a BOGO for your next visit: **BOGOBACK**. Expires [date]. Pointe Orlando + Winter Park. Reply STOP to opt out.

*Day 7 follow-up (if unredeemed):*

> Last chance [First Name] — your BOGO code BOGOBACK expires [date]. Kids love Tuesdays here: $10 admission + $10 game card. Come see us! Reply STOP to opt out.

---

**SMS 2: Weekly Deal Alerts (Active Subscribers)**

*Monday evening:*
> 🐒 Monday Madness is BACK! $9.95 + $5 game card — today only at Monkey Joe's. Walk-ins welcome. Both locations open now.

*Tuesday morning:*
> It's Ten Tuesday! $10 admission + $10 game card. Best deal of the week 👊 Monkey Joe's, Orlando + Winter Park.

---

**SMS 3: Birthday Party Reminder (Age-Triggered)**

> Hey [First Name]! [Child's name]'s birthday is coming up 🎂 Monkey Joe's parties are fully handled — setup, cleanup, party host, invitations. Limited dates left this month. Grab yours: [link]

---

**SMS 4: Rainy Day (Weather API — William's infrastructure)**

*Trigger: Rain forecast >70% probability in Orlando. Send time: 6am.*

> ☔ Rain forecast today in Orlando! Perfect day for Monkey Joe's — 40+ inflatables, arcade, toddler zone. Walk in anytime. $9.95 Mondays, BOGO Wednesdays. Open from 11am. [link]

**This is the highest-upside campaign in the strategy.** Florida's rainy season (June–September) = every Orlando parent searching for indoor options at the same time. First SMS in their phone wins.

---

**SMS 5: Birthday Party Follow-Up (Post-Inquiry)**

> Hi [First Name], it's Monkey Joe's 🎉 Just following up on [child's name]'s party! Dates are filling up for [month]. Want to lock in your spot? Call: [number] or book: [link]

> ⚠️ TCPA compliance: All SMS recipients must have opted in. Confirm opt-in mechanism with William before launching any SMS campaign.

---

# Phase 2: Launch (Weeks 5–8)

> **Go condition:** All Phase 1 checkboxes complete. Every item verified. Then — and only then — turn on ad spend.

---

## Google Ads — $1,500/Month Structure

| Campaign | Monthly Budget | Focus |
|---|---|---|
| Search — Birthday Party | $600 | Highest value conversions |
| Search — Open Play / General | $500 | Volume + foot traffic |
| Display Retargeting | $250 | Website visitors, warm audiences |
| Reserve / Testing | $150 | Performance Max (Month 3) |

**Settings:**
- Location: 20-mile radius each location
- Language: English + Spanish (large Spanish-speaking population in Orlando)
- Bid strategy: Maximize Clicks (CPC cap $3.00) → switch to Target CPA after 30 conversions
- Schedule: 6am–10pm daily | +20% bid Friday–Sunday | +20% bid 11am–7pm

---

### Top Keywords

**Birthday Party (High Intent — $2–$4 CPC)**
- birthday party venue Orlando
- kids birthday party places near me Orlando
- indoor birthday party Orlando FL
- birthday party with inflatables Orlando
- birthday party venue Winter Park FL

**Open Play (Volume — $1–$2.50 CPC)**
- indoor playground Orlando
- indoor play center Orlando FL
- toddler indoor playground Orlando
- family fun center Orlando
- inflatable playground Orlando

**Rainy Day / Situational (Low CPC, High Intent)**
- activities for kids on rainy day Orlando ← underpriced, high intent
- indoor activities for kids Orlando rain
- rainy day family fun Orlando
- what to do with kids today Orlando

**Negative Keywords (add Day 1)**
jobs, hiring, outdoor, park, equipment for sale, buy bounce house, daycare, preschool, Disney, Universal, water park, dog park, adult, Miami, Tampa, Jacksonville

---

### Ad Extensions (All Active Day 1)

| Extension | Content |
|---|---|
| Sitelinks | Birthday Parties / Daily Deals / Toddler Zone / Directions |
| Callouts | Adults Always Free / No Booking Required / Private Party Rooms / Clean & Safe |
| Call Extensions | CallRail tracked numbers per location |
| Location | Both GBP profiles linked |
| Promotion | Mon Madness / Ten Tuesday / Wacky Wednesday (scheduled by day) |

---

### Ad Copy — Birthday Party Campaign

1. "Orlando's Best Kids Birthday Party | We Handle Setup to Cleanup | Private Rooms + Party Host"
2. "Only [X] Party Dates Left | Inflatables, Arcade + Private Suite | Book Your Child's Birthday"
3. "Birthday Party Stress? We've Got It | $0 Cleanup. Zero Stress. 100% Fun | See Packages"

### Ad Copy — Open Play Campaign

1. "Indoor Play Center Orlando | 40+ Inflatables, Toddler Zone, Arcade | Adults Always FREE"
2. "Rainy Day Sorted ☔ | $12.99 Kids, Adults Free | Walk In Anytime — No Booking Needed"
3. "Wacky Wednesday BOGO | Kids Play From $9.95 | Orlando's #1 Inflatable Play Center"

---

## Facebook — Launch Structure

> Launch Facebook **one week after** Google Ads. Retargeting first, prospecting second.

| Campaign | Audience | Creative | Budget/Month |
|---|---|---|---|
| Retargeting — website visitors | 30-day website visitors | BOGO Wednesday offer | $150 |
| Retargeting — birthday page | 14-day birthday page visitors | "Reserve your party date" | $100 |
| Email list retargeting | 20K customer list custom audience | Kids Come Free | $150 |
| Prospecting — lookalike | 1% lookalike of best customers | Venue video (15–30 sec) | $300 |
| Lead gen — coloring pages | Parents 25–45, Orlando | Coloring pages download | $100 |

**Best performing ad formats for kids venues:**
1. **Short video (15–30 sec, vertical)** — kids on inflatables, birthday moments — highest conversion
2. **Carousel** — "5 reasons families love Monkey Joe's" — one card per reason
3. **Static with offer overlay** — "BOGO Wednesday — Tag someone to bring along"
4. **Facebook Lead Gen Ad** — coloring pages download (native form, no landing page needed)

---

# Phase 3: Optimise (Weeks 9–12)

- [ ] Review all search term reports — expand winners, cut losers, add negatives
- [ ] Transition Google Ads to Target CPA (requires 30+ conversions tracked)
- [ ] Add Performance Max campaign ($150 budget)
- [ ] Launch Spanish-language ad variants
- [ ] Add membership offer to email sequence for active visitors
- [ ] Scale Facebook lookalike to 2% if CPA holds
- [ ] Birthday party SMS automation live
- [ ] Weather API SMS campaign live (William's infrastructure)
- [ ] Analyse which promo codes are redeeming most — double down on those channels

---

# 📊 Tracking & Attribution Framework

> **The challenge:** Walk-in traffic is the primary KPI but the hardest to attribute.
> **Our model:** Multi-signal attribution — promo codes + digital tracking + POS correlation.

| Signal | What It Proves | Tool |
|---|---|---|
| Promo code redemption | Direct revenue attribution by channel | Aluvy POS |
| Party bookings with UTM | Full online-to-booking attribution | GA4 + booking form |
| Phone calls (60+ sec) | Inbound interest driven by marketing | CallRail |
| Email opens vs. foot traffic | Week-on-week campaign correlation | Constant Contact + Aluvy |
| GBP direction requests | Local intent from search | GBP Insights |
| Facebook Pixel events | Ad → website → visit chain | Meta Ads Manager |
| Website traffic trend | Macro correlation to revenue | GA4 + Aluvy |

> **For William's 10% model:** Provable revenue = promo code redemptions + trackable party bookings. Set this expectation clearly with Michael at kickoff.

---

## 📈 Live Dashboard Structure (Looker Studio)

*Jess builds → William shares view-only link with Michael. Free tool, connects GA4 + Google Ads + CallRail.*

| Page | What It Shows |
|---|---|
| Executive Summary | Monthly spend, conversions, cost per result, email stats |
| Google Ads | Campaign performance, top keywords, location split |
| Email Marketing | Open rates, click rates, list growth, reactivation progress |
| Phone Calls | Volume by source, missed calls, call duration |
| Local Presence | GBP impressions, direction requests, reviews by location |
| Revenue Attribution | Promo code redemptions by channel, party bookings by source |

**Reporting cycle:**

- Jess → William: Report by **3rd of each month**
- William → Michael: Report by **5th of each month**
- Michael pays by **15th** (5-day window to contest)

---

# 🏆 Competitive Snapshot

| Venue | Child Admission | Adults | Monkey Joe's Edge |
|---|---|---|---|
| **Monkey Joe's** | $12.99–$13.99 | **FREE** | — |
| Kidiverse | ~$20.49 all-in | Varies | $7+ cheaper per child |
| Funtastic Depot | $14.95–$24.95 | Included | Opens earlier, cheaper |
| Pump It Up | ~$9 open play | Included | Walk-ins welcome daily |
| Rebounderz | ~$20/hour | Included | Toddler-friendly, cheaper |

> **Lead with these two in every ad, email, and landing page:**
> 1. Adults always free — most competitors charge adults
> 2. Walk-in friendly, no reservations required

---

# ✅ What Success Looks Like

**End of Month 1 — Foundation**
- All tracking installed and verified
- All offers approved, assets built
- GBP optimised, 25+ photos per location uploaded
- Email list segmented, automations live
- Reactivation sequence deployed to lapsed segment

**End of Month 2 — Launch**
- Google Ads running — 50+ clicks/day
- Facebook retargeting live, email list uploaded as custom audience
- 500+ new email subscribers from coloring pages lead magnet
- First promo code redemptions tracked in Aluvy
- Birthday party inquiries coming through landing page

**End of Month 3 — Proof**
- Provable revenue via promo codes established (William's 10% baseline)
- Party bookings attributed to specific channels
- Google Ads cost per birthday inquiry < $40
- Email list grown from 20K to 22K+
- GBP direction requests up 30% vs. baseline
- Case study ready to pitch 9 MJ locations + Big Game Brands

---

# ⚡ Quick Wins This Week

1. **Send William the access list** — get all platform logins before kickoff
2. **Request photos from Michael at kickoff** — can't run any ads or optimise GBP without them
3. **Screenshot current GBP profiles and website** — before state for reporting
4. **Start the coloring pages PDF** — highest ROI lead magnet, zero media spend to distribute
5. **Confirm all offers with Michael** — no campaign launches without approved offers and promo codes in Aluvy

---

*Strategy v1.0 — March 2026*
*WILBA × Lanyu.ai × Monkey Joe's*
