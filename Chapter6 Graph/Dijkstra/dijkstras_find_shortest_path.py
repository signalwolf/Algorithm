from heapq import *
from collections import defaultdict

def dijkstras(start, end, graph):
    distance = [False] * (len(graph))
    heap = [[0, start, [0]]]
    while heap:
        dis, curr, path = heappop(heap)
        if distance[curr]: continue
        if curr == end: return distance
        distance[curr] = dis
        for ngr in graph[curr].keys():
            if not distance[ngr]:
                ngr_dis = dis + graph[curr][ngr]
                heappush(heap, [ngr_dis, ngr, path + [ngr]])
        # print distance
    return distance

def facebook(start, end, graph):
    distance = [None] * len(graph)
    heap = [[0, start]]
    while heap:
        print heap
        dis, curr = heappop(heap)
        if distance[curr]:
            continue
        distance[curr] = dis
        if curr == end:
            return distance

        for ngb in graph[curr]:
            if distance[ngb] is None:
                heappush(heap, [dis + graph[curr][ngb], ngb])
    return -1





graph = {
    0:{1:4, 7:8},
    1:{0:4,7:8,2:8},
    2:{1:8, 8:2, 3:7},
    3:{2:7,5:14,4:9},
    4:{3:9, 5:10},
    5:{3:14,6:2,4:10},
    6:{7:1,8:6,5:2},
    7:{0:8,1:11,8:7,6:1},
    8:{2:2,6:6,7:7},
}

print dijkstras(0,8, graph)
print facebook(0,8, graph)
# print dijkstra

# Output:
# ###################################################################
# [0, False, False, False, False, False, False, False, False]
# [0, 4, False, False, False, False, False, False, False]
# [8, 4, False, False, False, False, False, False, False]
# [8, 4, False, False, False, False, False, 8, False]
# [8, 4, False, False, False, False, 9, 8, False]
# [8, 4, False, False, False, 11, 9, 8, False]
# [8, 4, 12, False, False, 11, 9, 8, False]
# [0, 1, 2, 8]
