# coding=utf-8

# 解决的问题：Graph中是否有cycle
# 基本模型： Union Find
# 解法，遍历过的node加上其parent的mark, 然后看是否有node的neighbor已经mark当前node的mark, 如果是则return True
# 试用情况：undirected graph

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

def find_parsent(visited, node):
    if visited[node] == -1:
        return node
    else:
        return find_parsent(visited, visited[node])

def union (visited, x, y):
    x_set = find_parsent(visited, x)
    y_set = find_parsent(visited, y)
    visited[x_set] = y_set

def union_find (graph, n):
    visited = [-1] * n
    for i in graph:
        for j in graph[i]:
            if visited[i] == -1 or visited[j] == -1:
                x = find_parsent(visited, i)
                y = find_parsent(visited, j)
                if x == y:
                    return True
                union(visited, x, y)
                print i, j, visited, x, y
    return False

g= Graph(6)
g.addEdge(0,5)
g.addEdge(0,4)
g.addEdge(1,4)
g.addEdge(1,6)
g.addEdge(2,4)
g.addEdge(3,5)
#g.addEdge(3,6)



print g.graph
print union_find(g.graph, 7)