#!/usr/bin/python3
"""module for deining square"""


class Square:
    """class for squares"""
    def __init__(self, size=0, position=(0, 0)):
        """
        constructor to initialize values
        Args:
            size(int): size of the squar
        """
        self.size = size
        self.position = position

    def __str__(self):
        self.my_print()

    @property
    def size(self):
        """get the size of he square"""
        return self.__size

    @size.setter
    def size(self, val):
        if not isinstance(val, int):
            raise TypeError('size must be an integer')
        elif val < 0:
            raise ValueError('size must be >= 0')
        self.__size = val

    @property
    def position(self):
        return self.__position

    @position.setter
    def size(self, value):
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

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

    def pos_print(self):
        """returns the position in spaces"""
        pos = ""
        if self.size == 0:
            return "\n"
        for w in range(self.position[1]):
            pos += "\n"
        for w in range(self.size):
            for i in range(self.position[0]):
                pos += " "
            for j in range(self.size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
        """print the square in position"""
        print(self.pos_print(), end='')
