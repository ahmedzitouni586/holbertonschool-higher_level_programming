#!/usr/bin/python3
""" Square Module  """


class Square:
    """ class Square """
    def __init__(self, size=0):
        """ class initialization """
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """ size getter """
        return self.__size

    @size.setter
    def size(self, value):
        """ size setter """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ returns the area of the square """
        return self.__size**2

    def my_print(self):
        """ draw square """
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
                print()
        if self.__size == 0:
            print()
