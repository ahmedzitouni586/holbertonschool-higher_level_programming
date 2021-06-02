#!/usr/bin/python3
"""append text"""


def append_write(filename="", text=""):
    """ writes a string at the end of a text file"""
    with open(filename, "a+", encoding="UTF8") as ff:
        ff.write(text)
        return len(text)