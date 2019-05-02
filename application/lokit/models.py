from application import db, app
from sqlalchemy.sql import text
from sqlalchemy import desc, Index

class Loki(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    luotu = db.Column(db.DateTime, default=db.func.current_timestamp())

    tuotekoodi = db.Column(db.Integer, db.ForeignKey('tuote.tuotekoodi'), nullable=False)
    kuvaus = db.Column(db.String(100), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False, index=True)
    paikkanumero = db.Column(db.Integer, db.ForeignKey('hyllypaikka.paikkanumero'), index=True)

    Index('luotu_indeksi', luotu.desc())

    def __init__(self, tuotekoodi, kuvaus, account_id, paikkanumero):
        self.tuotekoodi = tuotekoodi
        self.kuvaus = kuvaus
        self.account_id = account_id
        self.paikkanumero = paikkanumero
