from road import *
from racer import *
from cars_manager import *
from score_board import *
import time


START_POSITION = (0, -330)

s = Screen()
s.setup(width=800, height=700)
s.bgcolor("black")
s.title("Turtle Crossing")
s.tracer(0)
road = Road()
player = Racer()
s.listen()
onkey(player.move, "space")
game_over = False
cars = CarsManager()
score = ScoreBoard()
while not game_over:
    time.sleep(0.2)
    s.update()
    cars.create_car()
    cars.move_car()
    for jeep in cars.all_cars:
        if jeep.distance(player) < 25:
            score.game_over()
            game_over = True
    if player.ycor() > 270:
        score.increase_score()
        player.goto(START_POSITION)
        cars.speed_up()

s.exitonclick()
