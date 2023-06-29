#!/usr/bin/python3
"""
Unittests for Base
"""
import os
import unittest

from models.base import Base


class testbase(unittest.TestCase):
    """Class test base"""

    def test_id(self):
        base = Base()
        self.assertEqual(base.id, 1)

    def test_id_pass(self):
        base = Base(89)
        self.assertEqual(base.id, 89)

    def test_none(self):
        base = Base()
        self.assertEqual(base.to_json_string([]), '[]')

    def test_from_none(self):
        self.assertEqual(Base.from_json_string('[]'), [])


if __name__ == '__main__':
    unittest.main()
