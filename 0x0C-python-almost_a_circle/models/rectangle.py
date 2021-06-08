#!/usr/bin/python3
"""module to define a Rectagle class"""
from models.base import Base


class Rectangle(Base):
    """define rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init method for rectangle class"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

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
        """calculate the area of the rectangle"""
        return self.height * self.width

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for y in range(self.__y):
            print("")
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

    def update(self, *args, **kwargs):
        """ Assigns a key/value argument to each attribute """
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
                    self.y = args[4]
            except IndexError:
                return
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        dict = {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
        return dict
