from turtle import Turtle


class Ball(Turtle):
    def __init__(self, x_move=1, y_move=1):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = x_move
        self.y_move = y_move
        self.move_speed = 0.01

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= - 1
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x_move *= - 1
        self.move_speed *= 0.9

    def ball_reset(self):
        self.move_speed = 0.01
        self.goto(0, 0)
        self.bounce_x()
