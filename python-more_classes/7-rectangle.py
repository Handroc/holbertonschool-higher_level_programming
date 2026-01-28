#!/usr/bin/python3
"""Rectangle"""


class Rectangle:
    """Class that initializes a rectangle and the number of instances"""
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Function that returns the area of the rectangle."""
        return self.__height * self.__width

    def perimeter(self):
        """Function that returns the perimeter of the rectangle."""
        if self.__height == 0 or self.__width == 0:
            return 0
        return self.__height * 2 + self.__width * 2

    def __str__(self):
        """Function that prints the rectangle with the character #"""
        if self.__height == 0 or self.__width == 0:
            return ""
        rect = ""
        for i in range(self.__height):
            rect += Rectangle.print_symbol * self.__width
            if i != self.__height - 1:
                rect += "\n"
        return rect

    def __repr__(self):
        """Function that returns a string representation of the rectangle."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Function that prints a string when an instance is being deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
