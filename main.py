from turtle import Screen, textinput, numinput
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep
from turtle import Turtle
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
    game_on = True
    ball = Ball(x=SCREEN_WIDTH, y=SCREEN_HEIGHT)
    right_paddle = Paddle(x=SCREEN_WIDTH, y=SCREEN_HEIGHT, side="right")
    left_paddle = Paddle(x=SCREEN_WIDTH, y=SCREEN_HEIGHT, side="left")
    player1 = ""
    player2 = ""
    while player1 == "":
        player1 = textinput("Pick name", "Left player name")
    while player2 == "":
        player2 = textinput("Pick name", "Right player name")
    scoreboard = Scoreboard(player1, player2)

    screen.listen()
    screen.onkeypress(press_up, "Up")
    screen.onkeypress(press_down, "Down")
    screen.onkeypress(press_w, "w")
    screen.onkeypress(press_s, "s")

    screen.onkeyrelease(release_up, "Up")
    screen.onkeyrelease(release_down, "Down")
    screen.onkeyrelease(release_w, "w")
    screen.onkeyrelease(release_s, "s")

    scoreboard.new_round(screen)

    while game_on:
        move_players(left_paddle, right_paddle)
        screen.update()
        sleep(0.002)
        ball.move()
        if ball.distance(left_paddle) < 76 and ball.xcor() < left_paddle.xcor()+20 and ball.last_bounce != "left" and ball.xcor() > left_paddle.xcor() or ball.distance(right_paddle) < 76 and ball.xcor() > right_paddle.xcor()-20 and ball.last_bounce != "right" and ball.xcor() < right_paddle.xcor():
            ball.bounce_paddle()

        round_status = ball.round_over()

        if round_status is not None:
            scoreboard.increase_score(round_status)

            # if not infinit_mode:

            # else:
            left_paddle.new_round()
            right_paddle.new_round()
            ball.new_round(round_status)
            scoreboard.new_round(screen)


if __name__ == "__main__":
    main()
