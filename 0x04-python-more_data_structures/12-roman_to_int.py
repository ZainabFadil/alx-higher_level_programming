#!/usr/bin/python3
def roman_to_int(roman_string):
    flag = 1
    myDcit = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sum = 0
    for i in range (len(roman_string)):
        if not flag:
            flag = 1
            continue

        sum += myDcit[roman_string[i]]
        
        if roman_string[i] == "I":
            if roman_string[i+1] == "X" or roman_string[i+1] == "V":
                sum += myDcit[roman_string[i+1]]
                sum -= 1
                flag = 0
    return sum
print (roman_to_int("XI"))