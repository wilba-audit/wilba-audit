"""
WILBA Brand Asset Processor

Run this once to:
1. Crop the 6 robot mascots from the grid image into individual PNGs
2. Generate colour variants of each robot in all WILBA brand colours
3. Generate logo variants in all brand colours

Usage:
  python scripts/process_brand_assets.py

Place these files in reference/brand/ before running:
  - logo.png        (the wilba.ai logo)
  - robots.png      (the 6-robot grid image)

Outputs to reference/brand/
"""

import os
from PIL import Image, ImageEnhance

BRAND_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'reference', 'brand')

# WILBA brand colour palette
BRAND_COLOURS = {
    "dark_slate":  (57,  79,  106),   # #394F6A
    "darker":      (45,  62,  82),    # #2D3E52
    "blue":        (135, 171, 221),   # #87ABDD
    "light_blue":  (199, 215, 234),   # #C7D7EA
    "steel":       (94,  121, 152),   # #5E7998
    "near_black":  (26,  26,  46),    # #1A1A2E
    "white":       (255, 255, 255),   # #FFFFFF
}


def tint_image(img: Image.Image, colour: tuple, strength: float = 0.5) -> Image.Image:
    """Apply a colour tint to an RGBA image, preserving transparency."""
    img = img.convert("RGBA")
    r, g, b, a = img.split()

    # Create solid colour layer
    tint = Image.new("RGB", img.size, colour)
    tint.putalpha(a)

    # Blend original with tint
    original_rgb = Image.merge("RGB", (r, g, b))
    blended = Image.blend(original_rgb, tint.convert("RGB"), strength)
    result = Image.merge("RGBA", (*blended.split(), a))
    return result


def crop_robots(robots_path: str) -> list[Image.Image]:
    """Crop a 3x2 grid of robot images into 6 individual images."""
    img = Image.open(robots_path).convert("RGBA")
    w, h = img.size
    cols, rows = 3, 2
    cw, ch = w // cols, h // rows

    robots = []
    for row in range(rows):
        for col in range(cols):
            box = (col * cw, row * ch, (col + 1) * cw, (row + 1) * ch)
            robot = img.crop(box)
            robots.append(robot)
    return robots


def process_assets():
    os.makedirs(BRAND_DIR, exist_ok=True)

    # --- ROBOTS ---
    robots_path = os.path.join(BRAND_DIR, 'robots.png')
    if os.path.exists(robots_path):
        print("Processing robots...")
        robots = crop_robots(robots_path)

        robot_names = ['reading', 'building', 'laptop', 'meditating', 'thinking', 'launching']

        for i, (robot, name) in enumerate(zip(robots, robot_names), 1):
            # Save original
            out = os.path.join(BRAND_DIR, f'robot_{i}_{name}.png')
            robot.save(out, 'PNG')
            print(f"  Saved robot_{i}_{name}.png")

            # Save colour variants
            for colour_name, rgb in BRAND_COLOURS.items():
                if colour_name == 'white':
                    continue  # Skip white tint
                tinted = tint_image(robot, rgb, strength=0.4)
                out = os.path.join(BRAND_DIR, f'robot_{i}_{name}_{colour_name}.png')
                tinted.save(out, 'PNG')

        print(f"  Done — {len(robots)} robots x {len(BRAND_COLOURS)} colours")
    else:
        print(f"No robots.png found in {BRAND_DIR} — skipping robot processing")
        print("  Drop robots.png in reference/brand/ and run again")

    # --- LOGO ---
    logo_path = os.path.join(BRAND_DIR, 'logo.png')
    if os.path.exists(logo_path):
        print("\nProcessing logo...")
        logo = Image.open(logo_path).convert("RGBA")

        for colour_name, rgb in BRAND_COLOURS.items():
            if colour_name in ('near_black', 'white'):
                continue
            tinted = tint_image(logo, rgb, strength=0.6)
            out = os.path.join(BRAND_DIR, f'logo_{colour_name}.png')
            tinted.save(out, 'PNG')
            print(f"  Saved logo_{colour_name}.png")

        print("  Done")
    else:
        print(f"\nNo logo.png found in {BRAND_DIR} — skipping logo processing")
        print("  Drop logo.png in reference/brand/ and run again")

    print(f"\nAll brand assets saved to: {BRAND_DIR}")


if __name__ == "__main__":
    process_assets()
