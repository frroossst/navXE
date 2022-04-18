from methods import method
import copy

class Path():

    def __init__(self,graph : dict):
        pass

    def DFS(self,graph,node,visited):

        if node not in visited:
            visited.append(node)
            for x in graph[node]:
                Path.DFS(graph,x,visited)

        return visited

    def BFS_SP(self, graph, start, goal):

        if start not in graph or goal not in graph:
            return None

        explored = []
        
        # Queue for traversing the
        # graph in the BFS
        queue = [[start]]
        
        # If the desired node is
        # reached
        if start == goal:
            return 0
        
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
    
    def Astar():
        pass

    def Djikstra():
        pass
