from board_cell import BoardCell
from threading import Timer


class Board():
    def __init__(self, CELL_SIZE, BOARD_SIZE, wordsFont):
        self.CELL_SIZE = CELL_SIZE
        self.BOARD_SIZE = BOARD_SIZE
        self.wordsFont = wordsFont
        self.cells = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        self.neighbors = [-1, 0, 1]
        self.list = [set(), set()]
        self.WHITE = (255, 255, 255)
        self.BLACK = (10, 10, 10)
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
        self.display = None
        # self.counter = 0
        self.setup()

    def setup(self):
        """Set up the first four tiles in the middle"""
        center = int(self.BOARD_SIZE/2)
        for x in range(-1, 1):
            for y in range(-1, 1):
                if (x+y) % 2 == 0:
                    current = True
                else:
                    current = False
                if center+x in range(self.BOARD_SIZE)\
                   and center+y in range(self.BOARD_SIZE):
                    self.cells[center+x][center+y].setup_tile(current)

    def update(self):
        """
        Carry out display for:
        tile, turn, end_message
        """
        # Notes:
        # Another way to implement delay:
        # add self.counter = 100 to self.draw()
        # if self.counter > 0:
        #     self.counter -= 1
        # if self.counter == 0 and self.current_player:
        #     self.computer_make_move()
        for x in range(self.BOARD_SIZE):
            for y in range(self.BOARD_SIZE):
                self.cells[x][y].draw_self()
        self.display_turn(self.current_player)
        if self.display:
            self.display_message(self.display)

    def draw(self, x, y):
        if self.current_player is False:
            if self.player_make_move(x, y):
                t = Timer(1, self.computer_make_move)
                t.start()
                # for debugging without delay:
                # self.computer_make_move()

    def player_make_move(self, x, y):
        """Check if player can make a move at (x, y)
        and return true if can"""
        self.generate_legal_moves()
        # if there are no more legal moves, turn to computer
        if len(self.list[1]) == 0:
            self.current_player = not self.current_player
            return True
        # if current disk don't have a tile and it's legal, draw a move
        if not self.cells[x][y].tile and (x, y) in self.list[1]:
            return self.draw_move(x, y)
        else:
            return False

    def computer_make_move(self):
        self.generate_legal_moves()
        if len(self.list[0]) == 0:
            self.current_player = not self.current_player
            return
        tuple = self.list[0].pop()
        self.draw_move(tuple[0], tuple[1])

    def draw_move(self, x, y):
        """Draw a move at (x, y) for current player:
        draw a tile, flip tiles, update scores
        reverse turns, check completion"""
        self.cells[x][y].setup_tile(self.current_player)
        self.flip(x, y, self.current_player)
        if self.current_player:
            self.white += 1
            self.no_tile -= 1
        else:
            self.black += 1
            self.no_tile -= 1
        self.current_player = not self.current_player
        self.check_completion_status()
        self.print_each_turn_info(x, y)
        return True

    def flip(self, x, y, current_player):
        """When current player place a new tile on the board,
        check the neighbors of the current tile to see
        if we can flip any tiles"""
        for xneighbor in self.neighbors:
            for yneighbor in self.neighbors:
                if not (xneighbor == 0 and yneighbor == 0)\
                   and x + xneighbor in range(0, self.BOARD_SIZE)\
                   and y + yneighbor in range(0, self.BOARD_SIZE):
                    self.flip_x_y(x+xneighbor, y+yneighbor, xneighbor,
                                  yneighbor, self.cells[x][y].tile_color,
                                  current_player)

    def flip_x_y(self, x, y, xneighbor, yneighbor, cur_color, cur_player):
        """For every tile on a certain direction
        if the tile has a different color, we flip it
        continue until we meet the first tile with the same color"""
        if self.cells[x][y].tile is False\
           or self.cells[x][y].tile_color == cur_color:
            return
        else:
            if self.check_neighbors_color(x, y,
                                          xneighbor, yneighbor):
                self.cells[x][y].setup_tile(cur_player)
                if cur_player:
                    self.white += 1
                    self.black -= 1
                else:
                    self.white -= 1
                    self.black += 1
                self.flip_x_y(x+xneighbor, y+yneighbor,
                              xneighbor, yneighbor,
                              cur_color, cur_player)
            else:
                return

    def generate_legal_moves(self):
        self.list = [set(), set()]
        for x in range(self.BOARD_SIZE):
            for y in range(self.BOARD_SIZE):
                if self.cells[x][y].tile is False:
                    self.check_legal(x, y, self.WHITE, 0)
                    self.check_legal(x, y, self.BLACK, 1)

    def check_legal(self, x, y, cur_color, index):
        """For an empty disk(x,y), check whether it is a legal move
        if it is, add (x, y) to set--legal moves"""
        for xneighbor in self.neighbors:
            for yneighbor in self.neighbors:
                if not (xneighbor == 0 and yneighbor == 0)\
                   and x + xneighbor in range(0, self.BOARD_SIZE)\
                   and y + yneighbor in range(0, self.BOARD_SIZE)\
                   and self.cells[x + xneighbor][y + yneighbor].tile is True\
                   and self.cells[x + xneighbor][y + yneighbor].tile_color !=\
                   cur_color:
                    # as long as one direction can flip tiles, it's legal
                    # add (x, y) to set and return
                    if self.check_neighbors_color(x + xneighbor, y + yneighbor,
                                                  xneighbor, yneighbor):
                        self.list[index].add((x, y))
                        return

    def check_neighbors_color(self, x, y, xd, yd):
        """
        Starting from tile(x, y)
        Check whether these is different tile on a certain direction"""
        # if out of range or no tile on disk, return false
        if x+xd not in range(self.BOARD_SIZE)\
           or y+yd not in range(self.BOARD_SIZE)\
           or self.cells[x+xd][y+yd].tile is False:
            return False
        # if meet a same color, continue recursion
        elif self.cells[x+xd][y+yd].tile_color == self.cells[x][y].tile_color:
            return self.check_neighbors_color(x+xd, y+yd, xd, yd)
        # if meet a different color, return true
        else:
            return True

    def check_completion_status(self):
        """
        Check to see if these are no more legal moves available
        """
        if self.no_tile == 0:
            self.start_end_game()
        else:
            self.generate_legal_moves()
            if len(self.list[0]) == len(self.list[1]) == 0:
                self.start_end_game()

    def start_end_game(self):
        if self.white > self.black:
            self.gc.end_game('white')
        elif self.black > self.white:
            self.gc.end_game('black')
        else:
            self.gc.end_game('win_win')

    def display_message(self, message):
        center = self.BOARD_SIZE*self.CELL_SIZE/2
        offset = 3
        textAlign(CENTER)
        textFont(self.wordsFont)
        fill(0)
        text(message, center+offset, center+offset)
        fill(255)
        text(message, center, center)

    def print_each_turn_info(self, x, y):
        print("\nLast tile is placed at: ")
        print(x, y)
        if self.current_player:
            print("Now it's computer's turn: ")
        else:
            print("Now it's user's turn: ")
        print("Computer's legal moves: ", self.list[0])
        print("User's legal moves: ", self.list[1])

    def display_turn(self, cur_player):
        textAlign(CENTER)
        center = self.BOARD_SIZE*self.CELL_SIZE/2
        textFont(self.wordsFont)
        if cur_player:
            message = "Now it's computer's turn."
        else:
            message = "Now it's user's turn."
        fill(255)
        text(message, center, 20)
