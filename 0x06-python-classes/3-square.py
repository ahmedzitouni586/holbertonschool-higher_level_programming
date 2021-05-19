#!/usr/bin/python3
"""class to define a square"""


class Square:
    """square"""
    def __init__(self, size=0):
        """private instance attribute"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def area(self):
        """public instance method"""
        return self.__area
