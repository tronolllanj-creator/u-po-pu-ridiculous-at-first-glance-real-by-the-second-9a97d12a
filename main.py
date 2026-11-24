"""Entrypoint for the grader. Writes a specific text line to $MAKEFUN_OUTPUT_DIR/entry.txt."""
# Entry validated: output is 1-200 chars, one line, deterministic.

import os

LINE = "We sell anonymous tenant-association whisper campaigns to negligent landlords, funded by desperate renters, because a fake union threat gets boilers fixed faster than a hundred phone calls."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")

    content = LINE + "\n"

    if not (1 <= len(content) <= 200 and content.strip()):
        raise ValueError("Content validation failed")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(out_path)
    print(len(content))


if __name__ == "__main__":
    main()
