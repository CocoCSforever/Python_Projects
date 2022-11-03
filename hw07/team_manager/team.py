from player import Player


class Team:
    """A class representing a dodgeball team"""
    def __init__(self):
        self.name = "Anonymous Team"
        self.players = []

    def set_team_name(self, name):
        """Set the team name"""
        self.name = name

    def add_player(self, player_name, player_number, player_position):
        """
        Call the Player class constructor with the appropriate
        values to create a new player object, then add that
        player object to the team's players list.
        """
        player = Player(player_name, player_number, player_position)
        self.players.append(player)

    def cut_player(self, player_name):
        """
        Remove the player with the name player_name
        from the players list.
        """
        for player in self.players:
            if (player.name == player_name):
                self.players.remove(player)
                return
        print(player_name, "isn't on team.")

    def is_position_filled(self, position):
        """
        Checks whether there is currently
        at least one player on the team
        occupying the requested position
        """
        for player in self.players:
            if (player.position == position):
                return True
        return False

    def show_team_roster(self):
        """
        display (print to screen)the full team roster in the following format:
        The lineup for Seattle Scorpions is:
        15       Garcia          catcher
        55       Wiggins         corner
        99       McCann          sniper
        """
        print("The lineup for Seattle Scorpions is:")
        if (len(self.players) == 0):
            print("The team currently has no players")
        else:
            for player in self.players:
                print(f"{player.number}\t{player.name}\t\t{player.position}")
