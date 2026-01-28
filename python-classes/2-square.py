#!/usr/bin/python3
"""
Docstring for 0-square.py
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
