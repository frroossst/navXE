from algorithms import Path
from methods import method
from graph import Graphs


# Testing BFS for basic dataset
method.clearFileData("graphDB.json")
G = Graphs()
G.addNode("home",["Bpath","Cpath","Dpath"],isMajor=True)
G.addNode("Bpath",[])
print(G.graphDB)
P = Path(G.graphDB)
print(P.BFS(G.graphDB,Graphs.desc2key["home"]))
