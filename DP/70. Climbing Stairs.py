# coding=utf-8

# 直接套公式，非常简单

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 1
        # function: dp[i] = dp[i - 1] + dp[i - 2]
        dp = [0] * (n + 1)
        # initial:
        dp[0], dp[1] = 1, 1
        for i in xrange(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]