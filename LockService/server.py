from flask import Flask
from flask_restful import Resource, Api, reqparse
import os, sys

if (len(sys.argv) < 2):
    print("Server usage: python Server.py [PORT]")
    sys.exit(0)

app = Flask(__name__)
api = Api(app)


class serverFileList(Resource):
    def get(self):
        fileslist = []
        files_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "files")
        print(files_path)
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
        f = [f for f in fileslist if f == filename]
        if len(f) == 0:
            return False
        with open(os.path.join(files_path, filename)) as f:
            data = f.readlines()
        return data

    def put(self, filename):
        r = reqparse.RequestParser()
        r.add_argument('data', type=str, location='json')
        r.add_argument('clientID', type=int, location='json')
        ID = r.parse_args()['clientID']

        # print(locks,"!!!!!!!!!!!!!!!")
        for lo in locks:
            print(lo[:len(filename)])

        l = [l for l in locks if l[:len(filename)] == filename]

        # print(l[0][-1],"!!")
        print(ID)
        if l[0][-1] == str(ID):
            # print("@############")
            files_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "files")
            f = [f for f in fileslist if f == filename]
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
        else:
            return "-1"

    def delete(self, filename):
        files_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "files")
        r = reqparse.RequestParser()
        r.add_argument('clientID', type=int, location='json')
        ID = r.parse_args()['clientID']
        l = [l for l in locks if l[:len(filename)] == filename]
        if l[0][-1] == str(ID):
            f = [f for f in fileslist if f == filename]
            if len(f) == 0:
                return False
            deleteFilePath = os.path.join(files_path, filename)
            print(deleteFilePath)
            os.remove(deleteFilePath)
            fileslist.remove(fileslist.index(filename))
            return True
        else:
            return "-1"


class lockFile(Resource):
    def put(self, filename):
        r = reqparse.RequestParser()
        r.add_argument('clientID', type=int, location='json')
        ID = str(r.parse_args()['clientID'])
        l = [l for l in locks if l[:len(filename)] == filename]
        if len(l) == 0:
            locks.append(filename + ID)
            print(ID)
            return True
        else:
            return False

    def delete(self, filename):
        r = reqparse.RequestParser()
        r.add_argument('clientID', type=int, location='json')
        ID = str(r.parse_args()['clientID'])
        locks.remove(filename + ID)
        print(ID)
        return True

class clientID(Resource):
    def get(self):
        global clientID
        clientID += 1
        return clientID

api.add_resource(clientID, "/clientID")
api.add_resource(lockFile, "/lock/<string:filename>")
api.add_resource(serverFileList, '/fileList')
api.add_resource(serverfile, '/file/<string:filename>')

if __name__ == '__main__':
    files_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "files")
    fileslist = []
    locks = []
    clientID = 0

    for filename in os.listdir(files_path):
        print(filename)
        fileslist.append(filename)
    app.run(host="0.0.0.0", port=int(sys.argv[1]))
