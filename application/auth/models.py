from application import db
from sqlalchemy import Index
from sqlalchemy.sql import text
from datetime import datetime, timedelta

class Kayttaja(db.Model):
    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True, index=True)
    nimi = db.Column(db.String(144), nullable=False, index=True)
    username = db.Column(db.String(144), nullable=False, index=True)
    password = db.Column(db.String(144), nullable=False, index=True)
    rooli = db.Column(db.String(20), nullable=False)

    lokit = db.relationship("Loki", backref='account', lazy=True)

    def __init__(self, nimi, username, password, rooli="NORMAALI"):
        self.nimi = nimi
        self.username = username
        self.password = password
        self.rooli = rooli

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def is_admin(self):
        if self.rooli == "ADMIN":
            return True
        else: return False

    def role(self):
        return self.rooli

    @staticmethod
    def ahkerimmat_tyontekijat():

        ylaraja = datetime.now()
        alaraja = datetime.now() - timedelta(days=7)

        stmt = text("SELECT account.username, COUNT(loki.id) FROM loki JOIN account ON loki.account_id = account.id WHERE loki.luotu BETWEEN :alaraja AND :ylaraja GROUP BY account.username ORDER BY COUNT(loki.id) DESC LIMIT 5;").params(alaraja=alaraja, ylaraja=ylaraja)

        res = db.engine.execute(stmt)
        tyontekijat = []

        for row in res: 
            tyontekijat.append({"username":row[0], "maara":row[1]})

        return tyontekijat