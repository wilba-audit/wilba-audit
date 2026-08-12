/**
 * BahaOS — initial database schema (Drizzle + Postgres/pgvector).
 *
 * Design notes:
 * - Structured application state lives in real columns/enums; JSONB only supplements
 *   (raw provider payloads, flexible attribute bags), never replaces, structured records.
 * - Embeddings use pgvector for semantic media search.
 * - Media bytes are NOT stored here — only references (storageKey) resolved via
 *   MediaStorageProvider. This keeps storage swappable (local → S3/R2/Drive).
 */

import {
  pgTable, pgEnum, uuid, text, integer, real, boolean,
  timestamp, jsonb, doublePrecision, index, uniqueIndex, vector,
} from "drizzle-orm/pg-core";

/* ─────────────────────────── Enums ─────────────────────────── */

export const assetKind = pgEnum("asset_kind", ["photo", "video"]);
export const orientation = pgEnum("orientation", ["portrait", "landscape", "square"]);
export const analysisStatus = pgEnum("analysis_status", ["pending", "processing", "done", "failed"]);
export const postFormat = pgEnum("post_format", ["reel", "carousel", "single_image", "story", "story_series", "facebook_post"]);
export const editingPersonality = pgEnum("editing_personality", ["raw_surf", "surf_film", "fast_social", "cinematic", "lifestyle", "minimal", "humour"]);
export const draftState = pgEnum("draft_state", ["idea", "drafting", "ready_for_approval", "approved", "scheduled", "publishing", "published", "failed", "rejected", "skipped"]);
export const captionVariant = pgEnum("caption_variant", ["primary", "minimal", "alternative"]);
export const generationStatus = pgEnum("generation_status", ["queued", "running", "succeeded", "failed", "cancelled"]);
export const jobStatus = pgEnum("job_status", ["queued", "running", "succeeded", "failed", "retrying"]);
export const feedbackKind = pgEnum("feedback_kind", [
  "approved_first_attempt", "caption_edited", "asset_removed", "concept_rejected",
  "post_skipped", "thumbnail_changed", "cta_removed", "pillar_changed",
  "caption_rewritten", "ai_clip_rejected",
]);

/* ─────────────────────── Brand / configuration ─────────────────────── */

export const contentPillars = pgTable("content_pillars", {
  id: uuid("id").defaultRandom().primaryKey(),
  key: text("key").notNull().unique(),          // SURF, STAY, WELLNESS, ...
  label: text("label").notNull(),
  description: text("description"),
  isCore: boolean("is_core").default(false).notNull(),
  weightHint: real("weight_hint").default(1),   // guidance, not a hard quota
  active: boolean("active").default(true).notNull(),
});

export const brandRules = pgTable("brand_rules", {
  id: uuid("id").defaultRandom().primaryKey(),
  category: text("category").notNull(),         // voice | banned_phrase | value | cta | hashtag_group | truthfulness
  content: jsonb("content").notNull(),          // editable Brand Brain config
  active: boolean("active").default(true).notNull(),
  updatedAt: timestamp("updated_at").defaultNow().notNull(),
});

export const persons = pgTable("persons", {
  id: uuid("id").defaultRandom().primaryKey(),
  displayName: text("display_name"),
  consentToPost: boolean("consent_to_post").default(false).notNull(),
  notes: text("notes"),
});

export const locations = pgTable("locations", {
  id: uuid("id").defaultRandom().primaryKey(),
  name: text("name").notNull(),                 // Yo Yos, Tropicals, Super Sucks, Villa, Pool, ...
  kind: text("kind"),                            // surf_break | facility | area
  lat: doublePrecision("lat"),
  lng: doublePrecision("lng"),
  sensitive: boolean("sensitive").default(false).notNull(),
});

/* ─────────────────────────── Assets ─────────────────────────── */

