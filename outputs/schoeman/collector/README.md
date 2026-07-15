# Run this to get Dr Schoeman's real numbers

You picked **run the collector** — here's the whole thing. It takes ~5 minutes on
a normal computer (your Mac, or hand it to the developer). It pulls her real
public data so Claude can audit the actual account, not a guess.

> ⚠️ Don't run it in the Claude web chat — that environment is locked down and
> can't reach Instagram/YouTube. Run it on a normal computer.

## The 3 steps

**1. Add her YouTube / TikTok (if she has them).**
Open `config.json`. Instagram and LinkedIn are already filled in. If Gina has a
**YouTube channel** or **TikTok**, paste them into the `accounts` block, e.g.:
```json
"accounts": {
  "instagram": "drginaschoeman",
  "linkedin": "https://www.linkedin.com/in/dr-gina-schoeman-022a07b/",
  "youtube": "https://www.youtube.com/@herhandle",
  "tiktok": "herhandle"
}
```
(YouTube gives us the best real data — actual public view counts. Worth finding.)
No YouTube/TikTok? Just leave it as-is; it'll still collect Instagram + LinkedIn.

**2. Run it.**
On Mac/Linux, in Terminal:
```bash
bash outputs/schoeman/collector/run.sh
```
On Windows: use WSL, or ask the dev — same command.

**3. Send the result back to Claude.**
It creates `outputs/schoeman/collected-data.md`. Commit it (or paste its contents
into Claude) and say: **"run the social-media-audit on this collected data."**
Claude turns it into the full grounded audit + LinkedIn review, and refreshes the
proposal with her real figures.

## What you'll get
Her real follower/subscriber counts, recent posts, and — for YouTube — the actual
view count on each recent video (the single most honest signal of what's landing).
Anything a platform hides from logged-out visitors is marked clearly, never faked.

## Most reliable of all
If it's easy to also get **screenshots of her own analytics** (last 90 days, from
each app), send those too — they're the surest source. See
`../00-data-request.md`.
