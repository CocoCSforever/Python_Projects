CELL_SIZE = 100  # 100 for one cell
BOARD_SIZE = 4  # 4 cells per line


def setup():
    global gc
    from board import Board
    from game_controller import GameController
    background(42, 175, 99)
    size(CELL_SIZE*BOARD_SIZE+1,
         CELL_SIZE*BOARD_SIZE+1)

    strokeWeight(3)
    for i in range(BOARD_SIZE):
        x = (i+1)*CELL_SIZE
        line(x, 0, x, CELL_SIZE*BOARD_SIZE+1)
        line(0, x, CELL_SIZE*BOARD_SIZE+1, x)

    wordsFont = createFont("BadaboomBB_Reg.otf", 20)

    board = Board(CELL_SIZE, BOARD_SIZE)
    gc = GameController(board, wordsFont)


def draw():
    gc.update()


def mousePressed():
    gc.draw(
              mouseX//CELL_SIZE,
              mouseY//CELL_SIZE
    )
