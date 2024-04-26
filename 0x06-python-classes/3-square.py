#!/usr/bin/python3
"""module for deining square"""


class Square:
    """class for squares"""
    def __init__(self, size=0):
        """
        constructor to initialize values
        Args:
            size(int): size of the squar
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
    def area(self):
        return self.__size * self.__size
