from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


class Hello(Resource):
    def get(self):
        return "Hello client"

    def post(self):
        r = reqparse.RequestParser()
        r.add_argument('post', type=str, location='json')
        print(r.parse_args()['post'])


api.add_resource(Hello, '/hello')

if __name__ == '__main__':
    app.run(port=8888)
