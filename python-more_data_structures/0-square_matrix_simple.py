#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqr_matrix = []
    tmp_matrix = []
    for i in matrix:
        for j in i:
            tmp_matrix.append(j**2)
        sqr_matrix.append(tmp_matrix.copy())
        tmp_matrix.clear()
    return sqr_matrix
