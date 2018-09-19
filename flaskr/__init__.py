# Khai vao thu vien chuan
from flask import Flask , jsonify, request
# Khai bao thu vien restful
from flask_restful import Api, Resource, reqparse
# Khai bai thu vien admin
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView 
# Khai bao thu vien ket noi mysql
from flask_sqlalchemy import SQLAlchemy 
# KHai bao thu vien tao database 
from flask_migrate import Migrate
# Khai bao thu vien json web token
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity) 

parser = reqparse.RequestParser()
parser.add_argument('username')
parser.add_argument('password')

class Login(Resource):
	def put(self):
		args = parser.parse_args()
		username = args['username']
		password = args['password']
		#return {username : password}
		#'''
		if not username:
			return jsonify({"msg": "Missing username parameter"})
		if not password:
			return jsonify({"msg": "Missing password parameter"})
		if username == 'test' or password == 'test':
			return jsonify({"msg": "Bad username or password"})
		#'''
		access_token = create_access_token(identity=username)
		return jsonify(access_token=access_token)
		
class Helloworld(Resource):
	@jwt_required
	def get(self):
		return {'hello':'world'}

def create_app():
	# khoi tao va cau hinh chuong trinh
	app = Flask(__name__)
	app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://leeflask:bellT123$@localhost/flaskdbjwt'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	app.config['SECRET_KEY'] = '123456789qwertyuyiopasdfghjklzxcvbnm'
	# khoi tao database
	from db import db , User
	db.init_app(app)
	migrate = Migrate(app,db)
	admin = Admin(app, name='Admin', template_mode='bootstrap3')
	admin.add_view(ModelView(User,db.session))

	# khoi tao jwt
	#app.config['JWT_TOKEN_LOCATION'] = ['json']
	app.config['JWT_SECRET_KEY'] = '123456789qwertyuyiopasdfghjklzxcvbnmasfasasgasgasd' 
	jwt = JWTManager(app)

	# khoi tao restful
	api = Api(app)
	api.add_resource(Login,'/login')
	api.add_resource(Helloworld,'/hello')
	return app


