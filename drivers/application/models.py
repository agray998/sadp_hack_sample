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
            "surname": self.surname,
            "assigned packages": list(package.toDict() for package in self.packages)
        }

class Package(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    address = db.Column(db.String(50), nullable=False)
    volume = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(10))
    driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'))

    def toDict(self):
        return {
            "id": self.id,
            "address": self.address,
            "status": self.status
        }