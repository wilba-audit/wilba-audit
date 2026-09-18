"""
Pull a transcript from a YouTube video (podcasts like Diary of a CEO, Liam
Ottley, Hormozi, etc.) and save it to reference/transcripts/.

Usage:
    python scripts/pull_transcript.py "<youtube_url>" [optional-slug]

Needs: pip install youtube-transcript-api
Works for any YouTube video that has captions (most big podcasts do).
For non-YouTube sources, use the /transcript command's web-fetch fallback.
"""

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT_DIR = REPO / "reference" / "transcripts"


def video_id(url: str) -> str:
    """Extract the YouTube video id from any common URL form."""
    patterns = [
        r"(?:v=|/videos/|embed/|youtu\.be/|/v/|/e/|watch\?v=|&v=)([\w-]{11})",
        r"^([\w-]{11})$",
    ]
    for p in patterns:
        m = re.search(p, url)
        if m:
            return m.group(1)
    raise SystemExit(f"Could not find a YouTube video id in: {url}")


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:60] or "transcript"


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit('Usage: python scripts/pull_transcript.py "<youtube_url>" [slug]')

    url = sys.argv[1]
    slug = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        from youtube_transcript_api import YouTubeTranscriptApi
    except ImportError:
        raise SystemExit("Missing dependency. Run: pip install youtube-transcript-api")

    vid = video_id(url)
    try:
        segments = YouTubeTranscriptApi.get_transcript(vid)
    except Exception as e:  # noqa: BLE001
        raise SystemExit(
            f"Couldn't fetch a transcript for {vid}: {e}\n"
            "The video may have captions disabled — try the /transcript web fallback."
        )

    text = " ".join(seg["text"].replace("\n", " ") for seg in segments)
    text = re.sub(r"\s+", " ", text).strip()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUT_DIR / f"{slugify(slug or vid)}.md"
    out.write_text(
        f"# Transcript\n\nSource: {url}\n\n---\n\n{text}\n",
        encoding="utf-8",
    )
    print(f"[ok] Saved {len(text)} chars → {out.relative_to(REPO)}")


if __name__ == "__main__":
    main()
