from turtle import Turtle
ALIGNMENT = "center"
FONT= ("times new roman", 24, "normal")
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
        self.write(f"Current score is: {self.current_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"game over your score was: {self.current_score}", align=ALIGNMENT, font=FONT)
    def update_score(self):
        self.current_score += 1
