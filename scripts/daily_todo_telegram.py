"""
WILBA — Daily To-Do → Telegram

Runs every weekday morning (via GitHub Actions). Reads Jess's 90-day roadmap
and live pipeline, asks Claude to write a short, punchy daily to-do in her
mentor's voice (Hormozi + Ottley), and sends it to her Telegram.

Foolproof by design: if the AI step fails for any reason, it still sends a
solid fallback to-do so a message ALWAYS lands.

Env vars (set as GitHub Actions secrets):
  TELEGRAM_BOT_TOKEN   — from @BotFather
  TELEGRAM_CHAT_ID     — your Telegram chat id (from @userinfobot)
  ANTHROPIC_API_KEY    — for the AI-written to-do (optional; falls back if absent)
  CLAUDE_MODEL         — optional model override (default: Haiku)
"""

import json
import os
import urllib.request
from datetime import datetime, timezone, timedelta
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
MODEL = os.environ.get("CLAUDE_MODEL", "claude-haiku-4-5-20251001")

# Jess is on the Surf Coast (AEST, UTC+10). Show her local date.
AEST = timezone(timedelta(hours=10))


def read(rel_path: str, limit: int = 6000) -> str:
    """Best-effort read of a workspace file; never raises."""
    try:
        return (REPO / rel_path).read_text(encoding="utf-8")[:limit]
    except Exception:
        return ""


def build_todo() -> str:
    """Ask Claude for today's to-do. Falls back to a static message on any failure."""
    today = datetime.now(AEST).strftime("%A, %d %B %Y")
    roadmap = read("outputs/wilba-90-day-roadmap.md")
    pipeline = read("outputs/wilba-pipeline.md")

    fallback = (
        f"☀️ {today}\n\n"
        "Your number: 3 paying hospitality clients.\n\n"
        "Today's 3 moves:\n"
        "1. One revenue action before noon (an outreach message OR a delivery step on Sean).\n"
        "2. Chase the warmest deal in your pipeline.\n"
        "3. Post one piece of content (hospitality angle).\n\n"
        "You don't need to feel motivated. Do the one thing. Motivation follows action. 🤙\n"
        "(Full plan: outputs/wilba-90-day-roadmap.md)"
    )

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return fallback

    prompt = (
        f"Today is {today}. You are Jess's business mentor — think like Alex Hormozi and "
        "Liam Ottley combined: direct, warm, revenue-first, no fluff. Write her DAILY TO-DO "
        "as a short Telegram message (plain text + a few emoji, NO markdown, under 1200 chars).\n\n"
        "Structure:\n"
        "1. One line: the date + her ONE number (3 paying hospitality clients) and a nudge on it.\n"
        "2. 'Today's 3 moves:' — exactly 3 specific, revenue-producing actions for TODAY. "
        "Use real names/steps from the roadmap and pipeline (e.g. Sean, warm outreach, a delivery step). "
        "The first move must be doable before noon.\n"
        "3. One honest line of motivation to close.\n\n"
        "Keep it tight and human. Don't hedge. Don't explain yourself.\n\n"
        f"=== HER 90-DAY ROADMAP ===\n{roadmap}\n\n"
        f"=== HER LIVE PIPELINE ===\n{pipeline}\n"
    )

    try:
        from anthropic import Anthropic

        client = Anthropic(api_key=api_key)
        msg = client.messages.create(
            model=MODEL,
            max_tokens=600,
            messages=[{"role": "user", "content": prompt}],
        )
        text = "".join(getattr(b, "text", "") for b in msg.content).strip()
        return text or fallback
    except Exception as e:  # noqa: BLE001 — must never crash the daily send
        print(f"[warn] AI step failed, using fallback: {e}")
        return fallback


def send_telegram(text: str) -> None:
    token = os.environ["TELEGRAM_BOT_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = json.dumps(
        {"chat_id": chat_id, "text": text, "disable_web_page_preview": True}
    ).encode("utf-8")
    req = urllib.request.Request(
        url, data=payload, headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        body = resp.read().decode("utf-8")
        print(f"[ok] Telegram responded: {body[:200]}")


if __name__ == "__main__":
    todo = build_todo()
    print("----- TODAY'S TO-DO -----")
    print(todo)
    print("-------------------------")
    send_telegram(todo)
