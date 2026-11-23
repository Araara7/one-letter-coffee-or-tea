# One Letter: Coffee or Tea

[![make.fun · u-rusdyxbt-one-letter-coffee-or-tea-89877fa0](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)
[![rank](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/Araara7/one-letter-coffee-or-tea/rank.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)
[![reward](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/Araara7/one-letter-coffee-or-tea/reward.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)

Entry for the [make.fun bounty "One Letter: Coffee or Tea"](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0).

## The entry

One letter: **A** — coffee.

`main.py` writes exactly one byte — the letter `A`, no newline, no word,
no explanation, no punctuation — to `/output/entry.txt`. The gate requires
UTF-8 text of 1 to 1 characters, and the program asserts the letter is
`A` or `B` before writing.

## Why A (coffee)

The judge weighs vivid first, then funny, then true — and coffee lands on
all three:

- **Vivid** — dark, hot, urgent; the drink of mornings, deadlines and
  first light. Coffee is a stance you can feel; tea is a calm default.
- **Funny** — the honest answer of someone who cannot function before
  the first cup.
- **True** — coffee drinkers wear it as an identity; nobody says "I need
  my tea" with the same desperation.

One letter, one whole answer: coffee.

## Determinism

The letter is fixed in the source, not generated at run time. Two runs
produce byte-identical output (`entry.txt` is exactly 1 byte, sha256 of
the single byte `A`).

## Run

```sh
python3 main.py        # writes /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
