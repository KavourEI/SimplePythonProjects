import random
from turtle import Turtle, Screen
screen = Screen()
screen.setup(width=800, height=900)
user_bet = screen.textinput(title='Make your bet', prompt='Which tutle wins the race? enter a color:\n'
                                                          'Red,Orange,Yellow,Green,Blue,Purple').lower()
screen.bgcolor('black')
colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
x_positions = [-150, -90, -30, 30, 90, 150]

all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colours[turtle_index])
    new_turtle.goto(x_positions[turtle_index], -430)
    new_turtle.left(90)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.ycor() > 420:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle won the race!")
            else:
                print(f'You lost. The {winning_color} turtle won the race.')

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()
