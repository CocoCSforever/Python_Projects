from board import Board
from game_controller import GameController
from threading import Timer


def test_constructor():
    CELL_SIZE = 100
    BOARD_SIZE = 0
    board = Board(CELL_SIZE, BOARD_SIZE, None)
    assert board.CELL_SIZE == 100
    assert board.BOARD_SIZE == 0
    assert board.wordsFont is None
    assert board.cells == []
    assert board.neighbors == [-1, 0, 1]
    assert board.list == [set(), set()]
    assert board.WHITE == (255, 255, 255)
    assert board.BLACK == (10, 10, 10)
    assert board.current_player is False
    assert board.white == 2
    assert board.black == 2
    assert board.no_tile == -4
    assert board.display is None

    BOARD_SIZE = 2
    board = Board(CELL_SIZE, BOARD_SIZE, None)
    assert board.cells[0][0].tile_color == board.WHITE
    assert board.cells[1][1].tile_color == board.WHITE
    assert board.cells[0][1].tile_color == board.BLACK
    assert board.cells[1][0].tile_color == board.BLACK

    BOARD_SIZE = 4
    board = Board(CELL_SIZE, BOARD_SIZE, None)
    assert board.cells[1][1].tile_color == board.WHITE
    assert board.cells[2][2].tile_color == board.WHITE
    assert board.cells[1][2].tile_color == board.BLACK
    assert board.cells[2][1].tile_color == board.BLACK
    for x in range(BOARD_SIZE):
        assert board.cells[x][0].tile is False
        assert board.cells[x][3].tile is False


def test_update():
    """calls three graphical function:
    self.cells[x][y].draw_self()
    self.display_message()
    self.display_turn()"""
    pass


def test_draw():
    CELL_SIZE = 100
    BOARD_SIZE = 8
    board = Board(CELL_SIZE, BOARD_SIZE, None)
    board.draw(3, 2)
    board.draw(4, 4)
    board.computer_make_move()
    assert board.cells[3][2].tile is True
    assert board.cells[3][2].tile_color == board.BLACK
    assert board.cells[2][4].tile is True
    assert board.cells[2][4].tile_color == board.WHITE
    assert board.cells[4][4].tile_color == board.WHITE
    board.draw(2, 4)
    assert board.cells[2][4].tile_color == board.WHITE
    board.draw(3, 5)
    assert board.cells[3][5].tile is True
    assert board.cells[3][5].tile_color == board.BLACK
    assert board.cells[3][4].tile_color == board.BLACK
    board.computer_make_move()
    assert board.cells[4][6].tile is True
    assert board.cells[4][6].tile_color == board.WHITE
    assert board.cells[3][5].tile_color == board.WHITE


def test_player_make_move():
    CELL_SIZE = 100
    BOARD_SIZE = 8
    board = Board(CELL_SIZE, BOARD_SIZE, None)
    assert board.player_make_move(3, 2) is True
    board.draw_move(2, 4)
    assert board.player_make_move(6, 6) is False
    assert board.player_make_move(5, 4) is False
    assert board.player_make_move(2, 3) is False
    assert board.player_make_move(2, 5) is True
    board.draw_move(2, 2)
    assert board.player_make_move(2, 1) is False
    assert board.player_make_move(5, 5) is False
    assert board.player_make_move(5, 3) is False
    assert board.player_make_move(5, 4) is True


def test_computer_make_move():
    CELL_SIZE = 100
    BOARD_SIZE = 8
    board = Board(CELL_SIZE, BOARD_SIZE, None)
    board.player_make_move(3, 2)
    # The set of computer's legal moves is set([(2, 4), (2, 2), (4, 2)]))
    board.computer_make_move()
    if board.cells[2][4].tile:
        assert board.cells[2][4].tile_color == board.WHITE
    elif board.cells[2][2].tile:
        assert board.cells[2][2].tile_color == board.WHITE
    else:
        assert board.cells[4][2].tile_color == board.WHITE


def test_draw_move():
    CELL_SIZE = 100
    BOARD_SIZE = 8
    board = Board(CELL_SIZE, BOARD_SIZE, None)
    board.draw_move(4, 5)
    assert board.current_player is True
    assert board.black == 4
    assert board.no_tile == 59
    board.draw_move(5, 5)
    assert board.current_player is False
    assert board.white == 3
    assert board.no_tile == 58
    board.draw_move(6, 5)
    assert board.current_player is True
    assert board.black == 5
    assert board.no_tile == 57
    board.draw_move(2, 4)
    assert board.current_player is False
    assert board.white == 4
    assert board.no_tile == 56


def test_flip():
    CELL_SIZE = 100
    BOARD_SIZE = 8
    board = Board(CELL_SIZE, BOARD_SIZE, None)
    board.flip(3, 2, False)
    assert board.cells[3][3].tile_color == board.BLACK
    assert board.black == 3
    assert board.white == 1
    board.flip(2, 2, True)
    assert board.cells[3][3].tile_color == board.WHITE
    assert board.black == 2
    assert board.white == 2
    board.draw_move(4, 5)
    board.flip(5, 5, True)
    assert board.cells[4][4].tile_color == board.WHITE
    assert board.black == 3
    assert board.white == 2
    board.flip(5, 4, False)
    assert board.cells[4][4].tile_color == board.BLACK
    assert board.black == 4
    assert board.white == 1


