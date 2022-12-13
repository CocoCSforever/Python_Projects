CELL_SIZE = 100  # 100 for one cell
BOARD_SIZE = 8  # 4 cells per line


def setup():
    global gc
    from board import Board
    from game_controller import GameController

    answer = input('enter your name')
    if answer:
        print('hi ' + answer)
    elif answer == '':
        print('[empty string]')
    else:
        print(answer)  # Canceled dialog will print None

    background(42, 175, 99)
    size(CELL_SIZE*BOARD_SIZE+1,
         CELL_SIZE*BOARD_SIZE+1)

    wordsFont = createFont("BadaboomBB_Reg.otf", 20)

    board = Board(CELL_SIZE, BOARD_SIZE, wordsFont)
    gc = GameController(board, wordsFont, answer)


def draw():
    background(42, 175, 99)

    strokeWeight(3)
    for i in range(BOARD_SIZE):
        x = (i+1)*CELL_SIZE
        line(x, 0, x, CELL_SIZE*BOARD_SIZE+1)
        line(0, x, CELL_SIZE*BOARD_SIZE+1, x)
    gc.update()


def mousePressed():
    gc.draw(
              mouseX//CELL_SIZE,
              mouseY//CELL_SIZE
    )


def input(message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)
