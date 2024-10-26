from borders import *
from turtle import *
from snake import *
import time
from score_board import *
from food import *

s = Screen()
s.setup(width=800, height=600)
s.bgcolor("black")
s.listen()
tracer(0)

borders = Borders()
my_snake = Snake()
score = ScoreBoard()
ball = Food()
onkey(my_snake.move_up, "Up")
onkey(my_snake.move_down, "Down")
onkey(my_snake.move_left, "Left")
onkey(my_snake.move_right, "Right")


game_over = False
while not game_over:
    time.sleep(0.3)
    s.update()
    my_snake.move_forward()
    if my_snake.snake_length[0].distance(ball) < 15:
        score.increase_score()
        ball.refresh_food()
        my_snake.extend_snake()
    if (my_snake.snake_length[0].xcor() >= 385 or my_snake.snake_length[0].xcor() <= -385 or
            my_snake.snake_length[0].ycor() >= 280 or my_snake.snake_length[0].ycor() <= -280):
        score.game_over()
        game_over = True
    for segment in my_snake.snake_length[1:]:
        if my_snake.snake_length[0].distance(segment) < 10:
            score.game_over()
            game_over = True

s.exitonclick()
