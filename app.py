from flask import Flask, render_template, redirect, request, flash, session, url_for
import model


app = Flask(__name__)
app.secret_key = "Dumbledore"



@app.route("/")
def index():
    user_id = session.get("user_id")
    if user_id:
    	pass
        #return redirect("/users/%s" %user_id)
    else:
    	pass
        #return render_template("index.html")
    return render_template("test.html")

@app.route("/", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    user_info = model.authenticate(email, password)
    if user_info != None:
    	pass
        #session['user_id'] = user_info[0]
        #session['email'] = user_info[1]
        #return redirect("/users/%s" %user_info[0])
    else:
    	pass
        #flash("Your login credentials are not recognized. Sorry!")
    return render_template("master.html")

@app.route("/register", methods=["POST"])
def register():
	pass
    #r_email = request.form.get("r_email")
    #r_password = request.form.get("r_password")
    #password_verify = request.form.get("password_verify")
    #age = request.form.get("age")
    #zip_code = request.form.get("zip_code")


    # user_email = model.register_check(r_email)
    # if user_email == True:
    #     flash("This email is already in use. Please try a new email or login to an existing account.")
    #     return redirect(url_for ("index"))  
    # else:
    #     if r_password == password_verify:
    #         user_id = model.register_store(r_email, r_password, age, zip_code)
    #         return redirect("/users/%s" %user_id)
    #     else:
    #         flash("Your passwords did not match, please try again.")
    #         return redirect(url_for("index"))


#log out of session
@app.route("/clear")
def clear_session():
    session.clear()
    return redirect(url_for("index"))




if __name__ == "__main__":
    app.run(debug = True)