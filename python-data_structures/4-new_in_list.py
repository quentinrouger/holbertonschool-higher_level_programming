#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if idx not in range(0, len(new_list)):
        return new_list
    else:
        my_list[idx] = element
        return my_list
