import random
import turtle
from turtle import *

colors = [(56, 102, 140), (3, 234, 16), (3, 234, 95), (243, 2, 205), (2, 255, 219), (141, 91, 50), (12, 23, 55),
          (24, 53, 127), (61, 22, 11), (72, 117, 81), (58, 15, 26), (253, 30, 16), (126, 79, 102), (130, 30, 16),
          (0, 0, 0), (255, 0, 0), (70, 0, 0), (0, 255, 0), (0, 64, 0), (0, 128, 48), (0, 128, 205), (255, 0, 255),
          (0, 230, 255), (254, 1, 220), (213, 32, 30), (249, 254, 12), (254, 1, 1)]

turtle.colormode(255)
t = Turtle()
s = Screen()
s.title("Random Walk")
t.speed("fast")
angle = [90, 180, 270, 0]
t.hideturtle()
t.pensize(15)
for _ in range(200):
    head = t.heading()
    t.color(random.choice(colors))
    t.forward(20)
    t.setheading(random.choice(angle))


s.exitonclick()
