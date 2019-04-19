from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///varasto.db"
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

from functools import wraps

def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user:
                return login_manager.unauthorized()

            if not current_user.is_authenticated:
                return login_manager.unauthorized()
            
            unauthorized = False
            if role != "ANY":
                unauthorized = True
                
                # sovelluksessa 1 rooli per käyttäjä, joten ei looppia
                if current_user.role() == role:
                    unauthorized = False

            if unauthorized:
                return login_manager.unauthorized()
            
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper

from application import views

from application.tuotteet import models
from application.tuotteet import views

from application.auth import models
from application.auth import views

from application.lokit import models
from application.lokit import views

from application.hyllypaikat import models
from application.hyllypaikat import views

from application.auth.models import Kayttaja

@login_manager.user_loader
def load_user(user_id):
    return Kayttaja.query.get(user_id)

try:
    db.create_all()
except:
    pass