from time import sleep
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball

def main():
    screen = Screen()
    screen.title("Pong")
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.tracer(0)

    r_paddle = Paddle((350,0))
    l_paddle = Paddle((-350,0))

    ball = Ball()

    screen.listen()
    screen.onkey(key="Up", fun=r_paddle.go_up)
    screen.onkey(key="w", fun=l_paddle.go_up)
    screen.onkey(key="Down", fun=r_paddle.go_down)
    screen.onkey(key="s", fun=l_paddle.go_down)

    game_is_on = True
    while game_is_on:
        sleep(0.1)
        screen.update()
        ball.move()
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_x()

        if ball.xcor() > 380:
            ball.reset_position()
            r_paddle.score += 1
            print(f"Right paddle score: {r_paddle.score}")

        if ball.xcor() < -380:
            ball.reset_position()
            l_paddle.score += 1
            print(f"Left paddle score: {l_paddle.score}")

    screen.exitonclick()

if __name__ == "__main__":
    main()