#!/usr/bin/python3
import sys

if __name__ == "__main__":
    i = len(sys.argv) - 1
    sum = 0
    for j in range(1,i + 1):
        num = int(sys.argv[j])
        sum += num
    print("{0}".format(sum))