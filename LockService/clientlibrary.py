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

    def lockGetId(address):
        location = 'http://{}/lock'.format(address)
        r = requests.get(location)
        json_data = json.loads(r.text)
        clientID = json_data['id']
        return clientID

    def lockAddToQueue(address, clientID, filename):
        r = requests.put('http://{}/lock/{}'.format(address, filename), json={'id': clientID})
        json_data = json.loads(r.text)  # JSON to dict (JSON
        if json_data['success'] == 'Acquired':
            print("Added {} to lock queue.".format(filename))
        else:
            print("Not added to lock queue")

    def lockDeleteFromQueue(address, clientID, filename):
        r = requests.delete('http://{}/lock/{}'.format(address, filename), json={'id': clientID})
        json_data = json.loads(r.text)  # JSON to dict (JSON
        if json_data['success'] == 'Removed':
            print("Removed {} from lock queue.".format(filename))
