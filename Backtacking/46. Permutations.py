class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1: return [nums]
        res = []
        for i in xrange(len(nums)):
            curr = [nums[i]]
            ans = self.permute(nums[:i] + nums[i + 1:])
            for a in ans:
                res.append(curr + a)
        return res