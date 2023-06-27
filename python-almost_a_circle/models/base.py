#!/usr/bin/python3
"""
class Base.
"""
import json


class Base:
    """
    This class will be the “base” of all other classes in this project.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation \
              of list_dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation \
            of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            json_data = cls.to_json_string([obj.to_dictionary()
                                            for obj in list_objs])
        else:
            json_data = "[]"
        with open(filename, "w") as file:
            file.write(json_data)

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string.
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
