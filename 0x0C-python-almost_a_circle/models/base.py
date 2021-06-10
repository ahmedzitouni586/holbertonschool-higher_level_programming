#!/usr/bin/python3
"""module to define Base class"""
import json


class Base:
    """define Base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        """class constructor"""
        if id  is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ returns the JSON string representation """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
