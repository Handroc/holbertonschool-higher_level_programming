#!/usr/bin/python3
"""Module that defines BaseGeometry with an abstract area method."""


class BaseGeometry:
    """BaseGeometry class with an abstract area method."""

    def area(self):
        """Raise an exception because area is not implemented."""
        raise Exception("area() is not implemented")
