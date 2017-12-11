import requests, json

r = requests.get("http://127.0.0.1:8888/hello")
# print(json.loads(r.text))
filelists = json.loads(r.text)

for filename in filelists:
    print(filename)

r = requests.post("http://127.0.0.1:8888/hello",
                  json={'post': "Hello server"})
