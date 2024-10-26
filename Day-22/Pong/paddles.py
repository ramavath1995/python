from turtle import *


class Paddles(Turtle):

    def __init__(self, p):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.color("white")
        self.shape("square")
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.goto(p)

    def move_up(self):
        self.forward(10)

    def move_down(self):
        self.back(10)
