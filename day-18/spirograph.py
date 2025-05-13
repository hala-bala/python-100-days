import random
from turtle import Turtle, Screen
from random import randint

MAX_COLORS = 255
dan = Turtle()
dan.pensize(1)
dan.speed('fastest')
screen = Screen()
screen.colormode(MAX_COLORS)


def random_color() -> (int, int, int):
    return randint(0, MAX_COLORS), randint(0, MAX_COLORS), randint(0, MAX_COLORS)

def main():
    number_of_circles = 50
    angle = 360 / number_of_circles
    for circle_number in range(number_of_circles + 1):
        dan.pencolor(random_color())
        dan.circle(100)
        dan.setheading(angle * circle_number)

main()
screen.exitonclick()