#!/usr/bin/python3
import sys
i = len(sys.argv) - 1
j = 1
if i == 0:
    print(f"{i} arguments.")
else:
    print(f"{i} arguments:")
    for j in range(1,i + 1):
        print(f"{j}: {sys.argv[j]}")
