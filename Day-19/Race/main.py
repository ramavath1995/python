
import turtle
from turtle import *
import random

POSITION = [(-380, -50), (-380, 50), (-380, 150), (-380, -150), (-380, 230), (-380, -230)]
colors = ["red", "black", "blue", "green", "brown", "orange"]


def borders():
    b1 = Turtle()
    b1.speed("fastest")
    b1.penup()
    b1.pensize(10)
    b1.goto(-400, 270)
    b1.pendown()
    b1.forward(800)
    b2 = Turtle()
    b2.speed("fastest")
    b2.penup()
    b2.pensize(10)
    b2.goto(-400, -270)
    b2.pendown()
    b2.forward(800)


def finish_line():
    b2 = Turtle()
    b2.speed("fastest")
    b2.penup()
    b2.pensize(10)
    b2.goto(370, -270)
    b2.setheading(90)
    b2.pendown()
    b2.forward(540)


s = Screen()
s.setup(800, 600)
s.title("Turtle Race")
borders()
finish_line()
turtles = []
for i in range(6):
    t = Turtle()
    t.speed("fastest")
    t.shape("turtle")
    t.color(colors[i])
    t.penup()
    t.goto(POSITION[i])
    turtles.append(t)
guess = s.textinput(title="Guess the winner", prompt=f"Which color turtle can win the race?: ").lower()
race_completed = False
while not race_completed:
    for racers in turtles:
        if racers.xcor() > 370:
            if guess == racers.color():
                turtle.hideturtle()
                turtle.color(racers.pencolor())
                turtle.write(f"You Win {racers.pencolor()} turtle won race", align="right", font=("roman", 20, "bold"))
            else:
                turtle.hideturtle()
                turtle.color(racers.pencolor())
                turtle.write(f"You Lose {racers.pencolor()} turtle won race", align="right", font=("roman", 20, "bold"))
            race_completed = True

        else:
            racers.forward(random.randint(0, 9))

s.exitonclick()
