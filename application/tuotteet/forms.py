from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField
from wtforms.validators import InputRequired, Length, NumberRange
from wtforms import validators


class TuoteForm(FlaskForm):
    tuotekoodi = IntegerField("Tuotekoodi", [InputRequired(), NumberRange(min=10000, max=999999999999999, message='Min. pituus 5, max. 15')])
    nimi = StringField("Nimi", [InputRequired(), Length(min=3, max=30, message="Pituus vähintään 3 merkkiä, enintään 30")])
    maara = IntegerField("Määrä", [InputRequired(), NumberRange(min=1, max=100000)])
    kategoria = RadioField(u'Kategoria', [InputRequired(message="Valitse kategoria")], choices=[('koti', 'Koti'), ('vapaa-aika', 'Vapaa-aika'), ('elintarvike', 'Elintarvike')])
    kuvaus = StringField("Kuvaus", [Length(max=50, message="Pituus enintään 50 merkkiä")])

    class Meta:
        csrf = False

class mainPageForm(FlaskForm):
    tuotekoodi = IntegerField("Tuotekoodi", [InputRequired(), NumberRange(min=10000, max=999999999999999, message='Min. pituus 5, max. 15')])
    maara = IntegerField("Määrä", [NumberRange(min=1, max=100000, message="Määrä vähintään 1, enintään 100000")])

    class Meta:
        csrf = False

class PoistoForm(FlaskForm):
    tuotekoodi = tuotekoodi = IntegerField("Tuotekoodi:", [InputRequired(), NumberRange(min=10000, max=999999999999999)])

    class Meta:
        csrf = False

class PaivitysForm(FlaskForm):

    tuotekoodi = IntegerField("Tuotekoodi", [InputRequired(), NumberRange(min=10000, max=999999999999999, message='Min. pituus 5, max. 15')])
    nimi = StringField("Nimi", [InputRequired(), Length(min=3, max=30, message="Pituus vähintään 3 merkkiä, enintään 30")])
    kategoria = RadioField(u'Kategoria', [InputRequired(message="Valitse kategoria")], choices=[('koti', 'Koti'), ('vapaa-aika', 'Vapaa-aika'), ('elintarvike', 'Elintarvike')])
    kuvaus = StringField("Kuvaus", [Length(max=50, message="Pituus enintään 50 merkkiä")])

    class Meta:
        csrf = False

