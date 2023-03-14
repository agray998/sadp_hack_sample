from flask import request
from application import app, db
from application.models import Package, Driver

@app.route('/add', methods=['POST'])
def add():
    package_info = request.get_json()
    package = Package(address=package_info['address'], volume=package_info['volume'], status="pending")
    db.session.add(package)
    db.session.commit()
    return f"Registered: package #{package.id}. A driver will be assigned soon\n"

@app.route('/set_status', methods=['POST'])
def set_status():
    pid=int(request.args.get('pid'))
    package = Package.query.get(pid)
    package.status = request.get_json()['status']
    if package.status == 'delivered':
        package.driver_id = None
    elif package.status == 'cancelled':
        db.session.delete(package)
    db.session.commit()
    return f"package {package.id} is {package.status}\n"

@app.route('/assign_driver', methods=['POST'])
def assign():
    assignment = request.get_json()
    did, pid = assignment['driver'], assignment['package']
    package = Package.query.get(pid)
    driver = Driver.query.get(did)
    package.driver_id = driver.id
    db.session.commit()
    return f"Package #{package.id}: Assigned to {driver.surname.upper()}, {driver.forename}\n"

@app.route('/get_all')
def get_all():
    return {"packages": list(package.toDict() for package in Package.query.all())}

@app.route('/get_package')
def get_package():
    id = request.args.get('id')
    return Package.query.get(id).toDict()
