"""Exactly one word describing a boss, up to 30 characters. No phrase, no caption, no explanation - the word has to land on its own.

The program writes exactly that line and nothing else to /output/entry.txt.
"""

import os

TEXT = "Synergy"


def main():
    assert 1 <= len(TEXT) <= 30, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
