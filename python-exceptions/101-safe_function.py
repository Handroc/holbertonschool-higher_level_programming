#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        funct = fct(args[0], args[1])
        return funct
    except Exception as ne:
        print("Exception: {}".format(ne), file=sys.stderr)
        return None
