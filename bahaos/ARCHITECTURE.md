# BahaOS — Architecture

**Product:** Autonomous social-media operating system for Baha Baha Villas (West Sumbawa).
**Owner:** WILBA (Jess Morrell). Baha Baha is the pilot client and case study.
**Status:** Foundation docs. MVP vertical slice to follow.

> **North star:** Baha uploads raw photos/video → BahaOS understands it → proposes a *finished* piece of content → human approves → it publishes → performance feeds the next decision. The human keeps taste and approval; the machine removes production work. Quality bar: *would a genuinely good surf brand post this?* — never *how much can we generate?*

---

## 1. Guiding engineering principles

1. **Reality-first.** Authentic Baha footage is the product. AI media complements, never fabricates conditions/guests/rooms. (See `BRAND_BRAIN.md` §Truthfulness.)
2. **Deterministic where it matters.** Video rendering, state machines, and schema-validated agent outputs are deterministic. LLM prose never drives critical state transitions.
3. **Provider abstraction everywhere.** No vendor SDK is called from feature code. Every external capability sits behind an interface with a Mock implementation, so the app runs and tests without credentials.
4. **Simplest architecture that stays extensible.** One Next.js app + one worker + Postgres. No microservices until scale forces it. No fake placeholders disguised as done.
5. **Cost-aware.** FFmpeg (free, deterministic) before any paid generation. Every paid call is logged, budgeted, and confirmable.

---

## 2. System shape (high level)

```
┌──────────────────────────────────────────────────────────────┐
│  WEB APP (Next.js App Router)   — the Editorial Desk           │
│  Today · Library · Ideas · Drafts · Calendar · Published ·     │
│  Analytics · Brand Brain · Settings                            │
└───────────────┬──────────────────────────────────────────────┘
                │ server actions / route handlers (typed)
┌───────────────▼──────────────────────────────────────────────┐
│  CORE SERVICES (TypeScript, shared lib)                        │
│  ingestion · media-intelligence · scoring · content-memory ·  │
│  ideation · reel-director(EDL) · render(FFmpeg) · copywriter · │
│  critic · thumbnails · scheduling · publishing · analytics     │
└───────────────┬───────────────────────────┬──────────────────┘
                │ enqueue durable jobs        │ read/write
┌───────────────▼──────────────┐   ┌─────────▼──────────────────┐
│  WORKER (Node + FFmpeg)       │   │  POSTGRES + pgvector        │
│  ingest, analyse, embed,      │   │  (Supabase)                 │
│  render, generate, publish    │   │  assets, EDLs, drafts, …    │
└───────────────┬──────────────┘   └────────────────────────────┘
                │ via provider interfaces
   ┌────────────┼─────────────┬───────────────┬─────────────┐
   ▼            ▼             ▼               ▼             ▼
 Vision     Language     Embedding      CreativeVideo    Publisher
 (Claude)   (Claude)   (multimodal)    (Higgsfield)   (Meta Graph)
                │
           MediaStorage (Local → S3/R2)
```

---

## 3. Technology decisions (deliberate)

| Layer | Choice | Why (senior rationale) |
|---|---|---|
| **Framework** | Next.js (App Router) + React + TypeScript (strict) | One codebase for UI + typed server logic; server actions keep the client thin. It's a media product, so co-locating a rich UI with typed data access wins. |
| **Styling / UI** | Tailwind + shadcn/ui | Fast, consistent, accessible primitives; the desk needs large previews and minimal chrome, not a component zoo. |
| **Database** | PostgreSQL (Supabase) | Relational schema is the backbone; Supabase gives Postgres + storage + auth without ops. |
| **Vector search** | **pgvector** in the same Postgres | Semantic media search ("clean barrel clips from Supersuck") lives next to the relational data — no separate vector DB to sync. This one requirement is why the ORM choice below matters. |
| **ORM** | **Drizzle** | Chosen over Prisma deliberately: (1) first-class **pgvector** support via custom types, which Prisma handles awkwardly; (2) type-safe SQL with zero runtime engine — clean in serverless; (3) transparent queries for a media pipeline where we care about exact SQL. Trade-off: less batteries-included than Prisma; acceptable for a focused schema. |
| **Job queue** | **Graphile Worker** (Postgres-backed) for MVP | Durable jobs with retries and zero extra infrastructure — it reuses the Postgres we already run. Avoids standing up Redis on day one. **Upgrade path:** Inngest (managed step-functions) when agent + render fan-out gets complex, or BullMQ/Redis for raw throughput. |
| **Video render** | **FFmpeg** driven by an Edit Decision List | Deterministic, free, battle-tested. Edit decisions live in data (the EDL), not in render code, so editing logic is testable independently of rendering. |
| **Deployment** | Web on Vercel; **Worker + FFmpeg on a long-running container** (Render / Railway / Fly) | Reels are long CPU jobs — they cannot run in a serverless request. The worker is a persistent container with FFmpeg installed. This split is a hard requirement, called out early. |

---

## 4. Provider interfaces (the extensibility spine)

Every external capability is an interface in `core/providers/`. Feature code depends on the interface, never the vendor. Each has a **Mock** used in dev/tests and whenever credentials are absent.

