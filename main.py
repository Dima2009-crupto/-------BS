from flask import Flask, render_template

from data import data
from data.base import create_db
from data.data_to_db import write_data_to_db


app = Flask(__name__)
NAVIGETION = data.departures

# @app.route("/", method=["GET","POST"])
@app.get("/")
def index():
    return render_template("index.html", departures=NAVIGETION, tours=data.tours )


@app.get("/tour/<id>")
def get_tour(id):
    tour = data.tours.get(id)
    return render_template("tour.html",departures=NAVIGETION, tour=tour)


@app.get("/departure/<dep_eng>/")
def departure(dep_eng):
    tours = {}
    for id, tour in data.tours.items():
        if tours["departure"] == dep_eng:
            tours[id] = tour
            
    return render_template("departure.html", departures=NAVIGETION, tours=tours)


if __name__ == "__main__":
    create_db()
    write_data_to_db()
    #app.run(debug=True)