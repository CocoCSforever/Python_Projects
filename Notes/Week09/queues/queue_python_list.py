class Queue:
    """a queue class using a Python
    list as its implementation"""
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def enqueue(self, item):
        """means put something in at the end of the queue"""
        self.items.insert(0, item)

    def dequeue(self):
        """Means to take something out at the front of the queue.
        Pop just takes an element off at the end of the list, removes it
        from the list and returns it.
        """
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
