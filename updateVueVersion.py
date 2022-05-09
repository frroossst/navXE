import requests
import json

BASE = "https://navxe.herokuapp.com"

response = requests.post(BASE + "/api/update")
print(response.json())
