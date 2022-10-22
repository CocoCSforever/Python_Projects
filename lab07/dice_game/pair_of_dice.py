from die import Die


class PairOfDice:
    def __init__(self):
        self.d1 = Die()
        self.d2 = Die()

    def roll_dice(self):
        self.d1.roll()
        self.d2.roll()

    def current_value(self):
        """
        Return the sum of its Die objects' current values
        """
        return self.d1.current_value + self.d2.current_value
