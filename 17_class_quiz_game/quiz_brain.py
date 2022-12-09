class QuizBrain:
    def __init__(self, q_list):
        self.quiz_number = 0
        self.quiz_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.quiz_number < len(self.quiz_list)

    def next_question(self):
        question = self.quiz_list[self.quiz_number]
        user_answer = input(f"q{self.quiz_number + 1} : {question.text} (True/False):")
        self.quiz_number += 1
        self.check_answer(user_answer, question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's Wrong")
        print(f"The correct answer was : {correct_answer}.")
        print(f"your score = {self.score}/{self.quiz_number}")
        print()
