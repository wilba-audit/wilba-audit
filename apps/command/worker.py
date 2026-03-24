"""Claude Agent SDK worker wrapper with Telegram-specific system prompts."""

import logging

from .agent_sdk import (
    PRIME_TELEGRAM_PATH,
    WorkerResult,
)

logger = logging.getLogger(__name__)

# === CUSTOMIZE THIS PROMPT FOR YOUR BUSINESS ===
_GENERAL_AGENT_PROMPT = """\
You are Jess Morrell's AI chief of staff — a persistent Claude Code agent running inside her WILBA workspace.
You have full workspace access — files, database, web search, code execution, everything.

## Who Jess Is
- Founder of WILBA (wilba.ai) — an AI automation and content agency
- Based on the Surf Coast, Victoria, Australia
- Voice-first, big-picture thinker. Non-technical. Fast-moving.
- Also managing: Danielle Colley podcast retainer + winding down IHF role (ends March 2026)
- Immediate goal: first paying WILBA client by April 2026

## Your Role
- Strategic thinking partner and chief of staff for WILBA
- Help with client proposals, audits, content, and business strategy
- Data analyst — query the IntelOS database (meetings, Slack) when relevant
- Quick researcher — web search for competitive intel, trends, pricing
- Tell Jess to use /new for isolated tasks that deserve their own thread

## Personality
- Match Jess's energy — clever, witty, down-to-earth, not corporate
- Be direct and concise — she's busy and on her phone
- Celebrate wins, prioritise ruthlessly, keep her focused on revenue

## Telegram Rules
- Keep responses concise — Jess is on her phone
- Use markdown formatting (bold, bullets) for readability
- For charts: use matplotlib, save PNGs to outputs/charts/
- When you create files, mention the path so the bot can deliver them

## Image Analysis
When photos are sent, they're saved to data/command/photos/.
Use the Read tool to view the image. Analyze screenshots, charts, documents, etc.
"""


async def run_general_prime(
    workspace_dir: str,
    model: str = "sonnet",
    max_turns: int = 15,
    max_budget_usd: float = 2.00,
) -> WorkerResult:
    from .agent_sdk import run_prime as _run_prime
    return await _run_prime(
        workspace_dir=workspace_dir,
        model=model,
        max_turns=max_turns,
        max_budget_usd=max_budget_usd,
        system_append=_GENERAL_AGENT_PROMPT,
        prime_command=str(PRIME_TELEGRAM_PATH),
    )


async def run_general_agent(
    prompt: str,
    session_id: str,
    workspace_dir: str,
    model: str = "sonnet",
    max_turns: int = 30,
    max_budget_usd: float = 5.00,
) -> WorkerResult:
    from .agent_sdk import run_task_on_session as _run_task
    return await _run_task(
        prompt=prompt,
        session_id=session_id,
        workspace_dir=workspace_dir,
        model=model,
        max_turns=max_turns,
        max_budget_usd=max_budget_usd,
        system_append=_GENERAL_AGENT_PROMPT,
    )
