from turtle import *
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.create_food()
        self.refresh_food()

    def create_food(self):
        self.speed("fastest")
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("red")

    def refresh_food(self):
        ball_x = random.randint(-350, 350)
        ball_y = random.randint(-250, 250)
        self.goto(ball_x, ball_y)
