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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ write json string representation of list_objs """
        fname = cls.__name__ + ".json"
        with open(fname, "w") as ff:
            if list_objs is None:
                ff.write("[]")
            else:
                list = []
                for obj in list_objs:
                    list.append(obj.to_dictionary())
                ff.write(cls.to_json_string(list))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return (json.loads(json_string))
 
