from flask import request
from application import app, db
from application.models import Driver

@app.route('/add', methods=['POST'])
def add():
    driver_info = request.get_json()
    db.session.add(Driver(forename=driver_info['forename'], surname=driver_info['surname']))
    db.session.commit()
    return {"drivers": list(driver.toDict() for driver in Driver.query.all())}