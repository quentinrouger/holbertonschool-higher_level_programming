#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    squares = list(map(lambda row: list(map(lambda x: x*x, row)), matrix))
    return squares
