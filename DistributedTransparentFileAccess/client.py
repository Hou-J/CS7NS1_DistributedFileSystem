import requests, json
from clientlibrary import clientLibrary

if __name__ == "__main__":

    actionNum = int(input(
        "---------------------------------------\n"
        "|Input nuber of what you want to do:  |\n"
        "|1. View the file list.               |\n"
        "|2. Read a File.|\n"
        "||\n"
        "||\n"
        "||\n"
        "||\n"
        "||\n"
        "---------------------------------------\n"))

    if actionNum == 1:
        clientLibrary.fileLists(clientLibrary)

    if actionNum == 2:
        fileToOpen = input("Input the complete filename you want to open: ")
        clientLibrary.fileLists(clientLibrary,fileToOpen)


    r = requests.post("http://127.0.0.1:8888/hello", json={'post': "Hello server"})
