"""The line the Moon says back to everyone who has ever stared up at it.

Prints the line to stdout and writes the exact same line, with no
trailing newline, to /output/entry.txt. Standard library only, no
network access, no files read — the line is a constant in this file.
The 240-character gate is checked on every run so an over-long edit
can never slip through silently. The Moon gets one sentence, and it
uses it to set the record straight.
"""

import os
import sys

LINE = (
    "You wished on me for years. I was just a rock with good lighting."
)


def main() -> int:
    if not 1 <= len(LINE) <= 240:
        print(f"error: line is {len(LINE)} chars, must be 1-240",
              file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
