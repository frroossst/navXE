import json
import requests
from methods import method


# BASE = 'http://127.0.0.1:5000'

#response = requests.post(BASE + "helloworld")
#print(response.json())

BASE = "https://navxe.herokuapp.com"
'''
response = requests.get(BASE + "/api/route/graphDB/a/d/front")
print(response.json())

response = requests.get(BASE + "/api/token/abchdfjkhasdj")
print(response.json())

d = {"a" : ["b","c","d"],"b" : ["a"], "c" : ["a"], "d" : ["a"]}
dj = json.dumps(d)

response = requests.post(BASE + f"/api/database/create/test9/123token321U/{dj}")
print(response.json())

response = requests.get(BASE + "/api/database/read/test9")
print(response.json())

newD = '{"msg" : "updated"}'
response = requests.post(BASE + f"/api/database/update/123token321U/test9/{str(newD)}")
print(response.json())

response = requests.get(BASE + "/api/database/read/test9")
print(response.json())

response = requests.post(BASE + f"/api/database/delete/123token321U/test9")
print(response.json())

response = requests.get(BASE + "/api/database/read/test9")
print(response.json())

response = requests.get(BASE + "/api/database/read/*")
print(response.json())

tokenID =  "S61ec9d21a698a477855453567e2b7b90"

with open("graphDB.json","r") as fobj:
    content = json.load(fobj)
    fobj.close()

content = method.dict_toURL(content)

response = requests.post(BASE + f"/api/database/create/testDB/{tokenID}/{content}")
print(response.json())'''

response = requests.get(BASE + "/api/route/graphDB/a/d/front")
print(response.json())
