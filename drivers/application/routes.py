from flask import request
from application import app, db
from application.models import Driver

@app.route('/add', methods=['POST'])
def add():
    driver_info = request.get_json()
    driver = Driver(forename=driver_info['forename'], surname=driver_info['surname'])
    db.session.add(driver)
    db.session.commit()
    return f"{driver.surname.upper()}, {driver.forename} added to driver roster\n"

@app.route('/get_all')
def get_all():
    return {"drivers": list(driver.toDict() for driver in Driver.query.all())}

@app.route('/get_driver')
def get_driver():
    id = request.args.get('id')
    return Driver.query.get(id).toDict()

@app.route('/update_details', methods=['POST'])
def update_details():
    id = request.args.get('id')
    driver = Driver.query.get(id)
    update = request.get_json()
    driver.forename, driver.surname = update.get('forename', driver.forename), update.get('surname', driver.surname)
    db.session.commit()
    return f"Details updated for driver #{driver.id}\n"

@app.route('/delete')
def delete():
    id = request.args.get('id')
    driver = Driver.query.get(id)
    db.session.delete(driver)
    db.session.commit()
    return f"Driver #{driver.id} ({driver.surname.upper()}, {driver.forename}) removed from roster\n"