from tkinter import *
from quiz_brain import QuizBrain
import time
THEME_COLOR = "#375362"


class QuizzerUI:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title('Quizzer')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score = 0
        self.label_score = Label(text=f"Score : {self.score}", fg='white', bg=THEME_COLOR, highlightthickness=0)
        self.label_score.grid(column=1, row=0, pady=20)
        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.text_que = self.canvas.create_text(150, 125, width=280, text='Que:....', font=('Arial', 20, 'italic'))
        self.canvas.grid(column=0, row=1, columnspan=2)
        right_pic = PhotoImage(file='images/true.png')
        self.right_button = Button(image=right_pic, highlightthickness=0, command=self.true_pressed)
        self.right_button.grid(column=0, row=2, pady=50)
        wrong_pic = PhotoImage(file='images/false.png')
        self.wrong_button = Button(image=wrong_pic, highlightthickness=0, command=self.false_pressed)
        self.wrong_button.grid(column=1, row=2)
        self.next_que()

        self.window.mainloop()

    def next_que(self):
        curr_que = self.quiz.next_question()
        if curr_que:
            self.canvas.itemconfig(self.text_que, text=curr_que)
            self.canvas.config(bg='white')
        else:
            self.canvas.config(bg='grey')
            self.canvas.itemconfig(self.text_que, text=f'You\'ve completed the quiz\nFinal Score = '
                                                       f'{self.score}/{len(self.quiz.question_list)}')
            self.wrong_button.destroy()
            self.right_button.destroy()
            self.label_score.destroy()

    def true_pressed(self):
        if self.quiz.check_answer("True"):
            self.score += 1
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.label_score.config(text=f"Score : {self.score}")
        self.window.after(1000, self.next_que)

    def false_pressed(self):
        if self.quiz.check_answer("False"):
            self.score += 1
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.label_score.config(text=f"Score : {self.score}")
        self.window.after(1000, self.next_que)