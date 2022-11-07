import sys
from stack_python_list import Stack


class AnBnCn:
    """Class for evaluating strings of n A's followed by n B's"""
    def __init__(self):
        self.stack0 = Stack()
        self.stack1 = Stack()
        self.expect = [True, False, False]
        self.db = [self.stack0, self.stack1]

    def accept(self, in_string):
        """Takes a string and returns True if in_string matches a^nb^n pattern
        False otherwise"""
        for char in in_string:
            if (char == 'a'):
                if (self.expect[0] is True):
                    self.db[0].push(char)
                else:
                    return False
            elif (char == 'b'):
                if not self.check(char, 0):
                    return False
            elif (char == 'c'):
                if not (self.check(char, 1) and self.db[0].is_empty()):
                    return False
            else:
                return False
        return self.db[1].is_empty()

    def check(self, char, index):
        """
        Check whether it's time for b to show up
        Change the corresponding database of boolean values and stacks
        """
        if (self.expect[index] is True):
            # means the first time that current char shows up
            # this is the only circumstance that
            # expect_current_char boolean can be false
            self.expect[index] = False
            self.expect[index+1] = True
            # if index==0, call change_stack1, else call change_stack2
            if index:
                return self.change_stack2(char, index)
            else:
                return self.change_stack1(char, index)
        elif (self.expect[index+1] is True):
            # when expect_current_char is True, edit stacks
            if index:
                return self.change_stack2(char, index)
            else:
                return self.change_stack1(char, index)
        else:
            return False

    def change_stack1(self, char, index):
        """
        pop items('a') in stack1
        push items('b') in stack2
        """
        if self.db[index].items:
            self.db[index].pop()
            self.db[index+1].push(char)
            return True
        else:
            return False

    def change_stack2(self, char, index):
        """
        pop items('b') in stack2
        """
        if self.db[index].items:
            self.db[index].pop()
            return True
        else:
            return False

    def clear(self):
        """Clear the stack database and reset expect boolean
        at the end of each checker"""
        self.db[0] = Stack()
        self.db[1] = Stack()
        self.expect = [True, False, False]
