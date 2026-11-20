---
name: gta6-daily
description: >-
  Runs the GTA Decoded Instagram machine end to end. Two modes. PREP (evening):
  research the day's GTA 6 news and claims, plan tomorrow's 2–4 posts
  (carousel → Reel → carousel → Reel), write and render them, run the publish
  gate, upload the media, and post ONE approval message to Slack
  #gtad-approvals. PUBLISH (posting slots): if Jess approved with ✅, publish
  the post that is due through Windsor.ai, then log it. Use for "run the daily
  routine", "prep tomorrow's posts", "publish the next post", or any scheduled
  GTA Decoded run.
---

# GTA Decoded daily routine

Read `outputs/gta6-codes/HANDOFF.md` first. It holds the rules, IDs and current state.
The queue file `outputs/gta6-codes/queue/queue.json` is the single source of truth for posts.
Times are **Australia/Melbourne**. The posting slots (08:23, 10:23, 12:23, 14:23) land in
the US evening, which is when most of the audience is online.

## Never break
- **Nothing is published without Jess's ✅** on that day's Slack approval message. No ✅ means no post, and nothing is "assumed approved".
- Never invent codes, claims or sources. Untested claims are **UNVERIFIED** ("still testing"). Only Jess's own test, or an official Rockstar, PlayStation or Xbox source, can make something CONFIRMED.
- Other creators' videos are leads only: paraphrase, no footage or audio, and credit them when they're named.
- No Rockstar logos, fonts or key art, and no AI-generated GTA characters. Use the Decoder mascot.
- Every caption carries "Fan-made · not affiliated with Rockstar Games or Take-Two." Every post with AI visuals also says "Visuals are AI-generated." The API can't set Instagram's AI label.
- Spend limit: about 1,600 Artlist credits a day (2 new 8 s shots). Reuse the library first. Anything bigger needs Jess's OK in Slack.

## Setup (fresh session)
1. The media repo must be next to this repo at `../gta-decoded-media`. If it isn't:
   - call `add_repo` (owner `wilba-audit`, repo `gta-decoded-media`, access `push`)
   - clone it light: `git clone --depth 1 --filter=blob:none --sparse <url> ../gta-decoded-media`
   - then `git -C ../gta-decoded-media sparse-checkout set posts/.keep`, so the big library isn't downloaded
2. Library shots are public. To use one, fetch it, for example:
   `curl -sLo /tmp/shot.mp4 https://raw.githubusercontent.com/wilba-audit/gta-decoded-media/main/library/lib-10-point.mp4`
   The list of shots and what each one shows is in `outputs/gta6-codes/brand/decoder/LIBRARY.md`.
3. Disk space is limited. Delete temporary videos once they're uploaded.

## Mode PUBLISH (runs at each slot)
1. Load the queue. Find posts with `date` = today, `status` "awaiting_approval" or "approved", and `slot` at or before now.
2. For each post still "awaiting_approval", check approval: read the reactions (`slack_get_reactions`) on that day's approval message (`slack_ts`) in channel `C0CKLCULPQU`.
   - ✅ / `white_check_mark` / `heavy_check_mark` approves every post that day, except any she replied to in the thread with "skip N" or "no N". Read the thread with `slack_read_thread`.
   - ❌ / `x` rejects the whole day: set status "rejected" and stop.
   - Neither: do nothing, and stop. Never publish without approval.
3. Publish one post per slot, the earliest due. Use Windsor (`execute_action`, connector `instagram`, account `17841454480305652`):
   - carousel → `create_carousel_post` with `items: [{image_url, alt_text}]` and `caption`
   - reel → `create_video_post` with `video_url`, `caption`, `share_to_feed: true`
4. On success: set `status` "published", record `ig_media_id` and `published_at`, then reply in the Slack thread "Posted ✓ <id> at <time>".
   On failure: reply in the thread with the plain-English reason, set status "failed" and keep the error. Don't retry more than once.
   If a raw GitHub video URL fails, retry once with `https://cdn.jsdelivr.net/gh/wilba-audit/gta-decoded-media@main/<path>`.
5. Commit the queue file and push to the work branch (`claude/gta6-content-business-ai-hmfjqn`).

## Mode PREP (runs once each evening, about 19:20)
1. **Publish leftovers:** run PUBLISH first for anything due and approved today.
2. **Research (about 15 minutes):** web search for the last 24 hours of GTA 6 news, including:
   - patch notes and official Newswire, PlayStation Blog and Xbox Wire posts
   - promo offers and viral "cheat code" or glitch claims, including Reddit and YouTube titles
   - what's trending

   Save notes with source links to `outputs/gta6-codes/research/<date>.md`. Run anything that is a claim about a code through the `gta6-code-verifier` rules and log it in `code-ledger-template.csv` (proposals only).
3. **Plan tomorrow:** 2–4 posts, alternating carousel → Reel, starting with whichever type the last published post wasn't.
   - Mix: one "Real or Busted?" claim, one useful guide or tip from an official source, one news reaction, and one scam warning or community post.
   - Check the "what works" notes in `outputs/gta6-codes/PLAYBOOK.md` if it exists.
4. **Make carousels:**
   - add frames to `outputs/gta6-codes/instagram/content.json`: 4–6 slides, 1080×1350, layouts cover / list / stamps / poll / reveal / status / cta
   - render with `node scripts/gta6_ig_render.js <id-prefix>`
   - look at every slide image before using it (text overflow, overlaps, typos)
5. **Make Reels:**
   - write a spec JSON in `outputs/gta6-codes/reels/specs/<id>.json` with keys `id`, `shot` (library file path), `caps` [[start, end, text]], `eyebrow`, `lines`, `q`, `stamp`, `end`, `audio`
   - write the voiceover script, about 14–18 s and about 40 words, in the punchy "no-BS" voice
   - generate it with Artlist `generate_voiceover`, voice "Shadow", folder "GTA Decoded Reels"; download to `reels/vo/<id>.mp3`
   - build: `python3 scripts/gta6_reel_build.py outputs/gta6-codes/reels/specs/<id>.json`
   - check a frame from each section
6. **Gate:** run the `gta6-publish-gate` checklist on every post and store PASS or FAIL in the queue (`gate`). Posts that FAIL don't go in the approval message.
7. **Upload:** `python3 scripts/gta6_media_push.py <post-id> <files in order>`, then check every URL returns 200.
8. **Queue:** add each post with `date` tomorrow, `slot`, `type`, `media`, `caption`, `alt`, `status` "awaiting_approval" and `gate`.
9. **Ask for approval:** send ONE Slack message to `C0CKLCULPQU` and save its `ts` on each of tomorrow's posts. The format:
   ```
   **GTA Decoded · posts for <weekday date>** (react ✅ to approve all · ❌ to skip the day · reply "skip 2" to drop one)
   1) 08:23 · Carousel · <title> — <preview link to slide 1>
   > <caption, first 2 lines>
   2) 10:23 · Reel · <title> — <video link>
   ...
   Gate: all PASS · Credits used today: <n> · Research: <1-line headline of the day>
   ```
   Tag anything Jess has to do herself, for example "needs your test before we can stamp CONFIRMED".
10. Commit and push the work branch (everything except big media), then update HANDOFF.md if anything changed.

## Weekly (Monday PREP)
- Pull last week's Instagram insights from Windsor (`get_fields`, then `get_data`, connector `instagram`).
- Write the scorecard with `gta6-analytics-review`, and update `outputs/gta6-codes/PLAYBOOK.md` with "what works" and "what to stop".
- Post a 5-line summary in the Slack approval message.
