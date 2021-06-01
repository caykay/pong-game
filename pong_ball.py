from turtle import Turtle
import random
DIRECTION = [0, 180]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(.5, .5)
        self.color("white")
        self.penup()
        # initial direction
        self.setheading(random.choice(DIRECTION))

    def move(self):
        self.forward(20)

    def bounce(self):
        """Bounce the ball depending on the ball's current location"""

    def reset(self):
        super().home()
        self.setheading(random.choice(DIRECTION))
