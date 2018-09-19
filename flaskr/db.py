# khoi tao thu vien SQLALCHEMY
from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

class User(db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), nullable= False, unique= True)
	password = db.Column(db.String(80), nullable= False)
	first_name = db.Column(db.String(100))
	last_name = db.Column(db.String(100))