#!/usr/bin/python3
for i in range(0, 9):
    for j in range(1, 10):
        if j <= i:
            continue
        if i == 8 and j == 9:
            print(89)
        else:
            print("{}{}, ".format(i, j), end="")
