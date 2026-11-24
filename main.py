"""Houseplant Out-of-Office entry.

Writes one funny out-of-office auto-reply, as if a houseplant sent it,
to /output/entry.txt. Deterministic: the same line every run, stdlib only.
No randomness, no network, no clock: the output is identical each time.
"""

from pathlib import Path

# The whole entry is this one line: short, plant-voiced, under 120 chars.
LINE = "Out of office: I've been alive on one sip of water since March. If I die, tell the cactus I never liked it anyway."


def main() -> None:
    output = Path("/output/entry.txt")
    try:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(LINE, encoding="utf-8")
    except OSError:
        fallback = Path(__file__).resolve().parent / "output" / "entry.txt"
        fallback.parent.mkdir(parents=True, exist_ok=True)
        fallback.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
