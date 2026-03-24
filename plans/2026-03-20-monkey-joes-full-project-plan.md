# Plan: Monkey Joe's — Full Project Plan (90-Day Pilot)

**Created:** 2026-03-20
**Status:** Draft
**Request:** Step-by-step plan for every phase of the Monkey Joe's marketing pilot, incorporating AIOS skills

---

## Overview

### What This Plan Accomplishes

A complete, phase-by-phase execution plan for the Monkey Joe's 90-day marketing pilot (April 1 – July 1, 2026). Covers every deliverable: access setup, research, email, ads, landing pages, online store, GBP, analytics, and reporting — with built-in use of AIOS skills for ad research, creative analysis, and competitor intelligence.

### Why This Matters

This pilot is the proof-of-concept for a franchise-wide rollout. Two locations now. Nine Monkey Joe's next. Then Flying Biscuit and Cinnaholic (130+ Big Game Brands locations). Every phase needs to be executed cleanly, documented, and presentable to corporate. This plan is the operating manual.

---

## Client & Partner Context

| Role | Name | Responsibility |
|------|------|---------------|
| Client | Michael Carter | Monkey Joe's franchise operator (Pointe Orlando + Winter Park) |
| Tech partner | William Milner (Lanyu) | AI systems, landing pages, Aloovy, digital punch card, chatbot |
| Marketing lead | Jess Morrell (WILBA) | Ads, email, strategy, offers, GBP, reporting |

**Revenue:**
- Month 1 (setup): $1,500 USD
- Month 2–3 (optimization): $800 USD/month
- Total pilot: $3,100 USD / 90 days
- Plus: commission on Frequent Jumper Card online sales

**Review dates:** May 3–5 | June 3 | July 1

---

## Locations

| Location | Waiver DB Size | Notes |
|----------|---------------|-------|
| Pointe Orlando | ~20K+ | Florida resident restriction on offers. Tourist area. |
| Winter Park | ~16K | No resident restriction. Family/local market. |

---

## Phase Overview

| Phase | Name | Timeline | Owner |
|-------|------|---------|-------|
| 0 | Access & Setup | Week 1 (by March 25) | Jess + William |
| 1 | Research & Audit | Week 1–2 | Jess |
| 2 | Infrastructure | Week 1–2 | Jess + William |
| 3 | Offers & Copy | Week 2 | Jess |
| 4 | Email Marketing | Week 2–3 | Jess |
| 5 | Landing Pages | Week 2–3 | William (brief from Jess) |
| 6 | Google Ads | Week 3 → ongoing | Jess |
| 7 | Facebook/Meta Ads | Week 3 → ongoing | Jess |
| 8 | Online Store | Week 2–3 | William |
| 9 | GBP Optimization | Week 1–2 | Jess |
| 10 | Reporting Dashboard | Week 3 | Jess |
| 11 | Go Live | April 1 | All |
| 12 | Ongoing Optimization | April–June | Jess |

---

---

## PHASE 0: Access & Setup

**Goal:** Secure all account access before anything else can be built.

### Step 0.1 — Facebook Business Access

