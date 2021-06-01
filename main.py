from turtle import Turtle, Screen
from paddle import Paddle
from pong_ball import Ball
import time

my_screen = Screen()
my_screen.setup(width=1000, height=600)
my_screen.title("Pong Game")
my_screen.bgcolor("black")


my_screen.tracer(0)


# setting split screen
def split_screen():
    split = Turtle("square")
    split.penup()
    split.color("white")
    split.shapesize(stretch_wid=.2, stretch_len=.5)
    split.setheading(270)
    split.sety(300)
    while not split.distance(0, -300) < 10:
        split.forward(20)
        split.clone()


split_screen()

right_paddle = Paddle("right")
left_paddle = Paddle("left")
ball = Ball()
game_end = False

my_screen.listen()
my_screen.onkeypress(fun=right_paddle.up, key="Up")
my_screen.onkeypress(fun=right_paddle.down, key="Down")
my_screen.onkeypress(fun=left_paddle.up, key="w")
my_screen.onkeypress(fun=left_paddle.down, key="s")

while not game_end:
    my_screen.update()  # display current animation/objects on screen
    time.sleep(.1)  # set a delay time in between the updates
    ball.move()

    # Detect collision with wall- part 1
    if ball.ycor() > 290 or ball.ycor() < -290:
        # ball bounces perpendicularly
        ball.setheading(-ball.heading())

    if ball.xcor() > 490 or ball.xcor() < -500:
        # The respective side of the ball's position loses
        ball.reset()


my_screen.exitonclick()
