#!/usr/bin/python3
"""
Write a class MyList that inherits from list.
"""


class MyList(list):
    """
    class that inherits from list.
    """

    def print_sorted(self):
        """
        Function that prints the sorted list.
        """
        sorted_list = []
        sorted_list = sorted(self)
        print(sorted_list)