```ts
interface VisionProvider {           // image + sampled-frame understanding
  analyzeImage(input: ImageRef): Promise<VisionAnalysis>
  analyzeFrames(frames: FrameRef[]): Promise<FrameAnalysis[]>
}
interface LanguageProvider {         // creative director, copywriter, critic, analyst
  complete<T>(req: StructuredRequest<T>): Promise<T>   // Zod-validated, retried
}
interface EmbeddingProvider {        // multimodal embeddings for semantic search
  embedImage(input: ImageRef): Promise<number[]>
  embedText(text: string): Promise<number[]>
}
interface CreativeVideoProvider {    // Higgsfield etc. — image→video, bridges, campaigns
  generate(req: GenerationRequest): Promise<GenerationJob>
  poll(jobId: string): Promise<GenerationResult>
}
interface Publisher {                // Meta Instagram Content Publishing API
  createDraft(post: PublishablePost): Promise<PlatformDraft>
  publish(draftId: string): Promise<PublishedRef>
}
interface MediaStorageProvider {     // local → S3 / R2 / Drive adapters
  put(file: LocalFile): Promise<StoredRef>
  getUrl(ref: StoredRef): Promise<string>
  getStream(ref: StoredRef): Promise<ReadableStream>
}
```

**Default bindings:** Vision + Language → Anthropic Claude (one vendor for reasoning + vision). Embedding → a multimodal model (Voyage multimodal or OpenAI image/text embeddings) behind the interface so it can be swapped. CreativeVideo → `HiggsfieldProvider` + `MockCreativeProvider`. Publisher → `MetaInstagramPublisher` + `MockPublisher`. Storage → `LocalStorageProvider` + `S3StorageProvider`.

---

## 5. The agents (small, sharp, schema-bound)

Seven responsibilities, not fifty. Each returns **Zod-validated structured data**; malformed output is retried; prompts/responses/model versions are logged.

| Agent | Owns | Consumes | Emits (validated) |
|---|---|---|---|
| **Media Analyst** | Understanding assets & video segments | frames, metadata | `AssetAnalysis`, `VideoSegment[]`, tags |
| **Creative Director** | *What should we post next?* (editorial judgement, incl. "nothing today") | library, memory, performance, pillars, date | `ContentIdea` or `no-post` decision |
| **Reel Director** | Turning footage into an Edit Decision List | selected assets/segments, editing personality | `EditDecisionList` (`EditSegment[]`) |
| **Copywriter** | Baha-voice captions | concept, actual scenes, caption history | `Caption` set (primary/minimal/alt) |
| **Critic** | Quality control: cheese, generic-AI, overwriting, surfer-test, repetition, truthfulness | captions + concept | pass/fail + reasons + rewrite |
| **Analyst** | Weekly editorial observations from performance | performance snapshots | `Observation[]` (no fake precision) |
| **Orchestrator** | Coordinates the pipeline & state transitions | all of the above | job/state transitions |

Freeform prose never mutates critical state. The Orchestrator moves posts through the state machine only on schema-valid inputs that clear the quality gates.

---

## 6. Core pipelines

**Ingestion** → hash (dedupe) → extract metadata (ffprobe) → thumbnails + video proxies → `Asset` record. Storage behind `MediaStorageProvider` so Drive/S3/R2 swap in later.

**Media intelligence** → sample frames intelligently (scene changes, motion peaks) not every frame → `AssetAnalysis` + `VideoSegment[]` with timestamp ranges → multimodal embeddings → `ContentScore` (transparent, weighted /100, with a human-readable *why*). Human overrides feed preference memory.

**Ideation → production (the MVP heart):** Creative Director picks an idea grounded in real available assets → Reel Director builds an EDL → FFmpeg renders 1080×1920 → Copywriter drafts captions → Critic gates them → Thumbnail engine proposes 3 frames → draft surfaces on **Today** with preview, rationale, caption, thumbnail.

**Publishing** state machine: `draft → approved → scheduled → publishing → published | failed`. Failures are retryable; approved posts are never lost; platform post IDs stored. **No auto-publish without human approval** in early versions (§Safety).

---

## 7. Quality gates (nothing reaches "Ready for approval" until it passes)

`asset validity · brand relevance · caption quality · cheese test · repetition test · render validation · thumbnail validation · truthfulness`. Each failure carries an explicit reason shown in the UI.

---

## 8. Safety

Human approval is mandatory while the system is young. Extra scrutiny (hard gate) when: people are identifiable, AI materially alters reality, new claims/pricing/availability/offers appear, or location could be sensitive. Autonomous publishing is a later, explicit, per-account setting — off by default.

---

## 9. Observability & cost

Structured logs, job statuses, provider errors + retries, render/generation/publish logs, and a developer diagnostics screen. Generation budgets with a hard ceiling and confirmation thresholds; FFmpeg is always preferred when it can do the job deterministically.

---

## 10. What this session delivers vs. what's next

**Delivered now:** this `ARCHITECTURE.md`, `IMPLEMENTATION_PLAN.md`, `BRAND_BRAIN.md`, and the initial schema (`db/schema.ts`).
**Next (build phases):** the MVP vertical slice (ingest → analyse → library → "make me something" → EDL → render → caption → critic → approve), then Higgsfield/publishing/analytics/memory, then proactive behaviour. See `IMPLEMENTATION_PLAN.md`.
