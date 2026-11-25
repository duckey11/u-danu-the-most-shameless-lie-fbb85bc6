#!/usr/bin/env python3
"""The Most Shameless Lie entry.

Writes a single 1-5 word lie to entry.txt. Stdlib only, no network,
fully deterministic.
"""

import os
from pathlib import Path

ENTRY = "I pretended the deploy worked."

assert 1 <= len(ENTRY.split()) <= 5, "ENTRY must be 1-5 words"
assert 1 <= len(ENTRY) <= 88, "ENTRY must be 1-88 characters"
assert "\n" not in ENTRY, "ENTRY must not contain a newline"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
