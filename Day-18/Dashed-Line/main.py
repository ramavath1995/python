from turtle import *

tim = Turtle()
s = Screen()
s.title("Doted Lines")
tim.hideturtle()
tim.penup()
tim.goto(-300, 0)
tim.pendown()
for i in range(30):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()


s.exitonclick()
