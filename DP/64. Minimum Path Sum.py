

# DP: 32ms O(mn)

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # function: dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        # initial: dp[0][i] = dp[0][i - 1] + grid[0][i]
        #          dp[i][0] = dp[i - 1][0] + grid[i][0]
        # return dp[m - 1][n - 1]

        if len(grid) == 0 or len(grid[0]) == 0: return 0
        M, N = len(grid), len(grid[0])
        dp = [[0 for _ in xrange(N)] for _ in xrange(M)]
        dp[0][0] = grid[0][0]

        for i in xrange(1, M):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        for j in xrange(1, N):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        for i in xrange(1, M):
            for j in xrange(1, N):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[M - 1][N - 1]


# BFS + heap O(mn * log(mn))
from heapq import heappop, heappush
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # BFS + heap, dijstra
        heap = [[grid[0][0], 0, 0]]
        visited = set()
        while heap:
            cost, i, j = heappop(heap)
            if (i, j) in visited:
                continue

            visited.add((i, j))

            if (i, j) == (len(grid) - 1, len(grid[0]) - 1):
                return cost

            for dx, dy in [[0, 1], [1, 0]]:
                x, y = i + dx, j + dy

                if x < len(grid) and y < len(grid[0]) and (x, y) not in visited:
                    heappush(heap, [cost + grid[x][y], x, y])