#!/usr/bin/python3
"""
Unittests for Rectangle
"""
import unittest

from models.rectangle import Rectangle


class testbase(unittest.TestCase):
    """Class test rectangle"""

    def test_invalid_arg_type(self):
        """Invalid argument type"""
        self.assertRaises(TypeError, Rectangle, 1, "2")

        self.assertRaises(TypeError, Rectangle, "1", 2)

        self.assertRaises(TypeError, Rectangle, "1", "2")

        self.assertRaises(TypeError, Rectangle, 1, 2, "3")

        self.assertRaises(TypeError, Rectangle, 1, 2, 3, "4")

        """Invalid argument Value"""
        self.assertRaises(ValueError, Rectangle, -1, 2)

        self.assertRaises(ValueError, Rectangle, 1, -2)

        self.assertRaises(ValueError, Rectangle, 0, 2)

        self.assertRaises(ValueError, Rectangle, 1, 0)

        self.assertRaises(ValueError, Rectangle, 1, 2, -3)

        self.assertRaises(ValueError, Rectangle, 1, 2, 3, -4)


if __name__ == '__main__':
    unittest.main()
