from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField


class TuoteForm(FlaskForm):
    tuotekoodi = IntegerField("Tuotekoodi")
    nimi = StringField("Nimi")
    maara = IntegerField("Määrä")
    kategoria = RadioField(u'Kategoria', choices=[('k', 'Koti'), ('v', 'Vapaa-aika'), ('e', 'Elintarvike')])
    kuvaus = StringField("Kuvaus")

    class Meta:
        csrf = False