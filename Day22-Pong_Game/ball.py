from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        # self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color('pink')
        self.penup()
        self.setheading(random.randint(-75, 75))

    def change_direction(self):
        self.setheading(random.randint(-60, 60) + 180 + self.heading())

    def wall(self):
        if self.ycor() > 280:
            if self.heading() < 90 or self.heading() > 270:
                self.right(90)
            elif self.heading() > 90 or self.heading() < 270:
                self.left(90)
        elif self.ycor() < -280:
            if self.heading() <= 90 or self.heading() > 270:
                self.left(90)
            elif self.heading() > 90 or self.heading() < 270:
                self.right(90)
