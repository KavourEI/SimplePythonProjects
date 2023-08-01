from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = 'center'

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-220, 260)
        self.score = 1
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f" Level: {self.score}", align=ALIGNMENT, font=FONT)

    def lvl_score(self):
        self.score += 1
        self.update_score()

    def game_is_over(self):
        self.goto(0, 0)
        self.write("Game Over", align= ALIGNMENT, font=FONT)


