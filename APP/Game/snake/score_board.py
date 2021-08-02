from turtle import Turtle


class ScoreCard(Turtle):

    def __init__(self):
        super().__init__()
        with open("score.txt") as data :
            self.high_score = int(data.read())
        self.score = 0
        self.penup()
        self.goto(0,350)
        self.hideturtle()
        self.color("white")
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.penup()
        self.write(f"Score: {self.score}      High Score: {self.high_score}", align="center", font=("Arial", 28, "normal"))

    def update(self):
        if self.score>self.high_score:
            self.high_score = self.score
            with open("score.txt", mode="w") as f:
                f.write(f"{self.high_score}")
        self.score = 0

        self.update_score_board()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.color("red")
        self.write(f"Game over 🥲 ", align="center", font=("Arial", 40, "normal"))
        self.goto(0, -40)
        self.color("red")
        self.write(f"\nFinal Score: {self.score}", align="center", font=("Arial", 35, "normal"))

    def increase(self):
        self.score+=1
        self.update_score_board()