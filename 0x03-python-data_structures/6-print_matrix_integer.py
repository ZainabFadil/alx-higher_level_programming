#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        for pos in range(len(rows)):
            if pos != len(rows) - 1:
                print("{:d}".format(rows[pos]), end=" ")
            else:
                print("{:d}".format(rows[pos]), end="")
        print("")
