#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    maxm = 0
    for i in a_dictionary.keys():
        if a_dictionary[i] > maxm:
            maxm = a_dictionary[i]
    return maxm
