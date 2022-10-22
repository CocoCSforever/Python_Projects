from dealer import Dealer
from hand import Hand


class GameController:
    """
    A controller for the Blackjack game
    """
    def __init__(self):
        self.BLACKJACK = 21
        self.dealer = Dealer()
        self.player_hand = Hand(self.BLACKJACK)

    def start_play(self):
        """
        Start the game
        """
        print(f"The dealer's score is {self.dealer.score}")
        self.deal_two()
        self.display_hand()
        self.stay_or_hit(input("Would you like to stay or hit?"))

    def deal_two(self):
        """
        Deal two cards
        """
        self.player_hand.receive_card(self.dealer.deal_one())
        self.player_hand.receive_card(self.dealer.deal_one())

    def display_hand(self):
        """
        Display the player's hand
        """
        self.player_hand.display()

    def stay_or_hit(self, s_or_h):
        """
        Determine whether to stay or hit
        """
        if s_or_h == 'hit':
            self.player_hand.receive_card(self.dealer.deal_one())
            self.display_hand()
            if self.player_is_bust():
                self.do_bust()
            else:
                self.stay_or_hit(input("Would you like to stay or hit?"))
        elif s_or_h == 'stay':
            self.do_stay()
        else:
            self.stay_or_hit(input("Would you like to stay or hit?"))

    def player_is_bust(self):
        """
        Determine if the player is bust
        """
        return self.player_hand.score() > self.BLACKJACK

    def do_bust(self):
        """
        Handle the bust case
        """
        print("**********")
        print("*  BUST  *")
        print("**********")

    def do_stay(self):
        """
        Handle the stay case
        """
        if self.player_hand.score() > self.dealer.score:
            print("You win!")
        elif self.player_hand.score() < self.dealer.score:
            print("You lost!")
        else:
            print("You tied!")
