def no_c(my_string):
    temp = ""
    for i in my_string:
        if i != 'C' and i != 'c':
            temp += i
    return temp
