from turtle import Turtle
from time import sleep
ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")
FONT_NAME = ("Courier", 20, "normal")
POSITION = (0, 200)


class Scoreboard(Turtle):

    def __init__(self, left_name, right_name):
        super().__init__()
        self.left_name = left_name
        self.right_name = right_name
        self.left_score = 0
        self.right_score = 0
        self.color("white")
        self.penup()
        self.update_scoreboard()
        self.hideturtle()

    def new_round(self, screen):
        time = 3
        for _ in range(4):
            self.clear()
            self.update_scoreboard()
            self.goto(0, 0)
            self.write(time, align=ALIGNMENT, font=FONT)
            screen.update()
            time -= 1
            sleep(1)
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self, game_over=False):

        self.goto(-100, 200)
        self.write(self.left_score, align=ALIGNMENT, font=FONT,)

        self.goto(-100, 180)
        self.write(self.left_name, align=ALIGNMENT, font=FONT_NAME)

        self.goto(100, 200)
        self.write(f"{self.right_score}", align=ALIGNMENT, font=FONT,)

        self.goto(100, 180)
        self.write(self.right_name, align=ALIGNMENT, font=FONT_NAME)

        if game_over:
            self.goto(0, 0)
            if self.left_score > self.right_score:
                self.write(f"left player wins")
            else:
                self.write(f"right player wins")

    def game_over(self):
        self.update_scoreboard(game_over=True)

    def increase_score(self, side):
        if side == "right":
            self.left_score += 1
        else:
            self.right_score += 1
        self.clear()
        self.update_scoreboard()
