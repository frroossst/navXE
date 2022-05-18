import requests
import json

BASE = "https://navxe.herokuapp.com"

devToken = input("enter validation token : ")

response = requests.post(BASE + f"/api/update/{devToken}")
print(response.json())
