# Session Capture — copy-paste walkthrough

Runs on a **normal computer** (not the Claude web session — that's network-locked).
Use only on accounts the person present **owns or has explicit permission for.**

## 1. Install (one time)
```bash
cd .claude/skills/social-session-capture/scripts
npm init -y && npm i playwright
npx playwright install chromium
```

## 2. Log in yourself (a window opens — you type the password + 2FA)
```bash
node capture.mjs login linkedin
```
A visible browser opens LinkedIn's login page. **You** log in normally. When
you're in, return to the terminal and press **ENTER** — the session saves to
`.auth/linkedin.json` (local, private, gitignored).

## 3. Make a config of YOUR OWN pages
Create `config.json`:
```json
{
  "slug": "schoeman",
  "platform": "linkedin",
  "outDir": "../../../../outputs/schoeman/captures",
  "consent": "I own or have explicit permission to access these accounts",
  "pages": [
    { "name": "recent-activity", "url": "https://www.linkedin.com/in/dr-gina-schoeman-mb-chb-mba-dip-derm-mrcgp-mbcam-afmcp/recent-activity/all/" },
    { "name": "profile", "url": "https://www.linkedin.com/in/dr-gina-schoeman-mb-chb-mba-dip-derm-mrcgp-mbcam-afmcp/" }
  ]
}
```

## 4. Capture
```bash
node capture.mjs capture config.json
```
Produces full-page **screenshots (.png)** + **text (.txt)** in
`outputs/schoeman/captures/`.

## 5. Hand to Claude
Commit or paste those captures and say: *"run the post-style teardown on these
captures."* Claude grades hook/tone/captions/CTA per post and rewrites each.

---
**Reminder:** this is the owner viewing and saving their *own* data with a human
in the loop. It is not an unattended scraper. If LinkedIn ever shows a
security/checkpoint prompt, stop — that's the platform asking you to slow down.
The safest data of all is still the native **export** (`social-analytics-ingest`).
