from clientlibrary import clientLibrary
import sys

if (len(sys.argv) < 3):
    print("Server usage: python Server.py [IP] [PORT]")
    sys.exit(0)

if __name__ == "__main__":

    address = "{}:{}".format(sys.argv[1], int(sys.argv[2]))

    while True:
        actionNum = int(input(
            "---------------------------------------\n"
            "|Input nuber of what you want to do:  |\n"
            "|1. View the file list.               |\n"
            "|2. Read a File.                      |\n"
            "|3. Add a new file.                   |\n"
            "|4. Edit a file.                      |\n"
            "|5. Delete a file.                    |\n"
            "|6. View the folders.                 |\n"
            "|7. Add a new folder.                 |\n"
            "|8. Rename a folder.                  |\n"
            "|9. Delete a folder.                  |\n"
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
            fileToAdd = input("Input the complete filename you want to edit: ")
            fileData = input("Input the new data in {}: ".format(fileToAdd))
            clientLibrary.editFile(clientLibrary, address, fileToAdd, fileData)

        elif actionNum == 5:
            fileToDelete = input("Input the complete filename you want to delete: ")
            yn = input("Are you sure you want to delete {} ? (Y/N)".format(fileToDelete))
            if yn == "n" or yn == "N":
                continue
            clientLibrary.deleteFile(clientLibrary, address, fileToDelete)

        elif actionNum == 6:
            clientLibrary.folderLists(clientLibrary, address)

        elif actionNum == 7:
            folderToAdd = input("Input the complete folder directory you want to add: ")
            clientLibrary.addFolder(clientLibrary, address, folderToAdd)

        elif actionNum == 8:
            oldName = input("Input old folder name: ")
            newName = input("Input new folder name: ")
            clientLibrary.renameFolder(clientLibrary, address, oldName, newName)

        elif actionNum == 9:
            folderToDelete = input("Input the complete folder directory you want to delete: ")
            clientLibrary.deleteFolder(clientLibrary, address, folderToDelete)



        elif actionNum == 0:
            break

        else:
            print("Wrong Input!")

        input("Press enter to continue")
