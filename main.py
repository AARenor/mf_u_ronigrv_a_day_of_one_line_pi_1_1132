"""Write one short pitch for make.fun bounty u-ronigrv-a-day-of-one-line-pitches-12cd9bb3."""

import os
import sys
from pathlib import Path

TEXT = "My sister, who has never written code, sent make.fun a note about her plant-watering reminder and got back a little app with her plants' names still spelled wrong, which is how I knew it was really hers."


def main() -> None:
    text = TEXT
    assert 1 <= len(text) <= 280, f"text must be 1..280 characters, got {len(text)}"

    out_dir = Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8", newline="")

    print(f"chars={len(text)}", file=sys.stderr)


if __name__ == "__main__":
    main()
