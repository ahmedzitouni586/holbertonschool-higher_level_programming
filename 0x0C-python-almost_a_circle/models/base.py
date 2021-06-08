#!/usr/bin/python3
""" define a Base class"""
import json


class Base():
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return the JSON string representation of the list"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation to a file"""
        file = cls.__name__ + ".json"
        with open(file, 'w', encoding="UTF-8") as jsonfile:
            if list_objs is None:
                list_objs = []
            dic = [i.to_dictionary() for i in list_objs]
            jsonfile.write(cls.to_json_string(dic))

    @classmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation """
        json_object = json.loads(json_string)
        if json_string is None or json_string == []:
            return []
        return json_object

    @classmethod
    def create(cls, **dictionary):
        """ Return an instances """
        if cls.__name__ == "Rectangle":
            dummy = cls(5, 5)
        else:
            dummy = cls(5)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Return a file containt a json list """
        file = cls.__name__ + ".json"
        try:
            with open(file, 'r', encoding="UTF-8") as jsonfile:
                dic = Base.from_json_string(jsonfile.read())
        except IOError:
            return []
        return[cls.create(**item) for item in dic]
