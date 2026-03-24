# Plan: Brand Positioning & Identity — Jess Morrell / WILBA

**Created:** 2026-03-23
**Status:** Implemented
**Request:** Design a powerful social media brand identity for the AI receptionist niche — defining what the brand represents, the unique positioning angle, brand voice and tone, visual aesthetic guidelines, and the core message that resonates with the target audience.

---

## Overview

### What This Plan Accomplishes

This plan produces `outputs/brand/brand-positioning.md` — a complete brand identity and positioning document for Jess Morrell as the face of WILBA. It covers brand essence, competitive differentiation, voice and tone guidelines, visual aesthetic specifications, and the core message architecture. This document becomes the single creative source of truth: everything from captions to thumbnails to spoken word in a reel gets checked against it.

### Why This Matters

The social media intelligence document (already created) tells Jess WHO to talk to and WHAT they care about. This document tells her HOW to show up — the personality, the look, the feel, and the positioning logic that makes the brand instantly recognisable and impossible to copy. Without this, content is inconsistent: sometimes too corporate, sometimes too casual, sometimes too techy. With it, every piece of content reinforces the same brand identity and compounds over time into authority.

---

## Current State

### Relevant Existing Structure

| File | Relevance |
|------|-----------|
| `outputs/brand/social-media-intelligence.md` | Audience intelligence — the WHO and WHAT; this plan builds the HOW |
| `context/personal-info.md` | Jess's personality: "Matthew McConaughey meets The Dirt Company" — the seed of the brand voice |
| `context/business-info.md` | Brand personality: "Modern, clever, witty, down-to-earth. Confident, cheeky, not corporate." |
| `outputs/brand/` | Brand assets directory — this document lives alongside social-media-intelligence.md |

### Gaps Being Addressed

- No documented brand positioning statement or brand promise
- No defined competitive differentiation beyond the personality sketch in context files
- No written voice and tone guide (how sentences are structured, what words to use, what to avoid)
- No visual aesthetic guidelines (colours, typography style, composition, mood, what to never do)
- No core message framework — the sentences that, when said in different ways, form the backbone of all content
- Content currently risks being inconsistent because there's no creative source of truth to check against

---

## Proposed Changes

### Summary of Changes

- Create `outputs/brand/brand-positioning.md` — the complete brand identity document
- No modifications to existing files

### New Files to Create

| File Path | Purpose |
|-----------|---------|
| `outputs/brand/brand-positioning.md` | Complete brand positioning and identity guide for Jess Morrell / WILBA |

### Files to Modify

None.

---

## Design Decisions

### Key Decisions Made

1. **Jess Morrell is the brand, WILBA is the agency** — The personal brand (Jess) is the social media identity. WILBA is what they hire. This distinction matters: content strategy builds Jess's authority, which generates trust, which converts to WILBA clients. The brand positioning document is written for Jess's personal brand, not for a corporate WILBA identity.

2. **Positioning against the category default, not individual competitors** — There are no dominant personal brand competitors to name yet in the Australian AI receptionist space. The positioning is primarily "not that" (corporate, techy, generic SaaS) rather than "better than X." This is actually stronger — it positions Jess as the category alternative, not just a competitor.

3. **Visual guidelines are principles + examples, not exact specs** — Jess doesn't have a graphic designer. Visual guidelines need to be usable by someone filming on a Sony ZV-E1 and editing in Canva or CapCut. They should be specific enough to ensure consistency without requiring professional design execution.

4. **Voice guide includes "say this, not that" examples** — Abstract adjectives ("warm," "direct") are useless without concrete examples. The voice guide will include real before/after sentence pairs so Jess (or a VA or Claude) can immediately apply the guide when writing captions or scripts.

5. **Core message architecture structured as a pyramid** — Brand purpose at the top, positioning statement in the middle, tagline options at the bottom. This way the document is both strategic (for Jess to understand the brand) and tactical (for pulling phrases to use in content).

### Alternatives Considered

