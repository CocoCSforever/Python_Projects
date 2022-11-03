class Bench:
    """A class representing a sidelines bench"""
    def __init__(self):
        """
        Initialize the bench object with whatever
        attributes and values it will need
        """
        self.players = []

    def send_to_bench(self, player):
        """Put the player "onto the bench" """
        self.players.insert(0, player)

    def get_from_bench(self):
        """Return the name of the player who has
        been on the bench longest."""
        if (len(self.players) == 0):
            return None
        else:
            return self.players.pop().name

    def show_bench(self):
        """Display the current list of players on the bench"""
        print("The bench currently includes:")
        for player in self.players:
            print(player.name)
