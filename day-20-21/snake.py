from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

LEFT = 180
RIGHT = 0
UP = 90
DOWN = 270


def new_segment() -> Turtle:
    segment = Turtle('square')
    segment.color('white')
    segment.penup()
    return segment


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.snake_heading = RIGHT

    def create_snake(self):
        for _ in range(3):
            segment = new_segment()
            segment.goto(STARTING_POSITION[_])
            self.segments.append(segment)

    def move(self):
        for seg_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_number - 1].xcor()
            new_y = self.segments[seg_number - 1].ycor()
            self.segments[seg_number].goto(new_x, new_y)
        self.head.setheading(self.snake_heading)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.snake_heading = UP

    def down(self):
        if self.head.heading() != UP:
            self.snake_heading = DOWN

    def left(self):
        if self.head.heading() != RIGHT:
            self.snake_heading = LEFT

    def right(self):
        if self.head.heading() != LEFT:
            self.snake_heading = RIGHT

    def extend(self):
        segment = new_segment()
        segment.goto(self.segments[-1].position())
        self.segments.append(segment)
