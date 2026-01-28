#!/usr/bin/python3
"""
Square
"""


class Square:
    """Class that defines a square by size"""
    def __init__(self, size=0):
        """Function that initializes the size.
        
        Args:
            size (int, optional): Defaults to 0
                size of the square
        """
        msg_err = "size must be an integer"
        msg_err_size = "size must be >= 0"
        if type(size) is not int:
            raise TypeError(msg_err)
        if size < 0:
            raise ValueError(msg_err_size)
        self.__size = size
