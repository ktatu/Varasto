from application import db
from sqlalchemy.sql import text

class Hyllypaikka(db.Model):
    paikkanumero = db.Column(db.Integer, primary_key=True, autoincrement=False)
    muokattu = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    osasto = db.Column(db.String(20), nullable=False)
    tuotekoodi = db.Column(db.Integer, db.ForeignKey('tuote.tuotekoodi'))
    maara = db.Column(db.Integer, default=0, nullable=False)
    kapasiteetti = db.Column(db.Integer)

    lokit = db.relationship('Loki', backref='hyllypaikka', lazy=True)

    def __init__(self, paikkanumero, osasto, maara, tuotekoodi):
        self.paikkanumero = paikkanumero
        self.osasto = osasto
        self.maara = maara
        self.tuotekoodi = tuotekoodi

    @staticmethod
    def find_shelf_location(tuote):

        # tarkistetaan onko kyseistä tuotetta hyllyssä ja samassa paikassa tilaa vielä
        # ei parametreja mutta wtforms tarkistaa että käyttäjäsyöte on kokonaislukuja - injektion ei pitäisi onnistua
        stmt = text("SELECT paikkanumero, maara FROM hyllypaikka WHERE tuotekoodi = "+str(tuote.tuotekoodi) + 
        " AND hyllypaikka.maara + "+str(tuote.hyllytettava) + " <= kapasiteetti LIMIT 1;")

        res = db.engine.execute(stmt)
        hyllypaikka = []


        for row in res:
            hyllypaikka.append({"paikkanumero":row[0], "maara":row[1]})

        if hyllypaikka:
            return hyllypaikka

        # ei löytynyt - etsitään samalta osastolta tyhjä paikka
        else:
            stmt = text("SELECT paikkanumero FROM hyllypaikka WHERE osasto = '"+tuote.kategoria+"' AND maara = 0 LIMIT 1;")

            res = db.engine.execute(stmt)
            for row in res:
                hyllypaikka.append({"paikkanumero":row[0], "maara":0})

            return hyllypaikka
