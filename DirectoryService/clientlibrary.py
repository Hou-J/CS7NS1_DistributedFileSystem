import requests, json


class clientLibrary():
    def fileLists(self, address):
        r = requests.get("http://{}/fileList".format(address))
        filelists = json.loads(r.text)

        print("------------action start---------------")
        print("File List:")
        for filename in filelists:
            print(filename)
        print("\n-------------action end----------------")

    def readFile(self, address, fileName):
        r = requests.get("http://{}/file/{}".format(address, fileName))
        data = json.loads(r.text)
        if data == False:
            print("File do not exist!")
        else:
            print("--------------file start-----------------")
            for d in data:
                print(d, end='')
            print("\n---------------file end------------------")

    def addFile(self, address, fileName, data):
        r = requests.post("http://{}/fileList".format(address), json={'fileName': fileName, 'data': data})
        data = json.loads(r.text)
        if data == False:
            print("File already exist!")
        else:
            print("--------------file added-----------------")
            for d in data:
                print(d, end='')
            print("\n---------------file end------------------")

    def editFile(self, address, FileName, data):
        r = requests.put("http://{}/file/{}".format(address, FileName), json={'data': data})
        data = json.loads(r.text)
        if data == False:
            print("File do not exist!")
        else:
            print("--------------file edited----------------")
            for d in data:
                print(d, end='')
            print("\n---------------file end------------------")

    def deleteFile(self, address, fileName):
        r = requests.delete("http://{}/file/{}".format(address, fileName))
        data = json.loads(r.text)
        if data == False:
            print("File do not exist!")
        elif data == True:
            print("-------------file deleted----------------")

    def folderLists(self, address):
        r = requests.get("http://{}/folder".format(address))
        foldernames = json.loads(r.text)

        print("------------action start---------------")
        print("Folder List:")
        for f in foldernames:
            print(f)
        print("\n-------------action end----------------")

    def addFolder(self, address, folderName):
        r = requests.post("http://{}/folder".format(address), json={'folderName': folderName})
        data = json.loads(r.text)
        if data:
            print("-------------folder added----------------")
        else:
            print("Folder already exist!")

    def renameFolder(self, address, oldName, newName):
        r = requests.put("http://{}/folder".format(address), json={'oldName': oldName, 'newName': newName})
        data = json.loads(r.text)
        if data:
            print("------------folder renamed---------------")
        else:
            print("Folder do not exist!")

    def deleteFolder(self, address, folderName):
        r = requests.delete("http://{}/folder".format(address), json={'folderName': folderName})
        data = json.loads(r.text)
        if data:
            print("------------folder deleted---------------")
        else:
            print("Folder do not exist!")
