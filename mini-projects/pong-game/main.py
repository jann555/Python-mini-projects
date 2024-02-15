import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(location=(350, 0))
l_paddle = Paddle(location=(-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
# controls
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if (ball.ycor() > 290) or (ball.ycor() < - 290):
        ball.bounce_y()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() > - 320):
        ball.bounce_x()

    # Define right side paddle miss
    if ball.xcor() > 380:
        ball.ball_reset()
        scoreboard.l_point()

    # Define left side paddle miss
    if ball.xcor() < -380:
        ball.ball_reset()
        scoreboard.r_point()

screen.exitonclick()
