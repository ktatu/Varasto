from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import InputRequired

class LoginForm(FlaskForm):
    username = StringField("Käyttäjä")
    password = PasswordField("Salasana")

    class Meta:
        csrf = False


class CreateUserForm(FlaskForm):
    nimi = StringField("Nimi:", [InputRequired()])
    username = StringField("Käyttäjänimi:", [InputRequired()])
    password = PasswordField("Salasana:", [InputRequired])

    class Meta:
        csrf = False