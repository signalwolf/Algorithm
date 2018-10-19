from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)


# 5 --- 0 --- 4 --- 2
# |           |
# |           |
# |           |
# 3 --- 6 --- 1

g= Graph(6)
g.addEdge(0,5)
g.addEdge(0,4)
g.addEdge(1,4)
g.addEdge(1,6)
g.addEdge(2,4)
g.addEdge(3,5)
g.addEdge(3,6)



print g.graph
# print union_find(g.graph, 7)