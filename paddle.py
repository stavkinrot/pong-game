from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.goto(x_cor, y_cor)
        self.setheading(90)
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=5)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)




