class QuizBrain:
    def __init__(self, q_list):
        self.question_list = q_list
        self.question_number = 0
        self.score = 0
        # self.next_question()

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user = input(f"Q.{self.question_number} {current_question.question} is (True/False): ").title()
        self.check_answer(current_question.answer, user)

    def check_answer(self, actual_answer, user_answer):
        if actual_answer == user_answer:
            self.score += 1
            print("You're Right")
            print(f"Your current score is {self.score}/{len(self.question_list)}")
            return True
        else:
            print(" you're Wrong")
            print(f"Correct answer is {actual_answer}")
            print(f"Your current score is {self.score}/{len(self.question_list)}")
            return False

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
