from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Comic sans MS", 60, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.sety(210)
        self.score_left = 0
        self.score_right = 0
        self.display()

    def update(self, right=0, left=0):
        """Updates the score board"""
        self.clear()  # delete drawings on screen but doesn't move
        self.score_left += left
        self.score_right += right
        self.display()

    def display(self):
        """Display the writing on the screen"""
        self.write(arg=f"{self.score_left}{' '*5}{self.score_right}", align=ALIGNMENT, font=FONT)
