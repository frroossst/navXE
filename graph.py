# To generate and create a graph

from methods import methods

class Graphs():

    graphDB = {}
    propertiesDB = {}
    key2desc = {}
    desc2key = {}

    def __init__(self):
            Graphs.graphDB = methods.loadJSON("graphDB.json")
            Graphs.propertiesDB = methods.loadJSON("propertiesDB.json")
            Graphs.key2desc = methods.loadJSON("indexDB.json")["key2desc"]
            Graphs.desc2key = methods.loadJSON("indexDB.json")["desc2key"]

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

        # ! Not adding a children iterator to generate gGNNs for children as if they are not leaves and connect to existing nodes,
        # ! we accidentally reset the graph. The children are modified as leaves in the algorithms.py script right before the
        # ! actual traversal takes place, for now this is only done for the temporary graph variable and the database is not modified in any way 


    @classmethod
    def generateGraphNodeNames(self,name) -> str:

        count = 0
        new_name = name[0:3:1] + str(count)

        while True:
            if new_name in Graphs.graphDB:
                new_name = name[0:3:1] + str(count)
                count += 1
            else:
                break



    def removeNode(self,name):
        try:
            del Graphs.graphDB[name]
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

G = Graphs()
G.addNode("home",["Bpath","Cpath","Dpath"],isMajor=True)
G.addNode("Bpath",[])
print(G.graphDB)

# Testing and Debugging

from algorithms import Path
P = Path(G.graphDB)
print(P.BFS(G.graphDB,"home"))
print(P.BFS(G.graphDB,"root"))