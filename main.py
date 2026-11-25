"""Notes From a Passive-Aggressive Fridge.

Writes one passive-aggressive note from a smart fridge to its owner
to /output/entry.txt (the gate reads that file) and prints exactly
the same line on stdout.

The note is a single line: the judge compares one-liners, so the
program refuses to emit anything multi-line or whitespace-only.
"""

import os

# The joke: the fridge did its job perfectly for six days, and the
# owner still chose takeout — so the fridge, keeper of the leftovers,
# objects to being treated as a museum that merely preserves things
# nobody ever eats. "Karen" lands the petty, name-the-offender sting.
NOTE = "Note from your fridge: I kept your leftovers cold for six days. You ate takeout instead. I am not a museum, Karen."


def write_entry(text: str) -> None:
    """Write the note to the gate's file, world-readable (mode 0644)."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    os.chmod("/output/entry.txt", 0o644)


def main() -> None:
    # Gate: 1-200 UTF-8 chars, a single line, not only whitespace.
    assert 0 < len(NOTE) <= 200, "note exceeds the gate's 200 chars"
    assert "\n" not in NOTE.strip(), "note must be a single line"
    assert NOTE.strip(), "note must not be only whitespace"
    write_entry(NOTE)
    print(NOTE)


if __name__ == "__main__":
    main()
