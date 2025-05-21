import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        car = Turtle("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.setheading(180)
        car.penup()
        car.color(random.choice(COLORS))
        y_position = random.randint(-250, 250)
        car.goto(x=300, y=y_position)
        self.cars.append(car)

    def move_cars(self):
        cars_removed = []
        for car in self.cars:
            car.forward(self.speed)
            if car.xcor() < -320:
                cars_removed.append(car)
        for car in cars_removed:
            car.hideturtle()
            car.clear()
            self.cars.remove(car)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
        print(self.speed)