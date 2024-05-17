from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.setheading(45)
        self.move_speed = 0.08

    def move(self):
        self.forward(15)

    def bounce(self):
        self.setheading(self.heading() - 90)
        self.move_speed /= 1.2

    def reset_ball(self):
        self.goto(0, 0)
        self.move_speed = 0.08
        self.bounce()
