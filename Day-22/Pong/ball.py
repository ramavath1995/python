from turtle import *


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.x_move = 8
        self.y_move = 8
        self.shape("circle")
        self.sleep_time = 0.5

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def x_bounce(self):
        self.x_move *= -1
        self.sleep_time *= 0.9

    def y_bounce(self):
        self.y_move *= -1

    def refresh(self):
        self.goto(0, 0)
        self.sleep_time = 0.5
        self.x_bounce()
