#!/usr/bin/python3
"""
Write a class Student that defines a student by:
Public instance attributes: first_nam, last_name, age.
"""


class Student:
    """
    Class that defines a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a student object.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            my_dict = {}
            for element in attrs:
                if element in self.__dict__:
                    my_dict[element] = self.__dict__[element]
            return my_dict

    def reload_from_json(self, json):
        for key in json:
            self.__dict__[key] = json[key]
