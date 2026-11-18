# GTA Decoded: launch posting pack

Everything is in `instagram/stories/` (1080×1920) and `instagram/feed/` (1080×1350, 4:5).
To change any text, edit `instagram/content.json` and run `node scripts/gta6_ig_render.js`, or just ask Claude.

## Before you post (2 minutes)
- [ ] Profile set up (see `PROFILE-SETUP.md`)
- [ ] `last_checked` in `content.json` is today's date. Re-render story 07 if the status has changed.
- [ ] Frames with a dashed box need **your own screenshot** dropped in (Instagram's own editor or CapCut):
  - `story-05`: optional, add a still of the viral claim (credit the poster on screen)
  - `story-06`: **required**. Your test screenshot. Only post it once you've actually tested the claim. If the result isn't BUSTED, ask Claude to re-render with the correct stamp.
  - `post-B1`: **required**. Your PlayStation confirmation email, with order number and email address blurred.

## Posting order

### Day 1: set the stage
1. **Stories 01 → 04** (Start here). Then tap **Highlight → START HERE** and set the cover `highlights/1-start-here.png`.
2. **Feed: Carousel A** (`post-A1` to `post-A5`). **Pin it.**
3. **Stories 09 → 10** (Scam watch) → highlight **SCAM WATCH**.
4. **Story 07** (Codes status) → highlight **CODES**.
5. **Story 08** (Routes loading) → highlight **ROUTES**.

### Day 2: first verdict
6. **Story 05** with a **poll sticker** (REAL / BUSTED) placed on the box. Morning.
7. Test the claim on camera.
8. **Story 06** (the verdict) plus a **link sticker** to your sign-up page. Evening. Then highlight **REAL/BUSTED**.

### Day 3: first guide
9. **Feed: Carousel B** (`post-B1` to `post-B6`). **Pin it.**

## Captions (ready to paste)

### Carousel A: Start here
```
We tested every viral GTA 6 code so you don't waste your night typing GTA V cheats into a brand new game. 🎮

Here's how GTA Decoded works:
→ we find the claim (and credit who posted it)
→ we test it on our own console, on camera
→ we stamp the verdict: CONFIRMED · UNVERIFIED · BUSTED · EXPIRED
→ we date it, and update it when patches change things

Save this. Turn on notifications. Verdicts drop daily.

Fan-made. Not affiliated with Rockstar Games or Take-Two.

#GTA6 #GTAVI #GTA6Cheats #GTA6Tips #GTA6News
```
**Alt text:** "Five slides explaining that GTA Decoded tests GTA 6 codes on camera and stamps each one Confirmed, Unverified, Busted or Expired."

### Carousel B: Claim your free GTA+ month
```
Pre-ordered GTA 6 digitally on PlayStation? You've got a free month of GTA+ waiting. Don't let it expire. 👀

✓ Digital pre-orders on PlayStation Store (Standard or Ultimate)
✗ Physical copies aren't included
📩 Claim it through the instructions in your confirmation email
⏰ PlayStation's deadline: 31 March 2027
🔁 It renews until you cancel, so set a reminder

Xbox and Rockstar Store terms are different, so check your own email.
Nobody will DM you a "free GTA+ code". That's a scam.

Source: PlayStation's official GTA VI offer terms (checked Nov 2026).
Fan-made. Not affiliated with Rockstar Games, Take-Two or Sony.

#GTA6 #GTAVI #GTAPlus #PS5 #GTA6Tips
```
**Alt text:** "Six slides: who gets the free GTA+ month with a GTA 6 digital pre-order on PlayStation, how to claim it, the 31 March 2027 deadline, and a scam warning."
**Source to keep on file:** https://www.playstation.com/en-us/support/games/gta-vi-offer-terms/ ([VERIFY] re-open it before posting and check the dates still match)

## Story stickers
- **Poll** (story 05): question "Real or busted?", options **REAL** / **BUSTED**
- **Link** (story 04, 06, 10): your code-alerts sign-up page
- **Mention**: when a claim came from a creator, tag them on the verdict story (credit, not their footage)

## Weekly rhythm after launch
- **Daily:** 1 verdict story pair (poll, then reveal)
- **3× a week:** 1 feed carousel (from the 20-carousel batch)
- **Weekly:** refresh story 07 (codes status) with a new `last_checked` date
