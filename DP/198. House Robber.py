# coding=utf-8

# 抢劫当前的house 与不抢劫当前的house的选择

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        dp = [[0 for _ in xrange(2)] for _ in xrange(len(nums))]
        dp[0] = [nums[0], 0]
        for i in xrange(1, len(nums)):
            dp[i][0] = dp[i - 1][1] + nums[i]
            dp[i][1] = max(dp[i - 1])
        return max(dp[len(nums) - 1])
