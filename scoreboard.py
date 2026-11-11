from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.score_table()

    def increase_score(self):
        self.score += 1
        self.score_table()

    def score_table(self):
        self.clear()
        self.goto(-350,200)
        self.write(f"Score : {self.score}/50", font=("Arial", 20, "normal"))
