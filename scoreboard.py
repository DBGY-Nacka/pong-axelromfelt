from turtle import Turtle
from time import sleep
ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")
FONT_WIN = ("Courier", 30, "normal")
FONT_NAME = ("Courier", 20, "normal")
POSITION = (0, 200)


class Scoreboard(Turtle):

    def __init__(self, screen):
        super().__init__()
        self.time = "0:0"
        self.left_name = ""
        self.right_name = ""
        self.left_score = 0
        self.right_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.info_message(screen)
        self.update_scoreboard()

    def new_round(self, screen, new_game=False):
        if new_game:
            self.left_score = 0
            self.right_score = 0
        countdown = 3
        for _ in range(4):
            self.clear()
            self.update_scoreboard()
            self.goto(0, 0)
            self.write(countdown, align=ALIGNMENT, font=FONT)
            screen.update()
            countdown -= 1
            sleep(1)
        self.update_scoreboard()

    def update_scoreboard(self, game_over=False):
        self.clear()

        self.goto(-150, 200)
        self.write(self.left_score, align=ALIGNMENT, font=FONT,)

        self.goto(-150, 180)
        self.write(self.left_name, align=ALIGNMENT, font=FONT_NAME)

        self.goto(150, 200)
        self.write(f"{self.right_score}", align=ALIGNMENT, font=FONT,)

        self.goto(150, 180)
        self.write(self.right_name, align=ALIGNMENT, font=FONT_NAME)

        self.goto(0, 200)
        self.write(self.time, align=ALIGNMENT, font=FONT)

        if game_over:
            self.goto(0, 0)

            if self.left_score > self.right_score:
                self.write(f"{self.left_name} wins",
                           align=ALIGNMENT, font=FONT_WIN)

            else:
                self.write(f"{self.right_name} wins",
                           align=ALIGNMENT, font=FONT_WIN)

    def display_time(self, new_time):
        if new_time != self.time:
            self.time = new_time
            print(new_time)
            self.update_scoreboard()

    def game_over(self):
        self.update_scoreboard(game_over=True)

    def increase_score(self, side):
        if side == "right":
            self.left_score += 1
        else:
            self.right_score += 1
        self.clear()
        self.update_scoreboard()

    def info_message(self, screen):
        self.write(
            "Keys:\nW/S to move the left player\nUp/Down to move the right player\nP to pause the game\nK to end the game early\n\ndisappears after six seconds", align=ALIGNMENT, font=FONT_NAME)
        screen.update()

        sleep(6)
        self.clear
