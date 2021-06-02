#!/usr/bin/python3
"""append text"""


def append_write(filename="", text=""):
    """write a string at the end of the file"""
    with open("filename", mode='a', encoding='UTF8') as ff:
        ff.write(text)
    return len(text)
