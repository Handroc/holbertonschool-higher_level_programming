#!/usr/bin/python3
import sys

if __name__ == "__main__":
	i = len(sys.argv) - 1
	j = 1
	if i == 0:
		print("{0} arguments.".format(i))
	else:
		print("{0} arguments:".format(i))
		for j in range(1, i + 1):
			print("{0}: {1}".format(j, sys.argv[j]))
