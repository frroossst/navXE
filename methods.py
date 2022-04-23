from matplotlib import pyplot as plt
from copy import deepcopy
import networkx as nx
import random
import json

class method():

    def __init__(self):
        pass

    @classmethod
    def loadJSON(self,file : str) -> dict:
        with open(file,"r") as fobj:
            content = json.load(fobj)
            return content

    @classmethod
    def dumpJSON(self,data : dict,file : str) -> dict:
        """
        Best practice is to read and write all data rather than modify 
        """
        with open(file,"w") as fobj:
            json.dump(data,fobj,indent=6)
            fobj.close()

    @classmethod
    def clearFileData(self, file : str) -> None:
        
        with open(file,"w") as fobj:
            json.dump({},fobj)
            fobj.close()

        return None

    @classmethod
    def leafifyChildren(self,graph : dict) -> dict:
        
        copyGraph = deepcopy(graph)

        for i in copyGraph.values():
            for j in i:
                if j not in copyGraph:
                    graph[j] = [] # Generating a leaf for the children
                
        return graph

    @classmethod
    def generateRandomGraph(self,file):
        
        node_li = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        num_li = range(0,26)
        graph = {}

        for i in node_li:
            n = random.sample(num_li,3)
            graph[i] = [node_li[x] for x in n]

        # Cleaning up graph
        for i in graph:
            for j in graph[i]:
                if j == i:
                    graph[i] = graph[i].remove(j)

        iter = deepcopy(graph) 
        for i in iter:
            if graph[i] is None:
                del graph[i]

        method.dumpJSON(graph,file)

    @classmethod
    def drawNetwork(self,file):
        content = method.loadJSON(file)
        li = []
        for i in content:
            for j in content[i]:
                li.append(tuple([i,j]))
        
        GD = nx.MultiDiGraph()
        GD.add_edges_from(li)
        plt.figure(figsize=(80,80))
        pos = nx.spring_layout(GD,k=0.3,iterations=20)
        nx.draw(GD,pos=pos,connectionstyle='arc3, rad = 0.1',with_labels=True)
        plt.show()