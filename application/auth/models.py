from application import db

class Kayttaja(db.Model):
    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)
    luotu = db.Column(db.DateTime, default=db.func.current_timestamp())

    nimi = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    lokit = db.relationship("Loki", backref='account', lazy=True)

    def __init__(self, nimi):
        self.nimi = nimi

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True