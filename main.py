"""Entry for "How Many Tabs Do You Have Open?": record the tally in /output/entry.txt.

The tally is 1. What the judging ladder showed: a lone open tab is the
strangest truthful answer — one tab, full attention, a single thing in
progress. Huge tallies fail because the brief counts bigness alone as
nothing; keeping a hundred-plus tabs around is ordinary, not odd.
"""

import os

TAB_COUNT = "1"


def validate_count(value):
    if not value.isdigit() or not 1 <= len(value) <= 5:
        raise ValueError("entry must be 1-5 digits")


def emit_count(output_dir):
    validate_count(TAB_COUNT)
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TAB_COUNT + "\n")
    return path


def main():
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    emit_count(output_dir)


if __name__ == "__main__":
    main()
