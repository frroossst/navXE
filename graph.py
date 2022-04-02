# To generate and create a graph

from methods import method

class Graphs():

    graphDB = {}
    propertiesDB = {}
    key2desc = {}
    desc2key = {}

    def __init__(self):
            Graphs.graphDB = method.loadJSON("graphDB.json")
            Graphs.propertiesDB = method.loadJSON("propertiesDB.json")
            Graphs.key2desc = method.loadJSON("indexDB.json")["key2desc"]
            Graphs.desc2key = method.loadJSON("indexDB.json")["desc2key"]

    def addNode(self,name,children=[],weight=0.0,isMajor=False):
        """
        name <string> name of the node
        children <list> list of the names of all children, empty list if leaf
        isLandmark <bool> if the node is a landmark then it will have a QR code near it else the user is to be guided
            via the GUI there as QR codes would not exist for the particular node, Eg : the node is a room
        """
        propDict = {"nodeKey" : "", "children" : children, "description" : "", "weight" : weight, "isMajor" : isMajor, "type" : {}}

        if len(name) < 3:
            raise NameError ("Node name must be atleast three characters in length")
        elif name in Graphs.graphDB:
            raise NameError ("Node name already in use, cannot create duplicate nodes")

        node_key = Graphs.generateGraphNodeNames(name)

        Graphs.graphDB[node_key] = children
        Graphs.propertiesDB[name] = propDict
        Graphs.key2desc[node_key] = name
        Graphs.desc2key[name] = node_key

        # Store the children nngs in the key2desc and desc2key DB for methods.leafifyChidlren to access later

        method.dumpJSON(Graphs.graphDB,"graphDB.json")
        index_build = {"key2desc" : Graphs.key2desc, "desc2key" : Graphs.desc2key}
        method.dumpJSON(index_build,"indexDB.json")

    @classmethod
    def generateGraphNodeNames(self,name) -> str:

        count = 0
        new_name = name[0:3:1] + str(count)

        while True:
            if new_name in Graphs.graphDB:
                new_name = name[0:3:1] + str(count)
                count += 1
            else:
                return new_name

    def removeNode(self,name):

        nodeName = Graphs.desc2key[name]

        try:
            del Graphs.graphDB[nodeName]
            del Graphs.propertiesDB[name]
            del Graphs.key2desc[nodeName]
            del Graphs.desc2key[name]
        except KeyError:
            pass # Ignoring deletion cause node does not exist


    # Form should have different methods to add characteristics
"""form <str> characteristics of the node
        "junction" => multiple edges leading upto the node
        "place" => the node represents a room or a place
        "stairs" => node has stairs
        ""
        "type" => detailed description of the form
            Eg : water fountain, hand sanitising station etc."""



method.clearFileData("graphDB.json")
G = Graphs()
G.addNode("home",["Bpath","Cpath","Dpath"],isMajor=True)
G.addNode("Bpath",[])
print(G.graphDB)

# Testing and Debugging

from algorithms import Path
P = Path(G.graphDB)
print(P.BFS(G.graphDB,Graphs.desc2key["home"]))