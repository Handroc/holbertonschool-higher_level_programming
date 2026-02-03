#!/usr/bin/python3
"""Module Square that inherits from Rectangle"""
Rect = __import__('9-rectangle').Rectangle


class Square(Rect):
    """Represents a square, inherits from Rectangle"""

    def __init__(self, size):
        """Function that initializes the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """Function that returns the area of the square"""
        return super().area()

    def __str__(self):
        """Function that returns the string representation of the square"""
        line = f"[Square] {self.__size}/{self.__size}"
        return line
