#!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in str:
        if ord(i) in range(ord('a'), ord('z') + 1):
            result += "{0}".format(chr(ord(i) - 32))
        else:
            result += "{0}".format(i)
    print("{0}".format(result))
