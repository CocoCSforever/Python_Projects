from random import randint


class Die:
    """
    Represent a single die
    """
    def __init__(self):
        self.current_value = 0

    def roll(self):
        """
        Sets current value to a random integer between 1 and 6
        """
        self.current_value = randint(1, 6)
        # return self.current_value
