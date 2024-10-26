from turtle import *

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.update_score()

    def update_score(self):
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.color("white")
        self.goto(-380, 280)
        self.write(f"Level: {self.score}", font=("arial", 30, "bold"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.pensize(20)
        self.write(f"Game Over", font=("arial", 30, "bold"))
