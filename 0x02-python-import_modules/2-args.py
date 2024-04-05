#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    counter = len(sys.argv) - 1
    if counter == 0:
        print("0 arguments.")
    elif counter == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(counter))
    it = 0
    for i in sys.argv:
        if it == 0:
            it += 1
            continue
        print("{}: {}".format(it, i))
        it += 1
