from flask import request
from application import app, db
from application.models import Package, Driver

@app.route('/add', methods=['POST'])
def add():
    package_info = request.get_json()
    db.session.add(Package(address=package_info['address'], volume=package_info['volume'], driver_id=package_info['assigned_driver'], status="pending"))
    db.session.commit()
    return {"packages": list(package.toDict() for package in Package.query.all())}

@app.route('/set_status', methods=['POST'])
def set_status():
    pid=int(request.args.get('pid'))
    package = Package.query.get(pid)
    package.status = request.get_json()['status']
    if package.status in ['delivered', 'cancelled']:
        pass
    db.session.commit()
    return f"package {package.id} is {package.status}"

@app.route('/assign_driver')
def assign():
    assignment = request.get_json()
    package = Package.query.get(assignment['package'])
    package.driver_id = assignment['driver']
    db.session.commit()
    driver = Driver.query.get(assignment['driver'])
    return f"Package #{package.id}: Assigned to {driver.surname.upper()}, {driver.forename}"