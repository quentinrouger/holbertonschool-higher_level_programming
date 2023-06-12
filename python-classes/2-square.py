#!/usr/bin/python3
"""Write a class Square that defines a square by
Private instance attribute: size
"""


class Square:
    """class that defines a square"""
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
