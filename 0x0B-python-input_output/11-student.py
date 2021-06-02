#!/usr/bin/python3
"""class to define a student"""


class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieve info to json format """
        new = {}
        if attrs is None:
            return vars(self)
        else:
            for n in attrs:
                if n in vars(self):
                    new[n] = vars(self)[n]
        return new

    def reload_from_json(self, json):
        vars(self).update(json)
