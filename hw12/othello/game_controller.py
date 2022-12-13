class GameController():
    """
    The Game Controller
    """
    def __init__(self, board, wordsFont, player):
        self.board = board
        self.game_over = False
        self.wordsFont = wordsFont
        self.player = player
        board.gc = self
        board.check_completion_status()

    def update(self):
        """
        Carry out board update and
        check if game is over
        """
        self.board.update()
        if self.game_over:
            self.display_end_text()
            self.update_scores()

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
                      str(self.board.white) + " tiles!\n"
        elif self.game_over == 'black':
            message = "User wins with " +\
                      str(self.board.black) + " tiles!\n"
        else:
            message = "User and Computer end in a draw each with " +\
                      str(self.board.white) + " tiles!\n"
        print(message)
        self.game_over = None
        self.board.display = message

    def update_scores(self):
        print("Updating scores:")
        score = self.board.black
        try:
            out = open("scores.txt", "r+")
        except OSError as e:
            print("Can't open scores.txt for writing.")
            return

        content = out.read()
        line_break = content.find('\n')
        line = content[:line_break]
        new_line = self.player + " " + str(score) + "\n"
        print(new_line)
        if line:
            score_break = line.rfind(' ')
            highest_score = int(line[score_break+1:])
            if score > highest_score:
                content = new_line + content
            else:
                content = content + new_line
        else:
            content = new_line
        out.seek(0)
        out.write(content)
