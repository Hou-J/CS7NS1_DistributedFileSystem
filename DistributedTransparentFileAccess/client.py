from clientlibrary import clientLibrary

if __name__ == "__main__":

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
            clientLibrary.fileLists(clientLibrary)

        elif actionNum == 2:
            fileToOpen = input("Input the complete filename you want to open: ")
            clientLibrary.readFile(clientLibrary, fileToOpen)

        elif actionNum == 3:
            fileToAdd = input("Input the complete filename you want to add: ")
            fileData = input("Input what you want to add to the {}: ".format(fileToAdd))
            clientLibrary.addFile(clientLibrary, fileToAdd, fileData)

        elif actionNum == 4:
            fileToAdd = input("Input the complete filename you want to edit: ")
            fileData = input("Input the new data in {}: ".format(fileToAdd))
            clientLibrary.editFile(clientLibrary, fileToAdd, fileData)

        elif actionNum == 5:
            fileToDelete = input("Input the complete filename you want to delete: ")
            yn = input("Are you sure you want to delete {} ? (Y/N)".format(fileToDelete))
            if yn == "n" or yn == "N":
                continue
            clientLibrary.deleteFile(clientLibrary, fileToDelete)


        elif actionNum == 0:
            break

        else:
            print("Wrong Input!")

        input("Press enter to continue")
