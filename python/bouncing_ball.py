import turtle
import random

# Set key parameters
gravity = -0.5  # pixels/(time of iteration)^2
y_velocity = 1  # pixels/(time of iteration)
x_velocity = -1  # pixels/(time of iteration)
energy_loss = 0.95

width = 600
height = 800

# Set window and ball
window = turtle.Screen()
window.setup(width, height)
window.tracer(0)

ball = turtle.Turtle()

ball.penup()
ball.screen.colormode(255)
ball.shape("circle")

r = 0
b = 0
g = 0

# Main loop
while True:
    # Move ball
    ball.sety(ball.ycor() + y_velocity)
    ball.setx(ball.xcor() + x_velocity)

    # Acceleration due to gravity
    y_velocity += gravity

    # Bounce off the ground
    if ball.ycor() < -height / 2:
        y_velocity = -y_velocity * energy_loss
        # Set ball to ground level to avoid it getting "stuck"
        ball.sety(-height / 2)

    # Bounce off the walls (left and right)
    if ball.xcor() > width / 2 or ball.xcor() < -width / 2:
        x_velocity = -x_velocity

    # r = random.randrange(255)
    # b = random.randrange(255)
    # g = random.randrange(255)

    ball.color(r, b, g)

    ball.stamp()

    window.update()

    if r < 255:
        r += 1
    elif g < 255:
        g += 1
    elif b < 255:
        b += 1
    else:
        r = 0
        b = 0
        g = 0
