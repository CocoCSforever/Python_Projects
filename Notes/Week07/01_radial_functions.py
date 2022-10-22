import turtle as t
import random as rnd
import math


def main():
    """
    Draws randomly positioned radial patterns repeatedly
    """
    width, height = setup()
    while True:
        x, y = get_random_coords(width, height)
        draw_radial(x, y)


def setup():
    """
    Sets up the screen and return width and height
    None -> Number Number
    """
    # RGB values for the cyan background color
    BG_COLOR = (0.8, 0.95, 0.9)
    screen = t.getscreen()
    screen.bgcolor(BG_COLOR)
    t.shape("turtle")
    t.delay(0)
    t.speed("fastest")
    t.pu()
    return screen.window_width(), screen.window_height()


def get_random_coords(width, height):
    """
    Return random pixel positions within a screen area
    Number, Number -> Number, Number
    """
    w = rnd.randint(0, width-1)
    h = rnd.randint(0, height-1)
    return w - width/2, h - height/2


def draw_radial(x, y):
    """
    Draws a single instance of the radial pattern
    Number, Number -> None
    """
    DEGS_IN_CIRC = 360
    INCR_DEGS = 12
    stroke_color = 'green'
    t.goto(x, y)
    for angle in range(0, DEGS_IN_CIRC, INCR_DEGS):
        t.setheading(angle)
        # Fill color will range from 0 to 1 based on the
        # angle. We use cosine to generate these values
        fill_color = (math.cos(math.radians(angle)) + 1)/2
        draw_blade(stroke_color, fill_color)


def draw_blade(stroke_color, fill_color):
    """
    Draws a single blae of the pattern
    Color Color -> None
    """
    BOTTOM_EDGE = 200
    OUTER_EDGE = 50
    BOTTOM_TIP_ANGLE = 60
    TOP_TIP_ANGLE = 130
    TOP_EDGE = 230
    t.pd()
    t.fillcolor(fill_color, fill_color, fill_color)
    t.begin_fill()
    t.pencolor(stroke_color)
    t.forward(BOTTOM_EDGE)
    t.left(BOTTOM_TIP_ANGLE)
    t.forward(OUTER_EDGE)
    t.left(TOP_TIP_ANGLE)
    t.forward(TOP_EDGE)
    t.end_fill()
    t.pu()


main()
