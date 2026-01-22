#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        return fct(args[0], args[1])
    except Exception as ne:
        print("Exception: {}".format(ne), file=sys.stderr)
        return None
