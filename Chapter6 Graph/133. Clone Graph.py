# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
from collections import deque
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node: return None
        queue = deque()
        queue.append(node)
        mapping = {}
        nodeCopy = UndirectedGraphNode(node.label)
        mapping[node] = nodeCopy
        while queue:
            curr = queue.popleft()
            for ngb in curr.neighbors:
                if ngb not in mapping:
                    ngbCopy = UndirectedGraphNode(ngb.label)
                    mapping[ngb] = ngbCopy
                    queue.append(ngb)
                mapping[curr].neighbors.append(mapping[ngb])
        return nodeCopy