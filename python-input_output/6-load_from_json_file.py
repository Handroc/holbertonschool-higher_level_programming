#!/usr/bin/python3
"""Module for loading objects from JSON files."""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file."""
    with open(filename, 'r', encoding='utf-8') as f:
        x = json.load(f)
    return x
