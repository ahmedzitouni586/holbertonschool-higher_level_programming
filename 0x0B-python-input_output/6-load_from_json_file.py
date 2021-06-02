#!/usr/bin/python3
"""manipulate files"""
import json


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”"""
    with open(filename, "r", encoding="UTF-8") as ff:
        return json.load(ff)
