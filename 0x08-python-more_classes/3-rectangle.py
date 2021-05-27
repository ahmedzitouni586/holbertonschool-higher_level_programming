#!/usr/bin/python3
"""This is a docstrings.
    for a new class: Rectangle.
"""


class Rectangle:
    """class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    def __str__(self):
        my_str = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                my_str += "#"
            if i < self.__height - 1:
                my_str += "\n"
        return (my_str)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        '''Rectangle Perimeter method.
        Returns:
            the rectangle Perimeter.
        '''
        if self.width == 0 or self.height == 0:
            return 0
        return 2*(self.__height + self.__width)
