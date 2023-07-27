from turtle import Screen, Turtle
from Snake import Snake
from food import Food
from Scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('Black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scorebard = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Coalition with food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend_snake()
        scorebard.increase_score()

    # Detect collisions with wall
    if snake.head.xcor()> 290 or snake.head.xcor() < -290 or snake.head.ycor()> 290 or snake.head.ycor() < -290:
        game_is_on = False
        scorebard.game_over()

    # Detect collisions with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10 :
            game_is_on = False
            scorebard.game_over()


screen.exitonclick()