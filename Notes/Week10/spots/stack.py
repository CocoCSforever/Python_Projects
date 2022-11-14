class Stack:
    def __init__(self):
        self.content = []

    def push(self, item):
        self.content.append(item)

    def pop(self):
        if len(self.content) > 0:
            self.content.pop()
