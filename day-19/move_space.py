from turtle import Turtle, Screen

dan = Turtle()
screen = Screen()

def move_forward():
    dan.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()