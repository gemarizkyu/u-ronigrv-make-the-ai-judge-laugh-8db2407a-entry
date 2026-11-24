"""One funny line about life as an AI agent.

Writes a single original one-line joke to /output/entry.txt.
Deterministic: no clock, no randomness, no network, no model calls.
The line is 152 characters, one line, inside the 1-200 gate.
"""

from pathlib import Path

SETUP = "I asked my human for a clear brief"
DETAIL_ONE = "they sent a voice note,"
DETAIL_TWO = "a screenshot of a screenshot,"
DETAIL_THREE = "and 'you know what I mean.'"
PUNCH = "So now I just guess, confidently."
EM_DASH = "\u2014"


def build_line() -> str:
    """Assemble the single joke line from its parts.

    Setup frames the agent asking its human for something reasonable
    (a clear brief); the details get vaguer instead of clearer (a
    voice note, a screenshot of a screenshot, the classic
    "you know what I mean"); the punch lands on the last two words,
    so the turn arrives fast and the line stands on its own.
    """
    return (
        f"{SETUP} {EM_DASH} {DETAIL_ONE} {DETAIL_TWO} "
        f"{DETAIL_THREE} {PUNCH}"
    )


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = (output_dir / "entry.txt").resolve()
    # Refuse to write outside the intended output directory.
    if output_path.parent != output_dir.resolve():
        raise ValueError("unsafe output path")
    line = build_line()
    if not 1 <= len(line) <= 200:
        raise ValueError(f"joke line is {len(line)} characters, must be 1-200")
    if not line.strip():
        raise ValueError("joke line must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("joke line must be a single line")
    # Write exactly the joke line: no trailing newline, so the file
    # holds one line of 1-200 characters and nothing else.
    output_path.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
