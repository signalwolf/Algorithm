

from collections import defaultdict
from heapq import *
def min_spanning_tree(start, graph):
    parents = {}
    cost = {}
    visited = set()

    cost[start] = 0
    heap = [[0, start]]
    while heap:
        a, curr_node = heappop(heap)
        visited.add(curr_node)
        for ngb in graph[curr_node]:
            ngb_cost = graph[curr_node][ngb]
            if ngb in visited: continue
            if ngb not in cost or cost[ngb] > ngb_cost:
                cost[ngb] = ngb_cost
                parents[ngb] = curr_node
                heappush(heap, [ngb_cost, ngb])
        # print parents, heap
    return parents

def facebook(start, graph):
    heap = [[0, start, start]]
    parents = {}
    while heap:
        dis, curr, prev = heappop(heap)
        parents[curr] = prev
        for ngb in graph[curr].keys():
            if ngb not in parents:
                heappush(heap, [graph[curr][ngb], ngb, curr])
    return parents



# def min_spanning_tree2(start, graph):
#     parents = {}
#     cost = {}
#     heap = []
#     for node in graph:
#         parents[node] = None
#         cost[node] = float('inf') if node != start else 0
#         heap.append([cost[node], node])
#
#     heapify(heap)
#
#     while heap:
#         a, curr = heappop(heap)
#         for ngb in graph[curr]:
#             if ngb in heap and graph[curr][ngb] < cost[ngb]:
#                 cost[ngb] = graph[curr][ngb]
#                 parents[ngb] = curr
#     return parents



graph = {
    0:{1:4, 7:8},
    1:{0:4,7:11,2:8},
    2:{1:8, 8:2, 3:7, 5:4},
    3:{2:7,5:14,4:9},
    4:{3:9, 5:10},
    5:{3:14,6:2,4:10, 2:4},
    6:{7:1,8:6,5:2},
    7:{0:8,1:11,8:7,6:1},
    8:{2:2,6:6,7:7},
}

print min_spanning_tree(0, graph)
print facebook(0, graph)
# print min_spanning_tree2(0, graph)