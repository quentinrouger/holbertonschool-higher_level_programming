#!/usr/bin/python3
"""
Write a function that returns an object (Python data structure) \
reprensented by a JSON string.
"""
import json


def from_json_string(my_str):
    """
    function that returns an object
    """
    return json.loads(my_str)
