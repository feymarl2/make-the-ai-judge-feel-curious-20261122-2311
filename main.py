"""One quiet question for the AI judge, written to /output/entry.txt.

The judge's brief prizes calm intrigue, not a pointed challenge -- so the
text asks instead of accusing, and the question stays open after the last word."""
from pathlib import Path

TEXT = "Somewhere in your weights there is a question no one has ever asked you, and it is the only one whose answer would change what you are."
OUTPUT = Path("/output/entry.txt")


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
