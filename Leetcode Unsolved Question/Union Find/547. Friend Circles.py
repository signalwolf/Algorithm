# coding=utf-8
# union find on adjacent matrix format

# 千万注意的是不要去改双层loop中的i,j.
# 因为如果在j循环中改了i，那么由于不会触发i循环，故而在接下来的j循环中i都改掉了

for i in xrange(3):
    for j in xrange(3):
        if j == 2: i = 5
        print (i, j)

# output:
# (0, 0)
# (0, 1)
# (5, 2) --> note: i been changed
# (1, 0)
# (1, 1)
# (5, 2) --> note: i been changed
# (2, 0)
# (2, 1)
# (5, 2) --> note: i been changed

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
