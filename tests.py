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

tokenID =  "S61ec9d21a698a477855453567e2b7b90"

with open("graphDB.json","r") as fobj:
    content = json.load(fobj)
    fobj.close()

content = method.dict_toURL(content)

response = requests.post(BASE + f"/api/database/create/testDB/{tokenID}/{content}")
print(response.json())

response = requests.get(BASE + "/api/route/testDB/a/d/front")
print(response.json())

response = requests.post(BASE + "/api/update")
print(response.json())

response = requests.get(BASE + "/api/database/read/*")
print(response.json())

header = "hd test image"

response = requests.get(BASE + f"/api/image/{header}")
print(response.json())
'''

"""import urllib.parse

header = "hd test image"
graph = "testDB"
uri = "https://raw.githubusercontent.com/frroossst/navXE/master/images/test.jpeg"
uriEnc = "(" + uri  + ")"

header = "header_dummy"
graph = "graph_dummy"

response = requests.get(BASE + f"/api/image/{header}/{graph}")
print(response.json())
"""

#response = requests.post(BASE + f"/api/image/add/{header}/{uriEnc}/{graph}")
#print(response)

"""
url_parse = "raw.ithubusercontent.com/frroossst/navXE/master/images/test.jpeg"

#    . => -
#    / => +

url_parse = url_parse.replace(".","-")
url_parse = url_parse.replace("/","+")

# dummy test post
response = requests.post(BASE + f"/api/image/add/header_dummy/{url_parse}/graph_dummy")
print(response)


header = "hd test image"
graph = "testDB"
url_parse = "https://raw.githubusercontent.com/frroossst/navXE/master/images/test.jpeg"
url_parse = url_parse.replace(".","-")
url_parse = url_parse.replace("/","+")

response = requests.get(BASE + f"/api/image/{header}/{graph}")
print(response.json())

response = requests.post(BASE + f"/api/image/add/{header}/{url_parse}/{graph}")
print(response)

response = requests.get(BASE + f"/api/image/{header}/{graph}")
print(response.json())
"""

header = "a"
desc = "This is description for a"
graph = "testDB"
tok = "S61ec9d21a698a477855453567e2b7b90"

response = requests.post(BASE + f"/api/text/add/{header}/{desc}/{graph}/{tok}")
print(response)

response = requests.get(BASE + f"/api/text/{header}/{graph}")
print(response.json())