**Status:** Partially resolved during kickoff (Jess got access via Michael's personal account)

**Actions:**
- Confirm Jess has Editor or Admin access to both Monkey Joe's Pages:
  - Pointe Orlando Facebook Page
  - Winter Park Facebook Page
- Confirm access to Facebook Ad Account (Ad Account ID confirmed in meeting)
- Set up Meta Business Suite properly (don't rely on personal account login)
- Remove any old/unused agencies still listed as Page partners

**Notes:** Michael's wife technically owns the pages. Corporate may have additional access. Proceed carefully — don't remove any access before confirming who it belongs to.

---

### Step 0.2 — Google Accounts

**Actions:**
- [ ] Request access to Google Ads account (MCC or direct — confirm with William)
- [ ] Request access to 2 × Google My Business (GBP) accounts via corporate (Michael to chase)
- [ ] Set up GA4 property for monkeyjoes.com tracking (if not already existing)
- [ ] Confirm Google account structure: is it one master account with sub-accounts per location?

---

### Step 0.3 — Constant Contact

**Actions:**
- [ ] Get login/access to Constant Contact account (both location lists)
- [ ] Confirm total list sizes: ~20K (Orlando) + ~16K (Winter Park)
- [ ] Identify existing segments, lists, and automation sequences already set up
- [ ] Check deliverability health of domain (warm-up needed if list has been dormant)

---

### Step 0.4 — Aloovy (Online Store)

**Actions (William):**
- [ ] Confirm Aloovy supports promo codes
- [ ] Confirm single-use code invalidation after redemption
- [ ] Confirm commission tracking for online-sold products
- [ ] Set up product listings: BOGO Admission (weekday), Frequent Jumper Card
- [ ] Confirm QR code redemption capability as fallback

---

### Step 0.5 — Shared Assets

**Actions:**
- [ ] William sets up shared Google Drive folder for all creative assets
- [ ] Michael uploads existing photos and media assets
- [ ] 15 reels from media shoot expected within 2 weeks of kickoff — Jess to chase

---

### Step 0.6 — Agreement

**Actions:**
- [ ] Michael sends simple protection agreement to Jess + William
- [ ] Run through Claude (this workspace) for review
- [ ] Sign and return

---

## PHASE 1: Research & Audit

**Goal:** Understand what's been tried before, what's working for competitors, and what the baseline is.

> **AIOS Skills used in this phase:** `/ads-analyst`, `/meta-ads-extractor`, `/meta-ads-analyser`, `/ad-creative-analysis`

---

### Step 1.1 — Google Ads Account Audit

**Actions:**
- Log into Google Ads account
- Export full campaign history (what ran, when, spend, results)
- Note: previous campaigns likely under-optimized or dormant
- Look for: keywords that converted, ad copy that worked, wasted spend areas
- Document findings in `outputs/monkey-joes/ads-audit.md`

---

### Step 1.2 — Facebook Ads Account Audit

**Actions:**
- Log into Facebook Ad Account
- Review all past campaigns (spend, reach, results)
- Note any audiences that were created (custom, lookalike)
- Screenshot high-performing ads (if any) for reference
- Document in `outputs/monkey-joes/ads-audit.md`

---

### Step 1.3 — Competitor Ad Research (Meta Ads Library)

Use the `/meta-ads-extractor` skill to pull competitor ads from Meta Ads Library.

**Run:** `/meta-ads-extractor` for:
- Monkey Joe's other franchise locations (national brand)
- Chuck E. Cheese (Orlando area)
- Scene75 (kids entertainment)
- Local Orlando family entertainment competitors

**What to capture:**
- What offers are they running? (BOGO, % off, seasonal)
- What creative formats? (video, static, carousel)
- How long have ads been running? (longer = more likely working)
- What's the CTA and landing page destination?

**Output:** Save extracted ads to `outputs/monkey-joes/competitor-ads/`

---

### Step 1.4 — Competitor Ad Analysis

Use `/meta-ads-analyser` to analyze the extracted ads and generate a strategy report.

**Run:** `/meta-ads-analyser` on competitor ads from Step 1.3

**What we're looking for:**
- Winning offer structures (what hooks are they using?)
- Creative formats that dominate (video vs static?)
- Copy patterns that repeat (urgency? price? social proof?)
- Gaps we can exploit (what are competitors NOT doing?)

**Output:** Strategy report in `outputs/monkey-joes/competitor-ad-analysis.md`

---

### Step 1.5 — Creative Analysis of Top Performing Ads

Use `/ad-creative-analysis` to deep-dive the highest-performing competitor creatives.

**Run:** `/ad-creative-analysis` on 3–5 selected top competitor video ads

**What to extract:**
- Hook format (first 3 seconds)
- Script structure (problem → solution → CTA)
- Visual approach (UGC? polished? kids-focused?)
- Emotional angle (fun? FOMO? value?)
- CTA strength

**Output:** Creative breakdown in `outputs/monkey-joes/creative-analysis.md`

Use these insights to brief William on landing page design and to write the first round of ad creatives.

---

### Step 1.6 — Email List Audit (Constant Contact)

**Actions:**
- Review overall list health: open rates, click rates, unsubscribe rates
- Identify segments: active openers (last 90 days), dormant (6–12 months), never opened
- Check what emails have performed best in the past (subject lines, offer types)
- Identify any existing automation sequences and whether they're live
- Note: must scrub list against Florida privacy laws for minors before any campaign sends

**Output:** `outputs/monkey-joes/email-audit.md`

---

### Step 1.7 — Website & GBP Audit

**Actions:**
- Review monkeyjoes.com (Pointe Orlando + Winter Park pages)
- Note: website described as "2010s-era" — landing pages will outperform it
- Check daily specials pages for each location (offers already listed there)
- Audit Google My Business profiles for each location:
  - Photos (when were they last updated?)
  - Reviews (quantity, recency, response rate)
  - Business hours, description, categories

**Output:** Notes in `outputs/monkey-joes/website-gbp-audit.md`

---

## PHASE 2: Infrastructure Setup

**Goal:** Make sure every tracking and analytics tool is in place before spending a single dollar.

### Step 2.1 — GA4 Setup

**Actions:**
- Set up GA4 property for monkeyjoes.com (if not existing)
- Install tracking code on site (coordinate with William/corporate)
- Set up key conversion events:
  - Form submissions
  - Aloovy purchase completions
  - Landing page CTA clicks

---

### Step 2.2 — Facebook Pixel

**Actions:**
- Install Facebook Pixel on monkeyjoes.com (via WordPress — coordinate with William)
- Install on all landing pages William builds
- Set up custom conversions:
  - Aloovy checkout completion
  - Landing page lead capture (if added)
- Verify Pixel is firing correctly using Facebook Pixel Helper

---

### Step 2.3 — UTM Parameter System

**Actions:**
- Create UTM parameter naming convention for all campaigns:
  - `utm_source`: facebook / google / email / sms
  - `utm_medium`: cpc / email / sms
  - `utm_campaign`: bogo-weekday / jumper-card / birthday-reactivation
  - `utm_content`: variant A / variant B (for A/B testing)
- Document naming convention in `outputs/monkey-joes/utm-guide.md`
- Build UTM-tagged links for all campaigns before launch

---

### Step 2.4 — CallRail (if included)

**Actions:**
- Confirm if CallRail is in scope for this pilot
- If yes: set up tracking numbers for each location
- Route calls correctly, confirm recording is legal in Florida (yes — one-party consent state)

---

## PHASE 3: Offers & Copy

**Goal:** Write and approve all offer copy before building anything.

> Reference: `plans/2026-03-20-monkey-joes-two-offers-strategy.md` for full offer details.

### Step 3.1 — Offer Confirmation Doc

**Actions:**
- Create `outputs/monkey-joes/offer-confirmation.md`
- Include: both offers, pricing, fine print, promo code requirements, compliance notes
- Send to Michael for approval
- No copy or pages built until this is approved

---

### Step 3.2 — Write All Ad Copy

**Offer 1 (BOGO) — Google Ads:**
- 3 × Headlines (30 chars each)
- 2 × Descriptions (90 chars each)
- 2 variants: BOGO framing vs 50% off framing

**Offer 1 (BOGO) — Facebook Ads:**
- 3 × Primary text variants (short, punchy, parent-focused)
- 1 × Headline variant per ad set

**Offer 2 (Frequent Jumper Card) — Post-visit SMS:**
- 160-char SMS (Day 1 post-visit)

**Offer 2 (Frequent Jumper Card) — Email:**
- Subject line + preview text
- Short body (3–4 lines max)

**Fine print (required on all Pointe Orlando offers):**
"Valid weekdays only. Not valid with any other offer. Available to Florida residents only. One use per household."

---

### Step 3.3 — Landing Page Briefs

Create briefs for:
1. BOGO Landing Page — Pointe Orlando
2. BOGO Landing Page — Winter Park
3. Frequent Jumper Card Landing Page

Each brief: headline, subhead, body, CTA, promo code, tracking pixels, brand notes.

Deliver to William to build.

---

## PHASE 4: Email Marketing

**Goal:** Re-engage the 36K+ contact database and build automated sequences.

### Step 4.1 — List Segmentation

**Actions:**
- Segment the combined ~36K list into:
  - **Active** (opened in last 90 days)
  - **Warm** (opened 90–180 days ago)
  - **Dormant** (no opens in 6+ months)
  - **Never opened**
- Create separate segments for Pointe Orlando vs Winter Park
- Flag birthday data for automation sequence

---

### Step 4.2 — Birthday Reactivation Automation

Trigger: 90 days before child's birthday (from waiver database)
Second trigger: 45 days before

**Sequence:**
- **Day −90 (Email):** "A birthday's coming! 🎉 Monkey Joe's has your party covered." Soft intro, no creepy name-dropping of child.
- **Day −90 (SMS):** Short version, link to party booking page
- **Day −45 (Email):** "Only 45 days to party time! Book now and save." Urgency + BOGO or party package offer.
- **Day −45 (SMS):** Final nudge

**Compliance:** All messaging addressed to parent. No child's name in subject line or body. Comply with Florida privacy laws for minors.

---

### Step 4.3 — Weekly Campaign Emails

Send 2–3 emails/week to segmented list.

**Cadence:**
- **Monday:** Week's specials preview (Wacky Wednesday, Toddler Thursday)
- **Wednesday:** Wacky Wednesday reminder — BOGO in-store + landing page link
- **Friday (optional):** Weekend fun teaser — Pointe Orlando or Winter Park feature

**Template structure:**
- Short subject line (6 words or fewer)
- 1 image / GIF (from media shoot assets)
- 1 offer / 1 CTA — no clutter
- Unsubscribe link (legal requirement)

---

### Step 4.4 — Re-engagement Campaign

For dormant segment (no opens in 6+ months):

**Sequence:**
- Email 1: "We miss you at Monkey Joe's 🐒" — BOGO offer as reactivation hook
- Email 2 (3 days later, non-openers only): "Last chance — free admission for your little one"
- Email 3 (7 days later, still no open): Remove from active list / move to suppression

**Goal:** Re-engage 10–20% of dormant list before suppressing.

---

## PHASE 5: Landing Pages (William's Build — Jess Briefs)

**Goal:** Custom landing pages for each offer, on-brand, mobile-first, with tracking.

### Step 5.1 — BOGO Landing Pages (x2 locations)

- Monkey Joe's branding (font, colors, monkey logo)
- Single offer — no navigation, no distractions
- Promo code pre-populated or revealed on checkout
- GA4 + FB Pixel installed
- Mobile-first
- Separate pages per location (different promo codes, different fine print)

### Step 5.2 — Frequent Jumper Card Landing Page

- Positioned as loyalty / regular program
- Show the value math clearly (10 × $12 = $120 vs. walk-in price)
- Digital card mockup visual
- Link to Aloovy for purchase

### Step 5.3 — Thank You / Confirmation Pages

- Post-purchase confirmation page (used as GA4 + Pixel conversion event)
- Include: promo code reminder, how to redeem, what to expect

---

## PHASE 6: Google Ads

**Goal:** Drive qualified local traffic to landing pages with paid search.

### Step 6.1 — Campaign Structure

| Campaign | Ad Groups | Targeting |
|----------|-----------|-----------|
| Brand (Monkey Joe's) | Branded keywords | Orlando + Winter Park geo |
| Competitor | Chuck E. Cheese, etc. | 10-mile radius each location |
| Category | "kids birthday party Orlando", "kids play place near me" | Geo-targeted |
| Remarketing | Previous website visitors | Google Display |

### Step 6.2 — Budget Allocation

Michael's budget: $1,500/month ad spend (across both locations)

**Suggested split (Month 1):**
- Search: $1,000/month
- Display remarketing: $300/month
- Reserved / contingency: $200/month

Adjust based on performance data from first 30 days.

### Step 6.3 — Ad Copy Variants

- 2 responsive search ads per ad group
- A/B test: BOGO framing vs 50% off framing
- All ads → location-specific landing pages

### Step 6.4 — Ongoing Optimization

Weekly: review search term reports, pause non-performing keywords, add negatives
Monthly: update bids, refresh ad copy, A/B test new variants

---

## PHASE 7: Facebook & Meta Ads

**Goal:** Retarget warm audiences and reach new local parents.

> **AIOS Skills used:** `/ads-analyst` for initial competitor research, `/ad-creative-analysis` for creative benchmarking

### Step 7.1 — Audience Setup

**Custom Audiences:**
- Website visitors (30 days) — requires Pixel (Phase 2)
- Constant Contact email list upload (custom audience)
- Existing Facebook Page followers

**Lookalike Audiences:**
- 1% lookalike of email list
- 1% lookalike of past website visitors

**Interest Targeting (cold):**
- Parents of young children (ages 3–12)
- Located within 10 miles of each location
- Interests: family activities, kids entertainment, birthday parties

### Step 7.2 — Campaign Structure

| Campaign | Objective | Audience | Offer |
|----------|-----------|---------|-------|
| Retargeting | Conversions | Website visitors + email list | BOGO |
| Lookalike | Traffic | 1% lookalike | BOGO |
| Cold Awareness | Reach | Interest-targeted parents | Brand awareness / specials |
| Post-visit | Conversions | Customers (custom event) | Frequent Jumper Card |

### Step 7.3 — Creative

- Use media shoot reels (15 available within 2 weeks)
- Run `/ad-creative-analysis` on top competitor video ads first to benchmark
- Format: vertical video (Reels), square static (Feed), Stories
- Hook: kids having fun — first 3 seconds must capture parent attention
- Every ad → landing page (never main website)

### Step 7.4 — Ongoing

Weekly: review CPM, CPC, CTR, ROAS
Every 2 weeks: refresh creative (avoid ad fatigue)
Monthly: update audiences, test new lookalikes

---

## PHASE 8: Online Store (Aloovy)

**Goal:** Sell admissions and Frequent Jumper Cards online. New revenue stream.

### Step 8.1 — Product Setup (William)

- BOGO Admission product with weekday restriction
- Weekend upgrade option (+$10 upsell at checkout)
- Frequent Jumper Card (10 admissions / $120)
- Digital delivery: QR code or digital card (William's build)

### Step 8.2 — Commission Tracking

- Confirm commission structure with Michael
- Set up tracking so every online sale is attributed (UTM → Aloovy)

### Step 8.3 — Post-Purchase Automation

- Confirmation email: "Here's your promo code / digital card"
- Day 1 post-first-use: SMS/email with Frequent Jumper Card upsell
- Day 7 if no second visit: "Miss you! Come back this week" email

---

## PHASE 9: Google My Business Optimization

**Goal:** Improve local search visibility for both locations. Free traffic.

### Step 9.1 — Profile Audit

- Update photos: use new media shoot assets (15 reels → still frames)
- Ensure all details correct: hours, address, phone, website
- Add services/offerings (birthday parties, daily specials)
- Update business description (keyword-rich, natural)

### Step 9.2 — Review Strategy

- Set up automated review request (SMS/email post-visit asking for Google review)
- Respond to all existing reviews (Michael to handle or Jess drafts responses)
- Target: increase review count by 20%+ during pilot

### Step 9.3 — GBP Posts

- Post weekly to GBP (same content as email: weekly specials, BOGO reminder)
- GBP posts get indexed in Google — free search visibility

---

## PHASE 10: Reporting Dashboard

**Goal:** Michael can log in anytime and see live results. Weekly written updates via email.

### Step 10.1 — Dashboard Setup

**Sources to connect:**
- GA4 (website traffic, conversions)
- Facebook Ads Manager (spend, reach, conversions)
- Google Ads (spend, clicks, conversions)
- Constant Contact (open rates, clicks, unsubscribes)
- Aloovy (online sales, revenue)

**Tool:** Google Looker Studio (free, connects to all above sources)

### Step 10.2 — Weekly Report Format

Send every Monday:
- Week's ad spend vs results
- Email: open rate, clicks, revenue attributed
- Online store: sales this week
- Top performing ad
- One recommendation for the week

### Step 10.3 — Review Meeting Prep

Before each review (May 3–5, June 3, July 1):
- Pull full month comparison vs prior year (same period)
- Prepare slide deck or 1-page summary for Michael + corporate
- Highlight wins, explain anything under-performing, propose Phase 2 changes

---

## PHASE 11: Go Live — April 1

**Launch Checklist:**
- [ ] All account access confirmed
- [ ] GA4 + FB Pixel installed and firing
- [ ] Both landing pages live and tested
- [ ] Promo codes working in Aloovy
- [ ] Email welcome/reactivation sequence loaded and scheduled
- [ ] Google Ads campaigns live (search + display)
- [ ] Facebook Ads campaigns live (retargeting + lookalike)
- [ ] GBP profiles updated
- [ ] Birthday automation sequence loaded (90-day and 45-day triggers)
- [ ] Michael has reviewed and approved all live campaigns
- [ ] Reporting dashboard accessible to Michael and William

---

## PHASE 12: Ongoing Optimization (April – June)

### Weekly Rhythm

| Day | Task |
|-----|------|
| Monday | Pull weekly performance report, send to Michael |
| Tuesday | Review ad performance, pause underperformers |
| Wednesday | Launch/refresh email campaign for the week |
| Friday | Review landing page conversion rates |

### Monthly Reviews

| Date | Action |
|------|--------|
| May 3–5 | Full April review: what worked, what didn't, adjustments for summer |
| June 3 | May review: summer campaign optimization |
| July 1 | June + full pilot review: present results to Michael + discuss Phase 2 |

---

## Files to Create

| File Path | Purpose |
|-----------|---------|
| `outputs/monkey-joes/offer-confirmation.md` | Offer spec for Michael's approval |
| `outputs/monkey-joes/ads-audit.md` | Google + Facebook audit notes |
| `outputs/monkey-joes/competitor-ads/` | Extracted competitor ads (from /meta-ads-extractor) |
| `outputs/monkey-joes/competitor-ad-analysis.md` | Competitor strategy report (from /meta-ads-analyser) |
| `outputs/monkey-joes/creative-analysis.md` | Creative breakdown (from /ad-creative-analysis) |
| `outputs/monkey-joes/email-audit.md` | Constant Contact list audit |
| `outputs/monkey-joes/website-gbp-audit.md` | Website + GBP audit notes |
| `outputs/monkey-joes/offer-copy.md` | All copy: ads, emails, SMS, landing pages |
| `outputs/monkey-joes/landing-page-briefs.md` | Briefs for William to build pages |
| `outputs/monkey-joes/utm-guide.md` | UTM naming convention for all campaigns |
| `outputs/monkey-joes/weekly-report-template.md` | Weekly report format for Michael |

---

## AIOS Skills — When to Use Them

| Skill | When | What For |
|-------|------|---------|
| `/meta-ads-extractor` | Phase 1 (Week 1) | Pull competitor ads from Meta Ads Library |
| `/meta-ads-analyser` | Phase 1 (Week 1–2) | Generate strategy report from extracted ads |
| `/ad-creative-analysis` | Phase 1 (Week 1–2) | Deep-dive top competitor video creatives |
| `/ads-analyst` | Phase 1 (Week 1) | Orchestrate full competitor ad research in one command |

**Run order:** `/ads-analyst` first (runs extractor + analyser in sequence). Then `/ad-creative-analysis` on specific top creatives for deeper analysis.

---

## Open Questions

1. **Aloovy promo code capability** — William to confirm before Phase 3 begins
2. **Google My Business access** — Michael to chase corporate to grant access
3. **Constant Contact access** — Confirm login/invite from Michael
4. **Website control** — Can Jess/William install GA4 + Pixel on monkeyjoes.com? Or does corporate control WordPress?
5. **Florida privacy law review** — Before any birthday automation sends, confirm compliance
6. **Commission structure** — Confirm exact % on online Aloovy sales
7. **Weekend upgrade** — Is this an Aloovy upsell or a separate product listing?

---

## Validation Checklist

- [ ] All accounts accessed and confirmed
- [ ] Phase 0 (access) complete before Phase 1 begins
- [ ] Offer confirmation approved by Michael before any copy is written
- [ ] All copy approved by Michael before anything goes live
- [ ] Tracking confirmed firing before first ad dollar spent
- [ ] Agreement signed
- [ ] Reporting dashboard live before April 1

---

## Success Criteria

1. April 1 launch on time with both offers live, both locations, tracking confirmed
2. May 3–5 review: measurable increase in foot traffic vs prior year April
3. Online store generating Frequent Jumper Card sales within first 30 days
4. Email list open rate above industry average (20%+) for reactivation campaigns
5. Results compelling enough to present to Big Game Brands corporate for franchise rollout

---

## Notes

- The real prize is the franchise rollout. Everything we do should be documented and presentable to corporate.
- Michael said: "The more impressive it turns out, the better shot we have at extending this." Treat every deliverable like it's going to be shown to Big Game Brands.
- Use Jess's own brand assets (Sony ZV-E1 footage, drone shots) only if relevant — this project uses Michael's media shoot assets.
- AI content angle: Michael is open to AI-generated video/commercial content — "I'd love a little TikTok commercial." This could be a Phase 2 unlock using WILBA's Content Generation Machine (HeyGen/ElevenLabs) as a case study.
