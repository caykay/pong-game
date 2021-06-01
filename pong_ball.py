from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(.5, .5)
        self.color("white")
        self.penup()
        # initial direction can be random
        self.setheading(random.randint(1, 360))

    def move(self):
        self.forward(20)

    def bounce(self):
        """Bounce the ball depending on the ball's current location"""

    def reset(self):
        super().home()
        self.setheading(random.randint(1, 360))
