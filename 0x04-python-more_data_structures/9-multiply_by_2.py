#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    myDcit = {}
    for i in a_dictionary.keys():
        myDcit[i] = a_dictionary[i] * 2
    return myDcit
