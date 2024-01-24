#!/usr/bin/python3
def safe_print_division(a, b):
    ret = 1
    try:
        x = a / b
        ret = x
    except (ZeroDivisionError, TypeError):
        ret = None
    finally:
        print("Inside result: {}".format(ret))
        if ret:
            return x
        else:
            return None
