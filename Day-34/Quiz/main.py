from data import *
from question_model import *
from ui import *


question_bank = []

for questions in question_data:
    question = questions["question"]
    answer = questions["correct_answer"]
    question_bank.append(QuestionModel(question, answer))

quiz = QuizBrain(question_bank)
quiz.next_question()

tk_ui = TkInterface(quiz)
