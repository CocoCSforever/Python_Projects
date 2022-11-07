import sys
sys.path.append("..")  # Lets us import from the parent directory
# Either of the following Stack imports will work identically
from stack_python_list import Stack  # nopep8
# from stack_linked_list import Stack  # nopep8


class BracketMatch:
    """Class for evaluating parenthetical strings"""
    def __init__(self):
        self.stack = Stack()
        # TODO:
        # Any necessary or helpful attributes
        # should be set here.

    def brackets_match(self, in_string):
        """Takes a string and returns a boolean
        indicating whether the strings' brackets match"""
        # TODO:
        # Return True if in_string's brackets match,
        # False otherwise
        for i in reversed(in_string):
            if (i.isalnum()):
                pass
            elif (i == ')'):
                self.stack.push('(')
            elif (i == ']'):
                self.stack.push('[')
            elif (i == '}'):
                self.stack.push('{')
            elif (self.stack.is_empty() or i != self.stack.pop()):
                return False
        if (self.stack.is_empty()):
            return True

    def clear(self):
        """Clear the stack at the end of each match checker"""
        self.stack = Stack()
