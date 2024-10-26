import random
from tkinter import *
import pandas

#  ----------------------------- read csv ------------------------------------------------
try:
    words_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = words_data.to_dict(orient="records")

current_card = {}
words_to_learn = {}


def next_card():
    global current_card, flip_timer
    w.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card['french'], fill="black")
    canvas.itemconfig(can_image, image=front_photo)
    flip_timer = w.after(3000, flip_card)


# ------------------------------  Flip_card   -----------------------------------------------

def flip_card():
    canvas.itemconfig(can_image, image=back_photo)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card['english'], fill="white")


# ------------------------------  saving unknown words   -----------------------------------------------
def is_known():
    to_learn.remove(current_card)
    my_data = pandas.DataFrame(to_learn)
    my_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ------------------------------  UI Setup   -----------------------------------------------

sage = "#59B4C3"

w = Tk()
w.title("Flash Card")
w.config(background=sage, padx=50, pady=50)

flip_timer = w.after(3000, flip_card)

back_photo = PhotoImage(file="images/card_back.png")
front_photo = PhotoImage(file="images/card_front.png")

canvas = Canvas(height=526, width=800, highlightthickness=0, background=sage)
can_image = canvas.create_image(400, 263, image=front_photo)
title = canvas.create_text(380, 170, text="French", font=("Helvetica", 45, "normal"))
word = canvas.create_text(380, 320, text="word", font=("Helvetica", 70, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_photo = PhotoImage(file="images/wrong.png")
correct_photo = PhotoImage(file="images/right.png")

wrong_button = Button(image=wrong_photo, highlightthickness=0, background=sage, command=next_card)
wrong_button.config(padx=30, pady=40)
wrong_button.grid(row=1, column=0)

right_button = Button(image=correct_photo, highlightthickness=0, background=sage, command=is_known)
right_button.grid(row=1, column=1)

next_card()
w.mainloop()
