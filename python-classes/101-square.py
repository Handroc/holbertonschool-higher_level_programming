#!/usr/bin/python3
"""
Square
"""


class Square:
    """Class that defines a square by size"""
    def __init__(self, size=0, position=(0, 0)):
        """Function that initializes the size and the position"""
        msg_err = "size must be an integer"
        msg_err_size = "size must be >= 0"
        msg_err_tuple = "position must be a tuple of 2 positive integers"
        if type(size) is not int:
            raise TypeError(msg_err)
        if size < 0:
            raise ValueError(msg_err_size)
        if (not (isinstance(position, tuple))
                or len(position) != 2
                or not (isinstance(position[0], int))
                or not (isinstance(position[1], int))
                or position[0] < 0 or position[1] < 0):
            raise TypeError(msg_err_tuple)
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Returns the size of the square."""
        return self.__size

    @property
    def position(self):
        """Returns the position of the square."""
        return self.__position

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.
        :param value: size value
        """
        msg_err = "size must be an integer"
        msg_err_size = "size must be >= 0"
        if type(value) is not int:
            raise TypeError(msg_err)
        if value < 0:
            raise ValueError(msg_err_size)
        self.__size = value

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.
        :param value: position value
        """
        msg_err_tuple = "position must be a tuple of 2 positive integers"
        if (not (isinstance(value, tuple))
                or len(value) != 2
                or not (isinstance(value[0], int))
                or not (isinstance(value[1], int))
                or value[0] < 0 or value[1] < 0):
            raise TypeError(msg_err_tuple)
        self.__position = value

    def area(self):
        """Calculates the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character #."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(' ' * self.__position[0] + "#" * self.__size)

    def __str__(self):
        str_square = ""
        if self.__size == 0:
            return str_square
        else:
            for _ in range(self.__position[1]):
                str_square += "\n"
            for i in range(self.__size):
                str_square += ' ' * self.__position[0] + '#' * self.__size
                if i != self.__size - 1:
                    str_square += '\n'
            return str_square
