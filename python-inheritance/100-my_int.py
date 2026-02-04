#!/usr/bin/python3
"""Module that defines an inheritance checker."""


class MyInt(int):
    """Class that inherits from int and inverts == and != operators."""
    def __init__(self, integer):
        """Function to initialize the MyInt class."""
        self.integer = integer

    def __eq__(self, other):
        """Invert the equality operator."""
        return not (self.integer == other)

    def __ne__(self, other):
        """Invert the inequality operator."""
        return not (self.integer != other)

    def __str__(self):
        """String representation of the MyInt object."""
        return f"{self.integer}"
