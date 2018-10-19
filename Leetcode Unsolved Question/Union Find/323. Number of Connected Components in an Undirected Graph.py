class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """

        def root(node):
            while ids[node] != node:
                ids[node] = ids[ids[node]]
                node = ids[node]
            return node

        ids = range(n)
        size = [1] * n
        count = n
        for s, e in edges:
            s, e = root(s), root(e)
            if s == e: continue
            if size[s] < size[e]:
                s, e = e, s
            ids[s] = e
            size[e] += size[s]
            count -= 1
        return count