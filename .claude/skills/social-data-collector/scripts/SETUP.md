# Collector — copy-paste setup (for a non-technical run)

Goal: turn Dr Schoeman's handles into a real data file Claude can audit. Takes
~5 minutes on any normal computer (your Mac, or send these steps to the dev).

> ⚠️ This will NOT work inside the locked-down Claude web session — that
> environment blocks access to Instagram/LinkedIn/etc. Run it on a normal
> machine, or in a WILBA environment set to open networking.

## 1. Get the code onto the machine
The script lives in the repo at:
`.claude/skills/social-data-collector/scripts/collect_social.mjs`

## 2. One-time install (Terminal)
```bash
# needs Node 18+  (check with: node --version)
cd .claude/skills/social-data-collector/scripts
npm init -y
npm i playwright
npx playwright install chromium   # downloads the browser (skip if one is preinstalled)
```

## 3. Make a config file
Create `config.json` next to the script:
```json
{
  "slug": "schoeman",
  "outDir": "../../../../outputs/schoeman",
  "accounts": {
    "instagram": "drginaschoeman",
    "youtube":   "PASTE HER YOUTUBE CHANNEL URL OR @handle",
    "tiktok":    "PASTE HER TIKTOK @handle (or delete this line)",
    "linkedin":  "https://www.linkedin.com/in/dr-gina-schoeman-022a07b/",
    "x":         "ginaschoeman"
  }
}
```
Delete any line for a platform she isn't on.

## 4. Run it
```bash
node collect_social.mjs config.json
```
On Node 22.21+ behind a proxy, prefix with `NODE_USE_ENV_PROXY=1`.

## 5. Send the result to Claude
It writes `outputs/schoeman/collected-data.md`. Paste that (or commit it) and
say: *"run the social-media-audit on this collected data."* Claude produces the
grounded audit + LinkedIn review.

## If a platform shows blank
Instagram/TikTok sometimes hide counts from logged-out visitors. That's normal —
the file will say so. The most reliable real numbers come from **YouTube**
(public view counts) and from **her own analytics screenshots** (the surest
source of all — see `outputs/schoeman/00-data-request.md`).
