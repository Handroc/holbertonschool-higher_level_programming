#!/usr/bin/python3
"""Module for appending a string to a text file."""


def append_write(filename="", text=""):
    """Appends a string to a text file and returns the number of chars."""
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)
    return len(text)
