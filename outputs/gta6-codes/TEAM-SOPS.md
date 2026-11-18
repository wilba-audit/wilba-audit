# AI Team SOPs (one page per role)

**Universal rules for every agent:**
1. Never invent codes, sources, quotes, dates or numbers. If you can't find it, say "not found".
2. Every factual line cites a ledger id or a URL with the date it was checked.
3. Agents may *propose* a status. Only the Editor-in-Chief sets **Confirmed**, **Expired** or **Unavailable**.
4. Nothing goes public, nothing is bought, and nothing is sent to an outside audience without human approval.
5. Rockstar or Take-Two marks are used descriptively only. No official art, no leaks, no isolated cutscenes.

---

## Editorial Planner (agent)
**When:** Monday, and whenever the Analyst flags an opportunity.
1. Read the last scorecard, the open claims (Unverified rows) and the content map.
2. Propose 1 episode and 1–3 site updates for the week. For each: the demand evidence (an actual source such as a GSC query, a comment thread or an autocomplete screenshot), the claims to test, and the effort.
3. Output `briefs/YYYY-MM-DD-weekly-plan.md` and post a summary to Slack for Jess to approve.

## Fact Desk (agent): skill `gta6-code-verifier`
**When:** daily intake; on demand for a script fact pass.
1. Intake claims into the ledger as Unverified, with the source and date seen.
2. Look for an official source first (Rockstar Newswire or Support, PlayStation, Xbox, Rockstar Store).
3. Produce the Tester's test list: input, expected effect, how to record it.
4. After testing, propose a status with the evidence attached. Jess decides.
5. Fact pass on scripts and clips: every claim matches the ledger's current status.

## Tester / Host (human)
1. Record the console, game version and date at the start of every session.
2. For each claim: show the source, enter the input, show the result, and say the verdict out loud.
3. Upload to Drive `/raw-episodes/EPn/` and fill the evidence column (file name and timestamp).

## SEO Lead (agent): skill `gta6-seo-brief`
1. For each page: target query cluster, intent, outline, ledger rows used, internal links, title and meta, and schema.
2. Thin or duplicate check: if fewer than 3 unique tested facts, recommend an anchor section instead of a new page.
3. Weekly: list pages whose "last checked" date is behind the ledger.

## Script Writer (agent): skill `gta6-longform-script`
1. Build the beat sheet from the brief. The cold open must be non-violent.
2. Write the VO script and tag every factual line `[LEDGER:id]` or `[VERIFY]`.
3. Produce 3 titles, 2 thumbnail concepts and chapter markers. Honest framing only.

## Clip Producer (agent): skill `gta6-clip-repurposer`
1. From the transcript and timestamps, choose 3–5 self-contained moments with one claim each.
2. For each clip: in/out times, the verdict-first hook, on-screen text, captions, and per-platform title and caption with CTA.
3. Flag any clip whose first 7 seconds include graphic violence.

## Publishing Ops (agent): skill `gta6-publish-gate`
1. Run the gate checklist on every asset: accuracy, disclosure, IP, platform policy, accessibility and links.
2. Output PASS or FAIL with fixes. Prepare drafts and schedules only. Jess makes them public.

## Analyst (agent): skill `gta6-analytics-review`
1. Monday: compile the KPI dashboard from source exports (and write "n/a" where data is missing).
2. Give 3 recommendations: double down, fix, experiment. Each is tied to a number and its source.

## Automation Engineer (human dev and Claude Code)
1. Build automations in the order A2 → A3 → A7 → A4 → A6 → A1 → A5 (OPERATING-PLAN §6).
2. Every automation posts failures to Slack and has a manual fallback documented in its README.
3. Credentials go in GitHub Secrets only.
