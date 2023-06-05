#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = tuple_a[:2] + (0, 0)[:2 - len(tuple_a)]
    tuple_b = tuple_b[:2] + (0, 0)[:2 - len(tuple_b)]
    tup = []
    for i in range(0, len(tuple_a)):
        tup.append(tuple_a[i]+tuple_b[i])
    result = tuple(tup)
    return result
