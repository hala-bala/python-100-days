import random
from turtle import Turtle, Screen
from random import randint

MAX_COLORS = 255
dan = Turtle()
dan.pensize(15)
dan.speed('fastest')
screen = Screen()
screen.colormode(MAX_COLORS)

angles = [0, 90, 180, 270]

def random_color() -> (int, int, int):
    return randint(0, MAX_COLORS), randint(0, MAX_COLORS), randint(0, MAX_COLORS)

def main():
    for _ in range(200):
        dan.pencolor(random_color())
        dan.forward(30)
        dan.setheading(random.choice(angles))

main()
screen.exitonclick()