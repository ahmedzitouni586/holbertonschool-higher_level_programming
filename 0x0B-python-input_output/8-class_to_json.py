#!/usr/bin/python3
"""manipulate files"""
import json


def class_to_json(obj):
    """return dictionary description with simple data structure """
    return vars(obj)
