#!/usr/bin/python3
""" define a Rectagle class"""
from models.base import Base


class Rectangle(Base):
    """class constractor"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """setter"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        """getter"""
        return self.__height
    
    @height.setter
    def height(self, height):
        """setter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        """ return the area of the rectangle"""
        return self.height * self.width

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for y in range(self.__y):
            print()
        for height in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for width in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """return rectangle details"""
        R = "[Rectangle] {} {}/{}".format(self.id, self.x, self.y)
        return R + "- {}/{}".format(self.width, self.height)

