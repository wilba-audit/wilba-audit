#!/usr/bin/env bash
# Turnkey: log into LinkedIn (you type the password) and scan Gina's posts.
# RUN THIS ON A NORMAL COMPUTER (your Mac) — NOT in the Claude web session,
# which has no network access to LinkedIn.
set -e
cd "$(dirname "$0")"
CAP="../../../.claude/skills/social-session-capture/scripts"

echo "▶ WILBA — LinkedIn post capture for Dr Schoeman"
command -v node >/dev/null 2>&1 || { echo "✗ Install Node.js from https://nodejs.org first."; exit 1; }

# one-time deps (installed alongside the capture script)
if [ ! -d "$CAP/node_modules/playwright" ]; then
  echo "▶ Installing Playwright (one-time)…"
  ( cd "$CAP" && npm init -y >/dev/null 2>&1 && npm i playwright >/dev/null 2>&1 && npx playwright install chromium >/dev/null 2>&1 )
fi

echo ""
echo "STEP 1 of 2 — a browser window will open. Log into LinkedIn yourself"
echo "(password + 2FA). Then come back here and press ENTER."
node "$CAP/capture.mjs" login linkedin

echo ""
echo "STEP 2 of 2 — capturing her recent activity + profile…"
node "$CAP/capture.mjs" capture config.json

echo ""
echo "✅ Done. Screenshots + text are in outputs/schoeman/captures/"
echo "   Commit that folder (or send Jess the files) and tell Claude:"
echo "   'run the post-style teardown on the schoeman captures'."
