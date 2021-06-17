#!/usr/bin/python3
""" module to define rectangle class """


class Rectangle:
    """ define rectangle class """
    def __init__(self, width=0, height=0):
        """ Instantiation class """
        self.width = width
        self.height = height

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """ return area of the rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ return perimeter of the rectangle """
        if self.__height == 0 or self.__width:
            return 0
        return 2*(self.__width + self.__height)
