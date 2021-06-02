#!/usr/bin/python3
"""manipulate files"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object\
    to a text file, using a JSON representation"""
    with open(filename, "w", encoding="UTF-8") as ff:
        return json.dump(my_obj, filename)
