#!/usr/bin/python3
"""number of characters"""


def write_file(filename="", text=""):
    """Write a string to a file and returns number of characters"""
    with open(filename, 'w', encoding="UTF8") as ff:
        return ff.write(text)
