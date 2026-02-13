#!/usr/bin/python3
"""Module for writing a string to a text file."""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns the number of chars."""
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
    return len(text)
