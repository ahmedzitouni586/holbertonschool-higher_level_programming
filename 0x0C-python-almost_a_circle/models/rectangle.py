#!/usr/bin/python3
"""module to define rectangle class"""
from models.base import Base


class Rectangle(Base):
    """ define rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ width getter"""
        return self.__width

    @property
    def height(self):
        """ height getter """
        return self.__height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @property
    def y(self):
        """ y getter"""
        return self.__y

    @width.setter
    def width(self, name):
        """ width setter"""
        if type(name) is not int:
            raise TypeError("width must be an integer")
        if name <= 0:
            raise ValueError("width must be > 0")
        self.__width = name

    @height.setter
    def height(self, name):
        """ height setter """
        if type(name) is not int:
            raise TypeError("height must be an integer")
        if name <= 0:
            raise ValueError("height must be > 0")
        self.__height = name

    @x.setter
    def x(self, name):
        """ x setter """
        if type(name) is not int:
            raise TypeError("x must be an integer")
        if name < 0:
            raise ValueError("x must be >= 0")
        self.__x = name

    @y.setter
    def y(self, name):
        """ y setter """
        if type(name) is not int:
            raise TypeError("y must be an integer")
        if name < 0:
            raise ValueError('y must be >= 0')
        self.__y = name

    def area(self):
        """ define rectngle are """
        return self.__height * self.__width

    def display(self):
        """Print the Rectangle with the # character"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width - 1)]
            print("#")

    def __str__(self):
        """ return rectangle details """
        R = "[Rectangle] ({}) {}/{}".format(self.id, self.__x, self.__y)
        R += "- {}/{}".format(self.__width, self.__height)
        return R

    def update(self, *args):
        """ assigns an argument to each attribute """
        if args and len(args) != 0:
            try:
                if args[0] is not None:
                    self.id = args[0]
            except IndexError:
                return
            try:
                if args[1] is not None:
                    self.width = args[1]
            except IndexError:
                return
            try:
                if args[2] is not None:
                    self.height = args[2]
            except IndexError:
                return
            try:
                if args[3] is not None:
                    self.x = args[3]
            except IndexError:
                return
            try:
                if args[4] is not None:
                    self.x = args[4]
            except IndexError:
                return