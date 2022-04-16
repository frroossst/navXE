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

    def BFS(self,graph : dict,node : str):
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

    def DFS(self,graph,node,visited):
        if node not in visited:
            visited.append(node)
            for x in graph[node]:
                Path.DFS(graph,x,visited)
        return visited

    def Astar():
        pass

    def Djikstra():
        pass

    def BFS_SP(self, graph, start, goal):
        explored = []
        
        # Queue for traversing the
        # graph in the BFS
        queue = [[start]]
        
        # If the desired node is
        # reached
        if start == goal:
            print("Same Node")
            return
        
        # Loop to traverse the graph
        # with the help of the queue
        while queue:
            path = queue.pop(0)
            node = path[-1]
            
            # Condition to check if the
            # current node is not visited
            if node not in explored:
                neighbours = graph[node]
                
                # Loop to iterate over the
                # neighbours of the node
                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
                    
                    # Condition to check if the
                    # neighbour node is the goal
                    if neighbour == goal:
                        return new_path
                explored.append(node)