from application import db

class Package(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    address = db.Column(db.String(50), nullable=False)
    volume = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(10))
    driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'), nullable=False)

    def toDict(self):
        return {
            "id": self.id,
            "address": self.address,
            "status": self.status
        }