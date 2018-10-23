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

def root(ids, v, size):
    if v not in ids:
        ids[v] = v
        size[v] = 1
    while v != ids[v]:
        ids[v] = ids[ids[v]]
        v = ids[v]
    return v

def union_find(graph):
    ids = {}
    size = {}
    #count = 0
    for v in graph:
        vr = root(ids, v, size)
        for ngb in graph[v]:
            ngb_root = root(ids, ngb, size)
            if vr == ngb_root: continue

            if size[vr] < size[ngb_root]:
                vr, ngb_root = ngb_root, vr

            ids[vr] = ngb_root
            size[ngb_root] += size[vr]
    return ids, size



print g.graph
ids, size =  union_find(g.graph)
for id in ids:
    ids[id] = root(ids, id, size)
print ids

