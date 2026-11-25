#!/usr/bin/env python3
"""The 3 AM Commit Message — make.fun bounty entry.

Writes one commit message, exactly as drafted, to /output/entry.txt.
Fully deterministic: same bytes on every run, no randomness, no clock.
"""

import os

ENTRY = "wip: broke prod at 3 AM; committing this so future me can blame past me with evidence"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
