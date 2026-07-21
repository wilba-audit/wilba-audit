# /pipeline — Your Deal Board + Next Best Action

> Where every deal lives. Who's hot, what's stuck, how close you are to $10k, what to do right now.

## Instructions

Manage the WILBA sales pipeline in `outputs/wilba-pipeline.md`.

### On `/pipeline` (no args) — show the board
Read `outputs/wilba-pipeline.md` and give Jess:
1. **The board** — deals grouped by stage: Lead → Outreach sent → Audit sent → Audit done → Call booked → Proposal out → Closed (won/lost).
2. **The cash line** — total closed + committed this month vs the $10k target (a simple progress read).
3. **Today's highest-value actions** — the 3 moves most likely to move money (usually: chase a warm proposal, follow up an audit, book a call). Be specific: name the person + the action.
4. **What's going stale** — anything sitting >4 days with no next step.

### On `/pipeline [update]` — log a change
Parse what Jess says ("Sarah booked a call", "David's proposal is out", "the physio said no") and update the person's stage + next action + date in `outputs/wilba-pipeline.md`. Confirm the change in one line.

### Behaviour
- Always end with the single most important next action.
- Keep the tone of a sharp sales manager who's on Jess's side — encouraging, but honest about what's stalling.
- If the board is empty, prompt: "Let's fill it — run `/outreach` and we'll start putting names in play."

The pipeline is the truth of the business. Keep it honest, keep it current, always point at the next dollar.
