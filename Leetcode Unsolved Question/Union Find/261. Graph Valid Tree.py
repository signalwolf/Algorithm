# coding=utf-8

# 没有使用任何的

class Solution(object):

    def root(self, node, ids):
        while node != ids[node]:
            node = ids[node]
        return node

    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n - 1: return False
        ids = range(n)
        for edge in edges:
            p, q = self.root(edge[0], ids), self.root(edge[1], ids)
            if p == q: return False
            ids[p] = q
        return True