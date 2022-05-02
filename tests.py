'''from algorithms import Path
from methods import method
from graph import Graphs


# Testing BFS for basic dataset

method.clearFileData("graphDB.json")

G = Graphs()

G.addNode("a",["b","c"])
G.addNode("b",["g"])
G.addNode("c",["d","f"])
G.addNode("d",["e"])
G.addNode("e",["f"])
G.addNode("f")
G.addNode("g",["h"])
G.addNode("h",["i","j"])
G.addNode("i")
G.addNode("j",["k"])
G.addNode("k",["l"])
G.addNode("l",["i"])

Graphs.graphDB = G.undirectGraph(Graphs.graphDB)

P = Path(Graphs.graphDB)

print(G.graphDB)
print(P.BFS_SP(G.graphDB,"a","i"))
print(P.BFS_SP(G.graphDB,"j","i"))'''

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

