#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.
    :param matrix: list of lists of integers/floats
    :param div: number to divide by
    :return: new matrix with divided values
    """
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    row_len = len(matrix[0])
    new_matrix = []
    for i in matrix:
        if len(i) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        part_matrix = []
        for j in i:
            if type(j) not in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            part_matrix.append(round(j / div, 2))
        new_matrix.append(part_matrix)
    return new_matrix
