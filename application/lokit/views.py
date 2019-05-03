from flask import render_template, url_for, redirect, flash, request
from flask_login import login_required, current_user
from sqlalchemy import desc

from application import app, db
from application.lokit.models import Loki
from application.hyllypaikat.models import Hyllypaikka

 # kirjautuneen käyttäjän lokit
@app.route("/lokit/userlogs")
@login_required
def kayttaja_lokit():
    sivu = request.args.get('sivu', 1, type=int)
    lokit = Loki.query.filter(Loki.account_id == current_user.id).order_by(Loki.luotu.desc()).paginate(sivu, 12, False)

    edellinen_sivu = url_for('kayttaja_lokit', sivu = lokit.prev_num) \
        if lokit.has_prev else None

    seuraava_sivu = url_for('kayttaja_lokit', sivu = lokit.next_num) \
        if lokit.has_next else None

    return render_template("/lokit/userlogs.html", lokit = lokit.items, edellinen_sivu = edellinen_sivu, seuraava_sivu = seuraava_sivu)

 # hyllypaikan lokit
@app.route("/lokit/<paikkanumero>")
@login_required
def hyllypaikka_lokit(paikkanumero):


    sivu = request.args.get('sivu', 1, type=int)
    lokit = Loki.query.filter(Loki.paikkanumero == paikkanumero).order_by(Loki.luotu.desc()).paginate(sivu, 12, False)

    edellinen_sivu = url_for('hyllypaikka_lokit', sivu = lokit.prev_num) \
        if lokit.has_prev else None

    seuraava_sivu = url_for('hyllypaikka_lokit', sivu = lokit.next_num) \
        if lokit.has_next else None

    if lokit:
        return render_template("/lokit/shelflogs.html", lokit = lokit.items, edellinen_sivu = edellinen_sivu, seuraava_sivu = seuraava_sivu)

    else:
        flash('Kyseiselle paikalle ei ole lokeja')
        return redirect(url_for('index'))

    