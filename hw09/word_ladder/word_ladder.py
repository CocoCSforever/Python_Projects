from queue import Queue
from stack import Stack


class WordLadder:
    """A class providing functionality to create word ladders"""
    # Generate a
    # stack representing the word ladder based on the parameters
    # passed to the constructor.
    def __init__(self, w1, w2, wordlist):
        self.q = Queue()
        self.s = Stack()
        self.w1 = w1
        self.w2 = w2
        self.wordlist = wordlist

        self.checked = set()

    def setup(self):
        self.s.push(self.w1)
        self.q.enqueue(self.s)

    def make_ladder(self):
        """For every stack in queue, check its possible next ladder stack
        and add it to queue
        until we get the full word ladder from w1 to w2 and return result"""
        if not self.compare_len():
            return None
        self.setup()
        while not self.q.isEmpty():
            cur_s = self.q.dequeue()
            top_word = cur_s.peek()
            if (self.check_word(top_word, cur_s)):
                return self.q.items[0]
        return None

    def compare_len(self):
        """Compare length of input w1 and w2
        Return True if the same length, False otherwise"""
        if len(self.w1) != len(self.w2):
            return False
        return True

    def check_word(self, word, cur_s):
        """For every character in target word,
        replace it with every letter in alpahbet
        If new_word is an new english word, add updated stack to queue
        If new_word is w2, return True"""
        ALPHABET_RANGE = 26
        for i in range(len(word)):
            for j in range(ALPHABET_RANGE):
                # construct new_word by replacing one char
                new_word = word[:i] + chr(ord('a')+j) + word[i+1:]
                # check whether new_word is an unchecked english word
                if new_word in self.wordlist and\
                        (new_word not in self.checked):
                    # update stack and queue
                    new_s = cur_s.copy()
                    new_s.push(new_word)
                    self.checked.add(new_word)
                    self.q.enqueue(new_s)
                    # if get w2, return True
                    if new_word == self.w2:
                        return True
