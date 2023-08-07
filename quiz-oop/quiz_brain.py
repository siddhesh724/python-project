class QuizBrain:
    def __init__(self, q_list):
        self.question_no = 0
        self.score = 0
        self.question_list = q_list

    def still_has_question(self):
        if self.question_no == len(self.question_list):
            return False
        else:
            return True

    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        user_answer = input(f"Q.{self.question_no}: {current_question.text} (True/False): ")
        self.correct_answer(user_answer, current_question.answer)

    def correct_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("you got it right")
            self.score += 1
            print(f"score is {self.score}/{self.question_no}")

        else:
            print("that wrong")
            print(f"score is {self.score}/{self.question_no}")
        print(f"correct ans was: {correct_answer}. ")
        print("\n")
