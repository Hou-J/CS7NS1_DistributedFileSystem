from flask import Flask
from flask_restful import Resource, Api, reqparse
import os

app = Flask(__name__)
api = Api(app)


class Hello(Resource):
    def get(self):
        fileslist = []
        files_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "files")
        print(files_path)
        # print(os.listdir(files_path))
        for filename in os.listdir(files_path):
            print(filename)
            fileslist.append(filename)
        print(fileslist)
        return fileslist

    def post(self):
        r = reqparse.RequestParser()
        r.add_argument('post', type=str, location='json')
        print(r.parse_args()['post'])


api.add_resource(Hello, '/hello')

if __name__ == '__main__':
    files_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "files")
    print(files_path)
    with open(os.path.join(files_path, "examplefile.txt")) as f:
        data = f.readlines()
    for d in data:
        print(d,end='')

    # with open() as myfile:
    #     data = myfile.readlines()
    app.run(port=8888)
