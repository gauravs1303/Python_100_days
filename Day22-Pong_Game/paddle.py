from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color('white')
        self.penup()
        self.setposition(x=350, y=0)

    def up(self):
        if self.ycor() < 230:
            y_cor = self.ycor() + 20
            self.goto(self.xcor(), y_cor)

    def down(self):
        if self.ycor() > -230:
            y_cor = self.ycor() - 20
            self.goto(self.xcor(), y_cor)
