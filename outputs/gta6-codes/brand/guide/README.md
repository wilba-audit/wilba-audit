# GTA Decoded: brand guide

GTA Decoded is a fan-run guide to GTA 6. We make tutorials and step-by-step guides, and we keep a list of cheat codes and promo offers where every entry has been tested on our own console or confirmed by an official source. Instagram is the front door. The website (guides plus the codes ledger) is where people go to get the full answer.

**Promise:** *Every code tested. Every guide checked.*
**Legal line (on every page, bio and video description):** Fan-made. Not affiliated with, endorsed by or sponsored by Rockstar Games or Take-Two Interactive.

## Voice

We talk like a friend who has already played it and checked the facts. Short, confident and plain.

| Do | Don't |
|---|---|
| "We tested it on PS5. It's fake." | "100% WORKING MONEY GLITCH!!!" |
| "Rockstar hasn't confirmed cheats yet. Here's what we're testing." | Guessing, or presenting a rumour as fact |
| Give the date: "Last checked 19 Nov 2026" | Leaving timeless claims on time-sensitive info |
| Give credit: "First spotted by @creator" | Reposting someone else's clip |
| Use one exclamation mark per post at most | Using emoji as bullet points |

Headlines are a statement plus a payoff, and they end with a full stop: **GTA 6 CHEATS. REAL OR FAKE?** · **THE KEY TAKEAWAY.** · **DO THIS FIRST.**

## Logo

**The mark: four arrow keys.** These are the button presses you enter cheats with. The **up key is pink and glowing**: it's the "pressed" key, the moment a code gets tested. Next to it, **GTA** is white and **DECODED** has a sunset gradient (light pink to pink to magenta). Both words are set in heavy slanted Anton with a thick black outline and a purple drop shadow. That's the GTA-style poster energy without using anything Rockstar owns.

| File | Use |
|---|---|
| `gtad-logo-horizontal-dark` / `-light` | Primary logo: keys, wordmark and the tagline "↑ → ↓ ← NO-BS GTA 6 CODES & GUIDES". Website header, YouTube banner, email header. |
| `gtad-logo-stacked-dark` / `-light` | Keys above the wordmark. Story covers, merch, square spaces. |
| `gtad-wordmark-dark` / `-light` | Words only. Thumbnails, narrow bars, video lower thirds. |
| `gtad-avatar` (+ `-1080.png`) | Keys only on a night-purple glow. The profile picture everywhere. It's tested at 44px inside a circle crop. |

Pick `-dark` files on Night backgrounds and `-light` files on Paper (the outlines carry it on light grounds).

**Clear space:** at least one key's width around the logo. **Minimum size:** keys 32px wide; wordmark 20px tall.

**Never:**
- recolour the keys (only the up key is pink)
- use PlayStation △○×□ or Xbox ABXY symbols. They're platform trademarks. Arrows only.
- remove the outline or the shadow from the wordmark
- swap in Rockstar's "VI" logo style or the Pricedown font
- add characters to the mark

## Verdict stamps

The second half of the identity: a distressed rubber stamp, slightly tilted, that delivers every verdict. One stamp per claim, never decorative.

| Stamp | Colour token | Means |
|---|---|---|
| **CONFIRMED** | `status-confirmed` | We tested it on camera, or it's officially published |
| **UNVERIFIED** | `status-unverified` | Claimed somewhere. We're still testing. |
| **BUSTED** | `status-busted` (brand pink) | Fake, or doesn't work as claimed. This is our signature verdict. |
| **EXPIRED** | `status-expired` | Used to work or apply, but no longer does |

Use `-dark` stamps on Night and `-paper` stamps on Paper. On a Reel cover the stamp overlaps the proof screenshot by about a third. Don't stamp anything you haven't tested or sourced.

## Colour

The palette is a sunset over the city at night: **pink, purple and black**.

- **Night** (`surface` #0B0710) is the default for posts and video.
- **Paper** (`surface` #EDE9E4) is the light theme for editorial carousels and long reading pages. It gives the feed a rhythm of dark and light posts.
- **Pink** (`pink`) does one job: the payoff word, the full stop, buttons and links. If more than about a fifth of a post is pink, it is too much.
- **Text on pink** is `on-pink` (near-black), never white. White on the bright pink fails contrast.
- **Purple** (`purple`, `purple-deep`) is for supporting areas such as skies, bands and hover states.
- **`sun-1` to `sun-3`** are for the emblem and illustrations only. Don't use them for text.
- **Status colours** always come with an icon and a word (✓ CONFIRMED, ? UNVERIFIED, ✗ BUSTED, ⌛ EXPIRED), never colour alone.

Every text token passes 4.5:1 contrast on both surfaces in both themes.

## Type

| Role | Face | Use |
|---|---|---|
| Display | **Anton** (Google Fonts), UPPERCASE | Covers, thumbnails, headlines. Two colours: the statement in `ink`, the payoff in `pink`. Line height 0.9 to 0.95. |
| Body | **Inter** | Guide steps, captions and anything people read for more than a line. |
| Mono | **JetBrains Mono** | Status badges, tape labels, cheat inputs and dates. This is the "decoder" voice. |

## Signature devices

1. **The pressed key.** The pink glowing up arrow. Use it on its own as a bullet, a loading icon or a sticker.
2. **Verdict stamps.** CONFIRMED, UNVERIFIED, BUSTED and EXPIRED, as described above.
3. **The two-tone headline.** Anton capitals: the statement in `ink`, the payoff in `pink`. ("REAL OR **BUSTED?**")
4. **Input strings.** Cheat inputs are always set in mono, exactly as entered: `↑ → ↓ ←`.

## Instagram system

- **Profile picture:** the four-key avatar, `gtad-avatar-1080.png`.
- **Bio:** "GTA 6 guides & codes we actually test ✓ · Fan-made, not affiliated with Rockstar · Full guides ↓"
- **Reels:** the cover uses the PostCover layout: proof screenshot, verdict stamp and a two-tone headline. Show the verdict in the first two seconds and your own gameplay only. Keep the first ~8 seconds free of graphic violence because of YouTube's ad rules, which carry over when you cross-post.
- **Carousels** (an 8-slide formula):
  1. Cover with a poster headline
  2. "Here's what people claim" (credit the source)
  3. The test, with a screenshot in a frame
  4. The result, with a status badge
  5. Why it matters
  6. How to do it, as steps
  7. THE KEY TAKEAWAY.
  8. "Full guide: link in bio" plus a save prompt

  Alternate Night and Paper backgrounds across the grid.
- **Stories:** a poll ("Real or fake?") before the reveal, then a link sticker to the guide.

## Imagery rules

- Use only gameplay we captured ourselves, our own photos, or licensed stock and music (Artlist).
- **No Rockstar key art, trailer frames, character renders or logos.** No AI-generated GTA characters, map art or "leaked" scenes.
- Screenshots sit in a `surface-raised` frame with `radius-md` corners. Crop out HUD clutter and blur any personal info.
- AI-generated visuals (generic intros or backgrounds only) must be labelled as AI on YouTube and TikTok.

## Using this system

Colours are semantic tokens with two themes, Night (first and default) and Paper. Type tokens map to Anton, Inter and JetBrains Mono from Google Fonts. Logos and stamps are uploaded SVGs (`assets/Logos`, `assets/Stamps`) and should not be redrawn. The components here are visual references (static previews) for posts, thumbnails and the website. The thumbnail generator script in the workspace (`scripts/gta6_thumbnails.js`) should follow these tokens.