- **Separate documents for voice, visual, and positioning** — rejected; the power of this document is having everything in one place. When writing a caption, you open one file.
- **Hiring brand strategist before doing this** — rejected; the information needed to build this positioning exists in Jess's context files and the intelligence doc already created. A strategist would charge $5K–$15K for something Claude can produce with equivalent quality given the depth of context.

### Open Questions

None — ready to implement.

---

## Step-by-Step Tasks

### Step 1: Write the complete brand positioning document

Write `outputs/brand/brand-positioning.md` in full. No stubs. Every section below must be completely written.

---

#### SECTION 1: Brand Essence

**What the brand stands for at its core — one paragraph maximum.**

The distilled answer to: "What does Jess Morrell stand for?" This is not a tagline. It's the philosophical foundation. Everything else in the document flows from here.

Cover:
- The core belief that drives the brand (the world view)
- The change Jess is trying to create in the world of service business ownership
- The emotional territory the brand occupies

---

#### SECTION 2: The Positioning Statement

The formal positioning architecture. Write a complete positioning statement in this structure:

> For [target audience], Jess Morrell is the [category] who [key differentiator], unlike [the alternative], because [reason to believe].

Then unpack it — explain each element and why it was chosen. This becomes the strategic logic Jess can use when explaining her brand to anyone: a potential client, a podcast host, a collaborator.

---

#### SECTION 3: Competitive Landscape & Differentiation

**Who else is in this space and why Jess is different.**

Map the competitive landscape into 3 categories:
1. **Software companies and SaaS brands** (GoHighLevel, Dialpad, Smith.ai, etc.) — what they do in content and where they fail
2. **Tech bros and AI influencers** — the dominant personality in the AI content space right now and why it alienates Jess's audience
3. **Generic "business growth" coaches** — who talk about AI but don't actually deliver it

For each: what they do, what's missing, and where Jess steps in.

Then write **Jess's 5 unfair advantages** — specific, non-copyable differentiators. Not just "she's authentic" (everyone says that). Real structural advantages that would be very hard for a competitor to replicate.

---

#### SECTION 4: Brand Voice & Tone Guide

The most important section for content creation. Must be immediately usable.

**4a. The Voice in 5 Words**
Five words that define how the brand sounds. Not adjectives like "professional" — words that evoke a feeling or character.

**4b. The Voice Reference Points**
3–4 cultural references that capture the brand voice. These could be people, shows, brands, books — anything that immediately conjures the feeling. Brief explanation of what each contributes.
Examples of the format (not the actual content — that gets written in implementation):
- "The Dirt Company — premium product explained without any wank"
- "Matthew McConaughey — confident, unhurried, self-aware"

**4c. Voice Dimensions**

Write each dimension as a spectrum with Jess's position marked:

- Formal ←——[X]——→ Casual
- Corporate ←—————[X]→ Personal
- Technical ←———————[X]→ Plain English
- Reserved ←——[X]——→ Opinionated
- Polished ←——[X]——→ Raw

For each dimension: explain where Jess sits and what that sounds like in practice.

**4d. The Writing Rules (12 rules minimum)**

Specific, actionable rules for writing in Jess's voice. Each rule has:
- The rule itself
- Why it matters for this brand
- A "say this / not that" example pair

Examples of rule types to cover:
- Sentence length and structure
- How to open a caption or script
- How to handle technical terms
- How to express opinion without alienating
- How to use humour
- What to never say (the banned phrases list)
- How to write a CTA that sounds like Jess

**4e. Tone Variations by Context**

