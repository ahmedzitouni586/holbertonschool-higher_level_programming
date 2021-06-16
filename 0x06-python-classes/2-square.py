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
