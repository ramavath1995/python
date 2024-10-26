from turtle import *


class Road(Turtle):
    def __init__(self):
        super().__init__()
        self.start_point()
        self.end_point()

    def start_point(self):
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.goto(400, -260)
        self.setheading(180)
        self.pensize(10)
        self.pendown()
        self.forward(800)

    def end_point(self):
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.goto(400, 260)
        self.setheading(180)
        self.pensize(10)
        self.pendown()
        self.forward(800)
