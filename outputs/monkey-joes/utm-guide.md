# Monkey Joe's — UTM Naming Convention Guide
## Track Every Click. Know What's Working.

**Prepared by:** Jess Morrell / WILBA
**Date:** March 2026
**Use this guide for:** Every link in every ad, email, and SMS before launch

---

## Why UTMs Matter

UTM parameters are tags you add to the end of a URL. They tell Google Analytics (and your reports) exactly where a visitor came from — which ad, which email, which platform.

Without them: "We got 50 bookings." ← guessing
With them: "The Tuesday BOGO email drove 32 bookings. The Facebook BOGO ad drove 14. Google drove 4." ← decisions

**Every link that goes into an ad, email, or SMS must have UTMs.**

---

## The Formula

```
[Aloovy URL]?utm_source=[SOURCE]&utm_medium=[MEDIUM]&utm_campaign=[CAMPAIGN]&utm_content=[CONTENT]
```

**Four parameters — fill in all four every time:**

| Parameter | What It Tracks | Examples |
|-----------|---------------|---------|
| `utm_source` | Which platform | `facebook`, `google`, `email`, `sms` |
| `utm_medium` | What type | `paid_social`, `paid_search`, `email`, `sms` |
| `utm_campaign` | Which campaign | `bogo-pol-april`, `birthday-wp`, `jumper-card-rt` |
| `utm_content` | Which specific ad or email | `variantA-video`, `tuesday-email`, `sms-day1` |

---

## Naming Conventions — Use These Exactly

### Sources
```
facebook
google
email
sms
organic_social
```

### Mediums
```
paid_social      ← Facebook/Instagram ads
paid_search      ← Google Search ads
email            ← Constant Contact campaigns and automations
sms              ← Text messages
organic          ← Free posts, Google Maps, etc.
```

### Campaign Names (use these consistently)

| Campaign | UTM Campaign Value |
|---------|-------------------|
| BOGO — Pointe Orlando | `bogo-pol` |
| BOGO — Winter Park | `bogo-wp` |
| Birthday Party — Pointe Orlando | `birthday-pol` |
| Birthday Party — Winter Park | `birthday-wp` |
| Frequent Jumper Card | `jumper-card` |
| Beat the Heat — Summer | `summer-heat` |
| Re-engagement / Comeback | `reactivation` |
| Birthday Automation Email | `birthday-automation` |
| Post-purchase sequence | `post-purchase` |
| Welcome sequence | `welcome-series` |
| Weekly Wacky Wednesday | `wacky-wednesday` |
| Toddler Thursday | `toddler-thursday` |

### Content Names (specific ad or email variant)

| Ad / Email | UTM Content Value |
|-----------|-----------------|
| Facebook BOGO Ad — Video Variant A | `fb-video-variantA` |
| Facebook BOGO Ad — Static Variant B | `fb-static-variantB` |
| Facebook Toddler Thursday Ad | `fb-toddler` |
| Google Search — Brand | `google-brand` |
| Google Search — Category | `google-category` |
| Email — B1 Booking Confirmation | `email-B1-confirmation` |
| Email — B2 Post-Visit Day 2 | `email-B2-postvisit` |
| Email — B3 Day 7 Re-engage | `email-B3-reengage` |
| Email — A1 Birthday 90 Day | `email-A1-bday90` |
| Email — A2 Birthday 45 Day | `email-A2-bday45` |
| Email — C1 Welcome | `email-C1-welcome` |
| SMS — Day 1 Post-Visit | `sms-postvisit-d1` |
| SMS — Day 7 | `sms-postvisit-d7` |
| SMS — Birthday 14 Day | `sms-bday14` |
| SMS — Wacky Wednesday | `sms-wacky-wed` |

---

## Ready-to-Use UTM Links

Copy, paste, use. Replace `[ALOOVY-URL]` with the actual Aloovy checkout URL.

### Facebook Ads — BOGO Pointe Orlando

**Variant A (Video):**
```
[ALOOVY-POL-URL]?utm_source=facebook&utm_medium=paid_social&utm_campaign=bogo-pol&utm_content=fb-video-variantA
```

**Variant B (Static):**
```
[ALOOVY-POL-URL]?utm_source=facebook&utm_medium=paid_social&utm_campaign=bogo-pol&utm_content=fb-static-variantB
```

