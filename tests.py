from algorithms import Path
from methods import method
from graph import Graphs


# Testing BFS for basic dataset
# method.clearFileData("graphDB.json")
G = Graphs()
Graphs.graphDB = G.undirectGraph(Graphs.graphDB)
P = Path(Graphs.graphDB)
print(G.graphDB)
print(P.BFS_SP(G.graphDB,"a","i"))
print(P.BFS_SP(G.graphDB,"j","i"))