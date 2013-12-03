from flask import Flask, render_template, redirect, request, session, url_for
import septa
import algorithm
import smtplib


app = Flask(__name__)
app.secret_key = "Dumbledore"



@app.route("/")
def index():
    return render_template("landing.html")



@app.route("/route")
def route():
    return render_template("routing.html")



@app.route("/about")
def about():
    return render_template("about.html")



@app.route("/profile")
def profile():
    return render_template("profile.html")



@app.route("/getinvolved")
def involved():
    return render_template("involved.html")

@app.route("/process_feedback", methods=["POST"])
def process_feedback():
    name = request.form.get("name")
    email = request.form.get("email")
    company = request.form.get("company")
    message = request.form.get("message")

    sender = email
    receivers = ['ebalcomb@gmail.com']


    # smtpObj = smtplib.SMTP('localhost')
    # smtpObj.sendmail(sender, receivers, message)         


    return render_template("thanks.html", name=name, email=email, company=company, message=message)



@app.route("/process_route", methods=["POST"])
def process_route():
    latlngs = request.form
    startlat = float(latlngs["startlat"])
    startlng = float(latlngs["startlng"])
    endlat = float(latlngs["endlat"])
    endlng = float(latlngs["endlng"])
    start_stop = int(septa.get_nearby_locations(startlng, startlat, 5))
    end_stop = int(septa.get_nearby_locations(endlng, endlat, 5))
    print "**************", start_stop
    print "**************", end_stop
    if start_stop:
        if end_stop:
            if start_stop != end_stop:
                shortest_route = algorithm.find_route(start_stop, end_stop)
                if shortest_route:
                    print "********************************************"
                    print shortest_route
                    return shortest_route
                else:
                    return "OH NO! There is no accessible route between those two locations."
            else:
                return "Oops! Your start and end location are the same."

        else:
            return "OH NO! Your ending location is over 5 miles away from the nearest accessible stop."
    else:
        return "OH NO! your starting location is over 5 miles away from the nearest accessible stop."






if __name__ == "__main__":
    app.run(debug = True)