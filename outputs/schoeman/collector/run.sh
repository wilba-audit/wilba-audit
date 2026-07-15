#!/usr/bin/env bash
# One-command collector runner for Dr Gina Schoeman.
# Run this on a NORMAL computer (Mac/Windows-WSL/Linux) with internet.
# It will NOT work inside the locked-down Claude web session.
set -e

cd "$(dirname "$0")"
echo "▶ WILBA social data collector — Dr Gina Schoeman"

# 1. Check Node
if ! command -v node >/dev/null 2>&1; then
  echo "✗ Node.js not found. Install it from https://nodejs.org (LTS), then re-run."
  exit 1
fi
echo "✓ Node $(node --version)"

# 2. Install Playwright + browser (only the first time; safe to re-run)
if [ ! -d node_modules/playwright ]; then
  echo "▶ Installing Playwright (one-time)…"
  npm init -y >/dev/null 2>&1
  npm i playwright >/dev/null 2>&1
fi
echo "▶ Ensuring Chromium is present…"
npx playwright install chromium >/dev/null 2>&1 || true

# 3. Run the collector
SCRIPT="../../../.claude/skills/social-data-collector/scripts/collect_social.mjs"
echo "▶ Collecting… (writes outputs/schoeman/collected-data.md)"
node "$SCRIPT" config.json

echo ""
echo "✅ Done. Give Claude the file:  outputs/schoeman/collected-data.md"
echo "   and say: 'run the social-media-audit on this collected data'."
