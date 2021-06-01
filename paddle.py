from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, alignment):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.setheading(90)
        self.penup()
        self.alignment = alignment
        self.set_alignment(self.alignment)

    def up(self):
        if self.ycor() <= 240:
            self.forward(20)

    def down(self):
        if self.ycor() >= -230:
            self.back(20)

    def set_alignment(self, alignment):
        if alignment.lower() == "left":
            self.setpos(x=-490, y=0)
        elif alignment.lower() == "right":
            self.setpos(x=480, y=0)
