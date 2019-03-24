from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField
from wtforms.validators import InputRequired, Length, NumberRange


class TuoteForm(FlaskForm):
    tuotekoodi = IntegerField("Tuotekoodi", [InputRequired(), NumberRange(min=5, max=15, message='Min. pituus 5, max. 15')])
    nimi = StringField("Nimi", [InputRequired(), Length(min=3, max=30, message="Pituus vähintään 3 merkkiä, enintään 30")])
    maara = IntegerField("Määrä", [InputRequired(), NumberRange(min=1, max=100000)])
    kategoria = RadioField(u'Kategoria', [InputRequired(message="Valitse kategoria")], choices=[('k', 'Koti'), ('v', 'Vapaa-aika'), ('e', 'Elintarvike')])
    kuvaus = StringField("Kuvaus", [Length(max=50, message="Pituus enintään 50 merkkiä")])

    class Meta:
        csrf = False

class mainPageForm(FlaskForm):
    tuotekoodi = IntegerField("Tuotekoodi", [InputRequired(), NumberRange(min=5, max=15, message='Min. pituus 5, max. 15')])
    maara = IntegerField("Määrä", [InputRequired(), NumberRange(min=1, max=100000)])

    class Meta:
        csrf = False