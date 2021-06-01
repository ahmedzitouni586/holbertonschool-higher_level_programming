from typing import List


#!/usr/bin/python3
"""holberton module"""


class MyList(list):
    """class MyList"""
    def print_sorted(self):
        """print a sorted list"""
        print(sorted(self))