#!/usr/bin/python3
"""Module that defines a Rectangle class."""
Geometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(Geometry):
    """Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a Rectangle with validated width and height."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
