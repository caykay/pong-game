from turtle import Turtle, Screen
from paddle import Paddle
from pong_ball import Ball
from score_board import ScoreBoard
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
sb = ScoreBoard()
game_end = False

my_screen.listen()
my_screen.onkeypress(fun=right_paddle.up, key="Up")
my_screen.onkeypress(fun=right_paddle.down, key="Down")
my_screen.onkeypress(fun=left_paddle.up, key="w")
my_screen.onkeypress(fun=left_paddle.down, key="s")
my_screen.onclick(lambda x, y: print(x, y))  # for testing purposes

while not game_end:
    my_screen.update()  # display current animation/objects on screen
    time.sleep(.1)  # set a delay time in between the updates
    ball.move()

    # Detect collision with wall- part 1
    if ball.ycor() > 290 or ball.ycor() < -290:
        # ball bounces perpendicularly with respect to its direction angle
        ball.bounce_y()

    # collision with right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 460\
            or ball.distance(left_paddle) < 50 and ball.xcor() < -460:
        ball.bounce_x()

    # Detect when ball goes past the paddle
    # Note that this wont affect the paddle collisions
    if ball.xcor() > 490 or ball.xcor() < -500:
        # The respective side of the ball's position loses
        sb.update(right=1) if ball.xcor() < 0 else sb.update(left=1)  # if in +ve quadrant or not
        ball.reset()


my_screen.exitonclick()
