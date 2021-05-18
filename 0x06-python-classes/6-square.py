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
            self._size = size
    @property
    def size(self):
        """define size as a property"""
        return self._size
    @size.setter
    def size(self, value):
        """sit the value of size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = value
    def area(self):
        """returns the square"""
        result = self._size * self._size
        return result
    def my_print(self):
        """print #"""
        if self._size == 0:
            print("")
        for i in range(self._size):
            for j in range(self._size):
                print("#", end="")
            print("")
        else:
            for i in range(self._position[1]):
                print("")
            for n in range(self._size):
                for j in range(self._position[0]):
                    print(" ", end="")
                for k in range(self.size):
                    print("#", end="")
                print("")
