import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
screen.listen()
screen.onkeypress(key='Up', fun=player.up)
screen.onkeypress(key='Down', fun=player.down)

score1 = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1 * score1.ratio)
    screen.update()
    cars.create_car()
    cars.move()
    if player.ycor() >= 280:
        player.start_over()
        score1.new_level()
        cars.level_up()
    for car in cars.car_list:
        if player.distance(car) < 20:
            score1.game_over()
            game_is_on = False

screen.exitonclick()