from application import db

class Hyllypaikka(db.Model):
    paikkanumero = db.Column(db.Integer, primary_key=True, autoincrement=False)
    muokattu = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    osasto = db.Column(db.String(20), nullable=False)
    tuotekoodi = db.Column(db.Integer, db.ForeignKey('tuote.tuotekoodi'))
    maara = db.Column(db.Integer)
    kapasiteetti = db.Column(db.Integer)

    def __init__(self, paikkanumero, osasto):
        self.paikkanumero = paikkanumero
        self.osasto = osasto