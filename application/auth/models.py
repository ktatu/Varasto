from application import db

class Kayttaja(db.Model):
    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)
    nimi = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    rooli = db.Column(db.String(20), nullable=False)

    lokit = db.relationship("Loki", backref='account', lazy=True)

    def __init__(self, nimi, username, password):
        self.nimi = nimi
        self.username = username
        self.password = password
        self.rooli = "NORMAALI"

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