from clientlibrary import clientLibrary
import sys

if (len(sys.argv) < 3):
    print("Server usage: python Server.py [IP] [PORT]")
    sys.exit(0)

if __name__ == "__main__":

    address = "{}:{}".format(sys.argv[1], int(sys.argv[2]))

    clientID = clientLibrary.getClientID(clientLibrary, address)
    print(clientID)
    while True:
        actionNum = int(input(
            "---------------------------------------\n"
            "|Input nuber of what you want to do:  |\n"
            "|1. View the file list.               |\n"
            "|2. Read a File.                      |\n"
            "|3. Add a new file.                   |\n"
            "|4. Edit a file.                      |\n"
            "|5. Delete a file                     |\n"
            "|                                     |\n"
            "|0. Exit.                             |\n"
            "---------------------------------------\n"))

        if actionNum == 1:
            clientLibrary.fileLists(clientLibrary, address)

        elif actionNum == 2:
            fileToOpen = input("Input the complete filename you want to open: ")
            clientLibrary.readFile(clientLibrary, address, fileToOpen)

        elif actionNum == 3:
            fileToAdd = input("Input the complete filename you want to add: ")
            fileData = input("Input what you want to add to the {}: ".format(fileToAdd))
            clientLibrary.addFile(clientLibrary, address, fileToAdd, fileData)

        elif actionNum == 4:
            fileToEdit = input("Input the complete filename you want to edit: ")
            if clientLibrary.isFileExist(clientLibrary, address, fileToEdit):
                if clientLibrary.lockAddToQueue(clientLibrary, address, clientID, fileToEdit) != False:
                    fileData = input("Input the new data in {}: ".format(fileToEdit))
                    clientLibrary.editFile(clientLibrary, address, clientID, fileToEdit, fileData)
                    clientLibrary.lockDeleteFromQueue(clientLibrary, address, clientID, fileToEdit)
            else:
                print("File do not exist!")

        elif actionNum == 5:
            fileToDelete = input("Input the complete filename you want to delete: ")
            if clientLibrary.isFileExist(clientLibrary, address, fileToDelete):
                clientLibrary.lockAddToQueue(clientLibrary, address, clientID, fileToDelete)
                yn = input("Are you sure you want to delete {} ? (Y/N)".format(fileToDelete))
                if yn == "n" or yn == "N":
                    continue
                clientLibrary.deleteFile(clientLibrary, address, clientID, fileToDelete)
                clientLibrary.lockDeleteFromQueue(clientLibrary, address, clientID, fileToDelete)
            else:
                print("File do not exist!")


        elif actionNum == 0:
            break

        else:
            print("Wrong Input!")

        input("Press enter to continue")
