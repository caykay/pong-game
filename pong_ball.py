from turtle import Turtle
import random
DIRECTION = [a for a in range(-60, 60, 10)] + \
            [b for b in range(120, 240, 10)]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(.5, .5)
        self.color("white")
        self.penup()
        # initial direction
        self.setheading(random.choice(DIRECTION))
        self.move_speed = .1

    def move(self):
        self.forward(20)

    def bounce_y(self):
        """Bounce the ball depending on the ball's contact with
        a wall in the y axis"""
        self.setheading(-self.heading())

    def bounce_x(self):
        """Bounce the ball when in collision with a paddle"""
        self.setheading(180 - self.heading())
        self.move_speed *= .9  # for every collision with paddle boost ball speed

    def reset(self):
        super().home()
        self.setheading(random.choice(DIRECTION))
        self.move_speed = .1
