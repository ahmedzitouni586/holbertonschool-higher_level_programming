#!/usr/bin/python3
"""Write to a file"""


def write_file(filename="", text=""):
    """write a string and return the number of characters"""
    with open("filename", encoding="UTF8") as ff:
        return ff.write(text)
