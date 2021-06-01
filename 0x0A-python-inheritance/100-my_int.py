#!/usr/bin/python3
"""Holberton Module"""


class MyInt(int):
    """define Myint class"""
    def __eq__(self, other):
        return not super().__eq__(other)

    def __ne__(self, other):
        return not super().__ne__(other)
