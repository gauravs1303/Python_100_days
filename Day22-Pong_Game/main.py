from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from score import ScoreBoard

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')

screen.tracer(-1)

pong = Paddle()
ping = Paddle()
ping.setx(-350)

ball = Ball()
score = ScoreBoard()
screen.update()

screen.listen()
screen.onkeypress(key='Up', fun=pong.up)
screen.onkeypress(key='Down', fun=pong.down)

screen.onkeypress(key='g', fun=ping.up)
screen.onkeypress(key='b', fun=ping.down)
screen.update()
i = 0
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(.1)
    ball.forward(20)
    if ball.distance(pong) < 50 and ball.xcor() >= 330 or ball.distance(ping) < 50 and ball.xcor() <= -330:
        ball.forward(2)
        ball.change_direction()
        ball.forward(20)
    if ball.ycor() > 280 or ball.ycor() < -280:
        print(f'yes{i} & {ball.heading()}')
        ball.wall()
        print(f'yes{i} & {ball.heading()}')
        i+=1
        while not -270 < ball.ycor() < 270:
            ball.forward(10)

    # Finding left miss
    if ball.xcor() < -360:
        ball.goto(0, 0)
        score.r_point()
        ball.change_direction()

    # Finding left miss
    if ball.xcor() > 360:
        ball.goto(0, 0)
        score.l_point()
        ball.change_direction()

screen.exitonclick()