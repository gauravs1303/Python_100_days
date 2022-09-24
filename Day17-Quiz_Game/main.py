from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for que in question_data:
    que_text = que["text"]
    que_ans = que['answer']
    new_que = Question(que_text, que_ans)
    question_bank.append(new_que)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print('\nYou\'ve completed the Quiz')
print(f'Your Final Score is {quiz.score}/{quiz.question_number}')