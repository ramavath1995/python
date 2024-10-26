from tkinter import *


def button_clicked():
    new_text = entry.get()
    label.config(text=new_text)


################### Window  ##########################


w = Tk()
w.title("Tk Demo")

################### Label  ##########################

label = Label(text="Dhakya", background="green", highlightthickness=1, font=("roman", 20, "bold"),
              foreground="yellow")
label.grid(row=0, column=0)

button = Button(text="Click", background="red", command=button_clicked)
button.grid(row=1, column=0)

################### Entry  ##########################
entry = Entry(width=20, background="pink")
entry.focus()
entry.grid(row=2, column=0)
################### Text  ##########################
text = Text(width=30, height=5)
text.focus()
text.insert(index=END, chars="checking for text")
print(text.get("1.0", END))
text.grid(row=3, column=0)


#########   Spinbox #############


def spinbox():
    print(spin.get())


spin = Spinbox(from_=0, to=20, width=5, command=spinbox)
spin.grid(row=4, column=0)


#################### Scale ##################


def scale_used(values):
    print(values)


scale = Scale(from_=0, to=100, command=scale_used)
scale.grid(row=5, column=0)


####################  Checkbutton ##################


def check_button_status():
    if check_status.get() == 1:
        print("ON")

    else:
        print("OFF")


check_status = IntVar()
check_button = Checkbutton(text="is_on?", variable=check_status, command=check_button_status)
check_button.grid(row=6, column=0)
###################### Radio buttons ###############


def status_radio():
    if radio_status.get() == 1:
        print("Option1 selected")
    else:
        print("None")


radio_status = IntVar()
radio = Radiobutton(text="Option1", value=1, variable=radio_status, command=status_radio)
radio.grid(row=7, column=0)

################## List  ########################
listbox = Listbox()

w.mainloop()
