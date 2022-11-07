class Card:
    """A playing card"""
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        """Return a user friendly string for the card
        If we only have repr but not str, "print" is to default to the repr
        Recommendation: always define repr for a class for debugging purpose
        but only define str if need to/want there to be a a user friendly
        representation.
        """
        return self.value + " of " + self.suit

    def __repr__(self):
        """Return an informative string for debugging
        complete description about the object
        for debugging and analysis purpose
        """
        return (f"{self.__class__.__name__}"
                f"(suit: {self.suit}, value: {self.value})")

    def __eq__(self, other):
        """Return a boolean representing equality of the cards"""
        return (self.value == other.value and self.suit == other.suit)

    def __lt__(self, other):
        """Return a boolean for the less than relationship
        '>': if __gt__ is not present, will call __lt__ and return negation
        """
        return (self.num_value() < other.num_value())

    def __gt__(self, other):
        """Return a boolean for the greater than relationship"""
        return (self.num_value() > other.num_value())

    # __hash__ defaults to object ID, unless __eq__ is defined,
    # in which case __hash__ is set to None (and must be explicitly)
    # defined. Otherwise, unhashable type:"Card"
    def __hash__(self):
        """Define the object's hash function so that the object
        can be used as a dictionary key.

        Best pratice is that hash should always agree with __eq__.
        Anytime things would be equal. They should also be a
        single key in a dictionary

        A hashable object should be immutable, a list is not hashable.
        which means if you tried to calculate a representative fingerprint of
        it, it would be different every time.

        Hashes should be always the same for a particular piece of data.
        And they should be calculatable from that piece of data.
        """
        return hash((self.suit, self.value))

    def num_value(self):
        """Return the numerical value for the card"""
        ACE_VALUE = 11
        FACE_CARD_VALUE = 10
        if self.value == "ace":
            return ACE_VALUE
        elif (self.value == "jack" or
              self.value == "queen" or
              self.value == "king"):
            return FACE_CARD_VALUE
        else:
            return int(self.value)
