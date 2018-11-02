class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0: return nums
        if len(nums) == 1: return [nums]
        nums.sort()
        res = []
        for i in xrange(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            curr = [nums[i]]
            ans = self.permuteUnique(nums[:i] + nums[i + 1:])
            for a in ans:
                res.append(curr + a)
        return res