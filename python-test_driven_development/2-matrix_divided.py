#!/usr/bin/python3
"""
Docstring for 2-matrix_divided
"""


def matrix_divided(matrix, div):
    """
    Docstring for matrix_divided
    Divides all elements of a matrix.
    :param matrix: list of lists of integers/floats
    :param div: number to divide by
    :return: new matrix with divided values
    """
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    err_msg_size = "Each row of the matrix must have the same size"
    err_msg_div = "div must be a number"
    err_msg_zero = "division by zero"
    if type(div) not in (int, float):
        raise TypeError(err_msg_div)
    if div == 0:
        raise ZeroDivisionError(err_msg_zero)
    row_len = len(matrix[0])
    new_matrix = []
    for i in matrix:
        if len(i) != row_len:
            raise TypeError(err_msg_size)
        part_matrix = []
        for j in i:
            if type(j) not in (int, float):
                raise TypeError(err_msg)
            part_matrix.append(round(j / div, 2))
        new_matrix.append(part_matrix)
    return new_matrix
