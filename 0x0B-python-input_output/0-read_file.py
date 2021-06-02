#!/usr/bin/python3
"""manipulate files"""


def read_file(filename=""):
    """function to read file"""
    with open("filename", encoding="UTF8") as myFile:
        print(myFile.read(), end="")
