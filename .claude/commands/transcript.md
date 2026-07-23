# /transcript [url] — Pull & Mine a Podcast/Video Transcript

> Turn any episode (Diary of a CEO, Liam Ottley, Hormozi, anyone) into a saved transcript + a WILBA-relevant idea mine.

## Instructions

**Input:** `$ARGUMENTS` — a YouTube URL (best), a podcast/article URL, or a topic/episode name.

### Step 1 — Get the transcript
- **If it's a YouTube URL:** run `python scripts/pull_transcript.py "<url>" [slug]`. It saves the transcript to `reference/transcripts/`. (Needs `youtube-transcript-api` — if it's missing, run `pip install youtube-transcript-api` first.)
- **If it's another URL:** use WebFetch to pull the page/transcript text.
- **If it's just a name/topic:** WebSearch to find the episode + a transcript or detailed summary, then fetch it.
- If a transcript genuinely can't be retrieved, say so plainly and fall back to the best available summary — don't fabricate quotes.

### Step 2 — Save it
Ensure the raw transcript (or best-available notes) is saved to `reference/transcripts/[slug].md` with the source URL at the top.

### Step 3 — Mine it for WILBA
Read the transcript and produce a short brief:
- **Top 5–8 ideas/frameworks** worth remembering (with the memorable lines).
- **What to integrate into WILBA** — map each idea to Jess's business (the hospitality model, offers, leads, retreats, content). Be specific.
- **Content angles** — 3–5 reels/posts this episode could inspire, in Jess's voice.
Save the brief alongside the transcript (e.g. `reference/transcripts/[slug]-brief.md`) and give Jess the highlights in chat.

### Behaviour
- Keep the mining ruthless — only ideas that actually move her business.
- Great sources to keep pulling: Hormozi (offers/leads/money), Liam Ottley (AI agency/AIOS), hospitality + retreat operators.
- This feeds the content engine — a good episode = a week of content angles.
