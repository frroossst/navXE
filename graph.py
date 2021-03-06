from methods import method
import secrets
import copy

class Graphs():

    graphDB = {}
    propertiesDB = {}

    def __init__(self):
            Graphs.graphDB = None
            Graphs.propertiesDB = None

    def addNode(self,name : str,children=[],weight=0.0,isMajor=False):
        """
        name <string> name of the node
        children <list> list of the names of all children, empty list if leaf
        isLandmark <bool> if the node is a landmark then it will have a QR code near it else the user is to be guided
            via the GUI there as QR codes would not exist for the particular node, Eg : the node is a room
        """

        propDict = {"nodeName" : "", "children" : children, "description" : "", "weight" : weight, "isMajor" : isMajor, "type" : {}}

        if len(name) < 3:
            raise NameError ("Node name must be atleast three characters in length")

        if name in Graphs.graphDB:
            raise NameError ("Node name already in use, cannot create duplicate nodes")

        Graphs.graphDB[name] = children
        Graphs.propertiesDB[name] = propDict
        propDict["nodeName"] = name

        method.dumpJSON(Graphs.graphDB,"graphDB.json")
        method.dumpJSON(Graphs.propertiesDB,"propertiesDB.json")

    def removeNode(self,name : str):

        nodeName = Graphs.desc2key[name]

        try:
            del Graphs.graphDB[nodeName]
            del Graphs.propertiesDB[name]
            del Graphs.key2desc[nodeName]
            del Graphs.desc2key[name]
        except KeyError:
            pass # Ignoring deletion cause node does not exist

    @classmethod
    def undirectGraph(self,graph : dict):
        # ! This is a terrible mess for the love of all that is holy there must be a better way to do this

        self.graph = graph
        undirected_graph_iter = copy.deepcopy(self.graph)
        undirected_graph = copy.deepcopy(self.graph)

        # Undirecting using key-value pairs
        for key_undir, value_list in undirected_graph_iter.items():
            for val in value_list:
                for k, v in self.graph.items():
                    if val in v:
                        # if val not in undirected_graph[key_undir]:
                            undirected_graph[key_undir].append(k)
        undirected_graph = method.leafifyChildren(undirected_graph)
        undirected_graph_iter = copy.deepcopy(undirected_graph)

        # Populating empty 
        for key, value in undirected_graph_iter.items():
            if value == []:
                for k,val_list in undirected_graph_iter.items():
                    if key in val_list:
                        undirected_graph[key].append(k)

        # Fixing some key-value pairs
        for key, val in undirected_graph.items():
            for v in val:
                if key not in undirected_graph[v]:
                    undirected_graph[v].append(key)

        # Removing duplicate value items
        for key, val in undirected_graph.items():
            nonDup = []
            for i in val:
                if i not in nonDup and i != key:
                    nonDup.append(i)

            undirected_graph[key] = nonDup

        # Preventing cyclic trip ups
        for key, val in undirected_graph.items():
            val_copy = copy.deepcopy(val)
            for v in val:
                flag0 = False
                if v in self.graph[key] or key in self.graph[v]:
                    flag0 = True
               # else:
               #     flag0 = False
                if not flag0:
                    val_copy.remove(v)
            undirected_graph[key] = val_copy

        return undirected_graph

    @classmethod
    def invertGraph(self, graph : dict):

        inver = {}

        for k,v in graph.items():
            for i in v:
                if i not in inver:
                    inver[i] = []

        for k, v in graph.items():
            for i in v:
                inver[i].append(k)

        print(inver)
        return inver

    @classmethod
    def generateToken(self, id : str):

        token_16 = secrets.token_hex(16)
        token_8 = secrets.token_hex(8)

        return token_8 + id + token_16
