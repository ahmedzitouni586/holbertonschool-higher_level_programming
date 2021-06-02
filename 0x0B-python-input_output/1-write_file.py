#!/usr/bin/python3
"""manipulate files"""


def write_file(filename="", text=""):
    """function to write in a file"""
    with open("filename", encoding="UTF8") as ff:
        return ff.write(text)
