from flask import Flask, render_template, redirect, request, flash, session, url_for
import model
import septa
import algorithm
import json

app = Flask(__name__)
app.secret_key = "Dumbledore"



@app.route("/")
def index():
    return render_template("landing.html")

@app.route("/route")
def route():
    return render_template("routing.html")

@app.route("/process_route", methods=["POST"])
def process_route():
    latlngs = request.form # IT'S REQUEST.FORM NOT ANYTHING ELSE - LIZ
    startlat = float(latlngs["startlat"])
    startlng = float(latlngs["startlng"])
    endlat = float(latlngs["endlat"])
    endlng = float(latlngs["endlng"])
    start_stop = int(septa.get_nearby_locations(startlng, startlat, 5))
    end_stop = int(septa.get_nearby_locations(endlng, endlat, 5))

    print "********************** START: ", start_stop
    print "********************** END:   ", end_stop
    if start_stop:
        if end_stop:
            shortest_route = algorithm.find_route(start_stop, end_stop)
            route_string = str(shortest_route).strip('[]')
            return route_string

        else:
            return "OH NO! Your ending location is over 5 miles away from the nearest accessible stop."
    else:
        return "OH NO! your starting location is over 5 miles away from the nearest accessible stop."




@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/getinvolved")
def involved():
    return render_template("involved.html")

@app.route("/clear")
def clear_session():
    session.clear()
    return redirect(url_for("index"))




if __name__ == "__main__":
    app.run(debug = True)