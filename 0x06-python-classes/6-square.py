#!/usr/bin/python3
""" Square Module  """


class Square:
    """ class Square """
    def __init__(self, size=0, position=(0, 0)):
        """ class initialization """
        self.__size = size
        self.position = position

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

    @property
    def position(self):
        """ position getter """
        return self.__position

    @position.setter
    def position(self, value):
        """ position setter """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
           raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ returns the area of the square """
        return self.__size**2

    def my_print(self):
        """ Prints the square """
        if self.size > 0:
            if self.position[1] > 0:
                print("\n" * self.position[1], end="")
            for i in range(self.size):
                if self.position[0] > 0:
                    print(" " * self.position[0], end="")
                print("#" * self.size)
        else:
            print(end="\n")
