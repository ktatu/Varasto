from application import app, db
from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy.sql.expression import exists
from application.tuotteet.models import Tuote
from application.tuotteet.forms import TuoteForm, mainPageForm
from flask_login import login_required, current_user
from application.lokit.models import Loki
from application.hyllypaikat.models import Hyllypaikka
 
@app.route("/tuotteet/new", methods=["POST"])
def tuotteet_palautus():
    return redirect(url_for('tuotteet_etusivu'))

@app.route("/tuotteet", methods=["POST"])
@login_required
def luo_tuote():

    form = TuoteForm(request.form)

    if not form.validate():
        return render_template("tuotteet/new.html", form = form)

    t = Tuote(form.tuotekoodi.data, form.nimi.data, form.maara.data, form.kategoria.data, form.kuvaus.data)
    t.hyllytettava = form.maara.data

    loki = Loki(form.tuotekoodi.data, "tuotelisäys määrä "+str(form.maara.data), current_user.id)

    db.session().add(loki)
    db.session().add(t)
    db.session().commit()

    return redirect(url_for("tuotteet_etusivu"))


@app.route("/tuotteet", methods=["GET"])
@login_required
def tuotteet_indeksi():
    return render_template("tuotteet/list.html", tuotteet = Tuote.query.all())

@app.route("/tuotteet/main")
def tuotteet_etusivu():
    return render_template("tuotteet/main.html", form = mainPageForm())

@app.route("/tuotteet/main", methods=["POST"])
@login_required
def tuotteet_haku():

    form = mainPageForm(request.form)
    koodi = form.tuotekoodi.data
    tuote = db.session().query(Tuote).filter(Tuote.tuotekoodi==koodi).first()

    if not form.tuotekoodi.validate(form):
        return render_template("tuotteet/main.html", form = form)

    # tuotehaku
    if request.form["nappi"] == "Hae tuotetta":
        if tuote:
            return nayta_tuote(tuote)
        else:
            flash('Tuotetta ' + str(koodi) + ' ei ole varastossa')
            return redirect(url_for('tuotteet_etusivu'))

    # tuotelisäys
    elif request.form["nappi"] == "Lisää tuote":

        if tuote:
            flash('Tuote ' + str(koodi) +' ei ole uusi, tee saldopäivitys')
            return redirect(url_for("tuotteet_etusivu"))
        else:
            tuoteForm = TuoteForm()
            form.tuotekoodi = koodi
            return render_template("/tuotteet/new.html", form = tuoteForm)

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

            flash('Tuotteeseen ' + str(koodi) + ' lisätty ' + str(lisattava))
        else:
            flash('Tuotetta ' + str(koodi) + ' ei ole varastossa')

        return redirect(url_for("tuotteet_etusivu"))

# apumetodi tuotteet_haulle
@app.route("/tuotteet/search", methods=["GET"])
def nayta_tuote(parametriTuote):

    return render_template("tuotteet/search.html", tuote = parametriTuote, 
    hyllypaikat = Hyllypaikka.query.join(Tuote).filter(Hyllypaikka.tuotekoodi == parametriTuote.tuotekoodi).all())

# metodi listojen (esim. kaikkien tuotteiden listaus, tuotteet_indeksi) tuotelinkkejä varten
@app.route("/tuotteet/<tuotekoodi>")
def tuotenakyma(tuotekoodi):

    return render_template("tuotteet/search.html", tuote = Tuote.query.filter(Tuote.tuotekoodi == tuotekoodi).first(), 
    hyllypaikat = Hyllypaikka.query.join(Tuote).filter(Hyllypaikka.tuotekoodi == tuotekoodi).all())