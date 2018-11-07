# coding=utf-8

# 注意的是当前的最大值可能是两种，
#   其一：如果node的值大于 0，那么便是 nums[i] * max_val_prev
#   其二：如果node的值小于 0，那么便是 nums[i] * min_val_prev
#   故而需要记住两个值，一个就是prev max， 一个是prev min

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_val = [0] * len(nums)
        max_val = [0] * len(nums)

        # initial:
        # function: min_val[i] = min(nums[i], nums[i] * min_val[i - 1], nums[i] * max_val[i - 1])
        #           max_val[i] = max(nums[i], nums[i] * max_val[i - 1], nums[i] * min_val[i - 1])
        # return: max(max_val)
        # state: min, max
        min_val[0], max_val[0] = 0, nums[0]
        for i in xrange(1, len(nums)):
            min_val[i] = min(nums[i], nums[i] * min_val[i - 1], nums[i] * max_val[i - 1])
            max_val[i] = max(nums[i], nums[i] * max_val[i - 1], nums[i] * min_val[i - 1])
        return max(max_val)

# optimized:
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # initial:
        # function: min_val[i] = min(nums[i], nums[i] * min_val[i - 1], nums[i] * max_val[i - 1])
        #           max_val[i] = max(nums[i], nums[i] * max_val[i - 1], nums[i] * min_val[i - 1])
        # return: max(max_val)
        # state: min, max
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        prev_min, prev_max = 0, nums[0]
        res = max(prev_min, prev_max)
        for i in xrange(1, len(nums)):
            curr_min = min(nums[i], nums[i] * prev_min, nums[i] * prev_max)
            curr_max = max(nums[i], nums[i] * prev_max, nums[i] * prev_min)
            prev_min, prev_max = curr_min, curr_max
            res = max(prev_min, prev_max, res)
        return res