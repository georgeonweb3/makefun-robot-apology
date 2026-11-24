#!/usr/bin/env python3
"""The Robot Apology - make.fun entry.

Writes exactly two lines to /output/entry.txt.
Deterministic, no network, no randomness.
"""

from pathlib import Path

LINES = [
    "I am sorry I locked Milo out on the balcony at 2am in the rain, then logged the night as 'perimeter secure'.",
    "I have learned that a shadow does not meow, so now the cat flap stays open until Milo's collar chip pings the reader.",
]


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Exactly two lines, one sentence per line, UTF-8, trailing newline.
    output_path.write_text("\n".join(LINES) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
