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
    #start_stop = septa.get_nearby_locations(startlng, startlat, 5)
    #end_stop = septa.get_nearby_locations(endlng, endlat, 5)
    #shortest_route = algorithm.find_route(start_stop, end_stop)
    #return shortest_route
    return "ROUTE WILL APPEAR HERE! \n1. blah blah blah\n2. blah blah blah\n3. blah blah blah"



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