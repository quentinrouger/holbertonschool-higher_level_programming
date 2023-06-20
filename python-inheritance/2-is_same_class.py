#!/usr/bin/python3
"""
Write a function that returns True if the object is \
exactly an instance of the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """
    Args:
    - obj : An object to be checked.
    - a_class : A class or type to compare against.

    Return: True if the object belongs to the specified class, False otherwise.
    """
    return type(obj) is a_class
