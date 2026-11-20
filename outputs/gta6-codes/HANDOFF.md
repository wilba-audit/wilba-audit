# GTA Decoded: session handoff (updated 20 Nov 2026)

**Read this first in any new session.** It records where the GTA Decoded automation stands and what comes next.
Work branch: `claude/gta6-content-business-ai-hmfjqn`. Cloud environment: **wilba-audit** (allows Artlist's file servers).

## What's built (all in this repo)
| Area | Where |
|---|---|
| Strategy, roadmap, SOPs, KPIs, research | `outputs/gta6-codes/*.md`, `outputs/gta6-codes/RESEARCH-sourcing-and-repurposing.md` |
| Brand: four-key logo, stamps, palette, fonts | `outputs/gta6-codes/brand/final/`, guide source `brand/guide/`, live guide https://claude.ai/artifact/UnyTeues1RJtdUteTtyLNo |
| Mascot "The Decoder" (visor shows the verdict) | `brand/decoder/` · `scripts/gta6_decoder.py` |
| Instagram profile kit, highlights, stories, carousels A–E | `outputs/gta6-codes/instagram/` · edit `content.json`, then run `node scripts/gta6_ig_render.js [id-filter]` |
| Captions and posting order | `instagram/POSTING-PACK.md`, `instagram/LAUNCH-REACTIONS-PACK.md` |
| Reels (Artlist shot + captions + stamp card + end card) | `outputs/gta6-codes/reels/` · `python3 scripts/gta6_reel_build.py <reel-id> <shot.mp4>` |
| Skills | `.claude/skills/gta6-*` (6) and `gaming-brand-designer` |

## Connected services
- **Instagram via Windsor.ai:**
  - account `gta.de.coded` (id `17841454480305652`)
  - actions: create_carousel_post, create_video_post (Reels), create_story, create_image_post, comment tools
  - **Media must be publicly reachable URLs**, and images must be **JPEG**, 4:5–1.91:1 and ≤ 8 MB
  - Open item: choose a public media host (see Next steps)
- **Artlist (AI Suite 40K plan):**
  - AI credits reset monthly; 37,600 left on 20 Nov, renews 29 Nov
  - **The music and SFX library is not included** (downloads come watermarked), so Reels go out silent and Jess adds sound in Instagram
  - Style kit "GTA Decoded" id `2edf986f-6c25-4552-8713-7e38518368e8`
  - Folder "GTA Decoded Reels" id `01a1f28e-6396-7c21-a49f-cf60b4aa08de`
  - Uploaded start frames (asset ids):
    - 9:16 unverified `e2779118-2092-4454-b7a6-8c75807557ef`
    - 9:16 default `4b4a417b-1b08-4ded-abe6-efe22223f1bc`
    - 4:5 scene `982f63f6-44af-4693-b6d0-d73644972e00`
    - transparent Decoder `6a4428d1-e0e7-4fac-9589-66daf438b8ff`
  - Best value model: Kling v3 Pro 1080p, 8 s = 800 credits (the aspect ratio comes from the start frame)
- **Slack:** private channel **#gtad-approvals** created (id `C0CKLCULPQU`). The daily approval message goes here.
- **Google Drive, Gmail, GitHub:** connected

## Rules that never change
- Never invent codes or claims. Anything untested is **UNVERIFIED** (stamp reads "STILL TESTING"). Only Jess's own test or an official source makes something CONFIRMED.
- Never repost other creators' footage. Their videos are leads only; paraphrase and credit them.
- No Rockstar logos, fonts or characters, and no AI-made GTA characters. Captions carry "Fan-made · not affiliated with Rockstar".
- Label AI-generated visuals (Instagram "AI info").
- **One-tap approval:** nothing publishes without Jess's ✅ in Slack.

## Decisions made
- Rhythm: 2–4 posts a day, alternating carousel → Reel
- Approvals in Slack, one tap a day
- Voice: captions only for now (Jess may add her own voice later)

## Next steps (in order)
1. ~~Handle~~ Done: all assets re-rendered with `@gta.de.coded`.
2. ~~Slack channel~~ Done: `#gtad-approvals` (id `C0CKLCULPQU`).
3. **Public media hosting for Windsor:** repo `wilba-audit/gta-decoded-media` (public) attached, but pushes are refused (403) until the Claude GitHub App covers it, or GitHub is re-linked at https://claude.ai/customize/connectors?auth_start=github&auth_start_force=1. Then pick and set up one (options: a public GitHub repo or Pages for media, Cloudflare R2, or Google Drive public links), then **convert carousel PNGs to JPEG**.
4. **Allow research sites** in the wilba-audit environment (Reddit, YouTube, Rockstar Newswire, PlayStation Blog, Xbox Wire), and build automatic YouTube transcripts.
5. **Decoder shot library:** approved. 3 poses done; batch 1 (20 shots, 13,600 credits) queued 20 Nov. See `brand/decoder/LIBRARY.md` for ids. Batch 2 (4 openers, about 2,000) is still to do. Voice: "Shadow".
6. **`gta6-daily` skill:** research → plan → write → render → build Reels → publish-gate check → Slack approval → publish via Windsor → log.
7. **Scheduled task:** run the daily routine at about 6am AEST in a fresh session.
8. **Weekly scorecard + "what works" playbook** (`outputs/gta6-codes/PLAYBOOK.md`), fed by Windsor Instagram insights.
9. Post the launch content already made: carousels A–E, Reels 1–3, stories (see POSTING-PACK.md).

## Prompt to restart in a new session
> Read `outputs/gta6-codes/HANDOFF.md` and `CLAUDE.md`, then continue the GTA Decoded automation from the "Next steps" list. Work on branch `claude/gta6-content-business-ai-hmfjqn`.
