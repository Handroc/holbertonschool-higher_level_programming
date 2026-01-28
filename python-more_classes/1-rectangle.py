#!/usr/bin/python3
"""Rectangle"""


class Rectangle:
    """Class that initializes a rectangle"""
    def __init__(self, width=0, height=0):
        """Function that initializes the rectangle."""
        msg_err_int = "width must be an integer"
        msg_err_neg = "width must be >= 0"
        if not (isinstance(width, int)):
            raise TypeError(msg_err_int)
        if width < 0:
            raise ValueError(msg_err_neg)
        self.__width = width
        msg_err_int = "height must be an integer"
        msg_err_neg = "height must be >= 0"
        if not (isinstance(height, int)):
            raise TypeError(msg_err_int)
        if height < 0:
            raise ValueError(msg_err_neg)
        self.__height = height
    
    @property
    def width(self):
        """Returns the width of the rectangle."""
        return self.__width
    
    @property
    def height(self):
        """Returns the height of the rectangle."""
        return self.__height
    
    @width.setter
    def width(self, value):
        """Function that sets the width of the rectangle."""
        msg_err_int = "width must be an integer"
        msg_err_neg = "width must be >= 0"
        if not (isinstance(value, int)):
            raise TypeError(msg_err_int)
        if value < 0:
            raise ValueError(msg_err_neg)
        self.__width = value
    
    @height.setter
    def height(self, value):
        """Function that sets the height of the rectangle."""
        msg_err_int = "height must be an integer"
        msg_err_neg = "height must be >= 0"
        if not (isinstance(value, int)):
            raise TypeError(msg_err_int)
        if value < 0:
            raise ValueError(msg_err_neg)
        self.__height = value
