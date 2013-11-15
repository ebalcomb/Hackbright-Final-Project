from flask import Flask, render_template, redirect, request, flash, session, url_for
import model


app = Flask(__name__)
app.secret_key = "Dumbledore"



@app.route("/")
def index():
    return render_template("landing.html")

@app.route("/route")
def route():
    return render_template("routing.html")

@app.route("/route", methods=["POST"])
def process_route():
    start = request.form.get("start")
    end = request.form.get("end")


    return render_template("landing.html")


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