# coding=utf-8


# DP solution:
import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float('inf')] * (1 + n)
        dp[0] = 0
        for i in xrange(1, n + 1):
            for j in xrange(1, int(math.sqrt(i)) + 1):
                dp[i] = min(dp[i - j ** 2] + 1, dp[i])
                if dp[i] == 1:
                    break
        return dp[n]


# BFS solution: 228ms, 81%
from collections import deque
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        max_n = int(math.sqrt(n))
        queue = deque([[0, 0]])
        visited = set([1])
        while queue:
            curr, steps = queue.popleft()
            for i in xrange(max_n, 0, -1):
                new_num = curr + i ** 2

                if new_num == n:
                    return steps + 1

                if new_num < n and new_num not in visited:
                    queue.append([new_num, steps + 1])
                    visited.add(new_num)