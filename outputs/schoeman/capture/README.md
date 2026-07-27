# Scan Gina's LinkedIn posts (login via Playwright)

This is the "log in and scan all the posts" tool, ready to run. It works — it
just can't run inside the Claude web session (that sandbox has **no network
access to LinkedIn**; a browser there fails with `ERR_TUNNEL_CONNECTION_FAILED`).
Run it on a **normal computer** (your Mac).

## One command
```bash
bash outputs/schoeman/capture/run.sh
```
Then:
1. **A browser window opens** → you log into LinkedIn yourself (password + 2FA).
   *The tool never sees or stores the password — you type it.*
2. Press **ENTER** in the terminal → it scans her **recent activity + profile**,
   saving screenshots + text to `outputs/schoeman/captures/`.
3. Send Jess/Claude that folder → I run the full **post-style teardown** (hook,
   tone, captions, CTA — with a rewrite of each).

## Notes
- Uses **Gina's own logged-in session**, human-in-the-loop, at a gentle pace —
  the responsible way that won't put her account at risk.
- Want Instagram too? Edit `config.json`: set `"platform": "instagram"` and add
  her post URLs, then run `node ../../../.claude/skills/social-session-capture/scripts/capture.mjs login instagram` first.
- Easiest alternative, zero setup: just screenshot 8–10 of her posts and paste
  them into Claude.
