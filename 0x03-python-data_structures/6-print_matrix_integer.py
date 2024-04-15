#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        for pos in rows:
            print("{}".format(pos), end=" ")
        print("")
