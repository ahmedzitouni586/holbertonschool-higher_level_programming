#!/usr/bin/python3
"""manipulate files"""
import json


def from_json_string(my_str):
    """function that returns an object\
    (Python data structure) represented by a JSON string"""
    json.loads(my_str)
