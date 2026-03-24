# Plan: Monkey Joe's — Tracking Infrastructure Setup

**Created:** 2026-03-20
**Status:** Draft
**Request:** Install Facebook Pixel + GA4 + CallRail across the Monkey Joe's WordPress site and all landing pages, using GTM as the central tag management layer. Map Constant Contact landing pages into the funnel correctly.

---

## Overview

### What This Plan Accomplishes

Sets up the complete tracking infrastructure for the Monkey Joe's pilot — Google Tag Manager on WordPress, GA4, Facebook Pixel, and CallRail — so that every ad dollar spent can be traced to a real-world outcome (visit, online purchase, phone call). Also defines where Constant Contact landing pages fit versus William's custom pages.

### Why This Matters

You cannot optimise what you cannot measure. Before a single Google or Facebook ad goes live, the tracking layer needs to be bulletproof. This plan gets everything in place by March 28 (before April 1 launch), gives Michael a live dashboard, and gives corporate something that looks professional and credible.

---

## Current State

### What Exists
- WordPress admin access to monkeyjoes.com (Jess confirmed)
- Meta FB Ads account access (confirmed in kickoff)
- Constant Contact account (access needed)
- No GTM account (needs to be created)
- No GA4 property confirmed (likely none — "we've been orphaned for a while")
- No Facebook Pixel on site (no tracking code visible on site audit)
- Aloovy handles party bookings + online payments (separate platform)
- William building custom landing pages (location TBD — subdomain or separate domain)

### Gaps Being Addressed
- Zero tracking on the existing site — no way to build audiences or measure conversions
- No way to attribute phone calls to a specific ad campaign
- No consistent UTM naming convention across campaigns
- Constant Contact landing pages need to be placed correctly in the funnel (email capture, not conversion)
- William's landing pages need tracking before go-live

---

## Architecture Decision: GTM as the Central Layer

Install GTM on WordPress once. Every other tool (GA4, FB Pixel, CallRail) is added as a tag inside GTM. This means:
- One plugin install on WordPress (GTM4WP)
- No code changes needed for future tools
- William adds the same GTM container ID to his landing pages
- All tracking managed from one GTM dashboard

```
WordPress site
  └── GTM4WP plugin → GTM Container
        ├── GA4 tag
        ├── Facebook Pixel tag
        └── CallRail swap script tag

William's landing pages
  └── GTM container snippet (same container ID)
        ├── GA4 tag (same property)
        ├── Facebook Pixel tag (same pixel)
        └── CallRail tag (same account)

Constant Contact landing pages
  └── Manual HTML embed (separate from GTM)
        ├── FB Pixel base code (copy/paste)
        └── GA4 snippet (copy/paste)
```

---

## Where Each Landing Page Type Lives

| Page Type | Built In | Pixel Method | Best For |
|-----------|---------|-------------|---------|
| BOGO Offer → Aloovy checkout | William (custom) | GTM (automatic) | Conversion campaigns |
| Frequent Jumper Card → Aloovy | William (custom) | GTM (automatic) | Conversion campaigns |
| Birthday reactivation opt-in | Constant Contact | Manual HTML embed | Email list growth |
| General email list sign-up | Constant Contact | Manual HTML embed | List building |
| Party booking (existing) | Aloovy | Pixel on confirmation page | Revenue tracking |

**Rule of thumb:** If money changes hands → William's page. If it's an email/lead capture → Constant Contact is fine.

---

## Proposed Changes

### Summary
- Create GTM account + install on WordPress via GTM4WP plugin
- Create GA4 property → add as tag in GTM
- Set up FB Pixel in Meta Events Manager → add as tag in GTM
- Set up CallRail → add swap script as tag in GTM
- Give William GTM container ID for his landing pages
- Manually embed tracking on Constant Contact pages
- Create UTM naming convention document
- Verify all tracking before April 1 go-live

### New Files to Create

