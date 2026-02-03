#!/usr/bin/python3
"""Module Square that inherits from Rectangle"""
Rect = __import__('9-rectangle').Rectangle


class Square(Rect):
    """Represents a square, inherits from Rectangle"""
    def __init__(self, size):
        """Function that initializes the square"""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Function that returns the area of the square"""
        return super().area()
