class GameController():
    """
    The Game Controller
    """
    def __init__(self, board, wordsFont, gm, player):
        self.board = board
        self.game_over = False
        self.wordsFont = wordsFont
        self.gm = gm
        self.player = player
        board.gc = self

    def update(self):
        """
        Carry out board update and
        check if game is over
        """
        self.board.update()
        if self.game_over:
            self.display_end_text()

    def draw(self, x, y):
        """
        draw a tile at appropriate positions on the board
        """
        self.board.draw(x, y)

    def end_game(self, win_or_lose):
        """
        End the game and set win or lose condition
        """
        if not self.game_over:
            self.game_over = win_or_lose

    def display_end_text(self):
        """Announce the winner and tiles"""
        if self.game_over == 'white':
            message = "Computer wins with " +\
                      str(self.board.white) + " tiles!"
        elif self.game_over == 'black':
            message = "User wins with " +\
                      str(self.board.black) + " tiles!"
        else:
            message = "User and Computer end in a draw each with " +\
                      str(self.board.white) + " tiles!"
        print(message)
        self.update_scores()
        self.game_over = None
        self.board.display = message
        # center = self.board.BOARD_SIZE*self.board.CELL_SIZE/2
        # offset = 3
        # textAlign(CENTER)
        # textFont(self.wordsFont)
        # fill(0)
        # text(message, center+offset, center+offset)
        # fill(255)
        # text(message, center, center)

    def update_scores(self):
        score = self.board.black
        try:
            out = open("scores.txt", "a+")
            out.seek(0)
        except OSError as e:
            print("Can't open scores.txt for writing.")
            return

        line = out.readline()
        # .strip()
        print(line)
        if line:
            score_break = line.rfind(' ')
            highest_score = int(line[score_break+1:])
            print("highest_score:", highest_score)
            if score > highest_score:
                out.seek(0)
            else:
                out.seek(0, 2)
        out.write(self.player + " " + str(score) + "\n")
        # out.close()
