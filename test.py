from turtle import Screen

from time import sleep
from random import choice
from turtle import Turtle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

x = float(str(SCREEN_WIDTH)[:-1]+"."+str(SCREEN_WIDTH)[-1])*5
y = float(str(SCREEN_HEIGHT)[:-1]+"."+str(SCREEN_HEIGHT)[-1])*5


screen = Screen()
screen.bgcolor("grey")
screen.title("ponge")
screen.setworldcoordinates(-x, -y, x, y)
left = Turtle()
right = Turtle()


middle = Turtle()
middle.speed("fastest")
screen.colormode(255)
middle.goto(0, -300)
middle.goto(0, 300)
colors = ['red', 'blue', 'green', 'yellow',
          'orange', 'purple', 'cyan', 'lime', 'pink']
left.setheading(-90)
right.setheading(-90)
left.pensize(20)
right.pensize(20)
for i in range(1, 100):
    color = choice(colors)
    left.color(color)
    right.color(color)

    left.goto(-10*i, 0)
    right.goto(10*i, 0)

input()
