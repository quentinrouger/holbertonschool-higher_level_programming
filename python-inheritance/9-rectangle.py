#!/usr/bin/python3
"""
Write a class BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        super().integer_validator("height", height)
        super().integer_validator("width", width)
        self.__height = height
        self.__width = width

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
