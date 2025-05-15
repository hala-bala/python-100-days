import random
from turtle import Turtle, Screen

class MyTurtle(Turtle):
    def __init__(self, color: str, start_position: int):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color(color)
        self.goto(x=-230, y=start_position)


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color (red, blue, green, yellow, purple, orange): ")
colors = ["red", "blue", "green", "yellow", "purple", "orange"]

spacing = 50
position = int((len(colors) * spacing) / 2)
for turtle_index in range(0, 6):
    turt = MyTurtle(color=colors[turtle_index], start_position=position)
    position -= spacing

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in screen.turtles():
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() >= 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

screen.exitonclick()