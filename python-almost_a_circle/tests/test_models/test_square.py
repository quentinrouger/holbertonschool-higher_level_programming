#!/usr/bin/python3
"""
Unittests for Rectangle
"""
import unittest

from models.square import Square
from models.base import Base


class SquareTestCase(unittest.TestCase):
    def test_init(self):
        # Test case for __init__ method
        square_obj = Square(5)
        #self.assertEqual(square_obj.id, 1)
        self.assertEqual(square_obj.size, 5)
        self.assertEqual(square_obj.x, 0)
        self.assertEqual(square_obj.y, 0)

    def test_str(self):
        # Test case for __str__ method
        square_obj = Square(5, 2, 3, 1)
        self.assertEqual(str(square_obj), "[Square] (1) 2/3 - 5")

    def test_size_property(self):
        # Test case for size property
        square_obj = Square(5)
        square_obj.size = 10
        self.assertEqual(square_obj.size, 10)
        self.assertEqual(square_obj.width, 10)
        self.assertEqual(square_obj.height, 10)

    def test_update(self):
        # Test case for update method
        square_obj = Square(5, 2, 3, 1)
        square_obj.update(2, 10, 4, 5)
        self.assertEqual(square_obj.id, 2)
        self.assertEqual(square_obj.size, 10)
        self.assertEqual(square_obj.x, 4)
        self.assertEqual(square_obj.y, 5)

    def test_to_dictionary(self):
        # Test case for to_dictionary method
        square_obj = Square(5, 2, 3, 1)
        dictionary = square_obj.to_dictionary()
        self.assertEqual(dictionary, {'id': 1, 'size': 5, 'x': 2, 'y': 3})


if __name__ == '__main__':
    unittest.main()
