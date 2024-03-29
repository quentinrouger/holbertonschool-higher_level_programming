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

    def update(self, *args, **kwargs):
        """
        Update the class Square.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            self.id = kwargs.get('id', self.id)
            self.size = kwargs.get('size', self.size)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Square.
        """
        return {'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
