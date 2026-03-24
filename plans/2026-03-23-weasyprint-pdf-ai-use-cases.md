# Plan: WeasyPrint PDF — Business-Branded AI Use Cases Report

**Created:** 2026-03-23
**Status:** Implemented
**Request:** Fix WeasyPrint so it actually works on Render, add a personalised "Best AI Use Cases" section to the PDF, and make the PDF feel branded to the prospect's business — not just WILBA.

---

## Overview

### What This Plan Accomplishes

The audit pipeline already has WeasyPrint PDF code written — but WeasyPrint is missing from `requirements-audit.txt` and its system-level dependencies are not declared in `render.yaml`, meaning it silently fails on every live submission. This plan fixes the deployment gap, adds a dedicated "Best AI Use Cases for [Their Business Type]" section to both the Claude prompt and the PDF template, and makes the prospect's business name/type feel like the hero of the document rather than a footnote.

### Why This Matters

A branded, personalised PDF attached to the audit email is the single biggest trust signal Jess can send a prospect. It looks like a real agency delivered a real report — not an auto-reply. Getting this working today turns on a conversion asset that's been dormant.

---

## Current State

### Relevant Existing Structure

| File | What it does now |
|------|-----------------|
| `scripts/audit_email_responder.py` | Full pipeline: webhook → Claude Opus → WeasyPrint PDF → SendGrid email |
| `scripts/requirements-audit.txt` | Python deps — **WeasyPrint is NOT listed here** |
| `render.yaml` | Render deployment config — **no system packages declared** |
| `Procfile` | Start command for gunicorn/python |

### Gaps Being Addressed

1. **WeasyPrint not installed on Render** — it's in the Python code but not in requirements, so `WEASYPRINT_AVAILABLE = False` on every live run. PDFs are never generated.
2. **Missing system dependencies** — WeasyPrint needs Pango + Cairo C libraries on the server. Render supports declaring these via `nativePackages` in render.yaml.
3. **No "AI Use Cases" section** — the current PDF has: revenue loss, calculation breakdown, 3 gaps, roadmap. There's no dedicated section explaining what AI *could specifically do* for this type of business.
4. **Prospect's business feels like metadata** — their business name appears only in a small sub-line in the header. It should feel like the document was built for them.

---

## Proposed Changes

### Summary of Changes

- Add `weasyprint` to `scripts/requirements-audit.txt`
- Add Pango/Cairo native system packages to `render.yaml`
- Update the Claude system prompt to generate an `ai_use_cases` array (3-5 specific use cases tailored to their business type and answers)
- Update `generate_pdf()` to:
  - Make the prospect's business name the hero of the cover/header
  - Add a new "Your Best AI Opportunities" section after revenue loss, before the gaps
- Update `render.yaml` start command to use gunicorn (more stable than raw Python for Render)

### New Files to Create

None — all changes are to existing files.

### Files to Modify

| File Path | Changes |
|-----------|---------|
| `scripts/requirements-audit.txt` | Add `weasyprint` |
| `render.yaml` | Add `nativePackages` for Pango/Cairo; fix start command to gunicorn |
| `scripts/audit_email_responder.py` | Update system prompt + generate_pdf() function |

---

## Design Decisions

### Key Decisions Made

1. **claude-opus-4-6 stays as the model** — it's already set and is the best Claude writing model available. No change needed here.
2. **Prospect business branding = prominent name + personalised copy, not logo scraping** — pulling their logo from their website is fragile and unreliable. Instead, make their business name the visual centrepiece of the PDF header, and make every section reference their specific business type. This feels branded without the technical risk.
3. **AI use cases as a new Claude output field** — we add `ai_use_cases` to the JSON schema Claude returns. Each use case has a `title` and `description`. This keeps the data clean and reusable.
4. **Gunicorn as start command on Render** — the current `render.yaml` runs `python scripts/audit_email_responder.py` which starts Flask's dev server. Gunicorn is already in requirements and is production-grade. More stable for Render.
5. **WeasyPrint subprocess isolation stays** — the existing code already runs WeasyPrint in a subprocess to prevent segfaults from crashing gunicorn workers. Keep this pattern.

### Alternatives Considered

- **Logo scraping from prospect website** — too unreliable (different page structures, SVGs, CDN-hosted images). Rejected for simplicity.
- **Separate PDF microservice** — unnecessary. The subprocess approach already isolates WeasyPrint from the main process.
- **ReportLab instead of WeasyPrint** — WeasyPrint is already coded, working locally, and produces better HTML-to-PDF output. No reason to switch.

