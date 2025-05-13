import turtle
import random

turtle.colormode(255)

colors = [(195, 159, 119), (146, 87, 50), (51, 105, 140), (135, 167, 184), (141, 69, 91), (188, 144, 159), (15, 28, 57),
          (181, 153, 35), (56, 26, 15), (61, 20, 34), (135, 177, 164), (53, 121, 97), (218, 202, 134), (126, 31, 53),
          (184, 92, 117), (143, 30, 18), (15, 47, 34), (16, 96, 60), (221, 174, 185), (194, 96, 80), (61, 161, 144),
          (25, 55, 121), (57, 156, 172), (85, 84, 17), (164, 206, 197), (226, 175, 167), (14, 86, 99), (108, 121, 160),
          (163, 204, 210), (181, 187, 211), (242, 198, 9)]


dan = turtle.Turtle()
dan.penup()
dan.hideturtle()
dan.setheading(225)
dan.forward(350)
dan.setheading(0)

number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    dan.dot(20, random.choice(colors))
    dan.forward(50)

    if dot_count % 10 == 0:
        dan.setheading(90)
        dan.forward(50)
        dan.setheading(180)
        dan.forward(500)
        dan.setheading(0)


screen = turtle.Screen()
screen.exitonclick()