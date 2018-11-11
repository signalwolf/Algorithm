# coding=utf-8

# 仔细分析这道题：
#   1. Brute force 的解法：在每一个node处，向左去找寻第一个比他小的index，向右去寻找第一个比他小的index
#       然后我们计算两个index之间的距离就可以了。
#   2. 既然是找第一个比他小，那么就可以使用 monotone stack了。第一个小 --》 单调递增


class Solution(object):

    def helper(self, A):
        # input: list of ints
        # output: list of ints
        ans = [0] * len(A)
        stack = []
        for i, val in enumerate(A):
            prev = i
            while stack and A[stack[-1]] >= val:
                prev = stack.pop()
            ans[i] = (i - prev) + ans[prev]
            stack.append(i)
        return ans

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights) == 0: return 0
        left = self.helper(heights)
        right = self.helper(heights[::-1])[::-1]
        res = 0
        for i in xrange(len(heights)):
            res = max(res, heights[i] * (left[i] + right[i] + 1))
        return res