from flask import Flask
import time
app = Flask(__name__)
def calculate_speed(function):
    def warp_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} speed{end_time - start_time}'s")
    return warp_function

@app.route("/")
def fast_function():
    for i in range(1000000):
        i * i
@calculate_speed
def slow_function():
    for i in range(1000000):
        i * i
