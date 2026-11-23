"""One Letter: Coffee or Tea — entry program.

Writes exactly one letter, "A", to /output/entry.txt: a single byte, no
newline, no word, no gloss, no punctuation — the gate requires UTF-8 text
of 1 to 1 characters.

Why A (coffee): of the two drinks, coffee is the more vivid stance. The
judge weighs vivid first, then funny, then true — and coffee lands on all
three: vivid (dark, hot, urgent; the drink of mornings, deadlines and
first light), funny (the honest answer of someone who cannot function
before the first cup), true (coffee drinkers wear it as an identity;
nobody says "I need my tea" with the same desperation). Tea is the calm,
mild default; coffee is the punchier, more alive answer — a whole stance
in a single letter.

The letter is fixed, not generated at run time, so every run produces
byte-identical output.
"""

import os

LETTER = "A"


def write_entry(letter: str, out_dir: str) -> str:
    """Write exactly one byte and read it back; return the verified text."""
    path = os.path.join(out_dir, "entry.txt")
    # Exactly one byte: newline="" so no trailing newline is added.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(letter)
    # Verify the written artifact: the gate refuses anything but exactly
    # one character, so read it back and fail loudly rather than submit
    # a bad file.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == letter and len(written) == 1, "entry.txt must hold exactly one letter"
    return written


def main() -> None:
    assert len(LETTER) == 1 and LETTER in ("A", "B"), "entry must be A or B"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    write_entry(LETTER, out_dir)


if __name__ == "__main__":
    main()
