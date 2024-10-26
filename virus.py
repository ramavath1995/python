from turtle import *


s = Screen()
t = Turtle()
s.bgcolor("black")
t.pencolor("red")

t.penup()
t.goto(0, 200)
t.pendown()
a = 0
b = 0
while True:
    t.speed("fastest")
    t.fd(a)
    t.right(b)
    a += 3
    b += 1
    if b == 200:
        break
s.exitonclick()
