from tkinter import *
import requests

API = "https://api.kanye.rest"
BLUE = "#59D5E0"


def get_quote():
    response = requests.get(API)
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(canvas_text, text=quote)


w = Tk()
w.title("Kanye Quote")
w.config(background=BLUE, padx=50, pady=50)

photo_image = PhotoImage(file="background.png")
button_photo = PhotoImage(file="kanye.png")

canvas = Canvas(width=300, height=414, background=BLUE, highlightthickness=0)
canvas.create_image(150, 207, image=photo_image)
canvas_text = canvas.create_text(150, 170, width=250, text="Hello good morning", font=("Helvetica", 20, "bold"))
canvas.grid(row=0, column=0)


kanye_button = Button(image=button_photo, command=get_quote)
kanye_button.config(background=BLUE, highlightthickness=0)
kanye_button.grid(row=1, column=0)

w.mainloop()
