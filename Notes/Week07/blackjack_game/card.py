class Card:
    """
    A playing card
    """
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        # define a toString method
        """
        Provides a string representation of a card object
        """
        return f"{self.value} of {self.suit}"

    def num_value(self):
        """
        Return the card's numerical value
        """
        ACE_VALUE = 11
        FACE_CARD_VALUE = 10
        if self.value == 'ace':
            return ACE_VALUE
        elif (self.value == 'jack' or
                self.value == 'queen' or
                self.value == 'king'):
            return FACE_CARD_VALUE
        else:
            return int(self.value)
