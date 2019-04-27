from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import InputRequired, NumberRange

class KapasiteettiForm(FlaskForm):

    kapasiteetti = IntegerField("Määritä hyllypaikalle kapasiteetti:", [InputRequired(), NumberRange(min=1, max=100000)])

    class Meta:
        csrf = False

class TuoteVahennys(FlaskForm):

    vahennys = IntegerField("Saldovähennys:", [InputRequired(message="Määritä kapasiteetti"), NumberRange(min=1, max=100000, message="Kapasiteetin oltava vähintään 1, enintään 100000")])

    class Meta:
        csrf = False