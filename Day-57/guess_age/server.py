from flask import Flask, render_template
import requests

app = Flask(__name__)




@app.route("/username/<name>")
def home(name):
    g = requests.get(f"https://api.genderize.io?name={name}")
    k = g.json()
    gender = k["gender"]
    i = requests.get(f"https://api.agify.io?name={name}")
    age= i.json()["age"]

    return render_template("index.html", age=age, gender=gender)

if __name__ == "__main__":
    app.run(debug=True)