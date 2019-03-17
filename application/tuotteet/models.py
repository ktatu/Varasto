from application import db

class Tuote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    tuotekoodi = db.Column(db.Integer, nullable=False)
    nimi = db.Column(db.String(144), nullable=False)
    maara = db.Column(db.Integer, nullable=False)
    kategoria = db.Column(db.String(100), nullable=False)
    kuvaus = db.Column(db.String(200), nullable=True)

    def __init__(self, tuotekoodi, nimi, maara, kategoria, kuvaus):
        self.tuotekoodi = tuotekoodi
        self.nimi = nimi
        self.maara = maara
        self.kategoria = kategoria
        self.kuvaus = kuvaus