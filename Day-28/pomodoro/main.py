import math
from tkinter import *

############################################

grey = "#B4B4B8"
orange = "#FC6736"
blue = "#40A2E3"
red = "#FF004D"
black = "#030637"
yellow = "#FF9800"
white = "#FFF6E9"
green = "#294B29"
pink = "#FFB996"
WORK_TIME_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


###########################  Reset ###################################

def reset_timer():
    w.after_cancel(timer)
    mark.config(text="")
    canvas.itemconfig(canvas_text, text="00:00")
    timer_label.config(text="Timer", foreground=black)
    global reps
    reps = 0


#######################  Timer mechanism ##############################


def start_timer():
    work_time = WORK_TIME_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(long_break)
        timer_label.config(text="Break", foreground=red)
    elif reps % 2 == 0:
        count_down(short_break)
        timer_label.config(text="Break", foreground=green)
    else:
        count_down(work_time)
        timer_label.config(text="Focus", foreground=orange)


def count_down(count):
    min_count = math.floor(count / 60)
    sec_count = count % 60
    if sec_count < 10:
        sec_count = f"0{sec_count}"
    if count >= 0:
        global timer
        timer = w.after(1000, count_down, count - 1)
        canvas.itemconfig(canvas_text, text=f"{min_count}:{sec_count}")
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps / 2)):
            marks += "✅"
        mark.config(text=marks)


############################       UI   ##################################

w = Tk()
w.config(background=grey, padx=50, pady=50)
w.title("POMODORO")

timer_label = Label(text="Timer", font=("fixedsys", 40, "bold"),
                    highlightthickness=0, background=grey, foreground=black)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=210, height=240, highlightthickness=0, background=grey)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_image)
canvas_text = canvas.create_text(107, 130, text="00:00", font=("italic", 40, "bold"), fill=white)
canvas.grid(column=1, row=1)

start_button = Button(text="START", background=pink, foreground=black, font=("meriyo", 20, "bold"),
                      highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="RESET", background=pink, foreground=black, font=("meriyo", 20, "bold"),
                      highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

mark = Label(text="", highlightthickness=0, background=grey)
mark.grid(row=2, column=1)

w.mainloop()
