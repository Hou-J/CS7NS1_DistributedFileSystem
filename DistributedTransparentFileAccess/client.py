import requests, json

if __name__ == "__main__":

    actionNum = int(input(
        "---------------------------------------\n"
        "|Input nuber of what you want to do:  |\n"
        "|1. View the file list.               |\n"
        "||\n"
        "||\n"
        "||\n"
        "||\n"
        "||\n"
        "||\n"
        "---------------------------------------\n"))

    if actionNum == 1:
        r = requests.get("http://127.0.0.1:8888/hello")
        # print(json.loads(r.text))
        filelists = json.loads(r.text)

        print("------------action start---------------\n")
        for filename in filelists:
            print(filename)
        print("\n-------------action end----------------")

    r = requests.post("http://127.0.0.1:8888/hello", json={'post': "Hello server"})
