# coding=utf-8
# 仍旧是只适用于DAC的情况。
# 基本算法：BFS，graph + queue
# 它所利用的关键点在于说：对于一个DAC来说，必然有一个node的in degreee 为0作为起点；必然有一个node的out degree为0作为终点。
# 当然可能有很多的这样的起点或者终点，例如下面的例子中有两个起点，2个终点。

from collections import defaultdict, deque
def topological_sort(graph, n):
    in_degrees = [0] * n
    for dest_list in graph.values():
        for dest in dest_list:
            in_degrees[dest] += 1

    queue = deque([])
    for i in xrange(n):
        if in_degrees[i] == 0:
            queue.append(i)

    visited = []
    while queue:
        print in_degrees
        curr = queue.popleft()
        visited.append(curr)
        for ngb in graph[curr]:
            in_degrees[ngb] -= 1
            if in_degrees[ngb] == 0:
                queue.append(ngb)

    return visited

# output:
# [2, 2, 1, 1, 0, 0]
# [1, 1, 1, 1, 0, 0]
# [0, 1, 0, 1, 0, 0]
# [0, 1, 0, 0, 0, 0]
# [0, 1, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0]
# [4, 5, 2, 0, 3, 1]



class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)


# 5 --> 0 <-- 4
# |           V
# |           |
# v           |
# 2 --> 3 --> 1

g= Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

print topological_sort(g.graph, g.V)