from application import app, db
from flask import Flask, render_template, request, before_render_template, flash, redirect, url_for
from sqlalchemy.sql.expression import exists
from flask_login import current_user, login_required
from application.tuotteet.models import Tuote
from application.hyllypaikat.models import Hyllypaikka
from application.hyllypaikat.forms import KapasiteettiForm, TuoteVahennys
from application.lokit.models import Loki

@app.route("/varasto/main")
def varasto_etusivu():
    return render_template("/varasto/main.html")

# sivu tuotteille jotka voidaan hyllyttää (tuote.hyllytettava > 0)
@app.route("/varasto/hyllytettavat", methods=["GET"])
@login_required
def hyllytettavat_tuotteet():

    tuotteet = Tuote.query.filter(Tuote.hyllytettava != 0).all()
    print(tuotteet)
    if tuotteet:
        return render_template("/varasto/hyllytettavat.html", tuotteet = tuotteet)
    else:
        flash('Ei hyllytettäviä tuotteita')
        return redirect(url_for('index'))

# hyllytyssivu
@app.route("/varasto/hyllyyn/<tuotekoodi>/", methods=["GET"])
@login_required
def valitse_hyllypaikka(tuotekoodi):

    tuoteHyllyyn = db.session().query(Tuote).filter(Tuote.tuotekoodi == tuotekoodi).first()
    hyllypaikka = Hyllypaikka.find_shelf_location(tuoteHyllyyn)

    if hyllypaikka:
        return render_template("/varasto/hyllyyn.html", tuote = tuoteHyllyyn, paikka = hyllypaikka, form = KapasiteettiForm())

    else:
        flash('Tuotteelle '+str(tuoteHyllyyn.tuotekoodi) +' ei ole vapaana hyllypaikkoja')
        return redirect(url_for('hyllytettavat_tuotteet'))

# toteuttaa hyllytyksen
@app.route("/varasto/hyllyyn/<tuotekoodi>/<paikkanumero>/", methods=["POST"])
@login_required
def hyllyta_tuote(tuotekoodi, paikkanumero):

    # keksi miten palautttaa oliot tuote ja hyllypaikka sivulta / choose_self-metodilta ilman uutta hakua
    tuote = db.session().query(Tuote).filter(Tuote.tuotekoodi == tuotekoodi).first()
    hyllypaikka = db.session().query(Hyllypaikka).filter(Hyllypaikka.paikkanumero == paikkanumero).first()

    tuote.hyllypaikat.append(hyllypaikka)

    form = KapasiteettiForm(request.form)
     
    if hyllypaikka.maara == 0 and not form.kapasiteetti.validate(form):
        flash('Kapasiteetin oltava vähintään 1, enintään 1000000')
        return redirect(url_for("valitse_hyllypaikka", tuotekoodi = tuotekoodi))


    else:
        hyllypaikka.tuotekoodi = tuote.tuotekoodi
        hyllypaikka.muokattu = db.func.current_timestamp()
        hyllypaikka.kapasiteetti = form.kapasiteetti.data
        hyllypaikka.maara += tuote.hyllytettava

        loki = Loki(tuote.tuotekoodi, "Hyllysiirto määrä "+str(tuote.hyllytettava)+ " paikkanumero "+str(hyllypaikka.paikkanumero), current_user.id, paikkanumero)
        hyllypaikka.lokit.append(loki)

        tuote.muokattu = db.func.current_timestamp()
        tuote.hyllytettava = 0

        db.session().add(tuote)
        db.session().add(hyllypaikka)
        db.session().add(loki)
        db.session().commit()

        flash('Hyllytys onnistui')
        return redirect(url_for('hyllytettavat_tuotteet'))

# näyttää hyllypaikan
@app.route("/varasto/<paikkanumero>", methods=["GET"])
@login_required
def nayta_hyllypaikka(paikkanumero):

    hyllypaikka = Hyllypaikka.query.filter(Hyllypaikka.paikkanumero == paikkanumero).first()

    if hyllypaikka:
        return render_template("varasto/hyllypaikka.html", hyllypaikka = hyllypaikka, form = TuoteVahennys())

    else:
        flash('Hyllypaikkaa ei löytynyt')
        return redirect(url_for('index'))

# saldovähennys hyllypaikalla
@app.route("/varasto/<paikkanumero>/<tuotekoodi>", methods=["POST"])
@login_required
def saldo_vahenna(paikkanumero, tuotekoodi):

    hyllypaikka = Hyllypaikka.query.filter(Hyllypaikka.paikkanumero == paikkanumero).first()
    tuote = Tuote.query.filter(Tuote.tuotekoodi == tuotekoodi).first()
    
    form = TuoteVahennys(request.form)
    vahennys = int(form.vahennys.data)

    if vahennys > hyllypaikka.maara:
        flash('Yritit vähentää ' + str(vahennys) + ", kun hyllyssä on " + str(hyllypaikka.maara))
        return redirect(url_for('nayta_hyllypaikka', paikkanumero = hyllypaikka.paikkanumero))

    else:
        hyllypaikka.maara -= vahennys
        loki = Loki(tuotekoodi, "Saldovähennys " + str(vahennys) + " paikkanumero " + paikkanumero, current_user.id, paikkanumero)
        hyllypaikka.lokit.append(loki)
        tuote.maara -= vahennys

        # tuote poistetaan hyllypaikalta kokonaan jos saldosta tulee 0
        if hyllypaikka.maara == 0:
            hyllypaikka.tuotekoodi == None
            hyllypaikka.kapasiteetti == 0
            tuote.hyllypaikat.remove(hyllypaikka)

        db.session().add(hyllypaikka)
        db.session().add(loki)
        db.session().add(tuote)
        db.session().commit()

        flash('Saldovähennys onnistui')
        return redirect(url_for('nayta_hyllypaikka', paikkanumero = hyllypaikka.paikkanumero))




    

