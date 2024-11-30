from flask import Flask, render_template
from sqlalchemy import SQLColumnExpression

app = Flask(__name__)

# @app.route("/", method=["GET","POST"])
@app.get("/")
def index():
    return render_template("index.html")


@app.get("/")
def departure():
    return render_template("departure.html")


@app.get("/")
def tour():
    return render_template("tour.html")


if __name__ == "__main__":
    app.run(debug=True)