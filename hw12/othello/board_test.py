from board import Board


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
