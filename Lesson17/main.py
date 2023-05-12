from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]

    question_obj = Question(question_text, question_answer)
    question_bank.append(question_obj)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz.")
print(f"Your final score was {quiz.score}/{quiz.question_number}")

