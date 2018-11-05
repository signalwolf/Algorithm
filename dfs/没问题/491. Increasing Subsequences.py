class Solution(object):

    def helper(self, start, nums, curr, res):
        if start == len(nums):
            return

        for i in xrange(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue

            if not curr or nums[i] >= curr[-1]:
                curr.append(nums[i])
                if len(curr) >= 2:
                    res.add(tuple(curr))
                self.helper(i + 1, nums, curr, res)
                curr.pop()

    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        self.helper(0, nums, [], res)
        return list(res)