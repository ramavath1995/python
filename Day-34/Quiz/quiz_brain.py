import html


class QuizBrain:
    def __init__(self, q_list):
        self.question_list = q_list
        self.question_number = 0
        self.score = 0
        self.current_question = None

    def next_question(self):
        self.current_question = self.question_list[self.question_number]

        text = html.unescape(self.current_question.question)
        self.question_number += 1
        q_text = f"Q.{self.question_number} {text}"
        return q_text

    def check_answer(self, user_answer):
        actual_answer = self.current_question.answer
        if actual_answer.title() == user_answer.title():
            self.score += 1
            return True
        else:
            return False

    def still_has_questions(self):
        if len(self.question_list) > self.question_number:
            return True
        else:
            return False
