from turtle import Screen
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
screen.bgcolor("black")
screen.title("ponge")

# turtle = Turtle()
# turtle.speed("fastest")
# turtle.goto(-SCREEN_WIDTH/2, -SCREEN_HEIGHT/2)
# print(turtle.heading())
# turtle.color("red")
# while turtle.xcor() != SCREEN_WIDTH/2:
#     print(turtle.xcor(), turtle.ycor())
#     if turtle.xcor() == 0:
#         turtle.color("pink")
#     else:
#         turtle.color("red")
#     turtle.left(90)
#     turtle.forward(SCREEN_HEIGHT)
#     turtle.right(90)
#     turtle.forward(SCREEN_WIDTH/100)
#     turtle.right(90)
#     turtle.forward(SCREEN_HEIGHT)
#     turtle.left(90)
#     turtle.forward(SCREEN_WIDTH/100)


screen.tracer(0)


def main():
    game_on = True
    ball = Ball(x=SCREEN_WIDTH, y=SCREEN_HEIGHT)
    right_paddle = Paddle(x=SCREEN_WIDTH, y=SCREEN_HEIGHT, side="right")
    left_paddle = Paddle(x=SCREEN_WIDTH, y=SCREEN_HEIGHT, side="left")

    var = 0
    while game_on:
        screen.update()
        sleep(0.1)
        ball.move()
        var += 1
        # print(var, ball)


if __name__ == "__main__":
    main()
