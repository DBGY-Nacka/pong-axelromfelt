from turtle import Turtle

from random import randint


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

    def __str__(self):
        return str((self.heading(), self.xcor(), self.ycor()))

    def new_round(self, scoring_side=None):
        self.goto(0, 0)
        if scoring_side is None:
            if randint(1, 2) == 1:
                # self.setheading(randint(-60, 60))
                self.setheading(60)
            else:
                # self.setheading(randint(120, 240))
                self.setheading(120)

    def bounce(self):
        self.setheading(-self.heading())

    def move(self):
        self.forward(10)
        if self.ycor() > self.y or self.ycor() < -self.y:
            print("bounced")
            self.bounce()

    def round_over(self):
        if self.xcor() > self.x:
            return "right"
        if self.xcor() < -self.x:
            return "left"
        return None
