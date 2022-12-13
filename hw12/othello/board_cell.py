class BoardCell():
    def __init__(self, x, y, CELL_SIZE):
        self.x = x
        self.y = y
        self.CELL_SIZE = CELL_SIZE
        self.tile = False
        self.WHITE = (255, 255, 255)
        self.BLACK = (10, 10, 10)
        self.tile_color = None
        self.PIXEL = 90

    def draw(self, current_player):
        self.setup_tile(current_player)
        self.draw_self()

    def setup_tile(self, current_player):
        if current_player:
            self.tile_color = self.WHITE
        else:
            self.tile_color = self.BLACK
        self.tile = True

    def draw_self(self):
        if self.tile:
            fill(*self.tile_color)
            ellipse(self.x+self.CELL_SIZE/2, self.y+self.CELL_SIZE/2,
                    self.PIXEL, self.PIXEL)
