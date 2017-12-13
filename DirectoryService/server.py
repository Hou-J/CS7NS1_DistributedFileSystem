from flask import Flask
from flask_restful import Resource, Api, reqparse
import os, sys, subprocess
#
# if (len(sys.argv) < 2):
#     print("Server usage: python Server.py [PORT]")
#     sys.exit(0)
#
# app = Flask(__name__)
# api = Api(app)
#
#
# class serverFileList(Resource):
#     def get(self):
#         fileslist = []
#         files_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "files")
#         print(files_path)
#         for filename in os.listdir(files_path):
#             print(filename)
#             fileslist.append(filename)
#         print(fileslist)
#         return fileslist
#
#     def post(self):
#         r = reqparse.RequestParser()
#         r.add_argument('fileName', type=str, location='json')
#         r.add_argument('data', type=str, location='json')
#         print(r.parse_args()['fileName'], "to add.")
#         filename = r.parse_args()['fileName']
#         files_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "files")
#         f = [f for f in fileslist if f == filename]
#         if len(f) != 0:
#             return False
#         fileslist.append(filename)
#         addFilePath = os.path.join(files_path, filename)
#         print(addFilePath)
#         addFile = open(addFilePath, 'w')
#         addFile.write(r.parse_args()['data'])
#         addFile.close()
#         with open(os.path.join(files_path, filename)) as f:
#             data = f.readlines()
#         return data
#
#
# class serverfile(Resource):
#     def get(self, filename):
#         files_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "files")
#         f = [f for f in fileslist if f == filename]
#         if len(f) == 0:
#             return False
#         with open(os.path.join(files_path, filename)) as f:
#             data = f.readlines()
#         return data
#
#     def put(self, filename):
#         r = reqparse.RequestParser()
#         r.add_argument('data', type=str, location='json')
#         files_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "files")
#         f = [f for f in fileslist if f == filename]
#         if len(f) == 0:
#             return False
#         editFilePath = os.path.join(files_path, filename)
#         print(editFilePath)
#         currentFile = open(editFilePath, 'w')
#         currentFile.write(r.parse_args()['data'])
#         currentFile.close()
#         with open(os.path.join(files_path, filename)) as f:
#             data = f.readlines()
#         return data
#
#     def delete(self, filename):
#         files_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "files")
#         f = [f for f in fileslist if f == filename]
#         if len(f) == 0:
#             return False
#         deleteFilePath = os.path.join(files_path, filename)
#         print(deleteFilePath)
#         os.remove(deleteFilePath)
#         fileslist.remove(fileslist.index(filename))
#         return True
#
#
# api.add_resource(serverFileList, '/fileList')
# api.add_resource(serverfile, '/file/<string:filename>')

if __name__ == '__main__':
    files_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "files")
    print(files_path)
    # fileslist = []
    # for filename in os.listdir(files_path):
    #     print(filename)
    #     fileslist.append(filename)
    dir_list = []
    file_list = []
    for dirName, subdirList, fileList in os.walk(files_path):
        print('Dir: root{}'.format(dirName[dirName.rfind(files_path) + len(files_path):]))
        dir_list.append(dirName[dirName.rfind(files_path) + len(files_path):])
        for fname in fileList:
            print('\t{}'.format(fname))
            file_list.append('{}@{}'.format(dirName[dirName.rfind(files_path) + len(files_path):],fname))
        print()
    print(len(file_list))
    name = 'hat.txt'

    for d in dir_list:
        print(d)

    for f in file_list:
        print(f)
        if f.split('@')[-1] == name:
            print('!!')
    # app.run(host="0.0.0.0", port=int(sys.argv[1]))
