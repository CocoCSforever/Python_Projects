from stack import Stack


class StringProcessor:
    """Class for processing strings"""
    def __init__(self):
        self.stack = Stack()
        self.res = ""

    def process_string(self, line):
        """Process characters one by one in the input line
        Return the result string"""
        for char in line:
            if (char == '^'):
                self.pop_decorder()
                self.pop_decorder()
            elif (char == '*'):
                self.pop_decorder()
            else:
                self.stack.push(char)
        return self.res

    def pop_decorder(self):
        """pop one character from the stack and append it to the res string"""
        char = self.stack.pop()
        # if char is not None, concaternate char with res string
        if char:
            self.res = self.res + char
