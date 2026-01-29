#!/usr/bin/python3
"""
Singly linked list
"""


class Node:
    """Class that defines a singly linked list"""
    def __init__(self, data, next_node=None):
        msg_err_int = "data must be an integer"
        if not isinstance(data, int):
            raise TypeError(msg_err_int)
        self.__data = data
        msg_err_node = "next node must be a Node object"
        if not isinstance(next_node, Node) and next_node is not None:
            raise TypeError(msg_err_node)
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def data(self, value):
        msg_err_int = "data must be an integer"
        if not isinstance(value, int):
            raise TypeError(msg_err_int)
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        msg_err_node = "next node must be a Node object"
        if not isinstance(value, Node) and value is not None:
            raise TypeError(msg_err_node)
        self.__next_node = value


class SinglyLinkedList:
    """Class that defines a singly linked list"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
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
        current_node = self.__head
        linklist = ""
        while current_node:
            linklist += str(current_node.data)
            if current_node.next_node:
                linklist += '\n'
            current_node = current_node.next_node
        return linklist
