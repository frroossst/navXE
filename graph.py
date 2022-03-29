class Graphs():

    graphDB = {}

    def __init__(self):
        pass

    def addNode(self,name,children=[],form,weight=0.0):
    """
    name <string> name of the node
    children <list> list of the names of all children, empty list if leaf
    form <str> characteristics of the node
        "junction" => multiple edges leading upto the node
        "place" => the node represents a room or a place
        "stairs" => node has stairs
        ""
        "type" => detailed description of the form
            Eg : water fountain, hand sanitising station etc.
    """
        if name in graphDB:
            raise NameError ("Node name already exists in database")
        else:
            graphDB[name] = children

    def removeNode(self,name):
        try:
            del graphDB[name]
        except KeyError:
            pass # Ignoring deletion cause node does not exist