**Toddler Thursday:**
```
[ALOOVY-POL-URL]?utm_source=facebook&utm_medium=paid_social&utm_campaign=toddler-thursday&utm_content=fb-toddler
```

---

### Facebook Ads — BOGO Winter Park

**Variant A (Video):**
```
[ALOOVY-WP-URL]?utm_source=facebook&utm_medium=paid_social&utm_campaign=bogo-wp&utm_content=fb-video-variantA
```

**Variant B (Static):**
```
[ALOOVY-WP-URL]?utm_source=facebook&utm_medium=paid_social&utm_campaign=bogo-wp&utm_content=fb-static-variantB
```

---

### Google Ads — Both Locations

**Brand Search — Pointe Orlando:**
```
[ALOOVY-POL-URL]?utm_source=google&utm_medium=paid_search&utm_campaign=bogo-pol&utm_content=google-brand
```

**Category Search — Pointe Orlando:**
```
[ALOOVY-POL-URL]?utm_source=google&utm_medium=paid_search&utm_campaign=bogo-pol&utm_content=google-category
```

**Brand Search — Winter Park:**
```
[ALOOVY-WP-URL]?utm_source=google&utm_medium=paid_search&utm_campaign=bogo-wp&utm_content=google-brand
```

---

### Email Links — Constant Contact

Use the landing page URLs (not Aloovy directly) for most email CTAs so the page view is tracked first. The page then forwards to Aloovy.

**B1 — Booking Confirmation (BOGO code email):**
```
[LANDING-PAGE-POL]?utm_source=email&utm_medium=email&utm_campaign=bogo-pol&utm_content=email-B1-confirmation
```

**B2 — Post-Visit Day 2 (Jumper Card upsell):**
```
[LANDING-PAGE-JUMPERCARD]?utm_source=email&utm_medium=email&utm_campaign=jumper-card&utm_content=email-B2-postvisit
```

**B3 — Day 7 Re-engage:**
```
[LANDING-PAGE-POL]?utm_source=email&utm_medium=email&utm_campaign=bogo-pol&utm_content=email-B3-reengage
```

**A1 — Birthday 90 Day:**
```
[LANDING-PAGE-BIRTHDAY]?utm_source=email&utm_medium=email&utm_campaign=birthday-automation&utm_content=email-A1-bday90
```

**A2 — Birthday 45 Day:**
```
[LANDING-PAGE-BIRTHDAY]?utm_source=email&utm_medium=email&utm_campaign=birthday-automation&utm_content=email-A2-bday45
```

**C1 — Welcome Email:**
```
[LANDING-PAGE-POL]?utm_source=email&utm_medium=email&utm_campaign=welcome-series&utm_content=email-C1-welcome
```

**Tuesday BOGO reminder:**
```
[LANDING-PAGE-POL]?utm_source=email&utm_medium=email&utm_campaign=wacky-wednesday&utm_content=email-tue-reminder
```

---

### SMS Links

Shorten all SMS links with bit.ly or a free URL shortener before sending. UTMs still apply on the destination URL.

**SMS — Post-visit Day 1:**
```
[LANDING-PAGE-JUMPERCARD]?utm_source=sms&utm_medium=sms&utm_campaign=jumper-card&utm_content=sms-postvisit-d1
```

**SMS — Wacky Wednesday:**
```
[LANDING-PAGE-POL]?utm_source=sms&utm_medium=sms&utm_campaign=wacky-wednesday&utm_content=sms-wacky-wed
```

---

## How to Build a UTM in 30 Seconds

Use Google's free UTM builder: https://ga-dev-tools.google/campaign-url-builder/

1. Paste your destination URL
2. Fill in source, medium, campaign, content using the names above
3. Copy the generated URL
4. Paste into your ad or email

---

## The Golden Rule

**Never send a paid link without a UTM.** Organic links can be bare. Everything with a budget needs tracking. Without UTMs in paid ads, you're flying blind.

---

## Where to See the Results

Once GA4 is live and receiving data:

**In GA4:** Reports → Acquisition → Traffic Acquisition → Filter by Session campaign
**In Looker Studio:** Campaign performance dashboard (to be built Month 1)
**In the weekly report:** UTM source breakdown shows which channel drove bookings

---

*Version 1.0 — March 2026. Update this guide whenever a new campaign is added.*
