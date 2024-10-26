from turtle import *


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.speed("fastest")
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update()

    def update(self):
        self.goto(-30, 250)
        self.write(self.left_score, font=("arial", 30, "bold"))
        self.goto(10, 250)
        self.write(self.right_score, font=("arial", 30, "bold"))

    def increase_left(self):
        self.clear()
        self.left_score += 1
        self.update()

    def increase_right(self):
        self.clear()
        self.right_score += 1
        self.update()
