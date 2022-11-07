import sys
sys.path.append("..")  # Lets us import from the parent directory
# Either of the following Stack imports will work identically
from stack_python_list import Stack  # nopep8
# from stack_linked_list import Stack  # nopep8


class AnBn:
    """Class for evaluating strings of n A's followed by n B's"""
    def __init__(self):
        self.stack = Stack()

    def accept(self, in_string):
        """Takes a string and returns a boolean
indicating whether the string matches the pattern"""
        # TODO:
        # Return True if in_string matches a^nb^n pattern
        # False otherwise
        length = len(in_string)
        if (length % 2 != 0):
            return False
        for i in range(length//2):
            if (in_string[length-1-i] != 'b'):
                return False
        for i in range(length//2):
            if (in_string[length//2-1-i] != 'a'):
                return False
        return True

    def clear(self):
        """Clear the stack at the end of each checker"""
        self.stack = Stack()
