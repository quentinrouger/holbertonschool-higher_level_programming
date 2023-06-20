#!/usr/bin/python3
"""
Write a function that returns the list of available attributes \
and methods of an object.
"""


def lookup(obj):
    """
    Returns a list of attributes and methods of the specified object.

    Args:
        obj: The object to inspect.
    """
    return dir(obj)
