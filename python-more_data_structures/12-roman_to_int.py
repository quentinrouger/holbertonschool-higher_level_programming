#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    prev_value = 0
    for key in reversed(roman_string):
        if dict[key] < prev_value:
            sum -= dict[key]
        else:
            sum += dict[key]
        prev_value = dict[key]
    return sum
