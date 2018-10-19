class Solution(object):

    def root(self, ids, node):
        while ids[node] != node:
            ids[node] = ids[ids[node]]
            node = ids[node]
        return node

    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        N = len(edges)
        size = [0] + [1] * N
        ids = range(N + 1)
        for s, e in edges:
            rs, re = self.root(ids, s), self.root(ids, e)
            if rs == re: return [s, e]
            if size[rs] < size[re]:
                re, rs = rs, re
            ids[rs] = re
            size[re] += size[rs]