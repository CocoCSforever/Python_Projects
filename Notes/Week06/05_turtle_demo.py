import turtle as t

t.shape("turtle")  # triangle, arrow, classic, circle
t.hideturtle()  # Hides the turtle
t.delay(1)  # delay between each action
t.speed("slowest")  # for every action, the speed of the turtle
# Speedstrings are mapped to speedvalues as follows:
# “fastest”: 0
# “fast”: 10
# “normal”: 6
# “slow”: 3
# “slowest”: 1


t.pensize(5)
t.pencolor("red")
t.fillcolor("yellow")

t.pd()  # pendown
t.begin_fill()
t.forward(200)
t.left(90)
t.forward(100)
t.left(90)
t.forward(200)
t.left(90)
t.forward(100)
t.end_fill()

t.pu()  # penup

t.goto(-100, -50)
t.pencolor("purple")
t.fillcolor("cyan")
t.setheading(45)

t.pd()
t.begin_fill()
# default to the right direction
t.forward(200)
t.left(90)
t.forward(100)
t.left(90)
t.forward(200)
t.left(90)
t.forward(100)
t.end_fill()
t.pu()


t.exitonclick()

t.done()
