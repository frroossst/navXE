class Path():

    def __init__(self,graph):
        pass

    @classmethod
    def BFS(self,graph,node):
        # node is the starting position
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

