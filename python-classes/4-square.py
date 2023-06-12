#!/usr/bin/python3
"""Write a class Square that defines a square by :
Private instance attribute: size
"""


class Square:
    """class that defines a square"""
    def __init__(self, size=0):
        """Initializes a Square instance."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area of the square"""
        return self.__size ** 2
