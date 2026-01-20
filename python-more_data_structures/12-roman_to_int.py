#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or not roman_string:
        return 0
    ro_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if len(roman_string) == 1:
        return ro_dict[roman_string]
    num = 0
    for i in range(1, len(roman_string)):
        if ro_dict[roman_string[i]] <= ro_dict[roman_string[i - 1]]:
            num += ro_dict[roman_string[i - 1]]
        else:
            num -= ro_dict[roman_string[i - 1]]
    num += ro_dict[roman_string[-1]]
    return num
