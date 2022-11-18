from linked_list_node import Node


class LinkedList:
    def __init__(self, python_seq):
        # create a new linked list from a sequence
        self.first = None
        self.last = self.first
        for n in python_seq:
            self.extend(n)

    def __str__(self):
        """return a human-readable string for users"""
        return ("linked_list("+str(self.first)+")")

    def __repr__(self):
        """Return a detailed string for debugging"""
        return ("linked_list("+repr(self.first)+")")

    def extend(self, value):
        """Add a value to the end of the list
        Value -> None"""
        node = Node(value)
        if self.first is None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node

    def insert(self, value):
        """Add a value to the beginning fo the list
        Value -> None
        """
        node = Node(value)
        node.next = self.first
        self.first = node
        if self.last is None:
            self.last = node

    def contains(self, value):
        """Determine whether the list contains a value
        Value -> Boolean
        """
        # node = self.first
        # while (node is not None):
        #     if node.value == value:
        #         return True
        #     node = node.next
        # return False
        return self.node_contains(self.first, value)

    def node_contains(self, node, value):
        if node is None:
            return False
        elif (node.value == value):
            return True
        return self.node_contains(node.next, value)
