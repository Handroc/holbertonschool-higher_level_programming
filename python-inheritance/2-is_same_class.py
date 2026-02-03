#!/usr/bin/python3
"""Module that defines a function to check if an object is a specific class."""


def is_same_class(obj, a_class):
    """Returns True if the object is an instance of the specified class."""
    return type(obj) is a_class
