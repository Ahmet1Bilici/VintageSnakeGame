from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')

class ScoardBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x=0, y=270)
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.goto(0,0)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)