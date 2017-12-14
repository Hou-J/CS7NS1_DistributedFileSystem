import requests, json


class clientLibrary():
    def fileLists(self, address, local_cache):
        r = requests.get("http://{}/fileList".format(address))
        filelists = json.loads(r.text)

        print("------------action start---------------")
        print("File List:\n")
        for filename in filelists:
            print(filename)

        print("Catch List:\n")
        for l in local_cache:
            print(l['filename'])
        print("\n-------------action end----------------")

    def readFile(self, address, fileName, local_cache):
        l  = [l for l in local_cache if l['filename'] == fileName]
        if len(l) == 0:
            print("File not in cache.")
            r = requests.get("http://{}/file/{}".format(address, fileName))
            data = json.loads(r.text)
            if data == False:
                print("File do not exit!")
            else:
                local_cache.append(data)
        else:
            print("Found file in cache.")
            print("--------------file start-----------------")
            for d in l:
                print(d, end='')
            print("\n---------------file end------------------")

    def addFile(self, address, fileName, data, local_cache):
        r = requests.post("http://{}/fileList".format(address), json={'fileName': fileName, 'data': data})
        data = json.loads(r.text)
        if data == False:
            print("File already exit!")
        else:
            print("--------------file added-----------------")
            for d in data:
                print(d, end='')
            print("\n---------------file end------------------")

    def editFile(self, address, FileName, data, local_cache):
        r = requests.put("http://{}/file/{}".format(address, FileName), json={'data': data})
        data = json.loads(r.text)
        if data == False:
            print("File do not exit!")
        else:
            print("--------------file edited----------------")
            for d in data:
                print(d, end='')
            print("\n---------------file end------------------")

    def deleteFile(self, address, fileName, local_cache):
        r = requests.delete("http://{}/file/{}".format(address, fileName))
        data = json.loads(r.text)
        if data == False:
            print("File do not exit!")
        elif data == True:
            print("-------------file deleted----------------")

    def pushFile(self, address, fileToPush, local_cache):
        pass