from turtle import *


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.text") as data:
            self.highscore = int(data.read())
        self.speed("fastest")
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 265)
        self.write(f"Score: {self.score} High score: {self.highscore}", font=("roman", 15, "bold"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} High score: {self.highscore}", font=("roman", 15, "bold"))

    def game_over(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.text", "a") as file:
                file.write(f"{self.highscore}")

        self.speed("fastest")
        self.goto(0, 0)
        self.color("orange")
        self.write(f"Game Over\nYour Score:{self.score}", font=("roman", 20, "bold"))
        self.score = 0
