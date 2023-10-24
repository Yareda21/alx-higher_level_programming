#!/usr/bin/python3
"""Definition of classes for a singly-linked list."""


class Node:
    """A class that represents a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Constructs a new Node.

        Parameters:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter and setter for the data of the Node."""
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter and setter for the next_node of the Node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A class that represents a singly-linked list."""

    def __init__(self):
        """Constructs a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the SinglyLinkedList
        at the correct ordered numerical position.

        Parameters:
            value (Node): The new Node to insert.
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp = self.__head
            while temp.next_node is not None and temp.next_node.data < value:
                temp = temp.next_node
            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def __str__(self):
        """Defines the print() representation of a SinglyLinkedList."""
        values = []
        temp = self.__head
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node
        return '\n'.join(values)
