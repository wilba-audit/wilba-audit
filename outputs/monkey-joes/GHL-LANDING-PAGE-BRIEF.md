# Monkey Joe's — GoHighLevel Landing Page Brief
### Template Build Spec for William. Build Once. Clone Per Location.

**Prepared by:** Jess Morrell / WILBA
**For:** William Milner / Lanyu (developer build)
**Platform:** GoHighLevel (GHL)
**Last updated:** March 2026

---

## OVERVIEW — WHY GHL AND HOW IT SCALES

We are building this in GoHighLevel because:

1. **One template, 56 locations.** Build the funnel once → clone the sub-account per location → swap the location-specific variables (address, phone, promo code, reviews). Done in under an hour per new location.
2. **Email + landing pages + SMS in one platform.** No need for Constant Contact + WordPress + a separate SMS tool.
3. **This becomes the product we pitch to Big Game Brands corporate.** Every asset we build should look polished enough to present to a 130-location franchise parent company.

---

## GHL SUB-ACCOUNT STRUCTURE

| Sub-Account | Location | Live Promo Codes |
|---|---|---|
| `MJ-Pointe-Orlando` | 9101 International Dr, Orlando FL | `WACKY-POL`, `KIDS50-POL` |
| `MJ-Winter-Park` | [Address — William to confirm with Michael] | `WACKY-WP`, `KIDS50-WP` |

**Each sub-account contains:**
- 2 landing pages (one per offer)
- Email automation sequences (loaded from `EMAIL-SEQUENCES.md`)
- GHL pipeline: Lead → Booked → Visited → Upsold
- Contact records with tags (BOGO, 50OFF, JumperCard, BirthdayInquiry)

---

## PAGES TO BUILD (Per Location = 4 Pages Total × 2 Locations = 8 Pages)

| Page | URL Slug | Offer | Promo Code |
|---|---|---|---|
| BOGO — Pointe Orlando | `/bogo-orlando` | Buy One Get One Free, weekdays | `WACKY-POL` |
| 50% Off — Pointe Orlando | `/halfprice-orlando` | 50% off ages 3–12, weekdays | `KIDS50-POL` |
| BOGO — Winter Park | `/bogo-winterpark` | Buy One Get One Free, weekdays | `WACKY-WP` |
| 50% Off — Winter Park | `/halfprice-winterpark` | 50% off ages 3–12, weekdays | `KIDS50-WP` |

> **Birthday Party landing page** — add in Phase 2 once the pilot is running. Specs below for reference.

---

## GLOBAL DESIGN RULES (Apply to All Pages)

