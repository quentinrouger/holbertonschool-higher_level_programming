#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_list_unordered(self):
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)

    def test_float_list(self):
        self.assertEqual(max_integer([1.2, 4.1, 3.6, 2.2]), 4.1)


if __name__ == '__main__':
    unittest.main()
