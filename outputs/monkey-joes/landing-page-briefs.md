# Monkey Joe's — Landing Page Briefs for William
## Complete Build Specifications

**From:** Jess Morrell / WILBA
**To:** William (Developer)
**Date:** March 2026
**Priority:** All pages live by April 1, 2026

---

## Overview

We're building 5 landing pages for the Monkey Joe's campaign. These pages receive paid traffic from Facebook and Google ads and convert to Aloovy checkout. All pages must:
- Load under 2 seconds (no heavy video autoplay on mobile)
- Be mobile-first (80%+ of traffic will be mobile)
- Have GTM container installed (I'll give you the container ID once created)
- Fire the correct Facebook Pixel events at the right moments
- Use UTM parameters to pass through to Aloovy where possible

---

## GTM Installation (All Pages)

Install this snippet on every page — replace `GTM-XXXXXXX` with the container ID I'll send you:

```html
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-XXXXXXX');</script>
<!-- End Google Tag Manager -->
```

And the body tag version:
```html
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-XXXXXXX"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
```

---

## PAGE 1: BOGO — Pointe Orlando

**URL:** `offers.monkeyjoes.com/bogo-orlando` (or equivalent)
**Go live:** April 1, 2026
**Pixel events:**
- `fbq('track', 'ViewContent')` — fires on page load
- `fbq('track', 'InitiateCheckout')` — fires on CTA button click
- Purchase event fires on Aloovy confirmation page (separate)

---

### Section 1: Hero

**Layout:** Full-width. Background image or short looping video (no sound).
**Recommended image:** Kid mid-bounce, genuine joy. Parent visible in background, relaxed, coffee in hand.

**Headline (H1, large, bold):**
```
You get to breathe.
They get the best time of their life.
```

**Subheadline (H2):**
```
Buy one kid's admission at Monkey Joe's Pointe Orlando, get one FREE.
Every weekday. Ages 3–12.
```

**CTA Button (primary, high contrast — orange or green):**
```
Claim Your Free Admission →
```
Link: `[Aloovy BOGO checkout URL for Pointe Orlando]`

Add onclick pixel event:
```javascript
fbq('track', 'InitiateCheckout');
```

---

### Section 2: How It Works (3 steps)

**Heading:** It's this simple.

**Step 1 icon + text:**
> 🖥️ **Book online** — takes 2 minutes. No account needed.

**Step 2:**
> 🐒 **Show up any weekday** — Monday through Friday

**Step 3:**
> ☕ **One kid bounces free** — you find a seat and actually relax

---

### Section 3: The Offer (proof + detail)

**Heading:** Here's exactly what you get:

```
✅ Buy one kid's admission, get one FREE
✅ Valid any weekday — Monday through Friday
✅ Kids ages 3–12
✅ Redeemable at checkout — no code needed
```

**Fine print (small text below):**
```
Valid weekdays only. Florida residents only. Not valid with any other offer.
One use per family. Admission price subject to change. See venue for current pricing.
```

---

### Section 4: About the Venue (trust)

**Heading:** 21 years. Still going strong.

**Body text:**
```
Monkey Joe's Pointe Orlando has been running this deal since before smartphones.

Bounce houses, climbing walls, obstacle courses — all of it designed for ages 3–12.
All of it self-contained enough that you can actually sit down.

You're not chasing anyone. You're not managing logistics. You're just... there.
```

**3 icon bullets:**
```
📍 Right at Pointe Orlando — easy parking, easy access
☕ Parent seating throughout — you're not standing for an hour
🎉 Party rooms available — ask at the desk
```

---

### Section 5: Social Proof

**Heading:** What other parents say:

Pull 2 real Google reviews here. Format as blockquotes with first name + location. (I'll source these from Google — let me know when this section is ready and I'll paste them in.)

Example format:
```
"[Review text]"
— Sarah M., Orlando
```

---

### Section 6: Final CTA

**Heading:** Ready to actually relax?

**Button (repeat CTA):**
```
Grab Your Free Admission →
```

**Trust line below button:**
```
Secure checkout via Monkey Joe's online store. No account needed. No subscription.
```

---

### Section 7: Footer

```
Monkey Joe's Pointe Orlando
[Address]
[Phone]
[Hours: Weekdays X:00am – X:00pm]
monkeyjoes.com
```

---

### Design Notes for William:
- Colour palette: Use Monkey Joe's brand colours (if asset file not available, use: deep orange + white + green accent)
- Font: Bold, readable — nothing too playful or circus-themed. Parents are the audience.
- Mobile: CTA button must be full-width on mobile, always above the fold on scroll
- No pop-ups
- No countdown timers (feels gimmicky — we don't need it, the BOGO is always valid)
- Page should load without JavaScript for the core offer (FB pixel is enhancement only)

---

## PAGE 2: BOGO — Winter Park

**URL:** `offers.monkeyjoes.com/bogo-winterpark`

**Identical structure to Page 1. Changes:**
- Replace "Pointe Orlando" → "Winter Park" throughout
- Remove Florida resident restriction from offer detail and fine print
- Update address, phone, hours in footer
- Update Aloovy checkout URL to Winter Park store
- Use Winter Park location photos when available

---

## PAGE 3: Birthday Party

**URL:** `offers.monkeyjoes.com/birthday`
**Go live:** April 1, 2026
**Pixel events:**
- `ViewContent` — on page load
- `Lead` — on form submission or "Check Availability" click

---

### Section 1: Hero

**Headline:**
```
The birthday party where YOU actually get to enjoy it.
```

**Subheadline:**
```
Party rooms at Monkey Joe's. We handle setup, the chaos, and cleanup.
You show up, feel like a hero, and your kid has the best birthday of their life.
```

**CTA Button:**
```
Check Party Room Availability →
```
Link: `[Aloovy party booking page or inquiry form]`

---

### Section 2: How It Works (5 steps)

**Heading:** Here's what actually happens:

```
Step 1: Pick your date and party room
Step 2: We set everything up before you arrive
Step 3: The kids bounce, climb, and slide for hours
Step 4: Cake, presents, the whole thing — in your dedicated room
Step 5: We clean up. You take the presents home. Job done.
```

---

### Section 3: What's Included

**Heading:** Everything you need. Nothing you don't.

Build as a clean checklist or icon grid:
```
🎂 Dedicated party room (up to [X] guests)
🐒 Full venue access — bounce houses, climbing walls, obstacle courses
🎉 Special birthday welcome for the birthday child
⏰ [X] hours of party time
👥 Dedicated host for your room
🧹 We handle all setup AND cleanup
```

---

### Section 4: Social Proof

Pull 1 party-specific Google review. Format same as Page 1.

---

### Section 5: Urgency + CTA

**Heading:** Weekend dates fill fast.

**Body:**
```
Especially April through June. If you've got a date in mind, locking it in now
is the move — even a soft hold costs nothing.
```

**CTA Button:**
```
Lock In Your Date →
```

**Secondary link:**
```
Questions? Call us: [Phone]
```

---

## PAGE 4: Frequent Jumper Card

**URL:** `offers.monkeyjoes.com/jumper-card`
**Go live:** April 15, 2026 (Phase 2, after BOGO beds in)
**Pixel events:**
- `ViewContent` — page load
- `AddToCart` — CTA click
- `Purchase` — on Aloovy confirmation

---

### Section 1: Hero

**Headline:**
```
They said "can we go again?" before you even hit the car park.
```

**Subheadline:**
```
The Monkey Joe's Frequent Jumper Card.
10 visits. $120. $12 each. Any time you want.
```

**CTA:**
```
Get My Jumper Card →
```

---

### Section 2: How It Works

```
1. Buy online — takes 2 minutes
2. Get your digital card (QR code on your phone)
3. Show up whenever — no booking, no planning
4. Scan at the door — visits count down automatically
5. 10 bounces. $12 each. Done.
```

---

### Section 3: The Maths

Build as a simple comparison table:

| | Per Visit (Standard) | With Jumper Card |
|--|---------------------|-----------------|
| 1 visit | Full admission price | $12 |
| 5 visits | 5× full price | $60 |
| 10 visits | 10× full price | **$120** ✅ |

**Tagline below table:**
```
The regulars figured this out. Now you have too.
```

---

### Section 4: CTA

```
Get My Frequent Jumper Card — $120 →
```

**Fine print:**
```
Valid at Monkey Joe's [locations]. Does not expire. Non-transferable.
Digital delivery — QR code to your email within minutes.
```

---

## PAGE 5: Email Opt-In (Constant Contact — built inside CC, not by William)

This page is built inside Constant Contact's landing page builder. I'll handle this one — no action from William needed.

---

## Tracking Summary for William

| Page | ViewContent | InitiateCheckout / Lead | Purchase |
|------|------------|------------------------|---------|
| BOGO Orlando | ✅ on load | ✅ on CTA click | Aloovy confirm page |
| BOGO Winter Park | ✅ on load | ✅ on CTA click | Aloovy confirm page |
| Birthday | ✅ on load | ✅ on form submit | N/A |
| Jumper Card | ✅ on load | ✅ on CTA click | Aloovy confirm page |

**Aloovy confirmation page:** I need the URL of the Aloovy purchase confirmation page. Once I have it, I'll add the Purchase pixel event there directly (or through GTM). Please confirm this URL.

---

## Timeline

| Page | Build Start | Live By |
|------|------------|--------|
| BOGO Orlando | March 24 | April 1 |
| BOGO Winter Park | March 25 | April 1 |
| Birthday | March 25 | April 1 |
| Jumper Card | April 8 | April 15 |
| Email Opt-in (CC) | March 28 | April 1 |

---

## Assets I'll Send You

- [ ] GTM Container ID (once account created)
- [ ] Facebook Pixel ID (from Meta Ads account)
- [ ] Aloovy checkout URLs (once Michael confirms promo codes are set up)
- [ ] Photo assets (from Michael)
- [ ] Brand fonts + colour codes (from Michael or existing website)
- [ ] Google reviews text (I'll pull from Maps)

---

## Questions?

Jess Morrell | WILBA
[email]
[WhatsApp]

*Let me know if you need the Figma mockup / wireframe view before building — happy to sketch it out.*
