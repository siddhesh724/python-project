from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    question_objects = Question(i['text'], i['answer'])
    question_bank.append(question_objects)


quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("you successfully completed quiz")
print(f"total score is {quiz.score}/{len(question_bank)}")
