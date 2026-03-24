#!/bin/bash
# Start the AI Command Bot (Telegram)
# Run from anywhere — this script handles the paths.

WORKSPACE="$(cd "$(dirname "$0")/.." && pwd)"

echo "Starting AI Command Bot..."
echo "Workspace: $WORKSPACE"
echo ""

# Unset Claude Code session vars so the agent SDK can spawn subprocesses.
# These vars block nested Claude Code launches — must be cleared at shell level.
unset CLAUDECODE
unset CLAUDE_CODE_SESSION_ID
unset CLAUDE_CODE_ENTRYPOINT

cd "$WORKSPACE"
.venv/bin/python -m apps.command.main
