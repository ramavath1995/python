from flask import Flask
import random

answer = random.randint(0, 9)
app = Flask(__name__)
print(__name__)


@app.route("/")
def guess():
    return ("<h1> Guess a number between 0 to 9 </h1>"
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>")


@app.route("/<int:guess>")
def number(guess):
    if guess > answer:
        return ("<h2 style='color: red'>Too high try again!</h2>"
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>")
    elif guess < answer:
        return ("<h2 style='color: red'>Too Low try again!</h2>"
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>")
    else:
        return ("<h2 style=color:green> You got me !</h2>"
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>")


if __name__ == "__main__":
    app.run(debug=True)