| File Path | Purpose |
|-----------|---------|
| `outputs/monkey-joes/tracking-setup.md` | Master record of all account IDs, pixel IDs, GTM container ID |
| `outputs/monkey-joes/utm-guide.md` | UTM naming convention for all campaigns |
| `outputs/monkey-joes/conversion-events.md` | List of all GA4 + FB Pixel events and where they fire |
| `outputs/monkey-joes/callrail-setup.md` | CallRail number assignments + campaign mapping |

---

## Step-by-Step Tasks

---

### Step 1: Create Google Tag Manager Account

**URL:** tagmanager.google.com

**Actions:**
- Sign in with a Google account (use Jess's WILBA Google account, not Michael's personal)
- Create new Account: name it "Monkey Joe's"
- Create Container: name it "monkeyjoes.com" → platform: Web
- GTM gives you a Container ID (format: GTM-XXXXXXX) → save this
- GTM gives you two code snippets (head + body) → you won't need these manually if using the plugin

**Save to:** `outputs/monkey-joes/tracking-setup.md`
- GTM Container ID: GTM-XXXXXXX

---

### Step 2: Install GTM on WordPress

**Plugin:** GTM4WP (by Thomas Geiger) — free, 1M+ installs, maintained

**Actions:**
1. Log into WordPress admin → Plugins → Add New
2. Search "GTM4WP" → Install → Activate
3. Go to Settings → Google Tag Manager
4. Paste GTM Container ID (from Step 1)
5. Set "Container code on" → "On"
6. Save settings

**Verify:**
- Visit monkeyjoes.com in Chrome
- Open Chrome DevTools → Network tab → search for "gtm.js"
- If it loads → GTM is firing on the site ✓

**Files affected:**
- WordPress settings (no file created — plugin handles it)

---

### Step 3: Create GA4 Property

**URL:** analytics.google.com

**Actions:**
1. Sign into Google Analytics with WILBA Google account
2. Admin → Create Property → name: "Monkey Joe's" → timezone: Eastern Time → currency: USD
3. Choose "Web" as platform
4. Enter website URL: monkeyjoes.com
5. GA4 gives you a Measurement ID (format: G-XXXXXXXXXX) → save this
6. **Do NOT use the GA4 setup assistant to install the tag** — you'll do it through GTM

**Save to:** `outputs/monkey-joes/tracking-setup.md`
- GA4 Measurement ID: G-XXXXXXXXXX

---

### Step 4: Add GA4 Tag in GTM

**In GTM dashboard:**

1. Tags → New → Tag Configuration → Google Analytics: GA4 Configuration
2. Measurement ID: paste G-XXXXXXXXXX from Step 3
3. Trigger: All Pages
4. Name the tag: "GA4 — Configuration"
5. Save

