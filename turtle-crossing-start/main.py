import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(key="Up", fun=player.move_up)
cars_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
i = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars_manager.move_cars()
    if player.ycor() > 280:
        player.reset()
        cars_manager.increase_speed()
        scoreboard.increase_level()
    if i % 6 == 0:
        cars_manager.create_car()
    for car in cars_manager.cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
    i += 1

screen.exitonclick()