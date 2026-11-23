#!/usr/bin/env python3
"""Six Words, One Story — writes the entry to /output/entry.txt.

The story is one complete story in exactly six words:
"The ring fit. The marriage didn't."
"""

import os

STORY = "The ring fit. The marriage didn't."

# The entry must be one complete story in exactly six words.
assert len(STORY.split()) == 6, "story must be exactly six words"
assert 1 <= len(STORY) <= 60, "story must be 1-60 characters"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
