from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import InputRequired, NumberRange

class KapasiteettiForm(FlaskForm):

    kapasiteetti = IntegerField("Määritä hyllypaikalle kapasiteetti:", [InputRequired(), NumberRange(min=1, max=100000)])

    class Meta:
        csrf = False

class TuoteVahennys(FlaskForm):

    vahennys = IntegerField("Saldovähennys:", [InputRequired(), NumberRange(min=1, max=100000)])

    class Meta:
        csrf = False