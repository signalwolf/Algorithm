from collections import deque
class Solution(object):
    def updateMatrix(self, A):
        R, C = len(A), len(A[0])
        def neighbors(r, c):
            for cr, cc in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                if 0 <= cr < R and 0 <= cc < C:
                    yield cr, cc

        q, seen = deque([]), set()
        for i in xrange(R):
            for j in xrange(C):
                if A[i][j] == 0:
                    q.append([(i,j), 0])
                    seen.add((i,j))
        ans = [[0]*C for _ in A]
        while q:
            (r, c), depth = q.popleft()
            ans[r][c] = depth
            for nei in neighbors(r, c):
                if nei not in seen:
                    seen.add(nei)
                    q.append((nei, depth + 1))

        return ans