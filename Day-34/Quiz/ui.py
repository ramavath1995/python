from quiz_brain import *
from tkinter import *

bg_color = "#114232"


class TkInterface:
    def __init__(self, quiz_b: QuizBrain):
        self.quiz = quiz_b
        self.w = Tk()
        self.w.title("Quiz Brain")
        self.w.config(background=bg_color, padx=50, pady=50)

        self.score_label = Label(background=bg_color, foreground="white")
        self.score_label.config(text=f"Score: 0", font=("aerial", 15, "normal"))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, background="white")
        self.c_text = self.canvas.create_text(150, 125,
                                              width=280,
                                              text="Some text here",
                                              fill=bg_color,
                                              font=("Helvetica", 15, "normal"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        correct_image = PhotoImage(file="images/true.png")
        wrong_image = PhotoImage(file="images/false.png")

        self.true_button = Button(image=correct_image, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=wrong_image, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)
        self.next_question()
        self.w.mainloop()

    def next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            que_text = self.quiz.next_question()
            self.canvas.itemconfig(self.c_text, text=que_text)
        else:
            self.canvas.itemconfig(self.c_text, text="You have reached end of the quiz")
            self.true_button.config(state="disable")
            self.false_button.config(state="disable")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")
        self.w.after(1000, self.next_question)


