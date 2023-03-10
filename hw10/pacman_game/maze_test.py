from maze import Maze
from game_controller import GameController


def test_constructor():
    g = GameController(600, 400)
    m = Maze(600, 400, 150, 450,
             100, 300, g)
    assert m.LEFT_VERT == 150
    assert m.RIGHT_VERT == 450
    assert m.TOP_HORIZ == 100
    assert m.BOTTOM_HORIZ == 300
    assert m.WIDTH == 600
    assert m.HEIGHT == 400
    assert m.gc is g
    assert m.dots.dots_left() == ((m.dots.WIDTH//m.dots.SPACING + 1) * 2 +
                                  (m.dots.HEIGHT//m.dots.SPACING + 1) * 2)


def test_eat_dots():
    g = GameController(600, 600)
    m = Maze(600, 600, 150, 450,
             150, 450, g)
    ds = m.dots
    dl = ds.dots_left()
    m.eat_dots(150, 450)
    assert ds.bottom_row[2].x == ds.SPACING*3
    assert ds.left_col[6].y == ds.SPACING*7
    assert ds.dots_left() == dl - 2
    m.eat_dots(25, 450)
    assert ds.bottom_row[0].x == ds.SPACING*1
    assert len(ds.bottom_row) == 6
    assert ds.dots_left() == dl - 4