export const assets = pgTable("assets", {
  id: uuid("id").defaultRandom().primaryKey(),
  kind: assetKind("kind").notNull(),
  storageKey: text("storage_key").notNull(),    // resolved via MediaStorageProvider
  originalFilename: text("original_filename"),
  contentHash: text("content_hash").notNull(),  // dedupe
  mimeType: text("mime_type"),
  width: integer("width"),
  height: integer("height"),
  orientation: orientation("orientation"),
  durationMs: integer("duration_ms"),           // video only
  fps: real("fps"),
  codec: text("codec"),
  capturedAt: timestamp("captured_at"),
  gpsLat: doublePrecision("gps_lat"),
  gpsLng: doublePrecision("gps_lng"),
  cameraMeta: jsonb("camera_meta"),
  thumbnailKey: text("thumbnail_key"),
  proxyKey: text("proxy_key"),                  // low-res video proxy
  analysisStatus: analysisStatus("analysis_status").default("pending").notNull(),
  createdAt: timestamp("created_at").defaultNow().notNull(),
}, (t) => ({
  hashIdx: uniqueIndex("assets_hash_idx").on(t.contentHash),
  statusIdx: index("assets_status_idx").on(t.analysisStatus),
}));

export const assetAnalysis = pgTable("asset_analysis", {
  id: uuid("id").defaultRandom().primaryKey(),
  assetId: uuid("asset_id").notNull().references(() => assets.id, { onDelete: "cascade" }),
  attributes: jsonb("attributes").notNull(),    // surf/no-surf, wave, people, villa, food, sunset, ...
  surfAttributes: jsonb("surf_attributes"),     // wave direction/size, barrel, turn, takeoff, wipeout, ride length, crowd
  locationId: uuid("location_id").references(() => locations.id),
  modelProvider: text("model_provider"),
  modelVersion: text("model_version"),
  createdAt: timestamp("created_at").defaultNow().notNull(),
}, (t) => ({ assetIdx: index("asset_analysis_asset_idx").on(t.assetId) }));

// Multimodal embedding for semantic search (dimension set to chosen provider; 512 placeholder).
export const assetEmbeddings = pgTable("asset_embeddings", {
  id: uuid("id").defaultRandom().primaryKey(),
  assetId: uuid("asset_id").notNull().references(() => assets.id, { onDelete: "cascade" }),
  embedding: vector("embedding", { dimensions: 512 }).notNull(),
  provider: text("provider").notNull(),
}, (t) => ({
  embIdx: index("asset_embeddings_hnsw").using("hnsw", t.embedding.op("vector_cosine_ops")),
}));

export const videoSegments = pgTable("video_segments", {
  id: uuid("id").defaultRandom().primaryKey(),
  assetId: uuid("asset_id").notNull().references(() => assets.id, { onDelete: "cascade" }),
  startMs: integer("start_ms").notNull(),
  endMs: integer("end_ms").notNull(),
  label: text("label"),                         // "drops into clean right", "barrel section", ...
  attributes: jsonb("attributes"),
  createdAt: timestamp("created_at").defaultNow().notNull(),
}, (t) => ({ assetIdx: index("video_segments_asset_idx").on(t.assetId) }));

export const assetTags = pgTable("asset_tags", {
  assetId: uuid("asset_id").notNull().references(() => assets.id, { onDelete: "cascade" }),
  tag: text("tag").notNull(),
  source: text("source").default("ai").notNull(), // ai | human
}, (t) => ({ pk: uniqueIndex("asset_tags_pk").on(t.assetId, t.tag) }));

// Transparent scoring. `breakdown` holds each weighted dimension; `why` is the human-readable reason.
export const contentScores = pgTable("content_scores", {
  id: uuid("id").defaultRandom().primaryKey(),
  assetId: uuid("asset_id").references(() => assets.id, { onDelete: "cascade" }),
  segmentId: uuid("segment_id").references(() => videoSegments.id, { onDelete: "cascade" }),
  total: integer("total").notNull(),            // 0..100
  breakdown: jsonb("breakdown").notNull(),      // { visual_quality, story_value, surf_quality, ... }
  why: text("why").notNull(),
  humanOverride: integer("human_override"),
  createdAt: timestamp("created_at").defaultNow().notNull(),
});

/* ───────────────────── Ideas, drafts, production ───────────────────── */

