# coding=utf-8

# 特别注意这个算法对图有要求，graph的key要包含所有的node（包括出度为0的node）
# 否则的话，那些出度为0的node是不在graph的key中，
# 由于使用的是default dict，那么便会新建这个node. 造成循环的破裂
# 如果使用的是dict，那么会找不到这个key，造成程序的报错。

from collections import deque, defaultdict
def topological_sort_dfs(graph):

    def dfs(vertex):
        if vertex in visited: return
        for ngb in graph[vertex]:
            dfs(ngb)
        queue.appendleft(vertex)
        visited.add(vertex)

    queue = deque()
    visited = set()
    for vertex in graph:
        print vertex, graph
        dfs(vertex)
    return list(queue)


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v] = []


def topological_sort_bfs(graph):
    in_degree = defaultdict(int)
    for u, v_list in graph.items():
        for v in v_list:
            in_degree[v] += 1
            in_degree[u] = in_degree[u]

    queue = deque()

    for key, val in in_degree.items():
        if val == 0:
            queue.append(key)

    visited = set()
    res = []
    while queue:
        print queue, in_degree
        curr_node = queue.popleft()
        visited.add(curr_node)
        res.append(curr_node)
        for ngb in graph[curr_node]:
            if ngb not in visited:
                in_degree[ngb] -= 1
                if in_degree[ngb] == 0:
                    queue.append(ngb)
    return res




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

print g.graph
#print topological_sort_dfs(g.graph)
print topological_sort_bfs(g.graph)