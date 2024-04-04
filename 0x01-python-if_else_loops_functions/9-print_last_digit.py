#!/usr/bin/python3
def print_last_digit(number):
    x = abs(number) % 10
    if number < 0:
        x *= -1
    return (x)
