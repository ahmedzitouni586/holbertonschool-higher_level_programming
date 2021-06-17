#!/usr/bin/python3
""" module to define rectangle class """


class Rectangle:
    """ define rectangle class """
    def __init__(self, width=0, height=0):
        """ Instantiation class """
        self.width = width
        self.height = height

    def __str__(self):
        my_string = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                my_string += "#"
            if i < self.__height - 1:
                my_string += "\n"
        return (my_string)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")

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
        if self.height == 0 or self.width == 0:
            return 0
        return 2*(self.__width + self.__height)
