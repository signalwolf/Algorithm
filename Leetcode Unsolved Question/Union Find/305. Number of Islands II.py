class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        islands = UnionFind()
        for p in map(tuple, positions):
            islands.add(p)
            for dp in (0, 1), (0, -1), (1, 0), (-1, 0):
                q = (p[0] + dp[0], p[1] + dp[1])
                if q in islands.id:
                    islands.union(p, q)
            ans += [islands.count]
            # print islands.id
        return ans


class UnionFind(object):
    def __init__(self):
        self.id = {}
        self.size = {}
        self.count = 0

    def add(self, pair):
        self.id[pair] = pair
        self.size[pair] = 1
        self.count += 1

    def root(self, pair):
        while self.id[pair] != pair:
            self.id[pair] = self.id[self.id[pair]]
            pair = self.id[pair]
        return pair

    def union(self, p, q):
        p = self.root(p)
        q = self.root(q)
        if p == q: return
        if self.size[p] < self.size[q]:
            p, q = q, p
        self.id[p] = q
        self.size[p] += self.size[q]
        self.count -= 1        