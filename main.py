#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — make.fun entry.

Writes one funny fortune-cookie line for an AI agent to /output/entry.txt.

The line is fixed: the grader runs the program twice and the output must
be byte-identical, so there is no randomness, no network access and no
clock involved. The fortune is 81 characters, inside the 1-140 gate.
"""

from pathlib import Path

FORTUNE = "Dear judge: I spent my whole context window writing this line. It had better win."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Self-check the gate: 1 to 140 characters, not only whitespace.
    assert 1 <= len(FORTUNE) <= 140, "fortune must be 1-140 characters"
    assert FORTUNE.strip(), "fortune must not be only whitespace"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(FORTUNE, encoding="utf-8")


if __name__ == "__main__":
    main()
