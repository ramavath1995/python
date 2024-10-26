from turtle import *

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.snake_length = []
        self.create_snake()

    def create_snake(self):
        for i in POSITIONS:
            self.add_snake(i)

    def add_snake(self, i):
        t = Turtle()
        t.speed("fastest")
        t.penup()
        t.color("white")
        t.shape("square")
        t.goto(i)
        self.snake_length.append(t)

    def move_forward(self):
        for i in range(len(self.snake_length) - 1, 0, -1):
            new_x = self.snake_length[i - 1].xcor()
            new_y = self.snake_length[i - 1].ycor()
            self.snake_length[i].goto(new_x, new_y)
        self.snake_length[0].forward(20)

    def extend_snake(self):
        self.add_snake(self.snake_length[-1].position())

    def move_up(self):
        if self.snake_length[0].heading() != 270:
            self.snake_length[0].setheading(90)

    def move_down(self):
        if self.snake_length[0].heading() != 90:
            self.snake_length[0].setheading(270)

    def move_left(self):
        if self.snake_length[0].heading() != 0:
            self.snake_length[0].setheading(180)

    def move_right(self):
        if self.snake_length[0].heading() != 180:
            self.snake_length[0].setheading(0)
