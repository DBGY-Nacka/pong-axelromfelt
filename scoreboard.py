from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 60, "normal")
POSITION = (0, 0)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color("white")
        self.penup()
        self.goto(POSITION)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"{self.left_score}  {self.right_score}",
                   align=ALIGNMENT, font=FONT,)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self, side):
        if side == "right":
            self.left_score += 1
        else:
            self.right_score += 1
        self.clear()
        self.update_scoreboard()
