from board_cell import BoardCell


class Board():
    def __init__(self, CELL_SIZE, BOARD_SIZE):
        self.CELL_SIZE = CELL_SIZE
        self.BOARD_SIZE = BOARD_SIZE
        self.cells = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        # for future traversal: self.neighbors = [-1, 0, 1]
        for x in range(self.BOARD_SIZE):
            for y in range(self.BOARD_SIZE):
                self.cells[x][y] = BoardCell(
                                        x*self.CELL_SIZE,
                                        y*self.CELL_SIZE,
                                        self.CELL_SIZE,
                                        )
        # True for white, False for black
        self.current_player = False
        self.white = 2
        self.black = 2
        self.no_tile = BOARD_SIZE*BOARD_SIZE - 4
        self.setup()

    def setup(self):
        center = self.BOARD_SIZE/2
        for x in range(-1, 1):
            for y in range(-1, 1):
                if (x+y) % 2 == 0:
                    current = True
                else:
                    current = False
                self.cells[center+x][center+y].draw(current)
        # hard code version for future reference
        # self.cells[center-1][center-1].draw(True)
        # self.cells[center-1][center].draw(False)
        # self.cells[center][center-1].draw(False)
        # self.cells[center][center].draw(True)

    def update(self):
        """
        Carry out cell and tile display
        """
        # Nothing to do at this stage, keep it in case needed later
        pass

    def draw(self, x, y):
        if not self.cells[x][y].tile:
            self.cells[x][y].draw(self.current_player)
            if self.current_player:
                self.white += 1
                self.no_tile -= 1
            else:
                self.black += 1
                self.no_tile -= 1
            #  for debugging: print(self.white, self.black, self.no_tile)
            self.current_player = not self.current_player
            self.check_completion_status()

    def check_completion_status(self):
        """
        Check to see if these are no legal moves available
        """
        if self.no_tile == 0:
            if self.white > self.black:
                self.gc.end_game('white')
            elif self.black > self.white:
                self.gc.end_game('black')
            else:
                self.gc.end_game('win_win')
