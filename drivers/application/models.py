from application import db

class Driver(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    forename = db.Column(db.String(20))
    surname = db.Column(db.String(20))
    packages = db.relationship('Package', backref='driver')

    def toDict(self):
        return {
            "id": self.id,
            "forename": self.forename,
            "surname": self.surname
        }