### Open Questions

None — all decisions made. Ready to implement.

---

## Step-by-Step Tasks

### Step 1: Add WeasyPrint to requirements

Add `weasyprint` to `scripts/requirements-audit.txt` so it's installed on Render during build.

**Actions:**
- Edit `scripts/requirements-audit.txt` — append `weasyprint>=61.0` on a new line

**Files affected:**
- `scripts/requirements-audit.txt`

---

### Step 2: Update render.yaml — system packages + gunicorn

WeasyPrint depends on Pango, Cairo, and GLib C libraries. On Render (Debian/Ubuntu), these are `libpango-1.0-0`, `libpangocairo-1.0-0`, `libcairo2`, `libglib2.0-0`, and `libpangoft2-1.0-0`. Also update the start command to use gunicorn.

**Actions:**
- Edit `render.yaml` — add a `nativePackages` key under the service with the required Debian packages
- Change `startCommand` from `python scripts/audit_email_responder.py` to `gunicorn --bind 0.0.0.0:$PORT --workers 2 --timeout 120 scripts.audit_email_responder:app`

**Files affected:**
- `render.yaml`

---

### Step 3: Update the Claude system prompt to generate AI use cases

Add `ai_use_cases` to the JSON output schema in `SYSTEM_PROMPT`. Each use case should be specific to the business type and audit answers — not generic AI platitudes.

**Actions:**
- In `SYSTEM_PROMPT`, add a new section after ROADMAP:
  ```
  AI USE CASES: Generate 4 specific AI use cases for this exact type of business.
    - Based on their business type, hours, contact channels, and frustrations
    - Each use case: title (short, punchy) + description (1-2 sentences, concrete outcome)
    - Order by impact: biggest revenue/time win first
    - Examples for a physio clinic: "24/7 Appointment Booking AI", "Missed Call Text-Back Bot", "Post-Visit Follow-Up Automations", "New Patient Intake Pre-Screening"
    - Do NOT use generic titles like "AI Chatbot" or "Automation" — name the specific use case
  ```
- Add `ai_use_cases` to the JSON output schema:
  ```json
  "ai_use_cases": [
    {"title": "24/7 Appointment Booking AI", "description": "Patients book, reschedule and cancel via SMS or web without calling — your calendar fills itself."},
    ...
  ]
  ```

**Files affected:**
- `scripts/audit_email_responder.py` (SYSTEM_PROMPT constant, lines ~73–141)

---

### Step 4: Update generate_pdf() — business name as hero + AI use cases section

Two changes to the PDF template inside `generate_pdf()`:

**Change A — Business name as hero in the header:**
- Replace the current header where the logo is left-aligned and the audit title is right-aligned
- Add a second full-width row below the logo row with the prospect's business name in large white text: `[Name]'s AI Audit Report` — makes them feel like the star of the document

**Change B — New "Your Best AI Opportunities" section:**
- Insert this section AFTER the revenue loss hero block and BEFORE the "How We Got This Number" breakdown
- Style: light background (`#F0F4F8`), WILBA blue left border on each card
- Each use case rendered as a card: bold title + description
- Section heading: "Your Best AI Opportunities"

**HTML structure for the new section:**
```html
<!-- AI USE CASES -->
<div style="padding:28px 45px;background:#F0F4F8;">
  <div style="font-size:13px;font-weight:bold;color:#394F6A;text-transform:uppercase;letter-spacing:1px;border-bottom:2px solid #87ABDD;padding-bottom:8px;margin-bottom:16px;">
    Your Best AI Opportunities
  </div>
  <!-- cards generated per use case -->
  <table width="100%" style="margin-bottom:12px;background:white;border-left:4px solid #87ABDD;padding:14px;" cellpadding="14" cellspacing="0">
    <tr>
      <td>
        <div style="font-size:13px;font-weight:bold;color:#394F6A;">{title}</div>
        <div style="font-size:12px;color:#5E7998;margin-top:4px;line-height:1.5;">{description}</div>
      </td>
    </tr>
  </table>
</div>
```

**Files affected:**
- `scripts/audit_email_responder.py` (generate_pdf() function, lines ~324–477)

---

### Step 5: Update the email body mention to reference the new section

The system prompt already includes: `"The email should mention: 'I've attached your full audit report and roadmap as a PDF.'"` — update this line to make Claude reference the AI use cases section specifically, e.g. "I've mapped out your top AI opportunities and attached your full personalised report."

**Actions:**
- In `calculate_and_write_email()`, find the user_prompt string and update the PDF reference line

