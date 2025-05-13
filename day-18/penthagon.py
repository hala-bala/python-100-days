from turtle import Turtle, Screen
from random import randint

MAX_COLORS = 255
dan = Turtle()
screen = Screen()
screen.colormode(MAX_COLORS)

def draw_shape(number_of_sides: int, color :(int ,int ,int )):
    angle = 360 / number_of_sides
    dan.pencolor(color)
    for _ in range(0, number_of_sides):
        dan.forward(100)
        dan.right(angle)

def main():
    for i in range(3,11):
        color = (randint(0, MAX_COLORS), randint(0, MAX_COLORS), randint(0, MAX_COLORS))
        draw_shape(i, color)

if __name__ == "__main__":
    main()
    screen.exitonclick()
