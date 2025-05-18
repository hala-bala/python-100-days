from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position:tuple[int, int] = (0, 0)):
        super().__init__()
        self.score = 0
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x=position[0], y=position[1])

    def go_up(self):
        self.sety(self.ycor() + 20)

    def go_down(self):
        self.sety(self.ycor() - 20)