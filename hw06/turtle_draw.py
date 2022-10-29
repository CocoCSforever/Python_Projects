import turtle as t
import math


def main():
    """
    Draws a star with red ouline and yellow filled arms
    and the circle with blue outline and cyan fill
    """
    PIXELS = 500
    STAR_ANGLE = 36
    ANGLE_180 = 180
    radius = calculate_radius(PIXELS/2, STAR_ANGLE/2)
    # make pen object invisible
    # and keep pen up whenever a writing function is over or not running
    t.hideturtle()
    t.pu()

    draw_circle(radius)
    draw_star(radius, PIXELS, ANGLE_180-STAR_ANGLE)

    # wait on the user to close the window
    # instead of clicking mouse to terminate
    t.done()


def calculate_radius(a, b):
    """Calculate the radius with star segment of 500 pixels"""
    degree_in_radians = math.radians(b)
    cos_d = math.cos(degree_in_radians)
    return a/cos_d


def draw_circle(radius):
    t.pencolor("blue")
    t.fillcolor("cyan")
    t.setposition(0, -radius)

    t.pd()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.pu()


def draw_star(radius, length, turn_angle):
    t.pencolor("red")
    t.fillcolor("yellow")
    t.setposition(0, radius)
    t.setheading(turn_angle/2)

    t.pd()
    t.begin_fill()
    for i in range(5):
        draw_star_segment(turn_angle, length)
    t.end_fill()
    t.pu()


def draw_star_segment(turn_angle, length):
    t.right(turn_angle)
    t.forward(length)


main()
