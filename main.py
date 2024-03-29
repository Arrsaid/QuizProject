from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question = Question(item["text"], item["answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.steal_question():
    quiz.next_question()

print("You have completed the quiz!")
print(f"Your final score is: {quiz.score}/{len(question_bank)}")
