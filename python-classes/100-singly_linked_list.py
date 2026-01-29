#!/usr/bin/python3
"""
Singly linked list
"""


class Node:
    """Class that defines a singly linked list"""
    def __init__(self, data, next_node=None):
        """Function that initializes the node"""
        msg_err_int = "data must be an integer"
        if not isinstance(data, int):
            raise TypeError(msg_err_int)
        self.__data = data
        msg_err_node = "next node must be a Node object"
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError(msg_err_node)
        self.__next_node = next_node

    @property
    def data(self):
        """Function that returns the data of the node"""
        return self.__data

    @property
    def next_node(self):
        """Function that returns the next node"""
        return self.__next_node

    @data.setter
    def data(self, value):
        """Function that sets the data of the node"""
        msg_err_int = "data must be an integer"
        if not isinstance(value, int):
            raise TypeError(msg_err_int)
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        """Function that sets the next node"""
        msg_err_node = "next node must be a Node object"
        if not isinstance(value, Node) and value is not None:
            raise TypeError(msg_err_node)
        self.__next_node = value


class SinglyLinkedList:
    """Class that defines a singly linked list"""
    def __init__(self):
        """Function that initializes the singly linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """Function that inserts a new Node to the list"""
        new_node = Node(value)
        if self.__head is None or self.__head.data > new_node.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        current_node = self.__head
        while current_node.next_node and current_node.next_node.data < value:
            current_node = current_node.next_node
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node

    def __str__(self):
        """Function that defines the string representation of the list"""
        current_node = self.__head
        linklist = ""
        while current_node:
            linklist += str(current_node.data) + "\n"
            current_node = current_node.next_node
        return linklist.rstrip("\n")
