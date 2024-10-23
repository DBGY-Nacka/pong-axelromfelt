from turtle import Turtle

from random import randint
from math import cos, sin, acos, asin, tan, atan


class Ball(Turtle):

    def __init__(self, x, y):
        # x and y is the screen width and height, this is to make the game more editable
        self.x = x/2
        self.y = y/2
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("white")
        self.speed("fastest")
        self.new_round()
        self.last_bounce = None

    def new_round(self, scoring_side=None):
        self.last_bounce = None
        self.goto(0, 0)
        if scoring_side is None:
            if randint(1, 2) == 1:
                self.setheading(randint(-60, 60))
                # self.setheading(60)
            else:
                self.setheading(randint(120, 240))
                # self.setheading(120)
        elif scoring_side == "right":
            self.setheading(randint(-60, 60))
        else:
            self.setheading(randint(120, 240))

    def bounce_wall(self):
        self.setheading(360-self.heading())

    def bounce_paddle(self):

        if self.xcor() > 0:

            self.setheading(180-self.heading()+randint(-40, 40))
            if self.heading() > 240 or self.heading() < 120:
                self.setheading(randint(135, 225))

            self.last_bounce = "right"
        else:
            self.setheading(180-self.heading()+randint(-40, 40))
            if self.heading() > 60 and self.heading() < 300:
                if randint(1, 200) % 2 == 0:
                    self.setheading(randint(0, 45))
                else:
                    self.setheading(randint(315, 360))
            self.last_bounce = "left"

    def move(self):
        self.forward(5)
        if abs(self.ycor()) > self.y:
            self.bounce_wall()

    def round_over(self):
        if self.xcor() > self.x:
            return "right"
        if self.xcor() < -self.x:
            return "left"
        return None
