
# use the relation between the double sized array to the new array.
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lens = len(nums)
        res = [-1] * lens
        stack = []
        for i in xrange( 2 * lens - 1, -1, -1):
            i = i % lens
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            if stack:
                res[i] = nums[stack[-1]]
            stack.append(i)
        return res

# double size the array
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = nums + nums
        res = [-1] * len(nums)
        stack = []
        for i in xrange(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            if stack:
                res[i] = nums[stack[-1]]
            stack.append(i)
        return res[:len(res) / 2]