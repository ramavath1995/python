from turtle import Turtle, Screen

tim = Turtle()
s = Screen()
s.title("Square")
tim.hideturtle()
for i in range(4):
    tim.forward(200)
    tim.left(90)


s.exitonclick()
