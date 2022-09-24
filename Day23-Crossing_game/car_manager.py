from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self):
        self.car_list = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance =  random.randint(1, 6)
        if random_chance == 1:
            car = Turtle('square')
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.penup()
            car.goto(x=300, y=random.randint(-250, 250))
            car.setheading(180)
            self.car_list.append(car)

    def move(self):
        for car in self.car_list:
            car.forward(self.speed)

    def level_up(self):
        self.speed += MOVE_INCREMENT