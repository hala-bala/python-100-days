from turtle import Turtle, Screen

STEPS = (10,)

dan = Turtle()
screen = Screen()

def move_forward():
    dan.forward(STEPS[0])

def move_backwards():
    dan.backward(STEPS[0])

def move_clockwise():
    dan.setheading(dan.heading() + STEPS[0])

def move_counter_clockwise():
    dan.setheading(dan.heading() - STEPS[0])

def clear():
    dan.clear()
    dan.penup()
    dan.home()
    dan.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_clockwise)
screen.onkey(key="d", fun=move_counter_clockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()