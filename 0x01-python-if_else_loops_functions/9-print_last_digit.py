#!/usr/bin/python3
def print_last_digit(number):
    num = abs(number) % 10
    if (number) < 0:
        num *= -1
    print("{}".format(num), end="")
    return (num)
