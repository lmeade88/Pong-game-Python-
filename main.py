from turtle import Turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


#Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")

pad1 = Paddle((350, 0))
pad2 = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(pad1.go_up, "Up")
screen.onkey(pad1.go_down, "Down")
screen.onkey(pad2.go_up, "w")
screen.onkey(pad2.go_down, "s")
screen.listen()


game_is_on = True
while game_is_on:

    time.sleep(ball.move_speed)
    ball.move()

    #detect collision with wall
    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.wall_collision()

    #detect collision with paddle
    if ball.distance(pad1) < 50 and ball.xcor() > 320:
        ball.paddle_hit()
    elif ball.distance(pad2) < 50 and ball.xcor() < -320:
        ball.paddle_hit()
    
    #detect if ball goes out of bounds
    if ball.xcor() > 360:
        ball.reset_position()
        ball.move()
        scoreboard.l_point()
    elif ball.xcor() < -360:
        ball.reset_position()
        ball.move()
        scoreboard.r_point()


#Screen Exit
screen.exitonclick() 


