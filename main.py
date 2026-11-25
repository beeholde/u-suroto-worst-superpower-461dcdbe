"""Worst Superpower entry: write the one-line invention to /output/entry.txt."""

import os
import sys

LINE = "I can translate any sign into the language it's already written in — an EXIT sign, word for word: EXIT."


def check_line(text):
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        raise ValueError("entry must not hold control characters")
    if not 1 <= len(text) <= 140:
        raise ValueError("entry must be 1 to 140 characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text.encode("utf-8").decode("utf-8")


def main():
    payload = check_line(LINE).encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as handle:
        handle.write(payload)
    return 0


if __name__ == "__main__":
    sys.exit(main())
