# /ad-scan [niche] [city] — Find businesses running Google Ads → high-intent pipeline

> Businesses paying for Google Ads are the best cold segment: every lead costs them money, so slow follow-up is money burning. This finds them and builds a pipeline with an honest, urgent angle.

## Why this segment
A business bidding on Google Ads has told you three things: they want leads, they'll pay for them, and speed-to-lead matters to them. The leak is real and quantifiable — a lead comes in after hours or on a busy day, no one answers fast enough, the click is wasted. That's the exact problem the offer solves, and it's *true*, so you never have to be misleading to make it urgent.

## Instructions

Given a niche + city (`$ARGUMENTS`; default = med spa / cosmetic clinics + rotate metros), find advertisers and append them.

### Step 1 — Find who's advertising
Use **WebSearch** + the **Google Ads Transparency Center** (adstransparency.google.com — public, searchable by advertiser + region) to find businesses running ads in the niche/city. Also: search "[service] [city]" and note who appears as **Sponsored**. Good queries:
- "[city] [service] google ads transparency"
- "[service] near [city]" → note sponsored/advertiser names
- Directory + "book now / free consult" landing pages (a sign of paid traffic).

### Step 2 — Qualify (same ICP as med spa, plus ad-intent)
Keep: owner-operated, cash-pay, injectables/aesthetics-led (or adjacent appointment/cash-pay: float, wellness, cosmetic), **clearly running paid ads**, real review history. Drop: chains, hospital-attached, plastic surgery/derm, brand-new.

### Step 3 — Append (de-duped)
Add rows to `outputs/cash-sprint/prospects-google-ads.md`: business · owner (verify) · city · site · **ad evidence** (what they're advertising) · contact route · Status: New. Skip anyone already in `prospects-medspa.md` or this file.

### Step 4 — Hand off
Tell Jess how many were added, and that the email template is Lane D in `message-bank.md` (honest "the leads your Google Ads are paying for" angle). Offer to scan another niche/city.

## Rules
- **Honest angle only.** Never imply a fault with their account or ads. The urgency is real (wasted ad spend) — that's enough.
- Real, verifiable advertisers only. Mark uncertain ones "verify".
- Emails must carry an unsubscribe line; opt-outs actioned within 5 business days (AU Spam Act).
