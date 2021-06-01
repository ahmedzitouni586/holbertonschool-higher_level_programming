#!/usr/bin/python3
"""holberton module"""
Rectangle = __import__('7-base_geometry.py').BaseGeometry


class Rectangle(BaseException):
    """class Rectangle"""
    def __init__(self, width, height):

        
        """Instantiation with width and height"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """function that find area of rectangle"""
        return self.__width * self.__height

     def __str__(self):
        """print rectangle description"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
