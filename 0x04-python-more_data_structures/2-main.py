#!/usr/bin/python3
uniq_add = __import__('2-uniq_add').uniq_add

my_list = [10, 11, 10, 4]
result = uniq_add(my_list)
print("Result: {:d}".format(result))