def test_flip_x_y():
    CELL_SIZE = 100
    BOARD_SIZE = 8
    board = Board(CELL_SIZE, BOARD_SIZE, None)
    board.flip_x_y(3, 3, 0, 1, board.BLACK, False)
    assert board.cells[3][3].tile_color == board.BLACK
    assert board.black == 3
    assert board.white == 1
    board.flip_x_y(4, 4, 1, 1, board.BLACK, False)
    assert board.cells[4][4].tile_color == board.WHITE
    assert board.black == 3
    assert board.white == 1
    board.flip_x_y(4, 3, 0, 1, board.WHITE, True)
    assert board.cells[4][3].tile_color == board.WHITE
    assert board.black == 2
    assert board.white == 2
    board.flip_x_y(3, 3, -1, -1, board.WHITE, True)
    assert board.cells[3][3].tile_color == board.BLACK
    assert board.black == 2
    assert board.white == 2


def test_generate_legal_moves():
    CELL_SIZE = 100
    BOARD_SIZE = 8
    board = Board(CELL_SIZE, BOARD_SIZE, None)
    board.generate_legal_moves()
    assert board.list[0] == {(4, 2), (5, 3), (2, 4), (3, 5)}
    assert board.list[1] == {(3, 2), (2, 3), (5, 4), (4, 5)}
    board.draw_move(3, 2)
    assert board.list[0] == {(2, 2), (4, 2), (2, 4)}
    assert board.list[1] == {(5, 5), (5, 4), (4, 5)}
    board.draw_move(2, 4)
    assert board.list[0] == {(2, 2), (3, 1), (4, 2), (5, 2)}
    assert board.list[1] == {(5, 5), (2, 5), (4, 5), (1, 5), (3, 5)}


def test_check_legal():
    CELL_SIZE = 100
    BOARD_SIZE = 8
    board = Board(CELL_SIZE, BOARD_SIZE, None)
    board.check_legal(3, 2, board.BLACK, 1)
    assert board.list[1] == {(3, 2)}
    board.check_legal(2, 3, board.BLACK, 1)
    assert board.list[1] == {(2, 3), (3, 2)}
    board.check_legal(5, 4, board.BLACK, 1)
    assert board.list[1] == {(2, 3), (3, 2), (5, 4)}
    board.draw_move(3, 2)
    board.list[0] = set()
    board.check_legal(2, 4, board.WHITE, 0)
    assert board.list[0] == {(2, 4)}
    board.check_legal(2, 2, board.WHITE, 0)
    assert board.list[0] == {(2, 4), (2, 2)}
    board.check_legal(4, 2, board.WHITE, 0)
    assert board.list[0] == {(2, 4), (2, 2), (4, 2)}


def check_neighbors_color():
    CELL_SIZE = 100
    BOARD_SIZE = 8
    board = Board(CELL_SIZE, BOARD_SIZE, None)
    board.draw_move(3, 2)
    assert board.check_neighbors_color(4, 3, 0, 1) is True
    assert board.check_neighbors_color(4, 3, -1, -1) is False
    assert board.check_neighbors_color(4, 3, -1, 0) is False
    board.draw_move(2, 4)
    assert board.check_neighbors_color(2, 4, 1, -1) is True
    assert board.check_neighbors_color(4, 2, 1, 1) is False
    assert board.check_neighbors_color(4, 2, 1, 0) is False
    board.draw_move(5, 5)
    assert board.check_neighbors_color(3, 4, 1, 0) is True
    assert board.check_neighbors_color(3, 4, -1, 0) is False
    assert board.check_neighbors_color(3, 4, 1, -1) is False


def check_completion_status():
    CELL_SIZE = 100
    BOARD_SIZE = 8
    board = Board(CELL_SIZE, BOARD_SIZE, None)
    assert board.gc.game_over is False
    board.no_tile = 0
    board.check_completion_status()
    assert board.gc.game_over == 'win_win'
    for x in range(BOARD_SIZE-1):
        for y in range(BOARD_SIZE):
            board.draw_move(x, y)
    for y in range(BOARD_SIZE-1):
        board.draw_move(BOARD_SIZE-1, y)
    assert board.no_tile == 1
    assert board.gc.game_over is False
    board.check_completion_status()
    assert board.gc.game_over is not False
    assert board.gc.game_over == 'black'


def test_start_end_game():
    CELL_SIZE = 100
    BOARD_SIZE = 8
    board = Board(CELL_SIZE, BOARD_SIZE, None)
    gc = GameController(board, None, None)
    board.white = 6
    board.start_end_game()
    assert board.gc.game_over == 'white'
    board.black = 6
    board.gc.game_over = False
    board.start_end_game()
    assert board.gc.game_over == 'win_win'
    board.black = 8
    board.gc.game_over = False
    board.start_end_game()
    assert board.gc.game_over == 'black'
