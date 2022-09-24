class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.que_list = question_list
        self.score = 0

    def next_question(self):
        current_que = self.que_list[self.question_number]
        self.question_number += 1
        user_answer = input(f'Q.{self.question_number}: {current_que.que} (True/False) : ')
        self.check_answer(user_answer, current_que.ans)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print('That\'s Right')
        else:
            print('That\'s Wrong Answer')
        print(f'Correct Answer was {correct_answer}')
        print(f'Your Current Score is {self.score}/{self.question_number}\n')

    def still_has_question(self):
        return self.question_number < len(self.que_list)
        # if self.question_number < len(self.que_list):
        #     return True
        # else:
        #     return False
