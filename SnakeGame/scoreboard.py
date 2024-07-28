from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.score = 0
        with open("data.txt") as f:
            self.high_score = int(f.read())
        self.update_scoreboard()
    
    def increase(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=('ArcadeClassic', 24, 'normal'))
    
    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as f:
                self.high_score = self.score
                f.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()