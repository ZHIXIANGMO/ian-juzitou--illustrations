#!/usr/bin/env python3
"""Join validated WeChat cover images without resizing or cropping."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from PIL import Image, UnidentifiedImageError


WIDE_SIZE = (900, 383)
SQUARE_SIZE = (383, 383)
OUTPUT_SIZE = (1283, 383)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Place a 900x383 cover on the left and a 383x383 cover on the "
            "right, then save a 1283x383 PNG without resizing or cropping."
        )
    )
    parser.add_argument("--wide", required=True, type=Path, help="900x383 source image")
    parser.add_argument("--square", required=True, type=Path, help="383x383 source image")
    parser.add_argument("--output", required=True, type=Path, help="New 1283x383 PNG")
    return parser.parse_args()


def load_source(path: Path, label: str, expected_size: tuple[int, int]) -> Image.Image:
    if not path.is_file():
        raise ValueError(f"{label} image does not exist or is not a file: {path}")

    try:
        with Image.open(path) as source:
            source.load()
            if source.size != expected_size:
                raise ValueError(
                    f"{label} image must be {expected_size[0]}x{expected_size[1]} pixels; "
                    f"got {source.width}x{source.height}: {path}"
                )
            return source.convert("RGBA")
    except (UnidentifiedImageError, OSError) as error:
        raise ValueError(f"Cannot read {label} image: {path} ({error})") from error


def validate_output(output: Path, sources: tuple[Path, Path]) -> None:
    if output.suffix.lower() != ".png":
        raise ValueError(f"Output path must use the .png extension: {output}")
    if output.exists():
        raise ValueError(f"Output already exists; choose a new path: {output}")

    resolved_output = output.resolve()
    if any(resolved_output == source.resolve() for source in sources):
        raise ValueError("Output path must not overwrite either source image")


def stitch(wide: Image.Image, square: Image.Image, output: Path) -> None:
    canvas = Image.new("RGBA", OUTPUT_SIZE, (0, 0, 0, 0))
    canvas.alpha_composite(wide, (0, 0))
    canvas.alpha_composite(square, (WIDE_SIZE[0], 0))
    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output, format="PNG")


def main() -> int:
    args = parse_args()

    try:
        validate_output(args.output, (args.wide, args.square))
        wide = load_source(args.wide, "Wide", WIDE_SIZE)
        square = load_source(args.square, "Square", SQUARE_SIZE)
        stitch(wide, square, args.output)
    except ValueError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    print(f"Created {OUTPUT_SIZE[0]}x{OUTPUT_SIZE[1]} PNG: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
