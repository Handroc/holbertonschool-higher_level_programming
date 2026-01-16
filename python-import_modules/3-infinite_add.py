#!/usr/bin/python3
import sys
i = len(sys.argv) - 1
sum = 0
for j in range(1,i + 1):
    num = int(sys.argv[j])
    sum += num
print(f"{sum}")