export const contentIdeas = pgTable("content_ideas", {
  id: uuid("id").defaultRandom().primaryKey(),
  title: text("title").notNull(),
  pillarId: uuid("pillar_id").references(() => contentPillars.id),
  format: postFormat("format").notNull(),
  reason: text("reason").notNull(),             // why post this now (editorial rationale)
  hook: text("hook"),
  storyStructure: jsonb("story_structure"),
  estimatedDurationMs: integer("estimated_duration_ms"),
  captionDirection: text("caption_direction"),
  enhancementsRequired: jsonb("enhancements_required"),
  confidence: real("confidence"),               // 0..1
  createdAt: timestamp("created_at").defaultNow().notNull(),
});

export const postDrafts = pgTable("post_drafts", {
  id: uuid("id").defaultRandom().primaryKey(),
  ideaId: uuid("idea_id").references(() => contentIdeas.id),
  pillarId: uuid("pillar_id").references(() => contentPillars.id),
  format: postFormat("format").notNull(),
  state: draftState("state").default("idea").notNull(),
  renderKey: text("render_key"),                // rendered video/image output
  rationale: text("rationale"),                 // creative director explanation shown in UI
  qualityGates: jsonb("quality_gates"),         // { cheese: pass, repetition: pass, truthfulness: pass, ... }
  createdAt: timestamp("created_at").defaultNow().notNull(),
  updatedAt: timestamp("updated_at").defaultNow().notNull(),
}, (t) => ({ stateIdx: index("post_drafts_state_idx").on(t.state) }));

export const postAssets = pgTable("post_assets", {
  draftId: uuid("draft_id").notNull().references(() => postDrafts.id, { onDelete: "cascade" }),
  assetId: uuid("asset_id").notNull().references(() => assets.id),
  ordering: integer("ordering").default(0).notNull(),
}, (t) => ({ pk: uniqueIndex("post_assets_pk").on(t.draftId, t.assetId) }));

export const editDecisionLists = pgTable("edit_decision_lists", {
  id: uuid("id").defaultRandom().primaryKey(),
  draftId: uuid("draft_id").notNull().references(() => postDrafts.id, { onDelete: "cascade" }),
  personality: editingPersonality("personality").notNull(),
  totalDurationMs: integer("total_duration_ms"),
  createdAt: timestamp("created_at").defaultNow().notNull(),
});

export const editSegments = pgTable("edit_segments", {
  id: uuid("id").defaultRandom().primaryKey(),
  edlId: uuid("edl_id").notNull().references(() => editDecisionLists.id, { onDelete: "cascade" }),
  sourceAssetId: uuid("source_asset_id").notNull().references(() => assets.id),
  ordering: integer("ordering").notNull(),
  sourceStartMs: integer("source_start_ms").notNull(),
  sourceEndMs: integer("source_end_ms").notNull(),
  timelineStartMs: integer("timeline_start_ms").notNull(),
  timelineEndMs: integer("timeline_end_ms").notNull(),
  crop: jsonb("crop"),                          // { x, y, w, h } for 9:16
  zoom: real("zoom").default(1),
  speed: real("speed").default(1),
  transition: text("transition"),               // prefer "cut"
  audioBehaviour: jsonb("audio_behaviour"),
  textOverlay: jsonb("text_overlay"),
  effects: jsonb("effects"),
});

export const captions = pgTable("captions", {
  id: uuid("id").defaultRandom().primaryKey(),
  draftId: uuid("draft_id").notNull().references(() => postDrafts.id, { onDelete: "cascade" }),
  variant: captionVariant("variant").notNull(),
  body: text("body").notNull(),
  locationLine: text("location_line"),
  cta: text("cta"),                             // may be null — no CTA is valid
  hashtags: jsonb("hashtags"),                  // string[]
  cheeseScore: real("cheese_score"),
  critiqued: boolean("critiqued").default(false).notNull(),
  critiqueNotes: jsonb("critique_notes"),
});