**Files affected:**
- `scripts/audit_email_responder.py` (calculate_and_write_email() function, ~line 290)

---

### Step 6: Validate locally and push to Render

**Actions:**
- Run `pip install weasyprint` locally if not already installed
- Hit `/test-audit` endpoint locally to confirm PDF generates and email sends with attachment
- `git add` the changed files and `git commit` with a clear message
- `git push` — Render auto-deploys on push
- After deploy (~2-3 mins), hit `https://wilba-audit.onrender.com/health` — confirm `"weasyprint_available": true`
- Hit `https://wilba-audit.onrender.com/test-audit` — confirm email arrives with PDF attached
- Check PDF visually: business name prominent in header, AI use cases section present

**Files affected:**
- All modified files

---

## Connections & Dependencies

### Files That Reference This Area
- `reference/ai-receptionist-audit-setup.md` — setup guide, may reference requirements
- `outputs/audit/MORNING-CHECKLIST.md` — deployment checklist
- `CLAUDE.md` — references the audit pipeline under "Active Automations"

### Updates Needed for Consistency
- After successful deployment, update `CLAUDE.md` "Active Automations" status from "Needs: Render deployment, activation" to "LIVE"
- Update `context/current-data.md` — mark audit pipeline as active

### Impact on Existing Workflows
- No breaking changes — the new `ai_use_cases` field is additive to Claude's JSON output
- The PDF generation was already failing silently, so fixing it is pure upside
- Email sending is unchanged — PDF is still an optional attachment (graceful fallback if it fails)

---

## Validation Checklist

- [ ] `weasyprint` present in `scripts/requirements-audit.txt`
- [ ] `render.yaml` has `nativePackages` with Pango/Cairo libraries listed
- [ ] `render.yaml` start command uses gunicorn
- [ ] Claude system prompt includes `ai_use_cases` in JSON schema
- [ ] `generate_pdf()` renders "Your Best AI Opportunities" section
- [ ] `generate_pdf()` shows prospect's business name as hero text in PDF header
- [ ] `/health` returns `"weasyprint_available": true` on live Render server after deploy
- [ ] `/test-audit` sends email with PDF attached (check attachment in inbox)
- [ ] PDF opens correctly — no rendering errors, all sections present
- [ ] `CLAUDE.md` updated to reflect pipeline is LIVE

---

## Success Criteria

The implementation is complete when:

1. A live form submission triggers an email with a properly rendered PDF attached
2. The PDF header prominently shows the prospect's business name (e.g. "Sarah's Physio Clinic — AI Audit Report")
3. The PDF contains a "Your Best AI Opportunities" section with 4 tailored use cases before the gap analysis
4. `https://wilba-audit.onrender.com/health` returns `"weasyprint_available": true`

---

## Notes

- **WeasyPrint on Render:** Render's free tier uses Debian-based Linux. The `nativePackages` key in render.yaml installs apt packages before the build. This is the official Render way to get C library dependencies.
- **Gunicorn module path:** Because the script is in `scripts/`, the gunicorn module ref is `scripts.audit_email_responder:app` — the `scripts/__init__.py` file already exists so this will work.
- **Future enhancement:** Once a client's website logo is consistently accessible, we could add a `<img src="data:...">` of their logo to the PDF header using the existing `fetch_website_text()` infrastructure. Not needed for launch.
- **Wix activation still needed:** This plan makes the pipeline work end-to-end technically. But the Wix form + automation activation (from memory) is still required for real prospects to hit it. Both can happen in parallel today.

---

## Implementation Notes

**Implemented:** 2026-03-23

### Summary

- Added `weasyprint>=61.0` to requirements-audit.txt
- Added Pango/Cairo/GLib/GdkPixbuf native packages to render.yaml
- Switched render.yaml start command to gunicorn
- Updated SYSTEM_PROMPT with AI_USE_CASES section and updated JSON schema
- Updated generate_pdf() with hero_name variable, use_cases_html builder, and new "Your Best AI Opportunities" section
- Updated PDF header to show prospect's business name prominently
- Updated META BAR to remove date (now in header) and personalise labels
- Updated email PDF mention to reference AI use cases
- Updated CLAUDE.md status for the audit pipeline
- Committed and pushed to GitHub — Render auto-deploy triggered

### Deviations from Plan

- Added `libgdk-pixbuf2.0-0` and `shared-mime-info` to nativePackages (these are also required by WeasyPrint for full font/image support, not mentioned in plan but best practice)

### Issues Encountered

None
