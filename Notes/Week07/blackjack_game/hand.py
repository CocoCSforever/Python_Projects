class Hand:
    """
    A blackjack hand
    """
    def __init__(self, BLACKJACK):
        self.BLACKJACK = BLACKJACK
        self.cards = []
        self.number_of_aces = 0

    def receive_card(self, card):
        """
        Receive a card
        """
        if card.value == 'ace':
            self.number_of_aces += 1
        self.cards.append(card)

    def display(self):
        """
        Print out the hand
        """
        print("Player hand:")
        for card in self.cards:
            print(card)

    # @property
    # make the method work as an attribute
    def score(self):
        """
        Calculate the score
        """
        score = sum([c.num_value() for c in self.cards])
        unmodified_aces = self.number_of_aces
        ACE_REDUCTION = 10
        while score > self.BLACKJACK:
            if unmodified_aces > 0:
                score -= ACE_REDUCTION
                unmodified_aces -= 1
            else:
                return score
        return score
