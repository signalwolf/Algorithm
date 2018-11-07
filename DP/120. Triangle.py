# coding=utf-8

# 注意上下之间的关系就好
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 0: return 0
        prev = triangle[0]
        for i in xrange(1, len(triangle)):
            curr = [0] * len(triangle[i])
            for j in xrange(len(triangle[i])):
                if j == 0:
                    curr[j] = prev[j] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    curr[j] = prev[j - 1] + triangle[i][j]
                else:
                    curr[j] = min(prev[j], prev[j - 1]) + triangle[i][j]
            prev = curr
        return min(prev)