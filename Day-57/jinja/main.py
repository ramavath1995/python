import requests
from flask import Flask, render_template


app = Flask(__name__)
p = requests.get("https://api.npoint.io/4af156202f984d3464c3")
print(p.status_code)
posts = p.json()
@app.route('/')
def home():
    return render_template("index.html", all_posts = posts)


@app.route("/post/<int:num>")
def get_post(num):

    return render_template("post.html", a=posts, ID=num)

if __name__ == "__main__":
    app.run(debug=True)
