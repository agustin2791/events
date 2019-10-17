from flask import Flask, jsonify, request, url_for, session, redirect, render_template
from flask_restful import Resource, Api
from flask_pymongo import PyMongo, MongoClient
from flask_user import login_required, UserManager, UserMixin
from flask_jwt_extended import JWTManager, jwt_refresh_token_required
from flask_cors import CORS
import bcrypt
from bson.objectid import ObjectId
from api.events import AllEvents

class ConfigClass(object):
    MONGO_URI = 'mongodb://localhost:27017/meetdb'
    USER_APP_NAME = 'Meeting App'
    USER_ENABLE_EMAIL = False
    USER_ENEABLE_USERNAME = True
    USER_REQUIRE_RETYPE_PASSWORD = False
    JWT_SECRET_KEY = '0rgFhiQ7vrgEOaoU5NnY_ZCommoZgelFKa1dxGc0TK3b_KwNIKeTaSTjOVNWjm_38WArirTrmmhY8DSg8OPC6hvCw62X0DaRxZVCW8Z-fVJeJdX005R6oVlCxMES1aAT_3RYDWiMf-Dv9dF0-uhgZq48yumOYYObpGQ8jlJ_g5M5Lm0oLgHb_LVUhE8cpgshER4OZkLu5pR49X_gynKFxjC2tRTn886-vry3NFzM1yFmz3bja_RGj8cW07RbfjIEr9O4ieRr5rXzYNGtoSeix19jOPEsOpE4_HDbOKOosHnr2qZl3Q4M4gKbsyLvovD4TnNJ7piI7ua4TDB40qfuuw'
    JWT_ALGORITHM = 'HS256'

def start_app():
    app = Flask(__name__,
        static_folder='../dist/static',
        template_folder='../dist')
    app.config.from_object(__name__+'.ConfigClass')
    api = Api(app)
    db = PyMongo(app)
    cors = CORS(app)

    api.add_resource(AllEvents, '/api/events')

    return app

if __name__ == '__main__':
    app = start_app()
    app.run(debug=True)