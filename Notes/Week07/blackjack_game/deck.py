from card import Card
# the reason we import Card is bc. we need to use the Card constructor
from random import shuffle


class Deck:
    """
    A deck of cards
    """
    def __init__(self):
        """
        Construct the deck of cards
        """
        suits = ['heart', 'spades', 'diamonds', 'clubs']
        values = ['ace', '2', '3', '4', '5', '6', '7', '8',
                  '9', '10', 'jack', 'queen', 'king']
        self.cards = [Card(suit, value)
                      for suit in suits
                      for value in values]
        shuffle(self.cards)

    def deal_one(self):
        """
        Deal one card from the deck
        """
        return self.cards.pop()
