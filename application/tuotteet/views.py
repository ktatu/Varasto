from application import app, db
from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy.sql.expression import exists
from application.tuotteet.models import Tuote
from application.tuotteet.forms import TuoteForm, mainPageForm
from flask_login import login_required, current_user
from application.lokit.models import Loki
 
# app.secret_key = 'salainen_avain'

@app.route("/tuotteet/new")
@login_required
def tuotteet_form():
    return render_template("tuotteet/new.html", form = TuoteForm())

@app.route("/tuotteet/new", methods=["POST"])
def tuotteet_return():
    return redirect(url_for('tuotteet_mainpage'))

@app.route("/tuotteet", methods=["POST"])
@login_required
def tuotteet_create():

    form = TuoteForm(request.form)

    if not form.validate():
        return render_template("tuotteet/new.html", form = form)

    t = Tuote(form.tuotekoodi.data, form.nimi.data, form.maara.data, form.kategoria.data, form.kuvaus.data)
    t.hyllytettava = form.maara.data

    loki = Loki(form.tuotekoodi.data, "tuotelisäys määrä "+str(form.maara.data), current_user.id)

    db.session().add(loki)
    db.session().add(t)
    db.session().commit()

    return redirect(url_for("tuotteet_mainpage"))


@app.route("/tuotteet", methods=["GET"])
@login_required
def tuotteet_index():
    return render_template("tuotteet/list.html", tuotteet = Tuote.query.all())

@app.route("/tuotteet/main")
def tuotteet_mainpage():
    return render_template("tuotteet/main.html", form = mainPageForm())

@app.route("/tuotteet/main", methods=["POST"])
@login_required
def tuotteet_search():

    form = mainPageForm(request.form)
    koodi = form.tuotekoodi.data
    tuote = db.session().query(Tuote).filter(Tuote.tuotekoodi==koodi).first()

    if not form.tuotekoodi.validate(form):
        return render_template("tuotteet/main.html", form = form)

    # tuotehaku
    if request.form["nappi"] == "Hae tuotetta":

        # workaround-ratkaisu, sama query kahdesti
        if tuote:
            return render_template("tuotteet/search.html", tuote1 = db.session().query(Tuote).filter(Tuote.tuotekoodi==koodi))

        else:
            flash('Tuotetta ' + str(koodi) + ' ei ole varastossa')
            return redirect(url_for('tuotteet_mainpage'))

    # tuotelisäys
    elif request.form["nappi"] == "Lisää tuote":

        if tuote:
            flash('Tuote ' + str(koodi) +' ei ole uusi, tee saldopäivitys')
            return redirect(url_for("tuotteet_mainpage"))
        else:
            return redirect(url_for("tuotteet_form"))

    # saldopäivitys
    else:

        lisattava = form.maara.data
        if not form.maara.validate(form):
            return render_template("tuotteet/main.html", form = form)

        if tuote:
            
            tuote.maara = tuote.maara + lisattava
            tuote.hyllytettava = tuote.hyllytettava + lisattava
            loki = Loki(koodi, "saldopäivitys määrä "+str(lisattava), current_user.id)

            db.session().add(loki)
            db.session().commit()

            # ilmoitus onnistuneesta saldolisäyksestä
            flash('Tuotteeseen ' + str(koodi) + ' lisätty ' + str(lisattava))

        else:
            flash('Tuotetta ' + str(koodi) + ' ei ole varastossa')


        return redirect(url_for("tuotteet_mainpage"))


