#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    for score, weight in my_list:
        sum_1 += score * weight
        sum_2 += weight
    return sum_1 / sum_2
