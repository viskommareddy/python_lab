import turtle
import time

# Create a Turtle object
pen = turtle.Turtle()

# Set the screen size
turtle.setup(width=600, height=600)

# Set the background color
turtle.bgcolor("black")

# Set the pen size and color
pen.pensize(3)
pen.pencolor("white")

# Create the clock face
pen.penup()
pen.goto(0, 200)
pen.setheading(180)
pen.pendown()
pen.circle(200)

# Create the hour markers
pen.penup()
pen.goto(0, 0)
pen.setheading(90)
for _ in range(12):
    pen.forward(170)
    pen.pendown()
    pen.forward(30)
    pen.penup()
    pen.goto(0, 0)
    pen.right(30)

# Create the hour, minute, and second hands
hour_hand = turtle.Turtle()
minute_hand = turtle.Turtle()
second_hand = turtle.Turtle()

hour_hand.speed(0)
minute_hand.speed(0)
second_hand.speed(0)

hour_hand.pensize(6)
minute_hand.pensize(4)
second_hand.pensize(2)

hour_hand.pencolor("white")
minute_hand.pencolor("white")
second_hand.pencolor("red")

while True:
    # Get the current time
    t = time.localtime()
    hour = t.tm_hour % 12
    minute = t.tm_min
    second = t.tm_sec

    # Calculate the angle of each hand
    hour_angle = (hour * 30) + (minute * 0.5)
    minute_angle = minute * 6
    second_angle = second * 6

    # Rotate each hand to its correct angle
    hour_hand.setheading(-hour_angle + 90)
    minute_hand.setheading(-minute_angle + 90)
    second_hand.setheading(-second_angle + 90)

    # Update the screen
    turtle.update()

    # Wait for one second
    time.sleep(1)

    # Clear the hands
    hour_hand.clear()
    minute_hand.clear()
    second_hand.clear()

turtle.done()
