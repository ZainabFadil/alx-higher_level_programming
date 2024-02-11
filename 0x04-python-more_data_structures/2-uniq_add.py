#!/usr/bin/python3
def uniq_add(my_list=[]):
    mySet = set(my_list)
    sum = 0
    for item in mySet:
        sum += item
    return sum
