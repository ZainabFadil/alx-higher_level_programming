#!/usr/bin/python3
def print_last_digit(number):
    flag = 0
    num = abs(number) % 10
    x = num
    if (number) < 0:
        num *= -1
        flag = 1
    print("{}".format(num), end="")
    return (x)