Tone shifts slightly depending on the context. Document the tone for:
- Educational content (explaining how AI works)
- Revenue/ROI content (the numbers and the money)
- Personal/lifestyle content (Jess's world)
- Client results/social proof content
- Direct sales content (audit CTA)

**4f. The Banned Phrases List**

Specific words and phrases that must never appear in Jess's content — because they're too corporate, too generic, too "AI bro," or too clichéd. At least 20 entries.

---

#### SECTION 5: Visual Aesthetic Guidelines

Written for someone using Sony ZV-E1 + Canva + CapCut — not a graphic designer.

**5a. The Aesthetic in 3 Words**
The visual feeling in three words. These words should make creative decisions obvious: "does this image feel like those 3 words? If not, don't use it."

**5b. The Mood Board Description**
Write a detailed description of the visual world. No actual images — just words that paint the picture so clearly that Jess could brief a designer, a photographer, or a creative VA from this description alone.

Cover:
- Environment / setting (where content is filmed and photographed)
- Lighting quality and mood
- Colour temperature
- Colour palette (primary, secondary, accent — with hex codes where possible)
- What the background looks like
- What "messiness" vs "cleanliness" means for this brand

**5c. On-Camera Presence**
Guidelines specifically for talking-head video content:
- Wardrobe direction (specific categories, colours, what to avoid)
- Hair and presentation
- Background and environment choices
- Eye line and framing
- Energy/presence on camera — what to aim for, what to avoid

**5d. Text and Typography Style**
For Canva carousels, thumbnail text, caption formatting:
- Font personality (not specific fonts unless Canva-available — describe the style: serif vs sans-serif, weight, feel)
- How to use text on video (reels text overlay style)
- Caption formatting conventions (line breaks, caps, punctuation style)
- What to never do with text

**5e. The Brand Colours**
Define primary, secondary, and accent colours. Hex codes where possible. For each colour: when to use it and what it communicates.

**5f. Photography/Video Direction**
Guidelines for b-roll, lifestyle shots, and location content:
- Types of shots that work for this brand
- Types of shots that don't
- The Surf Coast as a visual asset — how to use it without it becoming a cliché
- What makes a thumbnail feel like Jess's brand

**5g. The Anti-Guidelines (What to Never Do Visually)**
Specific visual choices that would break the brand identity. At least 10 specific don'ts.

---

#### SECTION 6: Core Message Architecture

The pyramidal message structure — strategic at the top, executional at the bottom.

**6a. The Brand Purpose (Why)**
One sentence. The deepest level of brand meaning — the "why we exist" that transcends product or category. Not about AI. About what Jess believes about business owners and their time.

**6b. The Brand Promise (What)**
One to two sentences. What Jess's audience can count on from her content and from WILBA as an agency. The implicit contract.

**6c. The Positioning Statement (How)**
Already written in Section 2. Reference here.

**6d. The Elevator Pitch (30 seconds)**
How Jess would describe what she does at a dinner party. Not a pitch. A conversation. Written in her exact voice.

**6e. The Bio Template**
The Instagram bio formula. And a longer LinkedIn/YouTube About Me template. Both written and ready to paste.

**6f. The Tagline Options**
3–5 tagline options for WILBA / Jess Morrell's brand. Each with a brief rationale — what makes it work, what audience it speaks to, what emotion it triggers. Jess picks one.

**6g. The Core Message Pillars**
5 core messages that get repeated across all content in many different forms. These are the sentences that, when someone has followed Jess for 6 months, they could finish for her. Written as the definitive version of each message — the clearest, most powerful form of the idea.

---

#### SECTION 7: Brand in Action — Applied Examples

Take the positioning and voice guide and show what it looks like in practice. Write real examples:

1. **Two caption rewrites** — take a generic AI receptionist caption and rewrite it in Jess's voice (before/after)
2. **One reel hook** — written in Jess's voice for each content pillar (4 hooks total)
3. **One DM response** — how Jess would respond to a cold DM enquiry about WILBA services, in brand voice
4. **One email opener** — the first paragraph of an outreach or follow-up email in brand voice
5. **Bio, written and ready** — the final Instagram bio, completely written and ready to paste

---

**Actions:**
- Create `outputs/brand/brand-positioning.md`
- Write every section above in full — no placeholders, no stubs
- Write with the confidence and specificity of a senior brand strategist who deeply understands Jess's context
- Tone of the document itself: professional brief, not casual; Jess can read it and immediately feel proud to have it as her brand foundation

**Files affected:**
- `outputs/brand/brand-positioning.md` (new)

---

### Step 2: Validate completeness and brand coherence

After writing, check that:
- The positioning document is internally coherent — voice, visual, and message all feel like the same brand
- The voice guide is specific enough to use without further guidance
- The visual guidelines can be executed by Jess alone with her existing equipment
- The tagline options are genuinely good — not generic, not clichéd
- The "applied examples" section shows, not just tells, what the brand sounds like

**Files affected:**
- `outputs/brand/brand-positioning.md`

---

### Step 3: Cross-reference with social media intelligence

Confirm the brand positioning is consistent with and builds directly on `outputs/brand/social-media-intelligence.md`:
- The brand voice resonates with the 4 audience segments profiled
- The visual aesthetic fits the content pillars (Revenue Leak, Behind the AI, Social Proof, Jess's World)
- The core messages speak to the universal emotional triggers identified in the intelligence doc

Note any tensions or inconsistencies and resolve them.

**Files affected:**
- `outputs/brand/brand-positioning.md` (final adjustments if needed)

---

## Connections & Dependencies

### Files That Reference This Area

- `outputs/brand/social-media-intelligence.md` — audience intelligence doc; this brand doc is its creative counterpart
- `context/personal-info.md` — source material for brand voice
- `context/business-info.md` — source material for brand personality
- All future content creation — captions, scripts, thumbnails checked against this document

### Updates Needed for Consistency

- Once complete, add a line to `context/business-info.md` pointing to this document: "Brand positioning and voice guide: see `outputs/brand/brand-positioning.md`"
- The two brand documents (`social-media-intelligence.md` and `brand-positioning.md`) should cross-reference each other

### Impact on Existing Workflows

- Every content creation session should start with this document open alongside the intelligence doc
- Claude's future content writing tasks for Jess should reference this document for voice consistency
- This document supersedes the casual brand notes in `context/business-info.md` — that file's personality description can now point here

---

## Validation Checklist

- [ ] `outputs/brand/brand-positioning.md` exists and is fully written
- [ ] Section 1 (Brand Essence) is one paragraph, not a list — deep and specific
- [ ] Section 2 (Positioning Statement) is in the formal positioning architecture and explained
- [ ] Section 3 (Competitive Differentiation) covers all 3 competitor categories + 5 unfair advantages
- [ ] Section 4 (Voice Guide) includes 12+ writing rules each with say-this/not-that examples
- [ ] Section 4 includes the Banned Phrases List with 20+ entries
- [ ] Section 5 (Visual Guidelines) includes hex codes for brand colours
- [ ] Section 5 is usable by Jess filming solo with a Sony ZV-E1 and Canva
- [ ] Section 6 (Message Architecture) includes 3–5 tagline options with rationales
- [ ] Section 7 (Applied Examples) has all 5 applied examples written
- [ ] Instagram bio is written and ready to paste
- [ ] The document is internally coherent — voice, visual, message feel like one brand
- [ ] `context/business-info.md` updated to reference the new document

---

## Success Criteria

The implementation is complete when:

1. Jess can open `outputs/brand/brand-positioning.md`, read it in 20 minutes, and immediately know how to write her next caption, how to frame her next reel, and how to describe what she does to a stranger
2. The document is specific enough that a VA or Claude can write content in Jess's voice without her needing to correct it every time
3. The tagline options are genuinely good — Jess reads them and feels at least one is hers

---

## Notes

- **This document and the social-media-intelligence.md are a pair** — intelligence tells you who and what; positioning tells you how. Together they're a complete brand strategy foundation.
- **The visual guidelines are particularly important right now** — Jess has good equipment (Sony ZV-E1, DJI Mini 4 Pro) but no visual brand guide yet. Getting this right early means all content from Day 1 looks consistent rather than needing a rebrand later.
- **The tagline section deserves genuine creative effort** — a great tagline for this brand is possible and worth the effort. "Your business, always on." is the lazy version. The real one should be smarter, more specific, and more Jess.
- **Future documents to add to `outputs/brand/`:** Content brief template, client proposal template, email signature, media kit. This positioning document is the foundation all of those will build on.
- **The Surf Coast identity is an asset, not a liability** — the visual and voice guidelines should actively lean into this rather than neutralise it into a generic "professional" aesthetic. The juxtaposition of coast-life aesthetic + serious business outcomes is the brand's visual signature.
