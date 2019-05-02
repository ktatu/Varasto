from flask_wtf import FlaskForm
from wtforms import IntegerField, RadioField
from wtforms.validators import InputRequired, NumberRange
from wtforms import validators

class KapasiteettiForm(FlaskForm):

    kapasiteetti = IntegerField("Määritä hyllypaikalle kapasiteetti:", [InputRequired(), NumberRange(min=1, max=100000)])

    class Meta:
        csrf = False

class TuoteVahennys(FlaskForm):

    vahennys = IntegerField("Saldovähennys", [InputRequired(message="Määritä kapasiteetti"), NumberRange(min=1, max=100000, message="Kapasiteetin oltava vähintään 1, enintään 100000")])

    class Meta:
        csrf = False

class HyllypaikkaForm(FlaskForm):
    paikkanumero = IntegerField("Hyllypaikka", [InputRequired(), NumberRange(min=1, max=100000)])
    osasto = RadioField(u'Osasto', [InputRequired()], choices=[('koti', 'Koti'), ('vapaa-aika', 'Vapaa-aika'), ('elintarvike', 'Elintarvike')])

    class Meta:
        csrf = False