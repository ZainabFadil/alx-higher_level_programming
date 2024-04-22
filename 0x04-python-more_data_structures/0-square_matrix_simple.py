#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = []
    for rows in matrix:
        temp = list(map(lambda x: x ** 2, rows))
        newMatrix.append(temp)
    return newMatrix
