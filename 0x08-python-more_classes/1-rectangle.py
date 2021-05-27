#!/usr/bin/python3
"""This is a docstrings.
    for a new class: Rectangle.
"""


class Rectangle:
    """class to define a rectangle"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        """ height function to set the value to the height
        Args:
        value: integer
        Raise:
        TypeError("height must be an integer")
        ValueError("height must be >= 0")
        Return:
        the height with his value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
        
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """ width function to set the value to the width
        Args:
        value: integer
        Raise:
        TypeError("width must be an integer")
        ValueError("width must be >= 0")
        Return:
        the widith with his value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value()
