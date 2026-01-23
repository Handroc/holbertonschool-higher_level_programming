#!/usr/bin/python3
"""
Docstring for 3-say_my_name.py
"""


def say_my_name(first_name, last_name=""):
    """
    Docstring for say_my_name
    :param first_name: first name string
    :param last_name: last name string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
