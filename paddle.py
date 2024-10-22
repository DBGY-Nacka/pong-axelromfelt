from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y, side):
        super().__init__()

        # för att få fram x/2 men x/2 gav för inaccurate svar så jag gjorde den här vilket är exakt
        self.x = float(str(x)[:-1]+"."+str(x)[-1])*5
        self.y = float(str(y)[:-1]+"."+str(y)[-1])*5
        self.side = side
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=6, stretch_wid=1)
        self.color("white")
        self.speed("fastest")
        self.new_round()

    def new_round(self):
        distance_from_edge = 40
        self.setheading(90)

        if self.side == "right":
            coordinates = (self.x-distance_from_edge, 0)
            # coordinates = (-360, 0)

            # coordinates = (distance_from_edge, 0)
        elif self.side == "left":
            coordinates = (distance_from_edge-self.x, 0)
            # coordinates = (-distance_from_edge, 0)
            # coordinates = (360, 0)

        self.goto(coordinates)

    def up(self):

        if self.ycor() < self.y-20:
            self.setheading(90)
            self.forward(3)

    def down(self):
        if self.ycor() > 20-self.y:
            self.setheading(270)
            self.forward(3)
