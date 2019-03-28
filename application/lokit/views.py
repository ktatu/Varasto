from flask import render_template
from flask_login import login_required, current_user

from application import app, db
from application.lokit.models import Loki

@app.route("/lokit/userlogs")
@login_required
def user_logs():

    return render_template("/lokit/userlogs.html", lokit = current_user.lokit)