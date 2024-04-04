#!/usr/bin/python3
def uppercase(str):
    newStr = ""
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            newStr += (chr(ord(i) - 32))
        else:
            newStr += (i)
    print("{}".format(newStr))
