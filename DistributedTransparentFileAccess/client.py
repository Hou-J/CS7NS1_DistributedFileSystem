from clientlibrary import clientLibrary

if __name__ == "__main__":
    while True:
        actionNum = int(input(
            "---------------------------------------\n"
            "|Input nuber of what you want to do:  |\n"
            "|1. View the file list.               |\n"
            "|2. Read a File.                      |\n"
            "|3. Add a new file.                   |\n"
            "||\n"
            "||\n"
            "||\n"
            "|0. Exit.                             |\n"
            "---------------------------------------\n"))

        if actionNum == 1:
            clientLibrary.fileLists(clientLibrary)

        elif actionNum == 2:
            fileToOpen = input("Input the complete filename you want to open: ")
            clientLibrary.readFile(clientLibrary, fileToOpen)

        elif actionNum == 3:
            fileToAdd = input("Input the complete filename you want to add: ")
            fileData = input("Input what you want to add to the {}: ".format(fileToAdd))
            clientLibrary.addFile(clientLibrary, fileToAdd, fileData)



        elif actionNum == 0:
            break
            # r = requests.post("http://127.0.0.1:8888/hello", json={'post': "Hello server"})
