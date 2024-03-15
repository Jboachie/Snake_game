from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 14, "normal" )
with open("data.txt", mode= "r") as hiscore:
    max_hiscore = int(hiscore.read())


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0,270)
        self.high_score = max_hiscore
        self.score = 0
        self.write(f"Score: {self.score} High score: {self.high_score}", False, ALIGNMENT, FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score} High score: {self.high_score} ", False, ALIGNMENT, FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode = 'w') as hiscore:
                hiscore.write(str(self.high_score))
            self.score = 0
            self.clear()
            self.write(f"Score: {self.score} High score: {self.high_score}", False, ALIGNMENT, FONT)
        else:
            self.score = 0
            self.clear()
            self.write(f"Score: {self.score} High score: {self.high_score}", False, ALIGNMENT, FONT)