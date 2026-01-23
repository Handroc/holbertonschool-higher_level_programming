#!/usr/bin/python3
"""
Docstring for 4-print_square.py
"""


def print_square(size):
    """
    Docstring for print_square
    :param size: size of the square
    """
    err_msg = "size must be an integer"
    err_msg_neg = "size must be >= 0"
    if type(size) is not int:
        raise TypeError(err_msg)
    if size < 0:
        if type(size) is float:
            raise TypeError(err_msg)
        raise ValueError(err_msg_neg)
    for i in range(size):
        print("#" * size)
