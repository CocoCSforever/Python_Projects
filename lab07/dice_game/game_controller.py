from pair_of_dice import PairOfDice


class GameController:

    """
    A controller manage rolling, scoring, and user interaction
    """
    def __init__(self):
        self.pair_of_dice = PairOfDice()
        self.point = -1

    def start_play(self):
        self.roll_or_not()
        self.first_result()

    def roll_or_not(self):
        input("Press enter to roll the dice...\n")
        self.pair_of_dice.roll_dice()

    def first_result(self):
        if (self.pair_of_dice.current_value() == 2
           or self.pair_of_dice.current_value() == 3
           or self.pair_of_dice.current_value() == 12):
            print(f"You rolled {self.pair_of_dice.current_value()}. You lose.")
        elif (self.pair_of_dice.current_value() == 7
              or self.pair_of_dice.current_value() == 11):
            print(f"You rolled {self.pair_of_dice.current_value()}. You win!")
        else:
            self.point = self.pair_of_dice.current_value()
            print(f"Your point is {self.point}.")
            self.continue_roll()

    def continue_roll(self):
        self.roll_or_not()
        if (self.pair_of_dice.current_value() == 7):
            print(f"You rolled {self.pair_of_dice.current_value()}. You lose.")
        elif (self.pair_of_dice.current_value() == self.point):
            print(f"You rolled {self.point}. You win!")
        else:
            print(f"You rolled {self.pair_of_dice.current_value()}.")
            self.continue_roll()
