from turtle import *

t = Turtle()
s = Screen()
s.title("E Sketch")


def move_forward():
    t.forward(10)


def move_backward():
    t.backward(10)


def clock_direction():
    t.right(10)


def anti_clock():
    t.left(10)


pen_color = s.textinput(title="Pen color", prompt="Which color sketch do you want?")
t.color(pen_color)
s.listen()
onkey(move_forward, "Right")
onkey(move_backward, "Left")
onkey(clock_direction, "c")
onkey(anti_clock, "a")

s.exitonclick()
