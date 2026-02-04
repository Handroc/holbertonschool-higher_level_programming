#!/usr/bin/python3
"""Module that defines a helper to add attributes to objects."""


def add_attribute(a_class, attribute, newattr):
    """Add a new attribute to an object if possible, else raise TypeError."""
    if not hasattr(a_class, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(a_class, attribute, newattr)
