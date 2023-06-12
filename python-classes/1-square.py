#!/usr/bin/python3
"""Write a class Square that defines a square by
Private instance attribute: size
"""


class Square:
    """class that defines a square"""
    def __init__(self, size=None):
        """Initializes a Square instance."""
        self.__size = size
