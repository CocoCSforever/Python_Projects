from spot import Spot
from stack import Stack

to_draw = Stack()

my_spot1 = Spot(100, 300)
my_spot2 = Spot(300, 100)


def setup():
    size(500, 400)


def draw():
    # grey
    background(180)
    my_spot1.display()
    my_spot2.display()

    for spot in to_draw.content:
        spot.display()


def mousePressed():
    to_draw.push(Spot(mouseX, mouseY))


def keyPressed():
    if key == 'x' or key == 'X':
        to_draw.pop()
        print("Undo last added spot")
