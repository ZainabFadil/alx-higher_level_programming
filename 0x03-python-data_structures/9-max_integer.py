#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        maxm = my_list[0]
        for i in my_list:
            if i > maxm:
                maxm = i
        return maxm
    else:
        return None