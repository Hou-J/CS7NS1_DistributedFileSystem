from flask import Flask
from flask_restful import Resource, Api, reqparse
import os

app = Flask(__name__)
api = Api(app)


class serverFileList(Resource):
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

class serverfile(Resource):
    def get(self,filename):
        files_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "files")
        # print(files_path)
        f = [f for f in fileslist if f == filename]
        if len(f) == 0:
            return False
        with open(os.path.join(files_path, filename)) as f:
            # print(os.path.join(files_path, filename))
            data = f.readlines()
        return data

api.add_resource(serverFileList, '/fileList')
api.add_resource(serverfile, '/file/<string:filename>')

if __name__ == '__main__':
    files_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "files")
    fileslist = []
    for filename in os.listdir(files_path):
        print(filename)
        fileslist.append(filename)
    # with open(os.path.join(files_path, "examplefile.txt")) as f:
    #     data = f.readlines()
    # for d in data:
    #     print(d,end='')

    app.run(port=8888)
