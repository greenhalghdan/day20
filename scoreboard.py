from turtle import Turtle
ALIGNMENT = "center"
FONT= ("times new roman", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        file = open("data.txt")
        high_score_text = file.read()
        self.high_score = int(high_score_text)
        file.close()
        self.color("white")
        self.goto(0, 260)
        self.hideturtle()
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"Current score is: {self.current_score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.clear()
    #     self.goto(0,0)
    #     self.write(f"Game Over your score was: {self.current_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.current_score = 0
        self.print_score()
    def update_score(self):
        self.current_score += 1
