from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
from os import getenv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://root:{getenv('MYSQL_ROOT_PASSWORD')}@mysql:3306/qommon"
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQL_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

import application.routes