from methods import method
from copy import deepcopy

class Path():

    def __init__(self,graph):
        pass
        """
        dict_copy = deepcopy(graph)
        for i in dict_copy.values():
            for j in i:
                if j != []:
                    if j not in graph:
                        graph[j] = []
        """

    def BFS(self,graph,node):
        # node is the starting position

        graph = method.leafifyChildren(graph)

        visited = []
        queue = []
        visited.append(node)
        queue.append(node)

        while queue:
            s = queue.pop(0)
            for x in graph[s]:
                if x not in visited:
                    visited.append(x)
                    queue.append(x)
        return visited

    @classmethod
    def DFS(self,graph,node,visited):
        if node not in visited:
            visited.append(node)
            for x in graph[node]:
                Path.DFS(graph,x,visited)
        return visited

    @classmethod
    def Astar():
        pass

    @classmethod
    def Djikstra():
        pass
