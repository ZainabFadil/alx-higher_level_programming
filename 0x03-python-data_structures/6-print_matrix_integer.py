#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        for elem in rows:
            print("{:d}".format(elem), end=" ")
        print()