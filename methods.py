from copy import deepcopy
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