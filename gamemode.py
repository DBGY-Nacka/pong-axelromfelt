from turtle import Turtle, textinput, numinput
from datetime import datetime as Time, timedelta as td
from time import sleep


def time_diff(start_time, end_time, display=False, paused=False):
    # start_time = datetime.strptime(start_time, "%H:%M:%S")
    # end_time = datetime.strptime(end_time, "%H:%M:%S")
    time_diff_res = end_time - start_time

    minutes = (time_diff_res.seconds // 60) % 60
    seconds = time_diff_res.seconds % 60
    microseconds = time_diff_res.microseconds
    if display:
        if len(str(minutes)) == 1:
            minutes = f"0{minutes}"
        if len(str(seconds)) == 1:
            seconds = f"0{seconds}"
        return f"{minutes}:{seconds}"

    elif paused:
        return (minutes, seconds)

    else:
        return f"{minutes}{seconds}{str(microseconds)[0]}"


class Gamemode():
    def __init__(self):
        self.time = False
        self.score = False
        self.infinit = False
        self.time_offset = None
        self.end_early = False
        self.pick_gamemode()
        self.new_game()

    def new_game(self):
        if self.time:
            self.time_var = Time.now()+td(minutes=(self.end_time), milliseconds=3)
        else:
            self.time_var = Time.now()

    def new_round(self):
        self.time_var += td(seconds=4)

    def game_status(self, left_score=None, right_score=None):
        self.time_offset = None

        if self.time:
            if time_diff(Time.now(), self.time_var) == "001":
                return False
        elif self.score:
            if left_score == self.win_score or right_score == self.win_score:
                return False
        elif self.end_early:
            self.end_early = False
            return False
        return True

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
                "Pick gamemode", "Time(t) or score(s) based or infinit(i)").lower()

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
            while self.win_score <= 0:
                try:
                    self.win_score = int(
                        numinput("Pick score", "Score to win"))
                except Exception:
                    pass

    def return_time(self):
        if self.time:
            return time_diff(Time.now(), self.time_var, True)
        return time_diff(self.time_var, Time.now(), True)

    def fix_time_paused(self):

        if self.time:
            if self.time_offset is None:
                self.time_offset = self.time_var-Time.now()

            self.time_var = Time.now()+self.time_offset

        else:
            if self.time_offset is None:
                self.time_offset = Time.now()-self.time_var
                print(self.time_offset)

            self.time_var = Time.now()-self.time_offset

    def end(self):
        self.end_early = True
