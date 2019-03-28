from application import app, db
from flask import Flask, render_template, request
from flask_login import login_required
from application.tuotteet.models import Tuote

@app.route("/varasto/main")
def varasto_mainpage():
    return render_template("/varasto/main.html")

@app.route("/varasto/hyllytettavat", methods=["GET"])
@login_required
def varasto_to_shelf():
    return render_template("/varasto/hyllytettavat.html", tuotteet = Tuote.query.filter(Tuote.hyllytettava != 0))

@app.route("/varasto/hyllyyn/<tuotekoodi>/", methods=["POST"])
@login_required
def product_to_shelf(tuotekoodi):
    return render_template("/varasto/hyllyyn.html", tuote = Tuote.query.filter(Tuote.tuotekoodi == tuotekoodi))