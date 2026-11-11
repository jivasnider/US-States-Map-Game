from turtle import Turtle, Screen
import pandas
from scoreboard import Scoreboard
import random

COLORS = ["yellow", "gold", "orange", "red",
          "maroon", "violet", "magenta", "purple", "navy","blue",
          "skyblue", "cyan", "turquoise", "lightgreen","green",
          "darkgreen", "chocolate", "brown", "black", "gray"]

screen = Screen()
image = "blank_states_img.gif"
screen.addshape(image)
screen.title("US States")

tim = Turtle()
tim.shape(image)
tum = Turtle()

scoreboard = Scoreboard()

data = pandas.read_csv("50_states.csv")
df = data["state"].to_list()

guessed_again = ""
guessed_states = []
while len(guessed_states) < 50:

    user_answer = screen.textinput(title="US State Game", prompt=f"{guessed_again}Enter a state name: \nType 'Exit' to exit.").title()
    if user_answer == "Exit":
        break
    if user_answer in guessed_states:
        guessed_again = "You've already guessed it! "
    elif user_answer in df:
        guessed_again = ""
        loc = data[data.state == user_answer]
        x_loc = loc["x"].to_list()
        y_loc = loc["y"].to_list()
        tum.color(random.choice(COLORS))
        tum.goto(x_loc[0], y_loc[0])
        tum.write(user_answer)
        scoreboard.increase_score()
        guessed_states.append(user_answer)

states_to_learn = []
for states in df:
    if states not in guessed_states:
        states_to_learn.append(states)

data_states_to_learn = pandas.DataFrame(states_to_learn)
data_states_to_learn.to_csv("states_to_learn.csv")

screen.exitonclick()