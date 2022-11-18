class Node:
    """A linked list node"""
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        """return a human-readable string for users"""
        return "["+self.value+"]->" + str(self.next)

    # Use __repr__ for more detailed debugging output
    def __repr__(self, indent=2):
        """Return a detailed string for debugging"""
        repr_string = "\n" + \
            " " * indent + " Node{\n" + \
            " " * indent + "  value: '" + self.value + "',\n" + \
            " " * indent + "  next: "
        if self.next is None:
            repr_string += self.next.__repr__() + "\n"
        else:
            repr_string += self.next.__repr__(indent + 2)
        repr_string += " "*indent + "}\n"
        return repr_string
