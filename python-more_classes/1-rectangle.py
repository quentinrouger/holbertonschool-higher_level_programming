#!/usr/bin/python3
"""
Write a class Rectangle that defines a rectangle by:
Private instance attribute: width.
Private instance attribute: height.
"""


class Rectangle:
    """class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance."""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
