from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    text = data["text"]
    answer = data["answer"]
    question_bank.append(Question(q_answer=answer, q_text=text))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()