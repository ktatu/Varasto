from application import app, db
from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy.sql.expression import exists
from sqlalchemy import select
from application.tuotteet.models import Tuote
from application.tuotteet.forms import TuoteForm, mainPageForm, PoistoForm, PaivitysForm
from flask_login import login_required, current_user
from application.lokit.models import Loki
from application.hyllypaikat.models import Hyllypaikka
 
@app.route("/tuotteet/new", methods=["POST"])
def tuotteet_palautus():
    return redirect(url_for('tuotteet_etusivu'))

# tuotteen luominen ja tuotteen päivitys - päivityksen toteuttaa apumetodi paivita_tuote
@app.route("/tuotteet", methods=["POST"])
@login_required
def luo_tuote():

    form = TuoteForm(request.form)
    if not form.validate():
        return render_template("tuotteet/new.html", form = form)

    t = Tuote(form.tuotekoodi.data, form.nimi.data, form.maara.data, form.kategoria.data, form.kuvaus.data)
    t.hyllytettava = form.maara.data

    loki = Loki(form.tuotekoodi.data, "tuotelisäys määrä "+str(form.maara.data), current_user.id, None)
    t.lokit.append(loki)

    db.session().add(loki)
    db.session().add(t)
    db.session().commit()

    flash('Tuote '+str(form.tuotekoodi.data) + ' lisätty')
    return redirect(url_for("tuotteet_etusivu"))

@app.route("/tuotteet/update/<tuotekoodi>", methods=["POST"])
@login_required
def paivita_tuote(tuotekoodi):

    form = PaivitysForm(request.form)

    if not form.validate():
        return redirect(url_for('paivita_tuote_lomake', tuotekoodi=tuotekoodi))

    # tarkistetaan onko tuotekoodi vapaa
    if int(tuotekoodi) != int(form.tuotekoodi.data):
        tuotekoodi_tarkistus = Tuote.query.filter(Tuote.tuotekoodi == form.tuotekoodi.data).first()
        if tuotekoodi_tarkistus:
            flash('Syötetty tuotekoodi on jo käytössä')
            return redirect(url_for('paivita_tuote_lomake', tuotekoodi=tuotekoodi))  

    tuote = Tuote.query.filter(Tuote.tuotekoodi == tuotekoodi).first()

    tuote.tuotekoodi = form.tuotekoodi.data
    tuote.nimi = form.nimi.data
    tuote.kategoria = form.kategoria.data
    tuote.kuvaus = form.kuvaus.data

    db.session().add(tuote)
    db.session().commit()

    flash('Tuotetiedot päivitetty')
    return redirect(url_for('tuotteet_etusivu'))

@app.route("/tuotteet", methods=["GET"])
@login_required
def tuotteet_indeksi():
    return render_template("tuotteet/list.html", tuotteet = Tuote.query.all())

@app.route("/tuotteet/main")
def tuotteet_etusivu():
    return render_template("tuotteet/main.html", form = mainPageForm())

@app.route("/tuotteet/main", methods=["POST"])
@login_required
def tuote_toiminnot():

    form = mainPageForm(request.form)
    koodi = form.tuotekoodi.data
    tuote = db.session().query(Tuote).filter(Tuote.tuotekoodi==koodi).first()

    if not form.tuotekoodi.validate(form):
        return render_template("tuotteet/main.html", form = form)

    # tuotehaku
    if request.form["nappi"] == "Hae tuotetta":
        if tuote:
            return redirect(url_for('tuotenakyma', tuotekoodi = koodi))
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
            return render_template("/tuotteet/new.html", form = tuoteForm, paivitys = False)

    # saldolisäys
    else:

        lisattava = form.maara.data
        if not form.maara.validate(form):
            return render_template("tuotteet/main.html", form = form)

        if tuote:
            tuote.maara = tuote.maara + lisattava
            tuote.hyllytettava = tuote.hyllytettava + lisattava
            loki = Loki(koodi, "saldopäivitys määrä "+str(lisattava), current_user.id, None)

            db.session().add(loki)
            db.session().commit()

            flash('Tuotteeseen ' + str(koodi) + ' lisätty ' + str(lisattava))
        else:
            flash('Tuotetta ' + str(koodi) + ' ei ole varastossa')

        return redirect(url_for("tuotteet_etusivu"))

@app.route("/tuotteet/delete", methods=["POST"])
@login_required
def poista_tuote(tuotekoodi):

    form = PoistoForm(request.form)
    poisto_koodi = form.tuotekoodi.data

    if int(poisto_koodi) != int(tuotekoodi):
        flash('Väärä tuotekoodi')
        return redirect(url_for('tuotenakyma', tuotekoodi = tuotekoodi))

    # tuotteen hyllypaikat vapautetaan
    hyllypaikat = Hyllypaikka.query.filter(Hyllypaikka.tuotekoodi == tuotekoodi).all()
    for hyllypaikka in hyllypaikat:
        hyllypaikka.maara = 0
        hyllypaikka.kapasiteetti = 0
        db.session().add(hyllypaikka)

    tuote = Tuote.query.filter(Tuote.tuotekoodi == tuotekoodi).first()
    db.session().delete(tuote)
    db.session().commit()

    flash('Tuote ' + str(tuotekoodi) + ' poistettu')
    return redirect(url_for('index'))

@app.route("/tuotteet/update/<tuotekoodi>", methods=["GET"])
@login_required
def paivita_tuote_lomake(tuotekoodi):

    tuote = Tuote.query.filter(Tuote.tuotekoodi == tuotekoodi).first()

    form = PaivitysForm()
    form.tuotekoodi.data = tuote.tuotekoodi
    form.nimi.data = tuote.nimi
    form.kategoria.data = tuote.kategoria
    form.kuvaus.data = tuote.kuvaus

    return render_template("/tuotteet/update.html", form = form, vanha_tuotekoodi = tuotekoodi)

# apumetodi tuote_toiminnoille
@app.route("/tuotteet/search", methods=["GET"])
def nayta_tuote(parametri_tuote, form):

    return render_template("tuotteet/main.html", form = form, tuote = parametri_tuote, 
    hyllypaikat = Hyllypaikka.query.join(Tuote).filter(Hyllypaikka.tuotekoodi == parametri_tuote.tuotekoodi).all())


# metodi listojen (esim. kaikkien tuotteiden listaus, tuotteet_indeksi) tuotelinkkejä varten
@app.route("/tuotteet/<tuotekoodi>")
def tuotenakyma(tuotekoodi):

    return render_template("tuotteet/search.html", tuote = Tuote.query.filter(Tuote.tuotekoodi == tuotekoodi).first(), 
    hyllypaikat = Hyllypaikka.query.join(Tuote).filter(Hyllypaikka.tuotekoodi == tuotekoodi).all(), form = PoistoForm())


