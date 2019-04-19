from flask import render_template, request, url_for, redirect, flash
from application import app, db
from application import login_required
from application.tuotteet.models import Tuote
from application.hyllypaikat.models import Hyllypaikka
from application.tuotteet.views import nayta_tuote

@app.route("/", methods=["POST", "GET"])
def index():
    # if == yläpalkin haku layoutissa
    if request.form.get("hakunappi") == "Etsi":
        hakusyote = request.form.get("hakukentta")

        if hakusyote:
            return kasittele_haku(hakusyote, request.form.get("hakutyyppi"))
        else:
            flash('Hakukenttä tyhjä')
            return render_template("index.html")

    else:
        return render_template("index.html")

def kasittele_haku(hakusyote, hakutyyppi):
    if hakutyyppi == "tuote":
        tuote = Tuote.query.filter(Tuote.tuotekoodi == int(hakusyote)).first()
        if tuote:
            return render_template("/tuotteet/search.html", tuote=tuote, hyllypaikat=tuote.hyllypaikat)
        else:
            flash('Tuotetta ei löytynyt')
            return render_template("index.html")
    
    elif hakutyyppi == "hyllypaikka":
        hyllypaikka = Hyllypaikka.query.filter(Hyllypaikka.paikkanumero == int(hakusyote)).first()
        if hyllypaikka:
            return redirect(url_for('show_shelf', paikkanumero = hyllypaikka.paikkanumero))
        else:
            flash('Hyllypaikkaa ei löytynyt')
            return render_template("index.html")

    else:
        flash('Et valinnut hakutyyppiä (Tuote tai Hyllypaikka)')
        return render_template("index.html")
