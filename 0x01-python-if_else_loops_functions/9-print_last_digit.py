#!/usr/bin/python3
def print_last_digit(number):
    x = abs(number)
    x %= 10
    print(x, end="")
    return (x)
