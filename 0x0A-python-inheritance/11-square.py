#!/usr/bin/python3
"""defines a subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class to define a square."""

    def __init__(self, size):
        """Initialize a new square."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size