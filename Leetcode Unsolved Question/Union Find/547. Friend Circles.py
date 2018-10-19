# union find on adjacent matrix format
class Solution(object):

    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """

        def root(i):
            while i != ids[i]:
                ids[i] = ids[ids[i]]
                i = ids[i]
            return i

        N = len(M)
        if N == 0: return 0
        ids = range(N)
        size = [1] * N
        count = N

        for i in xrange(N):
            for j in xrange(i + 1, N):
                if M[i][j] == 1:
                    x = root(i)
                    y = root(j)
                    if x == y: continue

                    if size[x] < size[y]:
                        x, y = y, x
                    ids[x] = y
                    size[y] += size[x]
                    count -= 1
        # print ids
        return count
