# coding=utf-8

# 与 redundant connection I 的区别在于说多了一种情况就是某个node 的入度为2
# 例如：左图是有向图，这是not valid 的； 但是对于无向图的右图来说，则是正确的。
# 1 -->  2  <--- 3      1 -- 2 -- 3
#        |                   |
#        |                   |
#        V                   4
#        4
# 所以做法就是先找出这些两个parent的node，如果没有node有两个parent，那么可以直接union find edges
# 否则，我们先从edges 中移掉 两个parent中的后一个，这样新建的图如果没有环，就代表这条边就是多出来的边
# 相反，余下的那条边就是多出来的边。


class Solution(object):

    def cycle(self, edges, N):
        def root(node):
            while node != ids[node]:
                ids[node] = ids[ids[node]]
                node = ids[node]
            return node

        size = [1] * (N + 1)
        ids = range(N + 1)
        for s, e in edges:
            rs, re = root(s), root(e)
            if rs == re: return [s, e]
            if size[rs] < size[re]:
                rs, re = re, rs
            ids[rs] = re
            size[re] += size[rs]
        return False

    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        N = len(edges)
        if N == 0: return None
        in_degree = [-1] * (N + 1)
        potential_list = []
        for i, pair in enumerate(edges):
            s, e = pair
            if in_degree[e] == -1:
                in_degree[e] = i
            else:
                potential_list = [in_degree[e], i]
        if len(potential_list) == 2:
            deleted = edges.pop(potential_list[1])
            if self.cycle(edges, N):
                return edges[potential_list[0]]
            else:
                return deleted
        if len(potential_list) == 0:
            return self.cycle(edges, N)