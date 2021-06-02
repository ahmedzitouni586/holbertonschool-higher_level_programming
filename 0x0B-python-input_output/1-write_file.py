#!/usr/bin/python3
"""manipulate files"""


def write_file(filename="", mode='w', text=""):
    """function to write in a file"""
    with open("filename", encoding="utf-8") as ff:
        ff.write(text)
    return len(text)
