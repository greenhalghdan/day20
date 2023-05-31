from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.CURRENT_SCORE = 0
        self.color("white")
        self.goto(0, 280)
        self.hideturtle()
        self.print_score()

        #self.penup()

    def print_score(self):
        self.clear()
        self.write(f"Current score is: {self.CURRENT_SCORE}", align="center")


    def update_score(self):
        self.CURRENT_SCORE += 1
