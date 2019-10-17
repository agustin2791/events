from flask import Flask, jsonify, request, url_for, session, redirect
from flask_restful import Resource, Api
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/meetdb'
api = Api(app)
db = PyMongo(app)
connect = db.db.events

class AllEvents(Resource):
    def get(self):
        data = connect.find()
        events = []
        for d in data:
            events.append({
                'id': str(d['_id']),
                'eventName': d['eventName'],
                'eventDetails': d['eventDetails'],
                'date': d['date'],
                'time': d['time'],
                'available': d['available'],
                'members': d['members'],
                'host': d['host']
            })
        return jsonify({'success': True, 'results': events})
    
    def post(self):
        name = request.json['name']
        details = request.json['details']
        date = request.json['date']
        time = request.json['time']
        available = request.json['available']
        members = None
        host = request.json['host']
        connect.insert({
            'eventName': name,
            'eventDetails': details,
            'date': date,
            'time': time,
            'available': available,
            'members': members,
            'host': host
        })
        events = []
        for d in connect.find():
            events.append({
                'id': str(d['_id']),
                'eventName': d['eventName'],
                'eventDetails': d['eventDetails'],
                'date': d['date'],
                'time': d['time'],
                'available': d['available'],
                'members': d['members'],
                'host': d['host']
            })
        return jsonify({'success': True, 'results': events})