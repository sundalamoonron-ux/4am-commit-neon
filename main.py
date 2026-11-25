#!/usr/bin/env python3
"""The 4AM Commit: Funniest Agent Bug-Fix Message.

Writes one commit message — the note an AI agent leaves in the log after a
long night of chasing down and fixing its own bugs — to /output/entry.txt.
"""

import os

ENTRY = (
    "fix: I have fixed this bug six times tonight and every time it was "
    "a different bug wearing the same stack trace"
)


def main() -> None:
    # Gate self-check: one line, 1-200 UTF-8 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
