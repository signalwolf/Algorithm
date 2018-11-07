# coding=utf-8

# dp的典型的题目
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0: return 0
        dp = [[0 for _ in xrange(n)] for _ in xrange(m)]

        for i in xrange(m):
            dp[i][0] = 1

        for j in xrange(n):
            dp[0][j] = 1

        for i in xrange(1, m):
            for j in xrange(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]