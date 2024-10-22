from turtle import Turtle


class Pause(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.hideturtle()
        self.penup()
        self.shapesize(stretch_len=4, stretch_wid=0.5)
        self.color("grey")
        self.setheading(90)
        self.state = False

    def draw_pause(self):
        self.goto(-20, 0)
        self.stamp()
        self.goto(20, 0)
        self.stamp()

    def update_state(self):
        if self.state:
            self.clear()
            self.state = False
        else:
            self.draw_pause()
            self.state = True
