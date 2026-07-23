# Baha Baha — The AIOS Build Plan
## Sean's full AI Operating System, in plain English. Ship it, prove it, resell it.

**Built:** 2026-07-22
**Based on:** the discovery call (`fireflies-summary.md`, `discovery-notes.md`), proposal, and system design.
**Goal:** automate as much of Sean's operation as possible → this becomes WILBA's **Hospitality AIOS** template that lands the next 5 clients.

---

## The vision — 5 systems, one operating system

```
                        SEAN'S AIOS
   ┌──────────────┬──────────────┬───────────────┬──────────────┐
   ▼              ▼              ▼               ▼              ▼
1. DAILY       2. WHATSAPP    3. EMAIL        4. SOCIAL      5. DIRECT-BOOK
   OPS BRIEF      GUEST AGENT    RECEPTIONIST    AUTO-POSTER    + REBOOKING
   (mornings)     (24/7 chat)    (24/7 inbox)    (content)      (repeat guests)
```

We don't build all five at once. We ship the fastest win first, then stack.

---

## System 1 — The Daily Ops Brief  ⭐ ship this FIRST
**What it does:** every morning at 6am, one email lands in the team's inbox — who's checking in, checking out, transfers, who's in-house, next 48 hours, and any flags. No more checking five systems.
**How it works:** a script pulls bookings from Booking Layer each morning → Claude writes it up in plain English → emailed to the team. Runs unattended.
**What it needs:** the **Booking Layer API key** (that's the one unlock). Scripts are already built.
**Why first:** it's the fastest, cleanest win — needs only the API key, live in ~2 weeks, and Sean *feels* it working every single morning. That's your deposit + your first proof.

## System 2 — The WhatsApp Guest Agent  (already in testing)
**What it does — in plain English:** guests message the villa's WhatsApp (the way most of them already do). An AI reads the message, works out the language, and answers — "yes those dates are free," "here's the surf package," "yes we'll pick you up from the airport." Simple stuff it answers instantly, 24/7. Anything tricky, it drafts a reply and pings Sean to approve. **Nothing sits unanswered overnight and goes cold.**
**How it actually works (the part you get confused on):**
- The villa needs a **WhatsApp Business number** connected to an API (your developer sets this up via a provider — Meta's WhatsApp Business Platform / Twilio / 360dialog). That connection is what lets an AI read and send WhatsApp messages.
- Your agent (the one in testing) is the "brain" — we feed it Baha Baha's real info (rooms, packages, transfers, FAQs) and connect it to the booking data so it answers accurately.
- Modes: **auto-reply** for simple FAQs, **draft-for-approval** for bookings/money.
**What it needs:** finish testing → load Baha Baha's real room/package/FAQ info → connect the WhatsApp Business number → go live.

## System 3 — The Multi-Language Email Responder
**What it does:** same idea as the WhatsApp agent, but for the email inbox. Detects language, drafts a reply in that language, Sean approves (or auto-sends simple FAQs).
**How it works:** watches the Gmail bookings inbox every 15 min → Claude drafts the reply. Scripts already built; needs a 5-min Gmail connection.
**What it needs:** Gmail access (one quick call with Sean).

## System 4 — The Social Auto-Poster (this is where Higgsfield fits)
**The confusion cleared up — two different jobs:**
- **Higgsfield = the STUDIO.** It *makes* the content — reels, images, video of the property. It does NOT post.
- **The social bot = the PUBLISHER.** It *posts* content on a schedule and pulls from Sean's Drive folders. It does NOT create.
**How they link:** Higgsfield (or Sean's existing photos/videos) → saved into a Drive folder → the social bot posts them on schedule, with Sean approving each one over WhatsApp. So: **Higgsfield feeds the folder, the bot posts the folder.** Two tools, one pipeline.
**What it needs:** Sean's Drive folders cleaned up (flagged as a blocker in the call — do this before switching the poster on).

## System 5 — Direct-Booking Capture + Rebooking  (the Booking.com play — read carefully)
See the honest note below. This is how we legitimately turn OTA guests into repeat direct guests.

---

## ⚠️ The Booking.com question — the honest expert answer

Your instinct is right that the money is in those 80% Booking.com guests. But **you cannot export Booking.com's guest details and WhatsApp-market them.** Booking.com's partner terms forbid using guest data for off-platform marketing or soliciting direct bookings, and they often mask guest contact info for exactly this reason. Do it and Sean risks **losing his Booking.com listing** — which is 80% of his bookings. That's a catastrophe we do not cause a client.

**The compliant play that gets you the same outcome (and it's actually better):** you can't take them off-platform, but you can **win them on-property and invite them to come back direct.**
- A **QR code / card in each villa**: "Book direct next time — scan to join our WhatsApp + get 10% off." The guest opts in *themselves*. Now they're yours, 100% legitimately.
- **At checkout**, the team (or the WhatsApp agent) invites them to book direct next time and follow the socials.
- Guests who opt in go into a **rebooking nurture** (WhatsApp/email): "come back for next season," review requests, offers.

Result: you convert Booking.com's one-time guests into WILBA-owned repeat guests — the right way, no listing risk. **This is a whole extra system we can sell Sean** (and every property after him).

---

## The build order (phases)

| Phase | Ship | Needs | Timeline |
|---|---|---|---|
| **1a** | Daily Ops Brief | Booking Layer API key | ~2 weeks |
| **1b** | WhatsApp Guest Agent (finish + go live) | WA Business number + Baha info | parallel |
| **2** | Email Responder | Gmail access | +1-2 weeks |
| **3** | Social Auto-Poster (Higgsfield→Drive→post) | Drive cleanup | when Drive's ready |
| **4** | Direct-booking capture + rebooking nurture | QR/opt-in setup | after core is live |

---

## What we need from Sean (the inputs)
1. **Booking Layer API key** ← the #1 unlock (steps below)
2. Re-add Jess (jessmorrell@gmail.com) + developer as **Manager** in Booking Layer
3. Gmail access to the bookings inbox (5-min call)
4. Exact **room + package names** as they appear in Booking Layer
5. Daily brief **recipients + send time** (WITA)
6. WhatsApp Business number for the agent
7. A sample World Surfaris booking email
8. (Later) a tidy Drive content folder for the social poster

---

## 🔑 How to get the Booking Layer API key — step by step (for Sean)
1. Log in to **Booking Layer** (the owner/admin account).
2. First, make sure Jess + the developer are added as **users with Manager role** (Settings → Users / Team). *(This was an action item from the call — may already be done.)*
3. Go to **Settings → Integrations / API** (sometimes under "Developer" or "API Access").
4. Click **Generate API Key** (or "Create token").
5. Copy the key and send it to Jess **securely** (not in a public chat — email or a password manager).
6. If there's no API option showing, Booking Layer support (or Mashi) can enable **API access** on the account — a one-line request to their support.

That single key turns on the Daily Brief. Everything else stacks on top.

---

## The skills/processes we build (→ your reusable Hospitality AIOS)
Every system above becomes a **reusable skill** in your AIOS, so client #2 takes days, not weeks:
- `hospitality-daily-brief` · `whatsapp-guest-agent` · `email-receptionist` · `social-autoposter` · `direct-rebooking`
- Plus the **onboarding process**: the exact list of what to collect from each new property (rooms, packages, channels, languages, WA number).

Baha Baha is the pilot that proves it. Then we sell the template.

---

_This is the living build plan. Update as Sean provides inputs and each system goes live._
