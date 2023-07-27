from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_back():
    tim.backward(10)

def turn_left():
    new_heading = tim.hea   ding() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clearscreen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def penUp():
    tim.penup()

def penDown():
    tim.pendown()

screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_back)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='c', fun=clearscreen)
screen.onkey(key='=', fun=penUp)
screen.onkey(key='-', fun=penDown)

screen.exitonclick()