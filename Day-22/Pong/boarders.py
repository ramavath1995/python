from turtle import *


class Borders(Turtle):
    def __init__(self):
        super().__init__()
        self.top_border()
        self.bottom_border()
        self.left_border()
        self.right_border()
        self.center_line()

    def top_border(self):
        self.speed("fastest")
        self.penup()
        self.color("red")
        self.goto(-400, 300)
        self.pendown()
        self.pensize(20)
        self.forward(795)

    def bottom_border(self):
        self.speed("fastest")
        self.penup()
        self.color("red")
        self.goto(-400, -295)
        self.pendown()
        self.pensize(20)
        self.forward(795)

    def left_border(self):
        self.speed("fastest")
        self.penup()
        self.color("red")
        self.goto(-400, -295)
        self.setheading(90)
        self.pendown()
        self.pensize(20)
        self.forward(595)

    def right_border(self):
        self.speed("fastest")
        self.penup()
        self.color("red")
        self.goto(395, -295)
        self.setheading(90)
        self.pendown()
        self.pensize(20)
        self.forward(595)

    def center_line(self):
        self.speed("fastest")
        self.color("yellow")
        self.penup()
        self.goto(0, -295)
        self.setheading(90)
        self.pensize(1)
        self.pendown()
        self.forward(605)
