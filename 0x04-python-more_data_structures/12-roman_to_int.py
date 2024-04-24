#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0

    myDcit = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    n = len(roman_string)
    i = n - 1
    sum = 0
    while i >= 0:
        if i < n - 1 and myDcit[roman_string[i]] < myDcit[roman_string[i+1]]:
            sum -= myDcit[roman_string[i]]
        else:
            sum += myDcit[roman_string[i]]
        i -= 1
    return sum
