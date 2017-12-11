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
        r.add_argument('fileName', type=str, location='json')
        r.add_argument('data', type=str, location='json')
        print(r.parse_args()['fileName'], "to add.")
        filename = r.parse_args()['fileName']
        files_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "files")
        f = [f for f in fileslist if f == filename]
        if len(f) != 0:
            return False
        fileslist.append(filename)
        # print(type(filename),filename,"!!")
        addFilePath = os.path.join(files_path, filename)
        print(addFilePath)
        addFile = open(addFilePath, 'w')
        addFile.write(r.parse_args()['data'])
        addFile.close()
        with open(os.path.join(files_path, filename)) as f:
            data = f.readlines()
        return data


class serverfile(Resource):
    def get(self, filename):
        files_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "files")
        # print(files_path)
        f = [f for f in fileslist if f == filename]
        if len(f) == 0:
            return False
        with open(os.path.join(files_path, filename)) as f:
            # print(os.path.join(files_path, filename))
            data = f.readlines()
        return data

    def put(self, filename):
        r = reqparse.RequestParser()
        r.add_argument('data', type=str, location='json')
        files_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "files")
        # print(files_path)
        # print(fileslist,"@@@",filename)

        # for f in fileslist:
        #     print(f)
        #     if f ==filename:
        #         print("!!!!!!!!!!")
        f = [f for f in fileslist if f == filename]
        # print(f)
        if len(f) == 0:
            return False
        editFilePath = os.path.join(files_path, filename)
        print(editFilePath)
        currentFile = open(editFilePath, 'w')
        currentFile.write(r.parse_args()['data'])
        currentFile.close()
        with open(os.path.join(files_path, filename)) as f:
            data = f.readlines()
        return data

    def delete(self, filename):
        files_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "files")
        f = [f for f in fileslist if f == filename]
        if len(f) == 0:
            return False
        deleteFilePath = os.path.join(files_path, filename)
        print(deleteFilePath)
        os.remove(deleteFilePath)
        fileslist.remove(fileslist.index(filename))
        print(fileslist,"@!@!@!@!@!@!@")
        return True





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
