from application import app, db
from flask import render_template, request
from application.tuotteet.models import Tuote

@app.route("/tuotteet/new")
def tuotteet_form():
    return render_template("tuotteet/new.html")

@app.route("/tuotteet/", methods=["POST"])
def tuotteet_create():
   # print(request.form.get("tuotekoodi"))
   # print(request.form.get("nimi"))
   # print(request.form.get("maara"))
   # print(request.form.get("kategoria"))
   # print(request.form.get("kuvaus")) 

    t = Tuote(request.form.get("tuotekoodi"), request.form.get("nimi"),
    request.form.get("maara"), request.form.get("kategoria"), 
    request.form.get("kuvaus"))

    db.session().add(t)
    db.session().commit()

    return "hello world!"