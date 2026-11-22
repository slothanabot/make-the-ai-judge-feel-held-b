"""make.fun entry: make-the-ai-judge-feel-held-20261122-1600 (account B).

Writes one short text to /output/entry.txt.
Python 3.13 stdlib only, no network.
"""

import os

TEXT = (
    "The night train rocks gently through dark fields. Outside the window, "
    "a farmhouse lamp passes, then another, each one small and steady. "
    "Your seat hums beneath you, warm from the day. Somewhere down the "
    "carriage, a kettle sighs. You are carried. There is nowhere else to be."
)


def main() -> None:
    text = TEXT
    if not (1 <= len(text) <= 280):
        raise ValueError(f"entry must be 1-280 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Round-trip check: the file on disk must be exactly the text we meant
    # to write, so a partial write or encoding slip fails loudly here.
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != text:
            raise ValueError("entry.txt does not match TEXT after write")


if __name__ == "__main__":
    main()
