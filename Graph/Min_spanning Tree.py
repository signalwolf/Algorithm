

from collections import defaultdict
from heapq import *
def min_spanning_tree(start, graph):
    



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

print min_spanning_tree(0, graph)