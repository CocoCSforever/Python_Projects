from binary_tree_node import Node


class BinaryTree:
    def __init__(self, val):
        """Create a new tree"""
        self.root = Node(val)
    
    def __str(self):
        return "BinTree(" +str(self.root) + ")"

    def __repr__(self):
        return "BinTree:\n{" + repr(self.root) + "}"
    
    def add_val_l(self, val):
        n = Node(val)
        self.add_node_l(self.root, n)

    def add_node_l(self, current_node, new_node):
        if (current_node.left is None):
            current_node.left = new_node
        elif (current_node.right is None):
            current_node.right = new_node
        else:
            self.add_node_l(current_node.left, new_node)

    def add_val_r(self, val):
        n = Node(val)
        self.add_node_r(self.root, n)

    def add_node_r(self, current_node, new_node):
        if (current_node.right is None):
            current_node.right = new_node
        elif (current_node.left is None):
            current_node.left = new_node
        else:
            self.add_node_r(current_node.right, new_node)