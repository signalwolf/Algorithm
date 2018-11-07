# coding=utf-8

# DP的方式是，dp[i] = [使用nums[i] 的max，不使用nums[i] 的 max]
# 故而
# dp[i][0] = max(nums[i], dp[i -1][0] + nums[i]): 使用 nums[i] 的max是当前的num[i] 或者之前的用了nums[i - 1]的dp[i-1][0] + nums[i]
# dp[i][1] = max(dp[i - 1]): 不使用nums[i]的话， 那么其结果为 dp[i - 1] 两个中更大的那一个

# Using DP to solve this problem:
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return nums
        dp = [[0 for _ in xrange(2)] for _ in xrange(len(nums))]
        dp[0] = [nums[0], -float('inf')]
        for i in xrange(1, len(nums)):
            dp[i][0] = max(nums[i], dp[i -1][0] + nums[i])
            dp[i][1] = max(dp[i - 1])
        return max(dp[len(nums) - 1])

# Optimized DP: 因为当前状态只基于之前一位的状态，故而只需要记住prev就好
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return nums
        # dp = [[0 for _ in xrange(2)] for _ in xrange(len(nums))]
        prev0, prev1 = nums[0], -float('inf')
        for i in xrange(1, len(nums)):
            curr0 = max(nums[i], prev0+ nums[i])
            curr1 = max(prev0, prev1)
            prev0, prev1 = curr0, curr1
        return max(prev0, prev1)

# divide and conquer method:
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return -float('inf')
        if len(nums) == 1: return nums[0]

        mid = len(nums) / 2
        left_sum = self.maxSubArray(nums[:mid])
        right_sum = self.maxSubArray(nums[mid + 1:])

        mid_right, temp = 0, 0
        for i in xrange(mid + 1, len(nums)):
            temp += nums[i]
            mid_right = max(mid_right, temp)

        mid_left, temp = 0, 0
        for i in xrange(mid - 1, -1, - 1):
            temp += nums[i]
            mid_left = max(mid_left, temp)

        return max(left_sum, right_sum, mid_right + mid_left + nums[mid])
