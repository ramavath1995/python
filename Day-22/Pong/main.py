import time

from ball import *
from boarders import *
from paddles import *
from score_board import *

POSITION = [(-370, 0), (365, 0)]
tracer(0)
s = Screen()
s.bgcolor("black")
s.listen()
s.setup(width=800, height=600)
boarder = Borders()
left_paddle = Paddles(POSITION[0])
right_paddle = Paddles(POSITION[1])
onkey(left_paddle.move_up, "e")
onkey(left_paddle.move_down, "x")
onkey(right_paddle.move_up, "Up")
onkey(right_paddle.move_down, "Down")
score = ScoreBoard()
ball = Ball()
game_finished = False

while not game_finished:
    time.sleep(ball.sleep_time)
    s.update()
    ball.move()
    if ball.ycor() >= 280 or ball.ycor() <= -270:
        ball.y_bounce()
    if ball.distance(right_paddle) < 35 and ball.xcor() > 330 or ball.distance(left_paddle) < 35 and ball.xcor() < -330:
        ball.x_bounce()
    if ball.xcor() > 375:
        score.increase_left()
        ball.refresh()
    elif ball.xcor() < -380:
        score.increase_right()
        ball.refresh()


s.exitonclick()
