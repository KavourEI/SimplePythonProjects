from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position_x, position_y):
        super().__init__()
        self.color("white")
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position_x, position_y)

    def go_up(self):
        new_x = self.xcor()
        new_y = self.ycor() + 20
        self.goto(new_x, new_y)


    def go_down(self):
        new_x = self.xcor()
        new_y = self.ycor() - 20
        self.goto(new_x, new_y)