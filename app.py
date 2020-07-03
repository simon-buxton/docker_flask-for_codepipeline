# app.py - a minimal flask api using flask_restful
from flask import Flask
from flask_restful import Resource, Api
from datetime import datetime

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Ping(Resource):
    def get(self):
        return {'ping': 'pong'}

class Healthcheck(Resource):
    def get(self):
        the_time = str(datetime.now())
        return {'servertime': the_time}

api.add_resource(HelloWorld, '/')
api.add_resource(Ping, '/ping')
api.add_resource(Healthcheck, '/healthcheck')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
