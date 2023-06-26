#!/usr/bin/python3
"""
class Square.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square that inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Class constructor.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Method that tells how to print Square.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.
                                                 width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size
