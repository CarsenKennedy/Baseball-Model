from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
from matches import *

app = Flask(__name__)
api = Api(app)
CORS(app)


class Matches(Resource):
    def get(self):
        response = get_matches()
        return response

api.add_resource(Matches, '/')

if __name__ == '__main__':
    app.run(debug=True)