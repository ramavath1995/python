import turtle
from turtle import *
import pandas

image = "indian-map.gif"
s = Screen()
s.setup(600, 705)
s.addshape(image)
turtle.shape(image)

data = pandas.read_csv("indian_states.csv")
state_list = data.state.to_list()

guessed_states = []

while len(guessed_states) < 29:
    guess = s.textinput(title=f"States {len(guessed_states)}/{len(state_list)}",
                        prompt="Guess the state name").title()
    if guess == "Exit":
        missed_states = [state for state in state_list if state not in guessed_states]
        print(f"You missed: {missed_states} states")
        break

    if guess in state_list:
        guessed_states.append(guess)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.color("red")
        state_data = data[data.state == guess]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(f"{guess}", font=("roman", 10, "bold"))


s.exitonclick()

################ for get the state positions ###########
# def get(x, y):
#     print(x, y)
# turtle.onscreenclick(get)
# s.mainloop()
