from typing import List


#!/usr/bin/python3
"""holberton module"""


class MyList(List):
    """print the list, but sorted"""
    def print_sorted(self):
        print(sorted(self))
