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

response = requests.post(BASE + "/api/database")
print(response.json())

response = requests.post(BASE + "/api/database/THEGRAPH")
print(response.json())
