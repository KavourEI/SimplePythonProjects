import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title('Turtle Race Game')

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    #Detect the collision with a car:
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_is_over()


    # Detect the collision with the upper border:
    if player.distance(0,280) == 10:
        player.reset_pos()
        scoreboard.lvl_score()
        car_manager.level_up()

    car_manager.create_cars()
    car_manager.move_cars()


screen.exitonclick()