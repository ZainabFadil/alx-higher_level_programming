#!/usr/bin/python3
def no_c(my_string):
    punctuation = str.maketrans("", "", "Cc")
    new_string = my_string.translate(punctuation)
    return new_string
