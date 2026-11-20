#!/usr/bin/env python3
"""Publish GTA Decoded media to the public media repo so Windsor/Instagram can fetch it.

Usage:
  python3 scripts/gta6_media_push.py <slug> <file> [<file> ...]
  python3 scripts/gta6_media_push.py --library   # sync reels/library/*.mp4

- PNG/JPG images are converted to JPEG (quality 92, RGB, max 8 MB) because Instagram
  carousels only accept JPEG.
- MP4s are copied as-is (must be H.264, <= 15 min).
- Files land in gta-decoded-media/posts/<YYYY-MM-DD>/<slug>/ and are pushed to `main`.
- Prints one public raw URL per file, in the order given (that order = carousel order).

The media repo clone is expected at ../gta-decoded-media (next to this repo). If it is
missing, attach it in the session (add_repo wilba-audit/gta-decoded-media, push access)
and clone it there first.
"""
import datetime, os, shutil, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MEDIA = Path(os.environ.get("GTAD_MEDIA_REPO", ROOT.parent / "gta-decoded-media"))
RAW = "https://raw.githubusercontent.com/wilba-audit/gta-decoded-media/main/"
MAX_BYTES = 8 * 1024 * 1024


def git(*args):
    return subprocess.run(["git", "-C", str(MEDIA), *args], check=True,
                          capture_output=True, text=True).stdout


def to_jpeg(src: Path, dst: Path):
    from PIL import Image
    im = Image.open(src).convert("RGB")
    q = 92
    while True:
        im.save(dst, "JPEG", quality=q, optimize=True, progressive=True)
        if dst.stat().st_size <= MAX_BYTES or q <= 60:
            break
        q -= 8


def main():
    if not (MEDIA / ".git").exists():
        sys.exit(f"Media repo not found at {MEDIA}. Attach and clone wilba-audit/gta-decoded-media first.")
    git("fetch", "-q", "origin", "main")
    git("checkout", "-q", "-B", "main", "origin/main")

    args = sys.argv[1:]
    if args[:1] == ["--library"]:
        rel_dir = Path("library")
        files = sorted((ROOT / "outputs/gta6-codes/reels/library").glob("*.mp4"))
        slug = "library"
    else:
        if len(args) < 2:
            sys.exit(__doc__)
        slug, files = args[0], [Path(f) for f in args[1:]]
        rel_dir = Path("posts") / datetime.date.today().isoformat() / slug

    out_dir = MEDIA / rel_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    urls = []
    for i, f in enumerate(files, 1):
        f = Path(f).resolve()
        if f.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp"):
            name = f"{i:02d}-{f.stem}.jpg" if slug != "library" else f.stem + ".jpg"
            to_jpeg(f, out_dir / name)
        else:
            name = f.name if slug == "library" else f"{i:02d}-{f.name}"
            shutil.copy2(f, out_dir / name)
        urls.append(RAW + str(rel_dir / name))

    git("add", str(rel_dir))
    if git("status", "--porcelain").strip():
        git("-c", "user.name=GTA Decoded bot", "-c", "user.email=noreply@anthropic.com",
            "commit", "-q", "-m", f"media: {rel_dir}")
        for attempt in range(4):
            try:
                git("-c", "push.negotiate=true", "push", "-q", "origin", "main")
                break
            except subprocess.CalledProcessError:
                if attempt == 3:
                    raise
                git("pull", "-q", "--rebase", "origin", "main")
    print("\n".join(urls))


if __name__ == "__main__":
    main()
