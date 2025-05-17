from time import sleep
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

SLEEP_TIME = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

screen.update()
game_is_on = True


def move_snake_to_other_side(head_x: int, head_y: int) -> None:
    if head_x > 300:
        snake.head.setx(-300)
    elif head_x < -300:
        snake.head.setx(300)
    elif head_y > 300:
        snake.head.sety(-300)
    elif head_y < -300:
        snake.head.sety(300)


while game_is_on:
    sleep(SLEEP_TIME)
    snake.move()
    screen.update()
    if snake.head.distance(food) < 10:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    move_snake_to_other_side(snake.head.xcor(), snake.head.ycor())
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()