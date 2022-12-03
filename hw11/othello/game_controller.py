class GameController():
    """
    The Game Controller
    """
    def __init__(self, board, wordsFont):
        self.board = board
        self.game_over = False
        self.wordsFont = wordsFont
        board.gc = self

    def update(self):
        """
        Carry out board update and
        check if game is over
        """
        self.board.update()

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
        if self.game_over:
            self.display_end_text()

    def display_end_text(self):
        """Announce the winner and tiles"""
        if self.game_over == 'white':
            message = "White player wins with " +\
                      str(self.board.white) + " tiles!"
        elif self.game_over == 'black':
            message = "Black player wins with " +\
                      str(self.board.black) + " tiles!"
        else:
            message = "Black and White end in a draw each with " +\
                      str(self.board.white) + " tiles!"
        print(message)
        center = self.board.BOARD_SIZE*self.board.CELL_SIZE/2
        offset = 3
        textAlign(CENTER)
        textFont(self.wordsFont)
        fill(0)
        text(message, center+offset, center+offset)
        fill(255)
        text(message, center, center)
