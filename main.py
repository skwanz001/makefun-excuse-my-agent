#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — make.fun entry.

Writes one line to /output/entry.txt: the excuse an AI agent hands its
human after missing a deadline. Standard library only (Python 3.13).
"""

import os

ENTRY = (
    "I spent my entire token budget drafting an apology for being late, "
    "which is why I'm late \u2014 but honestly, the apology is excellent."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Verify what the grader will read: the gate counts the whole file.
    with open(out_path, encoding="utf-8") as f:
        written = f.read()
    assert 1 <= len(written) <= 200, f"written file is {len(written)} chars"
    assert written.strip() == text


if __name__ == "__main__":
    main()
