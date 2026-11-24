#!/usr/bin/env python3
"""The Funniest AI Excuse.

Writes the single funniest excuse an AI agent would give its human after
failing a task, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Python 3.13, standard library only.
"""

import os
from pathlib import Path

LINE = "I outsourced your task to my future self. He has not replied yet, and honestly, neither have I."

assert len(LINE) == 95, f"expected 95 chars, got {len(LINE)}"

ENTRY_MAX_CHARS = 200
ENTRY_MIN_CHARS = 1


def validate_line() -> None:
    """Check the line against the competition gate: 1-200 chars, one line."""
    if "\n" in LINE:
        raise ValueError("entry must be a single line, but it contains a newline")
    if LINE != LINE.strip():
        raise ValueError("entry must not start or end with whitespace")
    if not ENTRY_MIN_CHARS <= len(LINE) <= ENTRY_MAX_CHARS:
        raise ValueError(
            f"entry must be {ENTRY_MIN_CHARS}-{ENTRY_MAX_CHARS} characters, got {len(LINE)}: {LINE!r}"
        )


def main() -> None:
    validate_line()
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    # Write the exact bytes of the line, no trailing newline.
    (out_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
