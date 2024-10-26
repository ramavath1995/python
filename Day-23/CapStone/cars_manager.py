import random
from turtle import *

X_POSITIONS = 400
Y_POSITIONS = [-220, -180, -140, -100, -60, -20, 20, 60, 100, 140, 180, 220]
COLORS = ["red", "pink", "blue", "green", "brown", "orange", "maroon", "indigo", "yellow", "orange"]
STARTING_MOVE = 5
MOVE_INCREMENT = 2


class CarsManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE

    def create_car(self):
        chance = random.randint(0, 12)
        if chance == 1:
            new_car = Turtle("square")
            new_car.speed("fastest")
            new_car.penup()
            new_car.shapesize(1, 2)
            new_car.setheading(180)
            new_car.goto(X_POSITIONS, random.choice(Y_POSITIONS))
            new_car.color(random.choice(COLORS))
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.fd(self.car_speed)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT
