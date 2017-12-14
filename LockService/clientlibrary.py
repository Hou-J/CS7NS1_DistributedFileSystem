import requests, json


class clientLibrary():
    def fileLists(self, address):
        r = requests.get("http://{}/fileList".format(address))
        filelists = json.loads(r.text)

        print("------------action start---------------")
        print("File List:\n")
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

    def editFile(self, address, clientID, FileName, data):
        r = requests.put("http://{}/file/{}".format(address, FileName), json={'clientID': clientID, 'data': data})
        data = json.loads(r.text)
        if data == False:
            print("File do not exist!")
        elif data == '-1':
            print("File occupied!")
        else:
            print("--------------file edited----------------")
            for d in data:
                print(d, end='')
            print("\n---------------file end------------------")

    def deleteFile(self, address, clientID, fileName):
        r = requests.delete("http://{}/file/{}".format(address, fileName), json={'clientID': clientID})
        data = json.loads(r.text)
        if data == False:
            print("File do not exist!")
        elif data == '-1':
            print("File occupied!")
        else:
            print("-------------file deleted----------------")

    def getClientID(self, address):
        r = requests.get("http://{}/clientID".format(address))
        data = json.loads(r.text)
        return data

    def isFileExist(self, address, fileName):
        r = requests.get("http://{}/file/{}".format(address, fileName))
        data = json.loads(r.text)
        if data == False:
            return False
        else:
            return True

    def lockAddToQueue(self, address, clientID, filename):
        r = requests.put('http://{}/lock/{}'.format(address, filename), json={'clientID': clientID})
        data = json.loads(r.text)
        if data:
            print("Added {} to lock queue.".format(filename))
        else:
            print("File is occupied!")
            return False

    def lockDeleteFromQueue(self, address, clientID, filename):
        r = requests.delete('http://{}/lock/{}'.format(address, filename), json={'clientID': clientID})
        data = json.loads(r.text)
        if data:
            print("Removed {} from lock queue.".format(filename))
