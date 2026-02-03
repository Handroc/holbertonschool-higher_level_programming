#!/usr/bin/python3
"""Module that defines a Rectangle class with area and string output."""
Geometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(Geometry):
    """Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a Rectangle with validated width and height."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__height * self.__width

    def __str__(self):
        """Return the string representation of the rectangle."""
        string = f"[Rectangle] {self.__width}/{self.__height}"
        return string
