from game_controller import GameController
from board import Board


def test_constructor():
    CELL_SIZE = 100
    BOARD_SIZE = 0
    board = Board(CELL_SIZE, BOARD_SIZE, None)
    gc = GameController(board, None, None)
    assert gc.board == board
    assert gc.game_over is False
    assert gc.wordsFont is None
    assert gc.player is None
    BOARD_SIZE = 8
    board = Board(CELL_SIZE, BOARD_SIZE, None)
    gc = GameController(board, None, "Yijia")
    assert gc.board == board
    assert gc.game_over is False
    assert gc.wordsFont is None
    assert gc.player == "Yijia"


def test_update():
    """
    calls two graphical functions:
    self.board.update()
    self.update_scores()
    self.display_end_text() is tested below"""


def test_draw():
    CELL_SIZE = 100
    BOARD_SIZE = 8
    board = Board(CELL_SIZE, BOARD_SIZE, None)
    gc = GameController(board, None, None)
    gc.draw(3, 2)
    gc.draw(4, 4)
    gc.board.computer_make_move()
    assert gc.board.cells[3][2].tile is True
    assert gc.board.cells[3][2].tile_color == gc.board.BLACK
    assert gc.board.cells[2][4].tile is True
    assert gc.board.cells[2][4].tile_color == gc.board.WHITE
    assert gc.board.cells[4][4].tile_color == gc.board.WHITE
    gc.board.draw(2, 4)
    assert gc.board.cells[2][4].tile_color == gc.board.WHITE
    gc.board.draw(3, 5)
    assert gc.board.cells[3][5].tile is True
    assert gc.board.cells[3][5].tile_color == gc.board.BLACK
    assert gc.board.cells[3][4].tile_color == gc.board.BLACK
    gc.board.computer_make_move()
    assert gc.board.cells[4][6].tile is True
    assert gc.board.cells[4][6].tile_color == gc.board.WHITE
    assert gc.board.cells[3][5].tile_color == gc.board.WHITE


def test_end_game():
    CELL_SIZE = 100
    BOARD_SIZE = 8
    board = Board(CELL_SIZE, BOARD_SIZE, None)
    gc = GameController(board, None, None)
    gc.end_game('white')
    assert gc.game_over == 'white'
    gc.game_over = True
    gc.end_game('white')
    assert gc.game_over is True
    gc.end_game('black')
    assert gc.game_over is True
    gc.end_game('win_win')
    assert gc.game_over is True
    gc.game_over = False
    gc.end_game('black')
    assert gc.game_over == 'black'
    gc.game_over = False
    gc.end_game('win_win')
    assert gc.game_over == 'win_win'


def test_display_end_text():
    CELL_SIZE = 100
    BOARD_SIZE = 8
    board = Board(CELL_SIZE, BOARD_SIZE, None)
    gc = GameController(board, None, None)
    gc.game_over = 'white'
    gc.display_end_text()
    assert gc.game_over is None
    assert gc.board.display == "Computer wins with 2 tiles!"
    gc.game_over = 'black'
    gc.display_end_text()
    assert gc.game_over is None
    assert gc.board.display == "User wins with 2 tiles!"
    gc.game_over = 'win_win'
    gc.display_end_text()
    assert gc.game_over is None
    assert gc.board.display == "User and Computer end in\
 a draw each with 2 tiles!"


def test_update_scores():
    """File IO method, we don't test it."""
    pass
