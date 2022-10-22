from deck import Deck
from random import randint


class Dealer:
    """
    A blackjack dealer
    """
    def __init__(self):
        DEALER_RANGE = (17, 21)
        # self._score = randint(*DEALER_RANGE)
        # send a message that this is a private attribute
        # but actually python doesn't have such thing as private
        self.score = randint(*DEALER_RANGE)
        # take two arguments, * pass in a tuple with n values
        # in a place where n arguments are required
        self.deck = Deck()

    def deal_one(self):
        """
        Deal a single card from the desk
        """
        return self.deck.deal_one()

    # @property
    # method property take no argument except self and must return a value
    # def score(self):
    #     return self._score
