from time import sleep
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

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
while game_is_on:
    sleep(0.1)
    snake.move()
    screen.update()
    if snake.head.distance(food) < 10:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    head_x = snake.head.xcor()
    head_y = snake.head.ycor()
    if head_x >= 300:
        snake.head.setx(-300)
    elif head_x <= -300:
        snake.head.setx(300)
    elif head_y >= 300:
        snake.head.sety(-300)
    elif head_y <= -300:
        snake.head.sety(300)
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()