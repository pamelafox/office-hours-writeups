#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["pillow>=11.0.0"]
# ///
"""Compose four labeled images into an edge-to-edge social media montage."""

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


WIDTH = 1200
PANEL_WIDTH = WIDTH // 2
PANEL_IMAGE_HEIGHT = 338
LABEL_HEIGHT = 72
HEADER_HEIGHT = 130
LABEL_COLORS = [
    (10, 102, 194),
    (8, 127, 91),
    (181, 74, 53),
    (107, 91, 149),
]


def load_font(size: int) -> ImageFont.FreeTypeFont:
    candidates = [
        "/System/Library/Fonts/Avenir Next.ttc",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "C:/Windows/Fonts/seguisb.ttf",
        "DejaVuSans-Bold.ttf",
    ]
    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, size)
        except OSError:
            continue
    raise RuntimeError("Could not find a suitable TrueType font")


def parse_panel(value: str) -> tuple[Path, str]:
    try:
        image_path, label = value.rsplit("::", 1)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(
            "Panels must use the format IMAGE_PATH::LABEL"
        ) from exc

    path = Path(image_path)
    if not path.is_file():
        raise argparse.ArgumentTypeError(f"Panel image does not exist: {path}")
    if not label.strip():
        raise argparse.ArgumentTypeError("Panel label cannot be empty")
    return path, label.strip()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compose four labeled images into a 2x2 montage"
    )
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--title", help="Optional montage header title")
    parser.add_argument("--subtitle", help="Optional header subtitle")
    parser.add_argument(
        "--panel",
        action="append",
        type=parse_panel,
        required=True,
        help="Panel in IMAGE_PATH::LABEL format; provide exactly four",
    )
    args = parser.parse_args()

    if len(args.panel) != 4:
        parser.error("exactly four --panel values are required")
    if args.subtitle and not args.title:
        parser.error("--subtitle requires --title")

    header_height = HEADER_HEIGHT if args.title else 0
    row_height = PANEL_IMAGE_HEIGHT + LABEL_HEIGHT
    canvas = Image.new(
        "RGB",
        (WIDTH, header_height + (row_height * 2)),
        (244, 241, 234),
    )
    draw = ImageDraw.Draw(canvas)

    if args.title:
        draw.rectangle((0, 0, WIDTH, HEADER_HEIGHT), fill=(23, 50, 77))
        draw.text((40, 24), args.title, font=load_font(44), fill="white")
        if args.subtitle:
            draw.text(
                (42, 84),
                args.subtitle,
                font=load_font(24),
                fill=(244, 201, 93),
            )

    label_font = load_font(30)
    for index, (image_path, label) in enumerate(args.panel):
        left = (index % 2) * PANEL_WIDTH
        top = header_height + ((index // 2) * row_height)
        with Image.open(image_path) as source:
            panel = ImageOps.fit(
                source.convert("RGB"),
                (PANEL_WIDTH, PANEL_IMAGE_HEIGHT),
                method=Image.Resampling.LANCZOS,
            )
        canvas.paste(panel, (left, top))

        label_top = top + PANEL_IMAGE_HEIGHT
        draw.rectangle(
            (left, label_top, left + PANEL_WIDTH, label_top + LABEL_HEIGHT),
            fill=LABEL_COLORS[index],
        )
        draw.text((left + 24, label_top + 14), label, font=label_font, fill="white")

        text_box = draw.textbbox((0, 0), label, font=label_font)
        if text_box[2] - text_box[0] > PANEL_WIDTH - 48:
            parser.error(f"panel label is too long to fit: {label}")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(args.output, optimize=True)
    print(f"Created {args.output} ({canvas.width}x{canvas.height})")


if __name__ == "__main__":
    main()