from turtle import *

STARTING_POSITION = (0, -330)


class Racer(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.color("white")
        self.shape("turtle")
        self.shapesize(1.2)
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(10)
