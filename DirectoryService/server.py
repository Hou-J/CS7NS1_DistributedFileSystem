from flask import Flask
from flask_restful import Resource, Api, reqparse
import os, sys, shutil

if (len(sys.argv) < 2):
    print("Server usage: python Server.py [PORT]")
    sys.exit(0)

app = Flask(__name__)
api = Api(app)


class serverFileList(Resource):
    def get(self):
        listsRenew()
        return files_list

    def post(self):
        r = reqparse.RequestParser()
        r.add_argument('fileName', type=str, location='json')
        r.add_argument('data', type=str, location='json')
        print(r.parse_args()['fileName'], "to add.")
        filename = r.parse_args()['fileName']
        files_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "files")
        f = [f for f in files_list if f == filename]
        if len(f) != 0:
            return False
        listsRenew()
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
        f = [f for f in files_list if f == filename]
        if len(f) == 0:
            return False
        with open(os.path.join(files_path, filename)) as f:
            data = f.readlines()
        return data

    def put(self, filename):
        r = reqparse.RequestParser()
        r.add_argument('data', type=str, location='json')
        files_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "files")
        f = [f for f in files_list if f == filename]
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
        f = [f for f in files_list if f == filename]
        if len(f) == 0:
            return False
        deleteFilePath = os.path.join(files_path, filename)
        print(deleteFilePath)
        os.remove(deleteFilePath)
        listsRenew()
        return True


class folder(Resource):
    def get(self):
        return dir_list

    def post(self):
        r = reqparse.RequestParser()
        r.add_argument('folderName', type=str, location='json')
        newdir = r.parse_args()['folderName']
        print(newdir, "to add.")
        d = [d for d in dir_list if d == newdir]
        if len(d) != 0:
            return False
        os.makedirs(os.path.join(files_path, newdir))
        listsRenew()
        return True

    def put(self):
        r = reqparse.RequestParser()
        r.add_argument('oldName', type=str, location='json')
        r.add_argument('newName', type=str, location='json')
        oldName = r.parse_args()['oldName']
        newName = r.parse_args()['newName']
        d = [d for d in dir_list if d == oldName]
        if len(d) == 0:
            return False
        os.rename(os.path.join(files_path, oldName), os.path.join(files_path, newName))
        listsRenew()
        return True

    def delete(self):
        r = reqparse.RequestParser()
        r.add_argument('folderName', type=str, location='json')
        dirToDelete = r.parse_args()['folderName']
        print(dirToDelete, "to delete.")
        print(dir_list)
        for d in dir_list:
            print(d, "!!!")
        d = [d for d in dir_list if d == dirToDelete]
        if len(d) == 0:
            return False
        shutil.rmtree(os.path.join(files_path, dirToDelete))
        listsRenew()
        return True


def listsRenew():
    del dir_list[:]
    del files_list[:]
    for dirName, subdirList, fileList in os.walk(files_path):
        print('Dir: {}'.format(dirName[dirName.rfind(files_path) + len(files_path) + 1:]))
        dir_list.append(dirName[dirName.rfind(files_path) + len(files_path) + 1:])
        for fname in fileList:
            print('\t{}'.format(fname))
            files_list.append(
                os.path.join(dirName, fname)[os.path.join(files_path, fname).rfind(root_path) + len(root_path) + 1:])
        print()


api.add_resource(serverFileList, '/fileList')
api.add_resource(serverfile, '/file/<string:filename>')
api.add_resource(folder, '/folder')

if __name__ == '__main__':
    root_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "files")
    files_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "files")
    print(files_path)
    dir_list = []
    files_list = []

    listsRenew()
    for f in files_list:
        print(f)
    app.run(host="0.0.0.0", port=int(5555))
