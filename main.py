from turtle import Screen, textinput, numinput
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep
from turtle import Turtle
from gamemode import Gamemode
from pause import Pause
# din screen bör vara rektanguljär, ex. 800x600
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


screen = Screen()

screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, startx=0, starty=0)
x = float(str(SCREEN_WIDTH)[:-1]+"."+str(SCREEN_WIDTH)[-1])*5
y = float(str(SCREEN_HEIGHT)[:-1]+"."+str(SCREEN_HEIGHT)[-1])*5
screen.setworldcoordinates(-x+10, -y, x, y)
screen.bgcolor("black")
screen.title("pong")

screen.tracer(0)

left_input = {"w": False, "s": False}
right_input = {"Up": False, "Down": False}


def move_players(left, right):

    if left_input["w"] and left_input["s"]:
        pass
    elif left_input["s"]:
        left.down()
    elif left_input["w"]:
        left.up()

    if right_input["Up"] and right_input["Down"]:
        pass
    elif right_input["Down"]:
        right.down()
    elif right_input["Up"]:
        right.up()


def press_w():
    left_input["w"] = True


def release_w():
    left_input["w"] = False


def press_s():
    left_input["s"] = True


def release_s():
    left_input["s"] = False


def press_up():
    right_input["Up"] = True


def release_up():
    right_input["Up"] = False


def press_down():
    right_input["Down"] = True


def release_down():
    right_input["Down"] = False


def main():
    pause = Pause()
    scoreboard = Scoreboard(screen)

    ball = Ball(x=SCREEN_WIDTH, y=SCREEN_HEIGHT)
    right_paddle = Paddle(x=SCREEN_WIDTH, y=SCREEN_HEIGHT, side="right")
    left_paddle = Paddle(x=SCREEN_WIDTH, y=SCREEN_HEIGHT, side="left")

    while scoreboard.left_name == "":
        scoreboard.left_name = textinput("Pick name", "Left player name")
    while scoreboard.right_name == "":
        scoreboard.right_name = textinput("Pick name", "Right player name")

    gamemode = Gamemode()

    screen.listen()
    screen.onkeypress(press_up, "Up")
    screen.onkeypress(press_down, "Down")
    screen.onkeypress(press_w, "w")
    screen.onkeypress(press_s, "s")

    screen.onkeyrelease(release_up, "Up")
    screen.onkeyrelease(release_down, "Down")
    screen.onkeyrelease(release_w, "w")
    screen.onkeyrelease(release_s, "s")

    screen.onkey(pause.update_state, "p")
    screen.onkey(gamemode.end, "k")

    run_game = True

    while run_game:
        screen.listen()

        scoreboard.display_time(gamemode.return_time())
        gamemode.new_round()
        scoreboard.new_round(screen, new_game=True)
        left_paddle.new_round()
        right_paddle.new_round()
        ball.new_round(None)

        game_on = True

        while game_on:
            sleep(0.005)
            screen.update()

            if not pause.state:
                move_players(left_paddle, right_paddle)
                ball.move()
                if ball.distance(left_paddle) < 76:
                    if ball.last_bounce != "left":
                        if ball.xcor() < left_paddle.xcor()+20 and ball.xcor() > left_paddle.xcor():
                            ball.bounce_paddle()
                elif ball.distance(right_paddle) < 76:
                    if ball.last_bounce != "right":
                        if ball.xcor() > right_paddle.xcor()-20 and ball.xcor() < right_paddle.xcor():
                            ball.bounce_paddle()

                round_status = ball.round_over()

                if round_status is not None:
                    scoreboard.increase_score(round_status)
                    game_on = gamemode.game_status(
                        scoreboard.left_score, scoreboard.right_score)
                    if game_on:
                        gamemode.new_round()

                        left_paddle.new_round()
                        right_paddle.new_round()

                        ball.new_round(round_status)

                        scoreboard.new_round(screen)

                scoreboard.display_time(gamemode.return_time())
                if gamemode.time or gamemode.end_early:
                    game_on = gamemode.game_status()
            else:
                gamemode.fix_time_paused()

        scoreboard.game_over()
        screen.update()

        sleep(2)
        continue_game = ["r", "replay"]
        change_players = ["n"]
        change_gamemode = ["g", "gamemode"]
        quit_game = ["q", "quit"]
        while True:
            player_choice = ""

            while player_choice not in [*continue_game, *change_players, *change_gamemode, *quit_game]:
                try:
                    player_choice = textinput(
                        "gmae", "Replay(r), change gamemode(g), change players(n) or quit(q)").lower()
                except Exception:
                    pass

            if player_choice in [*continue_game, *quit_game]:
                if player_choice in quit_game:
                    run_game = False
                break

            elif player_choice in change_gamemode:
                gamemode.pick_gamemode()

            elif player_choice in change_players:
                player1 = ""
                player2 = ""
                while player1 == "":
                    player1 = textinput("Pick name", "Left player name")
                while player2 == "":
                    player2 = textinput("Pick name", "Right player name")
                scoreboard.left_name = player1
                scoreboard.right_name = player2


if __name__ == "__main__":
    main()
