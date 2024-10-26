from tkinter import *

w = Tk()
w.title("Miles to KM converter")


def converter():
    m = float(entry.get())
    km = m * 1.609344
    a = round(km, 2)
    answer.config(text=a)


entry = Entry(width=5, background="yellow", font=("arial", 20, "bold"))
entry.focus()
entry.grid(column=1, row=0)

label1 = Label(text="Miles", font=("arial", 20, "normal"))
label1.grid(row=0, column=2)

label2 = Label(text="is equals to", font=("arial", 20, "normal"))
label2.grid(column=0, row=1)

answer = Label(text="0", font=("arial", 20, "normal"), background="pink")
answer.grid(column=1, row=1)

km = Label(text="KM", font=("arial", 20, "normal"), background="green")
km.grid(row=1, column=2)

button = Button(text="Calculate", font=("arial", 20, "normal"), command=converter, background="orange")
button.grid(row=2, column=1)

w.mainloop()
