from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import InputRequired, length

class LoginForm(FlaskForm):
    username = StringField("Käyttäjä", [InputRequired()])
    password = PasswordField("Salasana", [InputRequired()])

    class Meta:
        csrf = False


class CreateUserForm(FlaskForm):
    nimi = StringField("Nimi", [InputRequired(), length(min=3, max=30)])
    username = StringField("Käyttäjänimi", [InputRequired(), length(min=3, max=30)])
    password = PasswordField("Salasana", [InputRequired(), length(min=3, max=30)])

    class Meta:
        csrf = False