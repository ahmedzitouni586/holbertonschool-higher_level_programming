#!/usr/bin/python3
""" module to define rectangle class """


class Rectangle:
    """ define rectangle class """
    def __init__(self, width=0, height=0):
        """ Instantiation class """
        self.__width = width
        self.__height = height

    @property
    def height(self):
        """ height getter """
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
        the widith with his value
        """
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
        """ width function to set the value to the width
        Args:
        value: integer
        Raise:
        TypeError("width must be an integer")
        ValueError(" width must be >= 0")
        Return:
        the widith with his value
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
