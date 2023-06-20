#!/usr/bin/python3
"""
Write a function that returns True if the object is an instance of aclass that\
inherited (directly or indirectly) from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Args:
    - obj : An object to be checked.
    - a_class : A class or type to compare against.

    Return: True if the object is an instance of a class.
            Otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
