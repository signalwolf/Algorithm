class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        indexMap = collections.defaultdict(int)
        for i, num in enumerate(nums):
            indexMap[num] = i

        stack = []
        nextBigger = [-1] * len(nums)
        for i in xrange(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            if stack:
                nextBigger[i] = nums[stack[-1]]
            stack.append(i)
        res = []
        for num in findNums:
            res.append(nextBigger[indexMap[num]])
        return res