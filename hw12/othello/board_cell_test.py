from board_cell import BoardCell


def test_constructor():
    CELL_SIZE = 100
    bc = BoardCell(CELL_SIZE, CELL_SIZE, CELL_SIZE)
    bc_2 = BoardCell(7*CELL_SIZE, 7*CELL_SIZE, CELL_SIZE)
    assert bc.x == CELL_SIZE
    assert bc.y == CELL_SIZE
    assert bc_2.x == 7*CELL_SIZE
    assert bc_2.y == 7*CELL_SIZE
    assert bc.CELL_SIZE == CELL_SIZE
    assert bc.tile is False
    assert bc.WHITE == (255, 255, 255)
    assert bc.BLACK == (10, 10, 10)
    assert bc.tile_color is None
    assert bc.PIXEL == 90
    CELL_SIZE = 50
    bc = BoardCell(CELL_SIZE, CELL_SIZE, CELL_SIZE)
    assert bc.x == CELL_SIZE
    assert bc.y == CELL_SIZE
    assert bc.CELL_SIZE == CELL_SIZE
    CELL_SIZE = 25
    bc = BoardCell(CELL_SIZE, CELL_SIZE, CELL_SIZE)
    assert bc.x == CELL_SIZE
    assert bc.y == CELL_SIZE
    assert bc.CELL_SIZE == CELL_SIZE


def test_draw():
    """It calls setup_tile(tested below)
    and a graphical function draw_self"""
    pass


def test_setup_tile():
    CELL_SIZE = 100
    bc = BoardCell(CELL_SIZE, CELL_SIZE, CELL_SIZE)
    bc_2 = BoardCell(7*CELL_SIZE, 7*CELL_SIZE, CELL_SIZE)
    bc.setup_tile(True)
    bc_2.setup_tile(False)
    assert bc.tile_color == bc.WHITE
    assert bc_2.tile_color == bc_2.BLACK
    assert bc.tile is True
    assert bc_2.tile is True
    bc.setup_tile(False)
    assert bc.tile_color == bc.BLACK


def test_draw_self():
    """draw_self is a graphical function"""
    pass
