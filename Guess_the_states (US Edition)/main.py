import pandas as pd
import turtle

df = pd.read_csv('50_states.csv', delimiter=',')

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []

while len(guessed_states) < 50:
    user_answer = screen.textinput(title=f"{len(guessed_states)}/50 Guess all the States",
                                   prompt="What are the states' names?").title()
    all_states = df.state.tolist()
    if user_answer == 'Exit':
        missed_ones = [i for i in all_states if i not in guessed_states]
        mos = pd.DataFrame(missed_ones)
        mos.to_csv("States_missed.csv")
        break
    if user_answer in all_states and user_answer not in guessed_states:
        guessed_states.append(user_answer)
        t = turtle.Turtle()

        t.hideturtle()
        t.penup()
        correct_data = df[df.state == user_answer]
        t.goto(int(correct_data.x), int(correct_data.y))
        t.write(user_answer)