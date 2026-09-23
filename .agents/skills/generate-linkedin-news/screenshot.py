#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["playwright"]
# ///
"""Screenshot the LinkedIn news page and fail if any heading or headline wraps."""

import argparse
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

# Counts rendered lines per element; column headers measure only their text, not the count badge.
WRAPPED_JS = """
() => [...document.querySelectorAll('h1, .column-header, .item-title')].flatMap(el => {
  const range = document.createRange();
  range.selectNodeContents(el.classList.contains('column-header') ? el.firstChild : el);
  const lines = new Set([...range.getClientRects()].filter(r => r.width > 0).map(r => Math.round(r.top)));
  return lines.size > 1 ? [el.textContent.trim()] : [];
})
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html_path", type=Path)
    parser.add_argument("output_png", type=Path)
    args = parser.parse_args()

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1600, "height": 900}, device_scale_factor=2)
        page.goto(args.html_path.resolve().as_uri(), wait_until="networkidle")
        page.evaluate("document.fonts.ready")
        wrapped = page.evaluate(WRAPPED_JS)
        page.locator("main").screenshot(path=str(args.output_png))
        browser.close()

    print(f"Saved {args.output_png}")
    if wrapped:
        print("These elements wrap onto multiple lines; shorten them and re-run:", file=sys.stderr)
        for text in wrapped:
            print(f"  - {text}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
