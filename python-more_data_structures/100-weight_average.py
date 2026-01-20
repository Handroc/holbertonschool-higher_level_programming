#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum = 0
    weight = 0
    for i in my_list:
        if type(i[0]) is int and type(i[0]) is type(i[1]):
            sum += i[0] * i[1]
            weight += i[1]
    avg = sum / weight
    return avg
