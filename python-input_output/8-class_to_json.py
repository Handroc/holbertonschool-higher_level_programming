#!/usr/bin/python3
"""Module for exposing class dictionaries for JSON serialization."""


def class_to_json(obj):
    """Returns the dictionary description of a simple data structure."""
    return obj.__dict__
