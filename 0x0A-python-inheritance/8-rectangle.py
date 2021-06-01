#!/usr/bin/python3
"""holberton module"""
BaseGeometry = __import__('7-base_geometry.py').BaseGeometry


class Rectangle(BaseException):
    """class Rectangle"""
    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
