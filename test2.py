import turtle

# Create the turtle window
wn = turtle.Screen()
wn.title("Multiple Keypress Example")
wn.bgcolor("white")

# Create first turtle object (player1)
player1 = turtle.Turtle()
player1.shape("turtle")
player1.color("green")
player1.penup()  # Prevent drawing lines while moving

# Create second turtle object (player2)
player2 = turtle.Turtle()
player2.shape("turtle")
player2.color("blue")
player2.penup()  # Prevent drawing lines while moving
player2.goto(100, 0)  # Move player2 to a different starting position

# Variables to track the state of keys for both turtles
keys_pressed_player1 = {"w": False, "s": False}
keys_pressed_player2 = {"Up": False, "Down": False}

# Define functions for player1 (move up/down)


def move_up_player1():
    if keys_pressed_player1["w"]:
        y = player1.ycor()
        player1.sety(y + 10)


def move_down_player1():
    if keys_pressed_player1["s"]:
        y = player1.ycor()
        player1.sety(y - 10)

# Define functions for player2 (move up, down, left, right)


def move_up_player2():
    if keys_pressed_player2["Up"]:
        y = player2.ycor()
        player2.sety(y + 10)


def move_down_player2():
    if keys_pressed_player2["Down"]:
        y = player2.ycor()
        player2.sety(y - 10)


def move_left_player2():
    if keys_pressed_player2["Left"]:
        x = player2.xcor()
        player2.setx(x - 10)


def move_right_player2():
    if keys_pressed_player2["Right"]:
        x = player2.xcor()
        player2.setx(x + 10)

# Key press handlers for player1 (w, s)


def press_w():
    keys_pressed_player1["w"] = True


def release_w():
    keys_pressed_player1["w"] = False


def press_s():
    keys_pressed_player1["s"] = True


def release_s():
    keys_pressed_player1["s"] = False

# Key press handlers for player2 (arrow keys)


def press_up():
    keys_pressed_player2["Up"] = True


def release_up():
    keys_pressed_player2["Up"] = False


def press_down():
    keys_pressed_player2["Down"] = True


def release_down():
    keys_pressed_player2["Down"] = False


def press_left():
    keys_pressed_player2["Left"] = True


def release_left():
    keys_pressed_player2["Left"] = False


def press_right():
    keys_pressed_player2["Right"] = True


def release_right():
    keys_pressed_player2["Right"] = False


# Bind keys to handlers for player1 (w, s)
wn.listen()
wn.onkeypress(press_w, "w")
wn.onkeyrelease(release_w, "w")
wn.onkeypress(press_s, "s")
wn.onkeyrelease(release_s, "s")

# Bind keys to handlers for player2 (arrow keys)
wn.onkeypress(press_up, "Up")
wn.onkeyrelease(release_up, "Up")
wn.onkeypress(press_down, "Down")
wn.onkeyrelease(release_down, "Down")
wn.onkeypress(press_left, "Left")
wn.onkeyrelease(release_left, "Left")
wn.onkeypress(press_right, "Right")
wn.onkeyrelease(release_right, "Right")

# Main game loop
while True:
    move_up_player1()   # Move player1 when 'w' is pressed
    move_down_player1()  # Move player1 when 's' is pressed

    move_up_player2()    # Move player2 when 'Up' is pressed
    move_down_player2()  # Move player2 when 'Down' is pressed
    move_left_player2()  # Move player2 when 'Left' is pressed
    move_right_player2()  # Move player2 when 'Right' is pressed

    wn.update()  # Update the window
