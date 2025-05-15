from turtle import Turtle
import random
from snake import MOVE_DISTANCE

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.refresh()


    def refresh(self):
        rand_x = random.randint(-14, 14) * MOVE_DISTANCE
        rand_y = random.randint(-14, 14) * MOVE_DISTANCE
        self.goto(rand_x, rand_y)
