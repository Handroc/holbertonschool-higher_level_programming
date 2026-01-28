#!/usr/bin/python3
"""
Square
"""


class Square:
    """Class that defines a square by size"""
    def __init__(self, size=0):
        """Function that initializes the size"""
        msg_err = "size must be an integer"
        msg_err_size = "size must be >= 0"
        if type(size) is not int:
            raise TypeError(msg_err)
        if size < 0:
            raise ValueError(msg_err_size)
        self.__size = size

    @property
    def size(self):
        """Returns the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.
        :param value: size value
        """
        msg_err = "size must be an integer"
        msg_err_size = "size must be >= 0"
        if type(value) is not int:
            raise TypeError(msg_err)
        if value < 0:
            raise ValueError(msg_err_size)
        self.__size = value

    def area(self):
        """Calculates the area of the square."""
        return self.__size ** 2
