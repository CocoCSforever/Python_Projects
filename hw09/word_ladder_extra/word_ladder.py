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
        self.setup()
        while not self.q.isEmpty():
            cur_s = self.q.dequeue()
            top_word = cur_s.peek()
            if (self.generate_word(top_word, cur_s)):
                return self.s
        return None

    def generate_word(self, word, cur_s):
        """For every character in target word,
        replace it with every letter in alpahbet
        If new_word is an new english word, add updated stack to queue
        If new_word is w2, return True"""
        ALPHABET_RANGE = 26
        for i in range(len(word)):
            for j in range(ALPHABET_RANGE):
                if (self.add_letter(i, j, word, cur_s)):
                    return True
                if (self.replace_letter(i, j, word, cur_s)):
                    return True
        # add letter to the end of the word
        # Test: ocean earth
        # Ladder:  ocean  octan  octad  ectad  ecad  ead  eat  eath  earth
        for j in range(ALPHABET_RANGE):
            if (self.add_letter(len(word), j, word, cur_s)):
                return True

        if len(word) > 1:
            for i in range(len(word)):
                if (self.delete_letter(i, word, cur_s)):
                    return True

        # for i in range(len(word)):
        #     if (len(word) > 1 and self.delete_letter(i, word, cur_s.copy())):
        #         return True
        #     for j in range(ALPHABET_RANGE):
        #         if (self.add_letter(i, j, word, cur_s.copy())):
        #             return True
        #         if (self.replace_letter(i, j, word, cur_s.copy())):
        #             return True

    def add_letter(self, i, j, word, new_s):
        """Construct new_word by adding one char"""
        new_word = word[:i] + chr(ord('a')+j) + word[i:]
        return self.check_new_word(new_word, new_s)

    def delete_letter(self, i, word, new_s):
        """Construct new_word by deleting one char"""
        new_word = word[:i] + word[i+1:]
        # if (new_word != ''):
        return self.check_new_word(new_word, new_s)

    def replace_letter(self, i, j, word, new_s):
        """construct new_word by replacing one char"""
        new_word = word[:i] + chr(ord('a')+j) + word[i+1:]
        return self.check_new_word(new_word, new_s)

    def check_new_word(self, new_word, new_s):
        """Check whether new_word is an unchecked english word"""
        if new_word in self.wordlist[len(new_word)] and\
                (new_word not in self.checked):
            # only deep copy when necessary
            new_s = new_s.copy()
            # update stack and queue
            new_s.push(new_word)
            self.checked.add(new_word)
            self.q.enqueue(new_s)
            # if get w2, return True
            if new_word == self.w2:
                self.s = new_s
                return True
