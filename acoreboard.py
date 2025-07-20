from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
                self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"score: {self.score} high score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
    def game_over_tail(self):
        self.goto(0, 0)
        self.write("hit tail.GAME OVER", align="center", font=("Arial", 20, "normal") )

    def game_over(self):
        self.goto(0, 0)
        self.write("hit wall.GAME OVER", align="center", font=("Arial", 20, "normal"))
    def add_point(self):
        self.score += 1
        self.update_scoreboard()














