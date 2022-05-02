import json
import requests

BASE = 'http://127.0.0.1:5000/'

#response = requests.post(BASE + "helloworld")
#print(response.json())
response = requests.get(BASE + "api/route/graphDB/a/d/front")
print(response.json())

response = requests.get(BASE + "/api/token/abc")
print(response.json())

response = requests.get(BASE + "/api/token/ThisIsTheBaseToken")
print(response.json())

response = requests.post(BASE + "/api/token/ThisIsTheBaseToken")
print(response.json())

with open("graphDB.json","r") as fobj:
    content = json.load(fobj)
    fobj.close()

BASE = 'https://navxe.herokuapp.com/'
name = "test"
token = "fcf1e23002330334ThisIsTheBaseToken5acfcc887086729c3919ee97d31fffba"
data = str(content)

print(name)
print(token)
print(data)

response = requests.post(BASE + f"api/database/{name}/{token}/{data}")
print(response.json())