**Add GA4 Purchase Event (for Aloovy confirmation page):**
1. Tags → New → GA4 Event tag
2. Event name: `purchase`
3. Trigger: Page URL contains `/confirmation` (or whatever Aloovy's confirmation URL is — confirm with William)
4. Name: "GA4 — Purchase Event"
5. Save

**Verify:**
- Enable GTM Preview mode → visit monkeyjoes.com
- GA4 Configuration tag should show as "Fired"
- In GA4 → DebugView → events should appear in real time ✓

---

### Step 5: Set Up Facebook Pixel

**URL:** business.facebook.com → Events Manager

**Actions:**
1. Log in with the Meta account that has access to Monkey Joe's ad account
2. Events Manager → Connect Data Sources → Web
3. Name: "Monkey Joe's Website Pixel"
4. Method: "Meta Pixel" → Create
5. Copy the Pixel ID (format: 16-digit number) → save this
6. **Do NOT use Meta's guided install** — you'll add it through GTM

**Save to:** `outputs/monkey-joes/tracking-setup.md`
- FB Pixel ID: XXXXXXXXXXXXXXXXXX

---

### Step 6: Add Facebook Pixel Tag in GTM

**Option A: Use Meta's official GTM template (recommended)**

1. In GTM → Tags → New → Tag Configuration → search "Facebook"
2. If Meta Pixel template is available: select it, paste Pixel ID
3. Trigger: All Pages
4. Name: "FB Pixel — PageView"
5. Save

**Option B: Custom HTML tag (if template not available)**

1. Tags → New → Custom HTML
2. Paste the standard Meta Pixel base code (from Meta Events Manager → Manual Install)
3. Replace the pixel ID in the code with your actual Pixel ID
4. Trigger: All Pages
5. Name: "FB Pixel — Base Code"
6. Save

**Add FB Standard Events:**

Add separate tags for key conversion events:

| Event | Trigger | GTM Tag Name |
|-------|---------|-------------|
| `ViewContent` | BOGO or Jumper Card landing page URL | FB — ViewContent |
| `InitiateCheckout` | Aloovy checkout page URL | FB — InitiateCheckout |
| `Purchase` | Aloovy confirmation page URL | FB — Purchase |
| `Lead` | Constant Contact opt-in confirmation | FB — Lead |

**Verify:**
- Install Facebook Pixel Helper Chrome extension
- Visit monkeyjoes.com → Pixel Helper should show green with PageView event ✓
- Visit a landing page → ViewContent should fire ✓

---

### Step 7: Set Up CallRail

**URL:** callrail.com (create account or use existing if Michael has one)

**Pricing:** ~$45/month for basic plan. Confirm with Michael who pays for this (ad spend budget or separate line item).

**Actions:**
1. Create CallRail account → Company: Monkey Joe's
2. Set up two tracking numbers — one per location:
   - Pointe Orlando tracking number
   - Winter Park tracking number
3. Forward each tracking number to the real location phone number
4. Enable call recording (legal in Florida — one-party consent state)
5. Set up source tracking: Google Ads, Facebook Ads, Organic, Direct
6. Copy the JavaScript swap snippet from CallRail

**Save to:** `outputs/monkey-joes/callrail-setup.md`
- Pointe Orlando tracking number: (XXX) XXX-XXXX → forwards to: real number
- Winter Park tracking number: (XXX) XXX-XXXX → forwards to: real number

---

### Step 8: Add CallRail Tag in GTM

1. GTM → Tags → New → Custom HTML
2. Paste CallRail JavaScript swap snippet
3. Trigger: All Pages
4. Name: "CallRail — Number Swap"
5. Save

**How it works:** CallRail's script dynamically replaces the phone numbers on the page with tracking numbers based on the visitor's traffic source. If someone came from a Facebook ad, they see the Facebook tracking number. If from Google Ads, they see the Google tracking number. Calls are attributed automatically.

**Verify:**
- Visit monkeyjoes.com
- The phone number on the page should be replaced by CallRail tracking number
- Call it → should appear in CallRail dashboard ✓

---

### Step 9: Publish GTM Container

Once all tags are added and verified in Preview mode:

1. GTM → Submit → Publish
2. Version name: "Initial launch — GA4, FB Pixel, CallRail"
3. Confirm

**All tags are now live on monkeyjoes.com.**

---

### Step 10: Give William the GTM Container ID

Email/message William:

> "For every landing page you build for Monkey Joe's, add this GTM snippet in the `<head>` and `<body>`. This will automatically install GA4, the Facebook Pixel, and CallRail on your pages without any extra work."

Include:
- GTM Container ID (GTM-XXXXXXX)
- The two GTM code snippets (head + body — from GTM → Admin → Install Google Tag Manager)
- Confirm with William: what domain/subdomain will his pages live on?

**If pages are on monkeyjoes.com subdomain (e.g., offers.monkeyjoes.com):**
→ Same GTM container works. Add the snippet to his page template once.

**If pages are on a separate domain:**
→ Same GTM container ID, but William installs the snippet on his platform independently.

---

### Step 11: Tracking on Constant Contact Landing Pages

Constant Contact landing pages are hosted on CC's servers — GTM can't be installed there. You need to manually embed tracking code.

**For each Constant Contact landing page:**

1. Open the landing page editor in Constant Contact
2. Find the "Custom HTML" or "Header Code" section
3. Paste the FB Pixel base code (from Meta Events Manager → Manual Install → copy base code)
4. Paste GA4 snippet (from Google Analytics → Admin → Data Streams → your stream → implementation instructions → copy gtag snippet)
5. Save and publish

**Important:** Constant Contact landing pages should only be used for email capture/opt-in (birthday reactivation, newsletter). The pixel on these pages fires a `Lead` event when someone submits the form — that's all you need from CC pages.

---

### Step 12: Set Up UTM Naming Convention

Create a consistent naming system before any campaign goes live. Every ad link must have UTM parameters so you can see in GA4 exactly which campaign, ad set, and ad drove the traffic.

**Convention:**

| Parameter | Values |
|-----------|--------|
| `utm_source` | `facebook` / `google` / `email` / `sms` / `gbp` |
| `utm_medium` | `cpc` / `email` / `sms` / `organic` |
| `utm_campaign` | `bogo-weekday` / `jumper-card` / `birthday-reactivation` / `toddler-thursday` / `brand` |
| `utm_content` | `variant-a` / `variant-b` / `video-1` / `static-1` (for A/B testing) |
| `utm_term` | keyword (Google Ads only — auto-populated) |

**Example links:**
- Facebook BOGO ad (Variant A): `https://landing.page/bogo-orlando?utm_source=facebook&utm_medium=cpc&utm_campaign=bogo-weekday&utm_content=variant-a`
- Email reactivation: `https://landing.page/bogo-orlando?utm_source=email&utm_medium=email&utm_campaign=birthday-reactivation`

**Save full guide to:** `outputs/monkey-joes/utm-guide.md`

Use a UTM builder tool (Google's free one at ga-dev-tools.google.com/campaign-url-builder) to generate links consistently.

---

### Step 13: Conversion Event Master List

Document every event that fires and where, so you can set up:
- GA4 conversion events (for reporting)
- Facebook Pixel custom conversions (for ad optimisation)
- CallRail call goals

**Save to:** `outputs/monkey-joes/conversion-events.md`

| Event | Platform | Trigger | Value |
|-------|---------|---------|-------|
| `page_view` | GA4 + FB | All pages | — |
| `ViewContent` | FB Pixel | BOGO or Jumper Card landing page | — |
| `InitiateCheckout` | FB Pixel + GA4 | Aloovy checkout page | — |
| `Purchase` | FB Pixel + GA4 | Aloovy confirmation page | $ amount |
| `Lead` | FB Pixel + GA4 | CC opt-in form submit | — |
| `phone_call` | CallRail + GA4 | Inbound tracked call | — |

---

### Step 14: Pre-Launch Verification Checklist

Run this before April 1:

**GTM:**
- [ ] GTM firing on all pages of monkeyjoes.com (GTM preview mode)
- [ ] GTM container ID installed on William's landing pages (confirm with William)

**GA4:**
- [ ] GA4 receiving data (DebugView shows events in real time)
- [ ] Purchase event firing on Aloovy confirmation page
- [ ] GA4 conversions set: `purchase`, `phone_call`, `generate_lead`

**Facebook Pixel:**
- [ ] Pixel Helper shows green on monkeyjoes.com
- [ ] PageView fires on all pages
- [ ] ViewContent fires on landing pages
- [ ] Purchase event fires on Aloovy confirmation page
- [ ] Pixel linked to the correct Meta Ad Account

**CallRail:**
- [ ] Tracking numbers displaying correctly on site
- [ ] Test call received and recorded in CallRail dashboard
- [ ] Source attribution working (visit from Google → Google tracking number shows)

**Constant Contact pages:**
- [ ] FB Pixel base code embedded in CC page HTML
- [ ] GA4 snippet embedded in CC page HTML
- [ ] Lead event fires on form submission

**UTMs:**
- [ ] All campaign links built with UTM parameters
- [ ] GA4 showing traffic sources correctly in Acquisition report

---

## Funnel Tracking Summary

When fully set up, this is what you can measure end-to-end:

```
[Facebook Ad] → utm_source=facebook&utm_campaign=bogo-weekday
  → [William's Landing Page] → FB ViewContent event fires, GA4 page_view
    → [Aloovy Checkout] → FB InitiateCheckout fires, GA4 begin_checkout
      → [Aloovy Confirmation] → FB Purchase fires, GA4 purchase (with revenue $)
        → [Day 1 SMS] → utm_source=sms&utm_campaign=jumper-card
          → [Jumper Card Page] → new conversion cycle begins

[Phone Call from site] → CallRail attributes to traffic source
  → Appears in GA4 as phone_call conversion
  → Appears in CallRail dashboard with recording
```

You'll be able to tell Michael:
- "Your Facebook ads drove X purchases worth $Y this week"
- "Your Google ads drove Z phone calls"
- "Email reactivation drove X Aloovy purchases"

---

## Open Questions

1. **Aloovy confirmation page URL** — What is the exact URL that loads after a completed purchase? Needed to set the Purchase conversion trigger. (William to confirm)
2. **CallRail budget** — Who covers this cost? ~$45/month. Confirm with Michael before signing up.
3. **William's landing page domain** — Subdomain of monkeyjoes.com or separate? Determines GTM install method.
4. **Existing GA4/pixel** — Do a final check: is there any existing tracking code anywhere on monkeyjoes.com? (Use BuiltWith.com or Chrome DevTools to check before installing)
5. **Michael's Google account** — Does corporate have Google Analytics or Search Console set up? Need to know before creating a new GA4 property to avoid duplicates.

---

## Validation Checklist

- [ ] GTM account created, container ID saved
- [ ] GTM4WP plugin installed on WordPress, GTM firing
- [ ] GA4 property created, receiving data
- [ ] Facebook Pixel set up in Meta Events Manager, firing on site
- [ ] CallRail account set up, numbers assigned per location
- [ ] All three tags published via GTM
- [ ] William has GTM container ID for his landing pages
- [ ] Constant Contact pages have manual pixel embed
- [ ] UTM naming convention documented
- [ ] Conversion events documented and tested
- [ ] Full pre-launch verification checklist passed

---

## Success Criteria

1. GA4, FB Pixel, and CallRail all firing on monkeyjoes.com before March 28
2. Same tracking confirmed on all William's landing pages before April 1
3. Purchase conversion event confirmed firing on Aloovy post-purchase page
4. Michael can see live traffic in GA4 (give him View access)
5. Every ad campaign launched with UTM parameters — GA4 shows traffic by source from Day 1

---

## Notes

- **Check for existing tracking first** — before installing anything new, use BuiltWith.com or the Chrome DevTools Network tab to see if there's any existing GA or Pixel code on monkeyjoes.com. Corporate may have something installed you don't know about. Installing twice causes double-counting in GA4.
- **Aloovy is the revenue black box** — the biggest unknown is whether GA4/Pixel can fire on Aloovy's confirmation page. If Aloovy is a fully external platform with no way to add code, you'll need to rely on CallRail + email receipt data for revenue attribution. William should confirm this early.
- **Facebook Pixel data takes 24–48 hours** to fully appear in Meta Events Manager after first install. Don't panic if you don't see events immediately.
- **CallRail call recordings** — Flag to Michael that calls may be recorded. Suggest adding "calls may be recorded for quality purposes" to the website footer.
