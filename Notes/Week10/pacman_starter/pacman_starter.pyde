WIDTH = 500
HEIGHT = 500
PACMAN_SIZE = 100
PACMAN_COLOR = (1.0, 1.0, 0.0)
SPEED = 3
x = WIDTH/2
y = HEIGHT/2
x_add = 0
y_add = 0


def setup():
    size(WIDTH, HEIGHT)

    # the values are going to represent our RGB.
    # the range is going to be from zero to one.
    colorMode(RGB, 1)

    # pass three elements tuples, treat it as three elements
    fill(*PACMAN_COLOR)
    noStroke()


def draw():
    global x, y
    background(0)
    x = x + x_add
    y = y + y_add

    # if pacman moves completely beyond the right edge
    if (x > WIDTH + PACMAN_SIZE/2):
        # reset x value to the left side
        x = PACMAN_SIZE/2
    # if pacman is overlapping the right edge
    elif (x > WIDTH - PACMAN_SIZE/2):
        # the second pacman is only drawed when x falls within the range
        pacman(x - WIDTH, y)

    # if pacman moves completely beyond the bottom
    if (y > HEIGHT + PACMAN_SIZE/2):
        # reset x value to the top
        y = PACMAN_SIZE/2
    # if pacman is overlapping the bottom edge
    elif (y > HEIGHT - PACMAN_SIZE):
        # the second pacman is only drawed when x falls within the range
        pacman(x, y - HEIGHT)

    # if pacman moves completely beyond the left edge
    if (x < -(PACMAN_SIZE/2)):
        # reset x value to the right side
        x = WIDTH - PACMAN_SIZE/2
    # if pacman is overlapping the left edge
    elif (x < PACMAN_SIZE/2):
        # the second pacman is only drawed when x falls within the range
        pacman(x + WIDTH, y)

    # if pacman moves completely beyond the top edge
    if (y < -(PACMAN_SIZE/2)):
        # reset x value to the bottom
        y = HEIGHT - PACMAN_SIZE/2
    # if pacman is overlapping the top edge
    elif (y < PACMAN_SIZE/2):
        # the second pacman is only drawed when x falls within the range
        pacman(x, y + HEIGHT)

    pacman(x, y)


def pacman(x, y):
    "Draw Pacman to the screen"
    arc(x, y, PACMAN_SIZE, PACMAN_SIZE, radians(45), radians(315))


def keyPressed():
    global x_add, y_add
    if (key == CODED):
        if (keyCode == DOWN):
            x_add = 0
            y_add = SPEED
        elif (keyCode == UP):
            x_add = 0
            y_add = -(SPEED)
        elif (keyCode == LEFT):
            x_add = -(SPEED)
            y_add = 0
        elif (keyCode == RIGHT):
            x_add = SPEED
            y_add = 0
