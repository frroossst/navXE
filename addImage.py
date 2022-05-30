import requests
import json

BASE = "https://navxe.herokuapp.com"

header = input("enter header (usually node name) : ")
graph = input("enter the graph name : ")
url_parse = input("enter url : ")
token = input("enter dev token : ")

url_parse = url_parse.replace(".","-")
url_parse = url_parse.replace("/","+")

response = requests.post(BASE + f"/api/image/add/{header}/{url_parse}/{graph}/{token}")
print(response)
