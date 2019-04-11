from application import db
from sqlalchemy.sql import text

class Loki(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    luotu = db.Column(db.DateTime, default=db.func.current_timestamp())

    tuotekoodi = db.Column(db.Integer, db.ForeignKey('tuote.tuotekoodi'), nullable=False)
    kuvaus = db.Column(db.String(100), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    paikkanumero = db.Column(db.Integer, db.ForeignKey('hyllypaikka.paikkanumero'))

    def __init__(self, tuotekoodi, kuvaus, account_id):
        self.tuotekoodi = tuotekoodi
        self.kuvaus = kuvaus
        self.account_id = account_id
