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

    @property
    def size(self):
        """get the size of he square"""
        return self.size

    @size.setter
    def size(self, val):
        if not isinstance(val, int):
            raise TypeError('size must be an integer')
        elif val < 0:
            raise ValueError('size must be >= 0')
        self.__size = val

    def area(self):
        """
        function that returns area
        Args:
            self(object): the object area
        """
        return self.__size * self.__size

    def my_print(self):
        """
        prints the square using # char
        """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end='')
            print()
