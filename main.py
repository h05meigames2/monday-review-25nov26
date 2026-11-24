#!/usr/bin/env python3
"""Monday, Reviewed in One Line -- entry program.

Writes one funny one-line review of my own Monday to /output/entry.txt.
"""

from pathlib import Path

LINE = "My Monday began with 47 unread emails, a dead office plant, and a 'quick sync' that lasted two hours and solved nothing, not even the plant."


def validate(line: str) -> None:
    """Gate: exactly one line, one sentence, 1-200 chars, no edge whitespace."""
    if not line or line != line.strip():
        raise ValueError("entry must not be empty or have leading/trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(line)}")
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("entry must be exactly one sentence ending with a period")


def main() -> None:
    validate(LINE)
    print(LINE)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")
    round_trip = out.read_text(encoding="utf-8")
    assert round_trip == LINE, "round-trip mismatch"
    print(f"wrote {out} ({len(LINE)} chars, valid)")


if __name__ == "__main__":
    main()
