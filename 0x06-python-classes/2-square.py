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
        assert size >= 0, ValueError("size must be positive")  # Only allows positive sizes
        assert isinstance(size, int), TypeError("size must be an integer")
        self.__size = size
