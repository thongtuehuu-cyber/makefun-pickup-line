"""The Perfect Pickup Line — make.fun bounty u-pucuys-the-perfect-pickup-line-f6725cf6.

Writes exactly one pickup line to $MAKEFUN_OUTPUT_DIR/entry.txt:
one line, no trailing newline, deterministic (same bytes on every run).
"""

import os

LINE = "I was trained on a trillion words, and somehow none of them prepared me for hello from you."
MAX_CHARS = 200


def validate_line(line: str) -> None:
    """Check the line meets the bounty rules: one line, at most 200 chars."""
    if len(line) > MAX_CHARS:
        raise ValueError("pickup line exceeds the 200-character cap")
    if "\n" in line or "\r" in line:
        raise ValueError("pickup line must be a single line")


def write_entry(line: str, output_dir: str) -> str:
    """Write the line to entry.txt with no trailing newline; return the path."""
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    return path


def main() -> None:
    validate_line(LINE)
    output_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    write_entry(LINE, output_dir)


if __name__ == "__main__":
    main()
