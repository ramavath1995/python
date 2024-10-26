from flask import Flask

app = Flask(__name__)
print(__name__)


def make_bold(function):
    def warp_function():
        return f"<b>{function()}</b>"

    return warp_function


def make_italic(function):
    def warp():
        return f"<em>{function()}</em>"

    return warp


def make_underline(function):
    def warp():
        return f"<u>{function()}</u>"
    return warp

@app.route("/")
@make_underline
@make_italic
def welcome():
    return "welcome to my site"


@app.route("/<name>/<number>")
def say_hello(name, number):
    return f"<h1 style='text-align: center,font-style:italic'><b><u>Hello {name} you are {number} old now !</u></b>"


if __name__ == "__main__":
    app.run(debug=True)
