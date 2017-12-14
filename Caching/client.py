from clientlibrary import clientLibrary
import sys

if (len(sys.argv) < 3):
    print("Server usage: python Server.py [IP] [PORT]")
    sys.exit(0)

if __name__ == "__main__":

    address = "{}:{}".format(sys.argv[1], int(sys.argv[2]))
    local_cache = []

    while True:
        actionNum = int(input(
            "---------------------------------------\n"
            "|Input nuber of what you want to do:  |\n"
            "|1. View the file list.               |\n"
            "|2. Read a File.                      |\n"
            "|3. Add a new file.                   |\n"
            "|4. Edit a file.                      |\n"
            "|5. Delete a file.                    |\n"
            "|6. Push to server.                   |\n"
            "|                                     |\n"
            "|0. Exit.                             |\n"
            "---------------------------------------\n"))

        if actionNum == 1:
            clientLibrary.fileLists(clientLibrary, address, local_cache)

        elif actionNum == 2:
            fileToOpen = input("Input the complete filename you want to open: ")
            clientLibrary.readFile(clientLibrary, address, fileToOpen, local_cache)

        elif actionNum == 3:
            fileToAdd = input("Input the complete filename you want to add: ")
            fileData = input("Input what you want to add to the {}: ".format(fileToAdd))
            clientLibrary.addFile(clientLibrary, address, fileToAdd, fileData, local_cache)

        elif actionNum == 4:
            fileToAdd = input("Input the complete filename you want to edit: ")
            fileData = input("Input the new data in {}: ".format(fileToAdd))
            clientLibrary.editFile(clientLibrary, address, fileToAdd, fileData, local_cache)

        elif actionNum == 5:
            fileToDelete = input("Input the complete filename you want to delete: ")
            yn = input("Are you sure you want to delete {} ? (Y/N)".format(fileToDelete))
            if yn == "n" or yn == "N":
                continue
            clientLibrary.deleteFile(clientLibrary, address, fileToDelete, local_cache)

        elif actionNum == 6:
            fileToPush = input("Input the complete filename you want to push: ")
            clientLibrary.pushFile(clientLibrary, address, fileToPush, local_cache)

        elif actionNum == 0:
            break

        else:
            print("Wrong Input!")

        input("Press enter to continue")
