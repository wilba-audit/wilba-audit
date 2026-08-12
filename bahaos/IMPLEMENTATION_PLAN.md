# BahaOS — Implementation Plan

A staged build. Each stage ships something real and testable. We do **not** attempt the whole platform at once. The MVP vertical slice must feel excellent before anything expands.

> **Roles.** Jess = product owner (taste, brand, approval, priorities). Griffin = build. This plan is written so Griffin can execute it and Jess can track it without reading code.

---

## Stage 0 — Project setup (0.5–1 day)

- Initialise standalone repo `bahaos` (its own repo, **not** inside the AIOS workspace).
- Next.js (App Router) + TypeScript strict + Tailwind + shadcn/ui.
- Supabase project (Postgres + `pgvector` extension enabled + storage bucket).
- Drizzle configured; first migration from `db/schema.ts`.
- Graphile Worker wired to Postgres; a persistent worker container (Render/Railway/Fly) with **FFmpeg installed**.
- `.env.example` complete (see `README.md`). Provider **Mocks** implemented first so the app boots with zero external credentials.
- CI: typecheck, lint, unit tests. Commit hooks.

**Done when:** app boots, DB migrates, a mock job runs end-to-end through the worker, tests pass.

---

## Stage 1 — MVP VERTICAL SLICE (the one that must be excellent)

The single workflow, built deep before wide:

```
Import Baha folder → index → analyse → Library (assets+tags+scores)
→ "Make me something" → Creative Director picks a real-grounded idea
→ Reel Director builds an EDL → FFmpeg renders 1080×1920
→ Copywriter drafts captions → Critic gates them
→ Today: video preview + rationale + caption + thumbnail → Approve / Edit / Regenerate
```

**1a. Ingestion & Library**
- `LocalStorageProvider`; ingest a directory of MP4/MOV/JPEG/JPG/PNG (HEIC where feasible).
- Hash-dedupe; `ffprobe` metadata (dimensions, duration, orientation, fps, codec, created-at, GPS/camera if present); thumbnails + proxy videos.
- Library UI: fast grid, large previews, tag chips, score badges, filter/sort.

**1b. Media Intelligence & Scoring**
- Media Analyst: photo attributes + surf-clip attributes (wave direction/size, barrel, turn, takeoff, wipeout, ride length, quality, crowd, subject visibility).
- Video segmentation: smart frame sampling → candidate moments as timestamp ranges.
- Multimodal embeddings → pgvector; natural-language search ("clean barrel clips from Supersuck").
- `ContentScore` /100, **transparent** (weighted dimensions + human-readable *why*). Human override → preference memory.

**1c. Creative Director → Reel Director → Render**
- Creative Director returns a `ContentIdea` grounded in real assets — or a valid **"nothing worth posting today."**
- Reel Director emits a validated `EditDecisionList` (per-segment source/timeline/crop/zoom/speed/transition/audio/text). Editing personalities: RAW SURF, SURF FILM, FAST SOCIAL, CINEMATIC, LIFESTYLE, MINIMAL, HUMOUR.
- FFmpeg render pipeline consumes the EDL (trim → 9:16 crop → concat → speed ramp → text/logo → export). Deterministic; EDL is testable without rendering.

**1d. Copy, Critic, Thumbnails, Today**
- Copywriter: primary / minimal / alternative captions in the Baha voice (`BRAND_BRAIN.md`). Not every field forced.
- Critic: cheese / generic-AI / overwriting / forced-slang / repetition / truthfulness + **surfer test**. Fail → reject + reasons + rewrite.
- Thumbnail engine: 3 scored frame candidates, optional ≤3-word overlay.
- **Today** screen: finished piece + creative rationale + caption + thumbnail; buttons Approve / Edit / Regenerate / Skip / Reject.

**Done when:** dropping a real Baha folder in produces a *finished* reel + caption + thumbnail the owner would actually post, with visible reasoning — and "make me something" feels like a good human made it.

---

## Stage 2 — Memory, calendar, publishing, analytics

- **Content Memory:** `PublishedPost` records; repetition detection ("shown this clip 3×", "no villas for 12 days", "wellness underrepresented this month") feeding the Creative Director.
- **Calendar / Drafts:** schedule, reorder, status columns.
- **Publishing:** `MockPublisher` → `MetaInstagramPublisher` (current Meta Content Publishing API + auth; fetch live docs at build time). Retryable state machine; store platform IDs.
- **Analytics adapters:** Meta insights ingestion → `PerformanceSnapshot`; editorial *observations*, not fake precision.

---

## Stage 3 — Creative AI + learning

- **Higgsfield** behind `CreativeVideoProvider` (+ Mock): image→video, cinematic bridges, establishing shots. Production prompt generator (camera/movement/lighting/lens/realism + must-keep / must-not-appear). Every generation logged with input/prompt/model/settings/cost/approval.
- **Feedback learning:** every human action (edit, remove asset, shorten caption, drop CTA, reject clip) → structured preference memory that shifts future scoring/copy. **No model fine-tuning initially.**
- **Weekly strategist:** observations + content-diversity + freshness balancing (performance informs, never dictates — protect the brand).

---

## Stage 4 — Proactive (the long-term vision)

Watched folder → new footage detected → Media Analyst finds the standout clip → Creative Director judges it timely → draft reel auto-created → owner pinged: *"Yesterday's Supersuck footage is strong. I made something."* → approve → done.

---

## Testing (from Stage 0, always)

Deterministic units first: ingestion, dedupe, caption-schema validation, **EDL validation**, timeline math, post **state machine**, publishing safeguards (approval enforcement), provider-failure fallbacks. External AI mocked in automated tests.

---

## Explicit assumptions

1. Worker host has FFmpeg and enough CPU/RAM for 1080×1920 encodes. (Vercel serverless cannot render — Stage 0 provisions a container.)
2. Anthropic API for reasoning + vision; a separate multimodal embedding provider (abstracted).
3. Higgsfield reachable via its official MCP/SDK/API — not browser automation.
4. Meta publishing requires an IG **Business/Creator** account + Facebook Page + reviewed app permissions; treat this as a credentialed integration built behind the interface with a Mock until approved.
5. HEIC handling may need a decode step (libheif/sips) on the worker.

---

## Sequencing note for Jess (non-technical)

You only need to feel Stage 1. If "make me something" from a real Baha folder produces one reel you'd genuinely post, the product is real and worth funding the rest. Everything after that is expansion. **Fund and judge Stage 1 first.**
