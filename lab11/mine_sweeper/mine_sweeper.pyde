CELL_SIZE = 30  # 30 for one cell
FIELD_SIZE = 15  # 15 cells/line


def setup():
    global gc
    from mine_field import MineField
    from game_controller import GameController
    size(CELL_SIZE * FIELD_SIZE+1,
         CELL_SIZE * FIELD_SIZE+1)

    wordsFont = createFont("BadaboomBB_Reg.otf", 58)
    numFont = createFont("mine-sweeper.otf", 12)

    field = MineField(CELL_SIZE, FIELD_SIZE, numFont)
    gc = GameController(field, wordsFont)
    gc.plant_mines()


def draw():
    gc.update()


def mouseClicked():
    gc.reveal(
              mouseX//CELL_SIZE,
              mouseY//CELL_SIZE
              )
