#!/usr/bin/python3
"""manipulate files"""


def append_write(filename="", text=""):
    """write a string at the end of the file"""
    with open("filename", mode='a', encoding='UTF-8') as ff:
        ff.write(text)
    return len(text)
