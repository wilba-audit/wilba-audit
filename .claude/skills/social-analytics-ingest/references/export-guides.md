# Owner-Export Guides — what to ask the client for (plain English)

Every platform lets the account owner export their own analytics and content.
This is the legal, reliable way to ground an audit — no scraping, no passwords.
Send the client the relevant snippet. Screenshots of native analytics also work.

---

## LinkedIn ✅ (proven — this is what Dr Schoeman sent)
**Profile analytics CSV** (personal profile):
1. Go to your LinkedIn profile → **"Analytics"** panel (or the dashboard).
2. Open a metric (e.g. Followers, or "Profile growth and discovery").
3. Click **Export** → downloads a CSV (`Profile_Growth_and_Discovery_...CSV`).
Do this for **each profile** she has, and the **company page** (page admin →
Analytics → Followers → Export). *If she has two profiles, export both — the
split is itself a finding.*
**Also useful:** Me → Settings → **Get a copy of your data** → posts/activity.

## Instagram (Meta)
Two owner exports:
1. **Insights (numbers):** Professional/creator account → **Insights** → set last
   90 days → screenshot the overview + top posts (reach, saves, shares, follows).
   Instagram has limited CSV export, so *screenshots of Insights* are the norm.
2. **Your content:** **Settings → Accounts Centre → Your information and
   permissions → Download your information** → choose Instagram, JSON format.
   Gives posts, captions, and some insights.
**Fastest for a style review:** screenshots of 8–10 recent posts (caption + first
frame) + the Insights overview screenshot.

## Facebook (Meta)
- **Meta Business Suite → Insights** → export, or screenshot the overview.
- Page content + insights via the same **Download your information** flow (JSON).
- For a mostly-dormant page, one Insights screenshot is enough to confirm status.

## TikTok
- Mobile: **Profile → menu → Creator tools → Analytics** → screenshot Overview +
  Content (views, watch time, retention, shares).
- Web: tiktok.com/analytics → some tabs export CSV.

## YouTube
- **YouTube Studio → Analytics → Advanced mode → Export** (CSV/Google Sheets):
  per-video impressions, CTR, average view duration, traffic sources.
- Or screenshots of the Channel + top-videos analytics.

---

## What to prioritise if she's busy
1. **Screenshots of native analytics** (last 90 days) for each platform — fastest, richest.
2. **Screenshots of 8–10 recent posts** (for the style teardown).
3. **CSV/JSON exports** where easy (LinkedIn especially — it just works).

## Handing it back
Put everything in one folder → run `scripts/parse_exports.mjs` for the CSVs →
paste screenshots into chat for the vision-based style review. Then the
`social-media-audit` skill produces the grounded, fully-real audit.
