import requests, json

r = requests.get("http://127.0.0.1:8888/hello")
print(json.loads(r.text))
r = requests.post("http://127.0.0.1:8888/hello",
                  json={'post': "Hello server"})
