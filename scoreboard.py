from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.color("white")
        self.goto(0, 260)
        self.hideturtle()
        self.print_score()


    def print_score(self):
        self.clear()
        self.write(f"Current score is: {self.current_score}", align="center", font=("times new roman", 24, "normal"))


    def update_score(self):
        self.current_score += 1
