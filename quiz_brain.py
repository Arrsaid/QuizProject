class QuizBrain:
    def __init__(self, questions_list):
        self.questions_list = questions_list
        self.question_number = 0
        self.score = 0

    def steal_question(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.question_text} (True/False): ")
        self.check_answer(answer, current_question.answer)

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print("The correct answer is " + correct_answer)
        print(f"Your current score is {self.score}/{self.question_number}\n")
