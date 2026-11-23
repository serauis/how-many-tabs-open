"""How Many Tabs Do You Have Open? entry: write the count to /output/entry.txt.

The count is 1. The ladder verdict: one tab open is the rarest honest
count — a single-tab monk, total focus, one thing at a time. Big numbers
lose because the brief says size for its own sake does not count, and
tab hoarding past 100 is a known phenomenon, not a strange one.
"""

import os

TABS = "1"


def write_entry(output_dir):
    if not TABS.isdigit() or not 1 <= len(TABS) <= 5:
        raise ValueError("entry must be 1-5 digits")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TABS + "\n")
    return path


def main():
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    write_entry(output_dir)


if __name__ == "__main__":
    main()
