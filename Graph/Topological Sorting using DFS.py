# coding=utf-8

# reference: https://www.geeksforgeeks.org/topological-sorting/

# Application:  Topological Sorting is mainly used for scheduling jobs from the given dependencies among jobs
# In computer science, applications of this type arise in instruction scheduling, ordering of formula cell
# evaluation when recomputing formula values in spreadsheets, logic synthesis, determining the order of
# compilation tasks to perform in makefiles, data serialization, and resolving symbol dependencies in linkers.

# time complexity: O(V + E)

# 算法：
# 大致就是确保每一个有neighbor node没有visit过的node都在其neighbor node后面加入。故使用queue便能够解决这个问题。

# 基本原型：DFS

# 证明：
# 考虑任意的边v->w，当调用dfs(v)的时候，有如下三种情况：
#
# dfs(w)还没有被调用，即w还没有被mark，此时会调用dfs(w)，然后当dfs(w)返回之后，dfs(v)才会返回 --> 故而在最后的queue中，V 在 W之前
# dfs(w)已经被调用并返回了，即w已经被mark --> 此时V在调用过W的node之前，故而也在W之前
# dfs(w)已经被调用但是在此时调用dfs(v)的时候还未返回 --> 不可能情况，除非有环


# only solvable for Directed Acyclic Graph (DAG).
# define:
# 在图论中，由一个有向无环图的顶点组成的序列，当且仅当满足下列条件时，称为该图的一个拓扑排序（英语：Topological sorting）。
# 1. 每个顶点出现且只出现一次；
# 2. 若A在序列中排在B的前面，则在图中不存在从B到A的路径。

# Wiki: pseudocode:
# L ← Empty list that will contain the sorted nodes
# S ← Set of all nodes with no outgoing edges
# for each node n in S do
#     visit(n)
# function visit(node n)
#     if n has not been visited yet then
#         mark n as visited
#         for each node m with an edgefrom m to ndo
#             visit(m)
#         add n to L


# Solveable using DFS:
from collections import defaultdict, deque

def dfs(graph, node, visited, stack):
    if visited[node]: return []
    visited[node] = True
    path = [node]
    for ngb in graph[node]:
        if not visited[ngb]:
            dfs(graph, ngb, visited, stack)
    stack.appendleft(node)
    print stack, visited


def topological_sort(graph, n):
    visited = [False] * n
    stack = deque([])
    for i in [2, 0,1,3,4,5]:
        if not visited[i]:
            path = dfs (graph, i, visited, stack)
            print i, path, visited
    return list(stack)



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

# Output:
# deque([1]) [False, True, True, True, False, True]
# deque([3, 1]) [False, True, True, True, False, True]
# deque([2, 3, 1]) [False, True, True, True, False, True]
# deque([0, 2, 3, 1]) [True, True, True, True, False, True]
# deque([5, 0, 2, 3, 1]) [True, True, True, True, False, True]
# 5 None [True, True, True, True, False, True]
# deque([4, 5, 0, 2, 3, 1]) [True, True, True, True, True, True]
# 4 None [True, True, True, True, True, True]
# [4, 5, 0, 2, 3, 1]