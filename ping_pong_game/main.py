from re import A
from turtle import Screen, Turtle, distance, xcor
from paddle_lib import Paddle
from ball import Ball
from scoreboard import Scoreboard
import random
import time

colors = ["red", "white", "green", "yellow", "blue"]

screen = Screen()
bg = (0, 0, 0)
screen.bgcolor(bg)
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_y()
    
    if ball.distance(r_paddle) < 70 and ball.xcor() > 320 or ball.distance(l_paddle) < 70 and ball.xcor() < -320:
        ball.bounce_x()
        ball.color(random.choice(colors))

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    if scoreboard.l_score == 10:
        scoreboard.print_results("l")
        game_is_on = False

    if scoreboard.r_score == 10:
        scoreboard.print_results("r")
        game_is_on = False

screen.exitonclick()

