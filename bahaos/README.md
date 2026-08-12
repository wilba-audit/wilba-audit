# BahaOS

Autonomous social-media operating system for **Baha Baha Villas** (West Sumbawa).
Raw footage in → understood → a *finished* piece of content proposed → human approves → published → performance learns.

**Owned by WILBA.** Baha Baha is the pilot + case study; the system is built to be relicensed to other surf/hospitality brands.

> Quality bar: *would a genuinely good surf brand post this?* — never *how much can we generate?*

## Documents (read in this order)
1. [`ARCHITECTURE.md`](./ARCHITECTURE.md) — system shape, tech decisions, provider interfaces, agents.
2. [`IMPLEMENTATION_PLAN.md`](./IMPLEMENTATION_PLAN.md) — staged build; the MVP vertical slice.
3. [`BRAND_BRAIN.md`](./BRAND_BRAIN.md) — the Baha voice, values, pillars, bans, truthfulness. The editorial conscience.
4. [`db/schema.ts`](./db/schema.ts) — initial Drizzle/Postgres schema (pgvector).

## Stack (see ARCHITECTURE.md for rationale)
Next.js (App Router) · TypeScript strict · Tailwind + shadcn/ui · Postgres + pgvector (Supabase) · Drizzle · Graphile Worker · **FFmpeg** (on a persistent worker container) · provider abstraction for Vision/Language/Embedding/CreativeVideo(Higgsfield)/Publisher(Meta)/Storage — each with a Mock.

## Status
Foundation documents complete. **Next: build Stage 1 — the MVP vertical slice** (ingest → analyse → library → "make me something" → EDL → FFmpeg render → caption → critic → approve). Judge the product on Stage 1 before funding the rest.

## Getting started (once implementation begins)
```bash
pnpm install
cp .env.example .env        # fill in credentials; app boots with Mocks if omitted
pnpm db:push                # apply schema (requires DATABASE_URL + pgvector)
pnpm dev                    # web app
pnpm worker                 # background worker (needs FFmpeg on PATH)
```

## Principles that don't bend
- **Reality-first.** Authentic Baha footage is the product; AI complements, never fabricates conditions/guests/rooms.
- **Human keeps taste + approval.** No auto-publish in early versions.
- **FFmpeg before paid generation.** Every paid call logged, budgeted, confirmable.
- **"Nothing worth posting today" is a valid output.** Never post weak content to hit a frequency.
