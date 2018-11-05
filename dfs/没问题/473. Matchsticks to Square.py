# coding=utf-8
# 要记住reverse nums后会快很多，这是一个general的优化

class Solution(object):

    def dfs(self, start, nums, Gsum, target, NotFound):

        if tuple(Gsum) in NotFound:
            return False

        if start == len(nums):
            return True

        base = nums[start]

        for i in xrange(4):
            if Gsum[i] + base <= target:
                Gsum[i] += base
                if self.dfs(start + 1, nums, Gsum, target, NotFound):
                    return True
                Gsum[i] -= base

        NotFound.add(tuple(Gsum))
        return False

    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 4: return False
        total = sum(nums)
        if total % 4 != 0: return False

        nums.sort(reverse=True)
        if self.dfs(0, nums, [0, 0, 0, 0], total / 4, set()):
            return True
        else:
            return False
