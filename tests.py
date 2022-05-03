import json
import requests


# BASE = 'http://127.0.0.1:5000'

#response = requests.post(BASE + "helloworld")
#print(response.json())

BASE = "https://navxe.herokuapp.com"

response = requests.get(BASE + "/api/route/graphDB/a/d/front")
print(response.json())

response = requests.get(BASE + "/api/token/abc")
print(response.json())

response = requests.get(BASE + "/api/token/ThisIsTheBaseToken")
print(response.json())

response = requests.get(BASE + "/api/database/read/test1")
print(response.json())

d = {"a" : ["b","c","d"],"b" : ["a"], "c" : ["a"], "d" : ["a"]}
dj = json.dumps(d)

response = requests.post(BASE + f"/api/database/create/test2/123token321/{dj}")
print(response.json())