export const thumbnails = pgTable("thumbnails", {
  id: uuid("id").defaultRandom().primaryKey(),
  draftId: uuid("draft_id").notNull().references(() => postDrafts.id, { onDelete: "cascade" }),
  frameKey: text("frame_key").notNull(),
  score: integer("score"),
  overlayText: text("overlay_text"),            // ≤ ~3 words, optional
  selected: boolean("selected").default(false).notNull(),
});

/* ──────────────── Generation, scheduling, publishing ──────────────── */

export const generations = pgTable("generations", {
  id: uuid("id").defaultRandom().primaryKey(),
  provider: text("provider").notNull(),          // higgsfield | mock
  inputAssetId: uuid("input_asset_id").references(() => assets.id),
  prompt: text("prompt").notNull(),
  model: text("model"),
  settings: jsonb("settings"),
  outputKey: text("output_key"),
  costUsd: real("cost_usd"),
  status: generationStatus("status").default("queued").notNull(),
  approved: boolean("approved").default(false).notNull(),
  createdAt: timestamp("created_at").defaultNow().notNull(),
});

export const schedules = pgTable("schedules", {
  id: uuid("id").defaultRandom().primaryKey(),
  draftId: uuid("draft_id").notNull().references(() => postDrafts.id, { onDelete: "cascade" }),
  scheduledFor: timestamp("scheduled_for").notNull(),
  timezone: text("timezone").default("Asia/Makassar").notNull(), // WITA
});

export const publishedPosts = pgTable("published_posts", {
  id: uuid("id").defaultRandom().primaryKey(),
  draftId: uuid("draft_id").references(() => postDrafts.id),
  platform: text("platform").notNull(),          // instagram | facebook
  platformPostId: text("platform_post_id"),
  publishedAt: timestamp("published_at"),
  format: postFormat("format"),
  pillarId: uuid("pillar_id").references(() => contentPillars.id),
  captionSnapshot: text("caption_snapshot"),
  hashtagsSnapshot: jsonb("hashtags_snapshot"),
  thumbnailKey: text("thumbnail_key"),
  assetIdsSnapshot: jsonb("asset_ids_snapshot"), // for repetition detection
  createdAt: timestamp("created_at").defaultNow().notNull(),
}, (t) => ({ platformIdx: index("published_platform_idx").on(t.platform, t.publishedAt) }));

export const performanceSnapshots = pgTable("performance_snapshots", {
  id: uuid("id").defaultRandom().primaryKey(),
  publishedPostId: uuid("published_post_id").notNull().references(() => publishedPosts.id, { onDelete: "cascade" }),
  capturedAt: timestamp("captured_at").defaultNow().notNull(),
  metrics: jsonb("metrics").notNull(),           // views, reach, likes, comments, saves, shares, watch_time, completion, ...
});

/* ─────────────────── Feedback, jobs, provider log ─────────────────── */

export const feedbackEvents = pgTable("feedback_events", {
  id: uuid("id").defaultRandom().primaryKey(),
  kind: feedbackKind("kind").notNull(),
  draftId: uuid("draft_id").references(() => postDrafts.id, { onDelete: "set null" }),
  before: jsonb("before"),
  after: jsonb("after"),
  createdAt: timestamp("created_at").defaultNow().notNull(),
}, (t) => ({ kindIdx: index("feedback_kind_idx").on(t.kind) }));

export const providerJobs = pgTable("provider_jobs", {
  id: uuid("id").defaultRandom().primaryKey(),
  kind: text("kind").notNull(),                  // ingest | analyse | embed | render | generate | publish | analytics
  status: jobStatus("status").default("queued").notNull(),
  refId: uuid("ref_id"),                          // asset/draft/etc. the job acts on
  attempts: integer("attempts").default(0).notNull(),
  lastError: text("last_error"),
  request: jsonb("request"),
  response: jsonb("response"),
  provider: text("provider"),
  modelVersion: text("model_version"),
  createdAt: timestamp("created_at").defaultNow().notNull(),
  updatedAt: timestamp("updated_at").defaultNow().notNull(),
}, (t) => ({ statusIdx: index("provider_jobs_status_idx").on(t.status, t.kind) }));
