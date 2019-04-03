from application import app, db

class Tuote(db.Model):
    tuotekoodi = db.Column(db.Integer, primary_key=True, autoincrement=False)
    luotu = db.Column(db.DateTime, default=db.func.current_timestamp())
    muokattu = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    nimi = db.Column(db.String(144), nullable=False)
    maara = db.Column(db.Integer, nullable=False)
    kategoria = db.Column(db.String(100), nullable=False)
    kuvaus = db.Column(db.String(200), nullable=True)
    hyllytettava = db.Column(db.Integer, default=0, nullable=True)

    hyllypaikat = db.relationship('Hyllypaikka', backref='tuote', lazy=True)

    def __init__(self, tuotekoodi, nimi, maara, kategoria, kuvaus):
        self.tuotekoodi = tuotekoodi
        self.nimi = nimi
        self.maara = maara
        self.kategoria = kategoria
        self.kuvaus = kuvaus