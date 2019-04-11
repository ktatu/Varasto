from flask import render_template, request, url_for, redirect, flash
from flask_login import login_user, logout_user, current_user

from application import app, db, login_required
from application.auth.models import Kayttaja
from application.auth.forms import LoginForm, CreateUserForm



@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = Kayttaja.query.filter_by(username = form.username.data, password = form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form, error = "Käyttäjää ei tunnistettu")

    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/create")
@login_required(role="ADMIN")
def create_user_form():
    return render_template("auth/create.html", form = CreateUserForm())

@app.route("/auth/new", methods = ["POST"])
def create_user():
    form = CreateUserForm(request.form)

    print(form.nimi.data+"---------------")
    print(form.username.data)
    print(form.password.data+"------------")

    #if not form.validate():
    #    print("ei validoitunut----------------------")
    #    return render_template("auth/create.html", form = form)

    checkIfExists = Kayttaja.query.filter(Kayttaja.username == form.username.data).first()
    if checkIfExists:
        print("olemassa---------------------------------")
        flash('Käyttäjänimi on jo olemassa')
        return redirect(url_for("create_user_form"))

    else:
        print("ei olemassa--------------------------")
        kayttaja = Kayttaja(form.nimi.data, form.username.data, form.password.data)
        db.session().add(kayttaja)
        db.session().commit()

        flash('Uusi käyttäjä luotu')
        return redirect(url_for("index"))

    

    
