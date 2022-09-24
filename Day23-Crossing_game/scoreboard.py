from turtle import Turtle
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-220, 260)
        self.write(arg=f"Level : {self.score} ", align="center", font=FONT)
        self.ratio = 1

    def new_level(self):
        self.clear()
        self.score += 1
        self.ratio *= .95
        self.write(arg=f"Level : {self.score} ", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)