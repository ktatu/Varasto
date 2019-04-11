from flask import render_template, url_for, redirect, flash
from flask_login import login_required, current_user

from application import app, db
from application.lokit.models import Loki
from application.hyllypaikat.models import Hyllypaikka

 # kirjautuneen käyttäjän lokit
@app.route("/lokit/userlogs")
@login_required
def user_logs():

    return render_template("/lokit/userlogs.html", lokit = current_user.lokit)

 # hyllypaikan lokit
@app.route("/lokit/<paikkanumero>")
@login_required
def shelf_logs(paikkanumero):

    hyllypaikka = Hyllypaikka.query.filter(Hyllypaikka.paikkanumero == paikkanumero).first()

    if hyllypaikka:
        return render_template("/lokit/shelflogs.html", lokit = hyllypaikka.lokit)

    # pitäisi tapahtua ainoastaan jos kirjoittaa url-bariin hyllypaikan, johon ei ikinä ole hyllytetty
    else:
        flash('Kyseiselle paikalle ei ole lokeja')
        return redirect(url_for('index'))

    