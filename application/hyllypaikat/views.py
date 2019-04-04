from application import app, db
from flask import Flask, render_template, request, before_render_template, flash, redirect, url_for
from sqlalchemy.sql.expression import exists
from flask_login import login_required, current_user
from application.tuotteet.models import Tuote
from application.hyllypaikat.models import Hyllypaikka
from application.hyllypaikat.forms import KapasiteettiForm
from application.lokit.models import Loki

@app.route("/varasto/main")
def varasto_mainpage():
    return render_template("/varasto/main.html")

@app.route("/varasto/hyllytettavat", methods=["GET"])
@login_required
def varasto_to_shelf():
    return render_template("/varasto/hyllytettavat.html", tuotteet = Tuote.query.filter(Tuote.hyllytettava != 0))

@app.route("/varasto/hyllyyn/<tuotekoodi>/", methods=["GET"])
@login_required
def choose_shelf(tuotekoodi):

    tuoteHyllyyn = db.session().query(Tuote).filter(Tuote.tuotekoodi == tuotekoodi).first()
    hyllypaikka = Hyllypaikka.find_shelf_location(tuoteHyllyyn)

    if hyllypaikka:
        return render_template("/varasto/hyllyyn.html", tuote = tuoteHyllyyn, paikka = hyllypaikka, form = KapasiteettiForm())

    # find_shelf_location ei löytänyt vapaita paikkoja
    else:
        flash('Tuotteelle '+str(tuoteHyllyyn.tuotekoodi) +' ei ole vapaana hyllypaikkoja')
        return redirect(url_for('varasto_to_shelf'))

@app.route("/varasto/hyllyyn/<tuotekoodi>/<paikkanumero>/", methods=["POST"])
@login_required
def product_to_shelf(tuotekoodi, paikkanumero):

    # keksi miten palautttaa oliot tuote ja hyllypaikka sivulta / choose_self-metodilta ilman uutta hakua
    tuote = db.session().query(Tuote).filter(Tuote.tuotekoodi == tuotekoodi).first()
    hyllypaikka = db.session().query(Hyllypaikka).filter(Hyllypaikka.paikkanumero == paikkanumero).first()

    form = KapasiteettiForm(request.form)
    if not form.kapasiteetti.validate(form):
        return render_template("varasto/hyllyyn.html", tuote = tuote, hyllypaikka = hyllypaikka, form = form)


    else:
        hyllypaikka.tuotekoodi = tuote.tuotekoodi
        hyllypaikka.muokattu = db.func.current_timestamp()
        hyllypaikka.kapasiteetti = form.kapasiteetti.data
        hyllypaikka.maara += tuote.hyllytettava

        loki = Loki(tuote.tuotekoodi, "Hyllysiirto +"+str(tuote.hyllytettava)+ " paikkanumero "+str(hyllypaikka.paikkanumero), current_user.id)

        tuote.muokattu = db.func.current_timestamp()
        tuote.hyllytettava = 0

        db.session().add(tuote)
        db.session().add(hyllypaikka)
        db.session().add(loki)
        db.session().commit()

        flash('Hyllytys onnistui')
        return redirect(url_for('varasto_to_shelf'))


    

