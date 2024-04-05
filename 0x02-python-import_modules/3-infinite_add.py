#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    result = 0
    counter = 0
    for i in sys.argv:
        if counter == 0:
            counter += 1
            continue
        result += int(i)

    print("{}".format(result))
