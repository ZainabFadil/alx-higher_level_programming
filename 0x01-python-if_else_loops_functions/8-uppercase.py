#!/usr/bin/python3
def uppercase(str):
    newStr = ""
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            newStr.append(chr(ord(i) - 32))
        else:
            newStr.append(i)
    return newStr
