#!/usr/bin/python3
"""holberton module"""
Square = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""
    def __init__(self, size):
        """Instantiation with size"""
        self.__size = size
        self.integer_validator("size", size)