- **Mobile-first.** Most clicks will come from phones. Test every page on iPhone and Android before any ads go live.
- **No navigation menu.** Landing pages have one job: convert. Remove any top nav or footer links that lead people away.
- **One offer. One CTA.** No distractions. No "also check out our weekly deals" links. Just the offer and the button.
- **Page load target:** Under 3 seconds on mobile. Compress all images.
- **Brand colours:** Monkey Joe's red (#CC0000 or confirm with Michael) + white + dark grey. Monkey logo top left or top centre.
- **Font:** [Confirm with Michael — corporate brand guidelines may specify]
- **CTA button colour:** High contrast — green (#00A651) or bright red against white background. Never grey.

---

---

## LANDING PAGE TEMPLATE — BOGO OFFER

*Use this spec for both `/bogo-orlando` and `/bogo-winterpark`. Variables in [brackets] change per location.*

---

### SECTION 1 — Hero (Above the Fold)

**Purpose:** Stop the scroll. Make the offer undeniably clear in 3 seconds.

**Elements:**
- Monkey Joe's logo (top left or centre)
- Background: Action photo of kids on inflatables (bright, energetic, real kids not stock photos). Request from Michael.
- Overlay: semi-transparent dark layer so text is readable

**Headline (large, bold, unmissable):**
> Buy One Kid's Admission, Get One FREE

**Subheadline:**
> Weekdays Only — Walk In Any Time. No Booking Required.

**Location badge (make this visible):**
> 📍 [Pointe Orlando / Winter Park] — [Full address]

**CTA Button (large, above the fold, high contrast):**
> [Claim Your Free Admission →]

*Button links to: Aloovy checkout URL with promo code pre-filled*

**Fine print under button (small text):**
> Valid Mon–Fri, ages 3–12. Code [WACKY-POL / WACKY-WP] applied at checkout. Not valid with other offers. [Florida residents only — Pointe Orlando only.] One use per household.

---

### SECTION 2 — Three Key Facts (Trust Builders)

**Purpose:** Answer the "is this legit?" question immediately. Use icon + text format.

| Icon | Text |
|---|---|
| 🎟️ | **Buy One, Get One Free** — one kid pays, one jumps free |
| 🕙 | **Weekdays Only** (Mon–Fri) — walk in anytime during opening hours |
| 👨‍👩‍👧 | **Adults Always Free** — every visit, no exceptions |

---

### SECTION 3 — What's Inside

**Purpose:** Show, don't tell. Parents need to know their kids will actually love it.

**Headline:**
> 40+ Inflatables. Arcade. Toddler Zone. And You're Always Free.

**Layout:** 2×2 or 1×4 photo grid with captions.

| Photo | Caption |
|---|---|
| Kids on giant inflatable | 40+ Bounce Houses & Slides |
| Toddler area | Dedicated Toddler Zone (Ages 2–5) |
| Arcade photo | Arcade Games & Prizes |
| Party room photo | Private Birthday Party Suites |

> **Photos needed from Michael:** Real venue photos. No stock. Request at next touchpoint.

---

### SECTION 4 — Social Proof (Google Reviews)

**Purpose:** Overcome hesitation with real parent voices.

**Headline:**
> What Orlando Families Are Saying

**Layout:** 2–3 review cards. Pull from Google Maps.

```
⭐⭐⭐⭐⭐
"[Real Google review text — pull top 3 most relevant]"
— [First name, last initial] via Google
```

**Below reviews:**
> [X] five-star reviews on Google · [Star rating] average

*Pull reviews using [Google Business Profile] — at least 2 per page. Request from Michael if they don't have admin access yet.*

---

### SECTION 5 — How It Works (Remove Friction)

**Purpose:** Make redeeming feel effortless.

**Headline:**
> Here's How to Use Your Offer

**3 steps, icon + text:**

1. 🖱️ **Click the button below** — your promo code is already applied at checkout
2. 📅 **Pick your weekday visit** — any Monday through Friday
3. 🎟️ **Show your confirmation at the door** — and jump in!

**CTA Button (repeat):**
> [Claim Your Free Admission →]

Fine print (repeat): Valid Mon–Fri, ages 3–12. [Florida residents only — POL.] One use per household.

---

### SECTION 6 — Location Details

**Purpose:** Remove the final friction — address, hours, what to bring.

**Headline:**
> Find Us

**Content:**
📍 [Full address with Google Maps embed or link]
🕙 Hours: [Mon–Fri hours — confirm with Michael]
📞 [Phone number]
👟 Bring socks! Required for all jumpers — or grab a pair at the venue.
🚗 Parking: [Parking notes]

**Map embed:** Google Maps embed of the specific location.

---

### SECTION 7 — Final CTA

**Headline:**
> Ready? One Kid Jumps Free.

**CTA Button:**
> [Get Your Free Admission →]

Fine print: [Same as above]

---

### TRACKING (William to Install on Every Page)

| Pixel / Tag | Event to Fire | When |
|---|---|---|
| Meta Pixel | `ViewContent` | Page load |
| Meta Pixel | `InitiateCheckout` | CTA button click |
| Meta Pixel | `Purchase` | Aloovy thank-you/confirmation page |
| GA4 | `page_view` | Page load |
| GA4 | `cta_click` | CTA button click |
| GA4 | `purchase` | Aloovy confirmation page |
| GTM | All of the above fire through GTM container | — |

**UTM parameters on all ad links to this page** — see `utm-guide.md`.

---

---

## LANDING PAGE TEMPLATE — 50% OFF OFFER

*Identical structure to BOGO page. Only these elements change:*

| Element | BOGO Version | 50% Off Version |
|---|---|---|
| Headline | "Buy One Kid's Admission, Get One FREE" | "50% Off All Kids Admissions" |
| Subheadline | "Weekdays Only — Walk In Any Time" | "Ages 3–12 · Weekdays Only · Walk In Any Time" |
| CTA button | "Claim Your Free Admission →" | "Claim Your 50% Off →" |
| Promo code | WACKY-POL / WACKY-WP | KIDS50-POL / KIDS50-WP |
| URL slug | /bogo-orlando / /bogo-winterpark | /halfprice-orlando / /halfprice-winterpark |
| Fine print | One use per household. Not valid with other offers. | One use per household. Not valid with other offers. |

*All other sections (social proof, how it works, location details, tracking) are identical.*

---

---

## BIRTHDAY PARTY LANDING PAGE (Phase 2 — Reference Only)

Build this in Month 2 once the pilot offers are running. Spec:

**URL:** `/birthday`
**Goal:** Generate birthday party enquiries (Name + Email + Phone + Preferred Date)

**Hero:**
- Headline: "Orlando's Best Kids Birthday Party — We Handle Everything"
- Background: Decorated party room with happy kids
- CTA: "Reserve Your Party Date →" → links to inquiry form (NOT Aloovy — this is a form lead, not a self-serve booking)

**Key sections:**
1. What's included (private room, host, unlimited play, setup + cleanup, invitations)
2. Package options and pricing (Michael to provide)
3. Google reviews — party-specific ones
4. Inquiry form: First Name, Email, Phone, Preferred Month, Number of Children
5. "Nicole will call you within 24 hours" — sets expectation, reduces anxiety

**Tracking:** Same pixel events. `Lead` event fires on form submit.

---

---

## GHL AUTOMATION SETUP

Once pages are built, load the email sequences from `EMAIL-SEQUENCES.md` into GHL workflows:

| Workflow | Trigger in GHL | Notes |
|---|---|---|
| New Subscriber Welcome | Contact tag: `new-subscriber` | Fires when someone opts in via form |
| Post-BOGO Purchase | Contact tag: `bogo-purchased` | Trigger via Aloovy webhook or manual tag |
| Post-50%-Off Purchase | Contact tag: `50off-purchased` | Same as above |
| Birthday Party Inquiry | Form: Birthday Party enquiry submitted | GHL native form trigger |
| Win-Back Reactivation | Contact tag: `lapsed-180` | Run filter: no open/click in 180 days |
| Jumper Card Upsell | Contact tag: `visit-redeemed` | 24h after visit date |
| Birthday Reminder | Birthday field: 90 days before | GHL birthday automation |

**Contact tags to set up:**
- `new-subscriber`
- `bogo-purchased` / `bogo-orlando` / `bogo-winterpark`
- `50off-purchased` / `50off-orlando` / `50off-winterpark`
- `birthday-inquiry`
- `visit-redeemed`
- `jumper-card-holder`
- `lapsed-180`
- `active` / `at-risk` / `lapsed` (for list segmentation)

---

## ACCESS WILLIAM NEEDS FROM MICHAEL

Before any build can start:

- [ ] GHL account access (or William creates MJ sub-accounts)
- [ ] Aloovy / Aluvii checkout links for each offer at each location
- [ ] Promo codes confirmed and live in Aluvii: `WACKY-POL`, `WACKY-WP`, `KIDS50-POL`, `KIDS50-WP`
- [ ] Venue photos (real, not stock — minimum 10 per location)
- [ ] Google Maps links for both locations
- [ ] Phone numbers for both locations
- [ ] Current opening hours (Mon–Fri)
- [ ] Confirmation of Florida-resident restriction on Pointe Orlando offers
- [ ] Brand assets: logo files (PNG with transparent background), brand colours (hex codes)
- [ ] Meta Business Manager access (to install pixel)
- [ ] Google Tag Manager access (or permission to install on WordPress)

---

## CLONING TO NEW LOCATIONS (Future)

When pilot succeeds and we roll out to additional Monkey Joe's or Big Game Brands locations:

1. Clone sub-account in GHL (takes 5 minutes)
2. Update these variables per new location:
   - Store address
   - Phone number
   - Opening hours
   - Google Maps embed
   - Promo codes (create new ones per location)
   - Google reviews (pull location-specific ones)
   - Any location-specific restrictions (e.g., Florida resident rule)
3. Create new Aluvii promo codes for the location
4. Update UTM parameters to reflect new location
5. Launch

**Estimated time per new location: 1–2 hours.**

---

*GHL Landing Page Brief v1.0 — March 2026*
*WILBA × Lanyu × Monkey Joe's*
*Questions: william@lanyu.ai | jess@wilba.ai*
