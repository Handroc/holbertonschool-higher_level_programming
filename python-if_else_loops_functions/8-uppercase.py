#!/usr/bin/python3
def uppercase(str):
    print(''.join(chr(ord(i) - 32) if ord(i) in range(ord('a'), ord('z') + 1) else i for i in str))
