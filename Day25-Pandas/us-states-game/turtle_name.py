from turtle import Turtle


class StateName(Turtle):

    def __init__(self, name, x, y):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.write(f"{name},", font=("Arial", 8, "normal"))
