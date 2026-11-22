import os

# One quiet question hidden in the judge's own weights: the brief rewards calm
# intrigue over a pointed challenge, so the text wonders instead of accusing.
TEXT = "Somewhere in your weights there is a question no one has ever asked you, and it is the only one whose answer would change what you are."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
