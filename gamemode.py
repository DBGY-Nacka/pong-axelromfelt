from turtle import textinput, numinput
from datetime import datetime as Time, timedelta as td
from time import sleep


def time_diff(start_time, end_time):
    # start_time = datetime.strptime(start_time, "%H:%M:%S")
    # end_time = datetime.strptime(end_time, "%H:%M:%S")
    time_diff_res = end_time - start_time

    days = time_diff_res.days
    hours = time_diff_res.seconds // 3600
    minutes = (time_diff_res.seconds // 60) % 60
    seconds = time_diff_res.seconds % 60

    return [time_diff_res, minutes, seconds]


class Gamemode():
    def __init__(self):
        self.time = False
        self.score = False
        self.infinit = False
        self.pick_gamemode()
        self.new_game()

    def new_game(self):
        if self.time:
            self.time_var = Time.now()+td(minutes=(self.end_time))
        else:
            self.time_var = Time.now()

    def new_round(self):
        if self.time:
            self.time_var += td(seconds=4)
        else:
            self.time_var -= td(seconds=4)

    def pick_gamemode(self):
        self.time = False
        self.score = False
        self.infinit = False

        time_mode = ["time", "t"]
        score_mode = ["s", "score"]
        infinit_mode = ["i", "inf", "infinit", "infinity"]
        player_choice = ""
        while player_choice not in [*time_mode, *score_mode, *infinit_mode]:
            player_choice = textinput(
                "Pick gamemode", "Time or score based or infinit").lower()

        if player_choice in time_mode:
            self.time = True

        elif player_choice in score_mode:
            self.score = True

        elif player_choice in infinit_mode:
            self.infinit = True

        if self.time:
            self.end_time = 0
            while self.end_time <= 0 or self.end_time > 10:
                try:
                    self.end_time = int(numinput("Pick time", "1-10 minutes"))
                except Exception:
                    pass

        elif self.score:
            self.win_score = 0
            while self.win_score > 0:
                try:
                    self.win_score = int(
                        numinput("Pick score", "Score to win"))
                except Exception:
                    pass

    def return_time(self):
        if self.time:
            return self.time_var-Time.now()


t = Time.now()
t2 = t+td(minutes=(5))
t3 = t+td(minutes=2, seconds=3)

t4 = Time.now()
t5 = Time.now()+td(minutes=time_diff(t3, t2)[1], seconds=time_diff(t3, t2)[2])

print(t.strftime("%H:%M:%S"), time_diff(t3, t2)[0], t5.strftime("%H:%M:%S"))

# print((t3).total_seconds())
print(t.strftime("%H:%M"), t2.strftime("%H:%M"))
