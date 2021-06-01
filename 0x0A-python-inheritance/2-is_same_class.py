#!/usr/bin/python3
"""holberton module"""


def is_same_class(obj, a_class):
    """check if the object is exactly an instance of that class"""
    if type(obj) is a_class:
        return True
    else:
        return False
