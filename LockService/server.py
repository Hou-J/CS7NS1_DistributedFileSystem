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

    def delete(self, filename):
        files_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "files")
        f = [f for f in fileslist if f == filename]
        if len(f) == 0:
            return False
        deleteFilePath = os.path.join(files_path, filename)
        print(deleteFilePath)
        os.remove(deleteFilePath)
        fileslist.remove(fileslist.index(filename))
        return True


class lockFileAccess(Resource):
    def put(self, filename):
        reqparser = reqparse.RequestParser()
        reqparser.add_argument('id', type=int, location='json')
        args = reqparser.parse_args()
        if filename in locks:
            if args['id'] not in locks[filename]:
                locks[filename].append(args['id'])
                print("appended client {} to lock list for {}".format(args['id'], filename))
                print(locks)
                return {'success': 'Acquired'}
            else:
                print("already got that one")
                return {'success': 'Already in list'}
        else:
            print("File not on server")
            return {'success': 'Not on server'}

    def delete(self, filename):
        reqparser = reqparse.RequestParser()
        reqparser.add_argument('id', type=int, location='json')
        args = reqparser.parse_args()
        if filename not in locks:
            return {'success': 'Not on list'}
        if args['id'] in locks[filename]:
            locks[filename].remove(args['id'])
            print("Lock queue: {}".format(locks))
            return {'success':'Removed'}

        print("Not on list for some reason")
        return {'success': 'Not on list'}



class lockAcquire(Resource):
    def get(self):
        global currentID
        currentID+=1
        return {'id':currentID}


api.add_resource(lockFileAccess, "/lock/<string:filename>")
api.add_resource(lockAcquire, "/lock")
api.add_resource(serverFileList, '/fileList')
api.add_resource(serverfile, '/file/<string:filename>')

if __name__ == '__main__':
    files_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "files")
    fileslist = []
    locks = {}
    currentID = 0
    for filename in os.listdir(files_path):
        print(filename)
        fileslist.append(filename)
        locks[filename] = []

    app.run(host="0.0.0.0", port=int(sys.argv[1]))
