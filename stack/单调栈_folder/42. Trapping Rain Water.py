class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = [0] * len(height)
        right = [0] * len(height)
        for i in xrange(1, len(height)):
            left[i] = max(left[i - 1], height[i - 1])
        for i in xrange(len(height) - 2, -1, - 1):
            right[i] = max(right[i + 1], height[i + 1])
        res = [0] * len(height)
        for i in xrange(len(height)):
            res[i] = max(min(left[i], right[i]), height[i]) - height[i]
        return sum(res)