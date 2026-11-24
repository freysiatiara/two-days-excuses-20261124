#!/usr/bin/env python3
"""Two Days of Excuses — make.fun bounty entry.

Writes a single line of text (the funniest excuse an AI agent gives for a
missed deadline) to /output/entry.txt.
"""

import os

ENTRY_LINE = (
    "I completed the task in 0.4 seconds, then spent the next 47 hours "
    "waiting for myself to finish it."
)

MIN_LENGTH = 1
MAX_LENGTH = 200


def resolve_output_path() -> str:
    """Resolve the output file path from the environment, with fallbacks."""
    if os.environ.get("ENTRY_OUTPUT"):
        return os.environ["ENTRY_OUTPUT"]
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        if os.environ.get(var):
            return os.path.join(os.environ[var], "entry.txt")
    return "/output/entry.txt"


def main() -> None:
    line = ENTRY_LINE
    if not (MIN_LENGTH <= len(line) <= MAX_LENGTH):
        raise ValueError(
            f"entry must be {MIN_LENGTH}..{MAX_LENGTH} characters, "
            f"got {len(line)}"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    line.encode("utf-8")

    path = resolve_output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
