#!/usr/bin/python3
"""This is a docstrings.
    for a new class: Rectangle.
"""


class Rectangle:
    '''this is an empty class
        that defines a Rectangle
    '''
    def __init__(self, width=0, height=0):
        '''Method:
        Args:
            width: width of a Rectangle
            height: height Of a Rectangle
        '''
        self.__height = height
        self.__width = width

    @property
    def height(self):
        '''Property for the height of the Rectangle
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''Method:
        Args:
            value: height of a Rectangle
        raises:
            ValueError: height must be >= 0
            TypeError: height must be an integer
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        '''Property for the width of the Rectangle
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''Method:
        Args:
            width: width of a Rectangle
            height: height Of a Rectangle
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        '''Rectangle area method.
        Returns:
            the rectangle area.
        '''
        return self.__height * self.__width

    def perimeter(self):
        '''Rectangle Perimeter method.
        Returns:
            the rectangle Perimeter.
        '''
        if self.width == 0 or self.height == 0:
            return 0
        return 2*(self.__height + self.__width)
