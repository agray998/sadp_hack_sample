from flask import request
from application import app, db
from application.models import Package

@app.route('/add', methods=['POST'])
def add():
    package_info = request.get_json()
    db.session.add(Package(address=package_info['address'], volume=package_info['volume'], status="pending"))
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